import requests
from pyquery import PyQuery as pq


url = 'http://106.52.72.239:11333/getsortdata_all_z.php?action=acg&page=3&year=2022&area=all&class=0&dect=&id=y2022'

rsp = requests.get(url)
rsp.encoding = 'utf-8'
details_tasks = []
doc = pq(rsp.text)

def parse_url(content):
    if len(content) > 11:
        # http//zimiyy.com/mov/39736/
        return content
    else:   
        # /mov/39736/

        # http://yhdm83.com/
        return 'http://yhdm83.com/' + content


item_list = doc('li.mb')  # 匹配所有class 属性中带有mb的li标签 
for tag in item_list.items():
    movie_url = parse_url(tag('a').attr('href'))
    movie_name = tag('a').attr('title')
    movie_cover = tag('div.img > img').attr('src')  
    details_tasks.append({'movie_name':movie_name, 'movie_url':movie_url, 'movie_cover':movie_cover})
# print(item_list)
# print(details_tasks )


def parse_detail(url):
    rsp = requests.get(url)
    rsp.encoding = 'utf-8'
    content = rsp.text
    def area_publishtime(content):
            if content:
                if len(content)==1:
                    if content[0].isdigit():
                        return '' , content[0] # ['', '2011'] 

                    else:
                        return content[0], '' # ['中国', ''] 
                else:
                    return content # ['中国', '2011'] 
            else:    
                return '', ''

    task = {}
    doc = pq(content)
    artists = doc('div.info > dl > dd:nth-child(2)').text()[3:].split(' ')
    categorys = doc('div.info > dl > dd:nth-child(4) > a').text().split(' ')
    area, year = area_publishtime(doc('div.info > dl > dd:nth-child(3)').remove('b').text().split(' '))  # ['中国', '2011'] 
    desc = doc('div.info > dl > dt.desd > div > div.des2').text()
    task['perfomer'] = artists
    task['category'] = categorys
    task['area'] = area
    task['publish_year'] = year
    task['desc'] = desc
    return task




if __name__ == '__main__':
    print('hello test')
    print(parse_detail('http://yhdm83.com/tv/67365/'))

