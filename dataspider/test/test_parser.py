from pyquery import PyQuery as pq
import requests

def test_list_parser(filename='list_page.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    doc = pq(content)
    item_list = doc('li.mb')  # 匹配所有class 属性中带有mb的li标签
    for tag in item_list.items():
        movie_url = 'http://yhdm81.com/' + tag('a').attr('href')
        movie_name = tag('a').attr('title')
        movie_cover = tag('div.img > img').attr('src')
        print(movie_url, movie_name, movie_cover)


def test_detail_parser(url=None, filename='detail_page.html'):
    if url:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Content-Type': 'text/heml;charset=utf-8'})
        res.encoding = None
        content = res.text
    else:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    doc = pq(content)
    artists = doc('div.info > dl > dd:nth-child(2)').text().split('：')
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
    # test_list_parser()
    """
        动漫: http://yhdm81.com/acg/74982/
        综艺: http://yhdm81.com/zongyi/56411/
        电视剧: http://yhdm81.com/tv/79711/
        电影: http://yhdm81.com/mov/75189/
    
    """
    test_detail_parser(url='http://yhdm81.com//tv/31929/')