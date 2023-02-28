import requests

def get_list_page(url):
    # "http://129.204.87.3:8877/getsortdata_all_z.php?action=mov&page=1&year=0&area=all&class=0&dect=&id="
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Content-Type': 'text/heml;charset=utf-8'})
    res.encoding = None
    if res.status_code == 200:
        with open('list_page.html', 'wb') as f:
            f.write(res.content)
        print('list page download success')
    else:
        print('something error')


def get_detail_pate(url):
    #"http://www.yhdm6.com/mov/15514/"
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Content-Type': 'text/heml;charset=utf-8'})
    res.encoding = None
    if res.status_code == 200:
        with open('detail_page.html', 'wb') as f:
            f.write(res.content)
        print('list page download success')
    else:
        print('something error')


if __name__ == "__main__":
    get_list_page(r"http://129.204.87.3:8877/getsortdata_all_z.php?action=mov&page=1&year=0&area=all&class=0&dect=&id=")
    get_detail_pate(r"http://www.yhdm6.com/mov/15514/")
