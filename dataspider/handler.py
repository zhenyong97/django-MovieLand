import requests
import threading
import time
import random
from queue import Queue
from pyquery import PyQuery as pq
import datetime
from fake_useragent import UserAgent
ua = UserAgent()

page_list = {"电视剧":'http://106.52.72.239:11333/getsortdata_all_z.php?action=tv&page=1&year=0&area=all&class=0&dect=&id=',
             "电影": 'http://106.52.72.239:11333/getsortdata_all_z.php?action=mov&page=1&year=0&area=all&class=0&dect=&id=',
             "动漫": 'http://106.52.72.239:11333/getsortdata_all_z.php?action=acg&page=1&year=0&area=all&class=0&dect=&id=',
             "综艺": 'http://106.52.72.239:11333/getsortdata_all_z.php?action=zongyi&page=1&year=0&area=all&class=0&dect=&id='}


download_domain = 'http://yhdm81.com/'

class ListDownloadThread(threading.Thread):
    """
        列表页下载线程
    """

    def __init__(self, channnel_type, task_queue):
        """
            channnel_type: 电视剧，电影，动漫，综艺
        """
        super().__init__()
        self.channnel_type = channnel_type
        self.task_queue = task_queue
        self.start_list_url = page_list[self.channnel_type]
    

    def run(self):
        for page in range(1, 4):
            now = datetime.datetime.now()
            print(f"go---> {now}", self.channnel_type, threading.current_thread(), self.start_list_url)
            url = self.start_list_url.replace('page=1', f'page={page}')
            self.parser_list(self.get_page_content(url))
            end = now = datetime.datetime.now()
            print(f'end---> {end}', self.channnel_type, threading.current_thread(), self.start_list_url)


    def parser_list(self, content):
        if content:
            doc = pq(content)
            item_list = doc('li.mb')  # 匹配所有class 属性中带有mb的li标签
            for tag in item_list.items():
                detail_url = download_domain + tag('a').attr('href')
                name = tag('a').attr('title')
                cover_url = tag('div.img > img').attr('src')
                self.task_queue.put({
                    "detail_url": detail_url,
                    "name": name,
                    "cover_url": cover_url,
                    "channel_type": self.channnel_type
                })



    def get_page_content(self, url):
        #"http://www.yhdm6.com/mov/15514/"
        res = requests.get(url, headers={'User-Agent': ua.random,
        'Content-Type': 'text/heml;charset=utf-8'})
        time.sleep(5)
        res.encoding = None
        if res.status_code == 200:
            return res.text
        else:
            print('something error', res.text)


class DetailDownloadThread(threading.Thread):
    """
        详情页下载线程
    """

    def __init__(self, task_queue, result_queue):
        super().__init__()
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        """
        
            data:{'detail_url': 'http://yhdm81.com//tv/80036/', 
                  'name': '江湖探案传奇', 
                  'cover_url': 'https://img.ukuapi.com/upload/vod/20230321-1/75cc23336c642e60439b52294d61b170.jpg', 
                  'channel_type': '电视剧'}
        """
        
        while True:
            try:
                now = datetime.datetime.now()
                data = self.task_queue.get(timeout=10)
                url = data['detail_url']
                print(f"go---> {now}",  threading.current_thread(), url)
                self.parser_detail(data, self.get_page_content(url))
            except Exception as e:
                break
    
    def get_page_content(self, url):
        #"http://www.yhdm6.com/mov/15514/"
        time.sleep(3)
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Content-Type': 'text/heml;charset=utf-8'})
        res.encoding = None
        if res.status_code == 200:
            return res.text
        else:
            print('something error', res.text)
    
    def parser_detail(self, data, content):
        doc = pq(content)
        try:
            artists = doc('div.info > dl > dd:nth-child(2)').text()[3:].split(' ')
            categorys = doc('div.info > dl > dd:nth-child(4) > a').text().split(' ')
            area, year = doc('div.info > dl > dd:nth-child(3)').remove('b').text().split(' ')
            desc = doc('div.info > dl > dt.desd > div > div.des2').text()
            data['artists'] = artists
            data['categorys'] = categorys
            data['area'] = area
            data['year'] = year
            data['desc'] = desc
            self.result_queue.put(data) # 送入结果· 
        except Exception as e:
            print("error in ", data['detail_url'])
        

if __name__ == "__main__":
    print(threading.current_thread())
    #channel_types = '电视剧,电影,动漫,综艺'.split(',')
    channel_types = ['电视剧', '电影']
    task_queue = Queue()
    result_queue = Queue()
    error_task_queue = Queue()

    thread_lists = []
    detail_thread_lists = []

    for t in channel_types:
        thread_lists.append(ListDownloadThread(channnel_type=t, task_queue=task_queue))
    
    
    # h1 = DownloadThread('电视剧')
    # h2 = DownloadThread('电影')
    # h1.start()
    # h2.start()
    # h1.join()
    # h2.join()

    for i in range(3):
        detail_thread_lists.append(DetailDownloadThread(task_queue=task_queue, result_queue=result_queue))

    for t in thread_lists:
        t.start()

    for t in detail_thread_lists:
        t.start()

    for t in thread_lists:
        t.join()

    for t in detail_thread_lists:
        t.join()
    
    result_qq = []
    while not result_queue.empty():
        result_qq.append(result_queue.get())
    print(len(result_qq))
    import pprint
    pprint.pprint(result_qq)