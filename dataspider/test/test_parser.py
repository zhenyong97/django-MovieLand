from pyquery import PyQuery as pq


def test_list_parser(filename='list_page.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    doc = pq(content)
    item_list = doc('li.mb')  # 匹配所有class 属性中带有mb的li标签
    for tag in item_list.items():
        movie_url = 'http://www.yhdm6.com' + tag('a').attr('href')
        movie_name = tag('a').attr('title')
        movie_cover = tag('div.img > img').attr('src')
        print(movie_url, movie_name, movie_cover)


def test_detail_parser(filename='detail_page.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    doc = pq(content)
    artists = doc('div.info > dl > dd:nth-child(2)').text()[3:].split(' ')
    print(artists)
    categorys = doc('div.info > dl > dd:nth-child(4) > a').text().split(' ')
    print(categorys)
    area, year = doc('div.info > dl > dd:nth-child(3)').remove('b').text().split(' ')
    print(area, year)
    desc = doc('div.info > dl > dt.desd > div > div.des2').text()
    print(desc)


"""
{'moive_name': '神话',
'detail_url': 'http://www.yhdm6.com//mov/15514/',
'moive_cover': 'http://ae01.alicdn.com/kf/H68c418d18de64bd7a0a7c81a1ce14827f.png',
'performer': ['成龙', '金喜善', '梁家辉', '邵兵', '玛丽卡·沙拉瓦特',
'category': ['喜剧', '动作', '奇幻', '剧情'],
'area': '中国',
'desc': '.....',
'publish_year': '2005'}

save_data(data_info) 入库

"""


if __name__ == "__main__":
    test_list_parser()
    test_detail_parser()