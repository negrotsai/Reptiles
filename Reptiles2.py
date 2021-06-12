# ptt八卦版
import bs4
import urllib.request as req


def getdata(url):
    request = req.Request(url, headers={
        # 滿18
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        print(data)
    root = bs4.BeautifulSoup(data, "html.parser")
    #titles = root.find("div", class_="title")
    # print(titles)
    # print(titles.a.string)
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
    # 抓取上一頁網址
    nextLink = root.find("a", string="‹ 上頁")  # 找內文是‹ 上頁的a標籤
    return (nextLink["href"])


# 抓取一個頁面標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 5:
    pageURL = "https://www.ptt.cc"+getdata(pageURL)
    count += 1
    print(pageURL)
