import requests
from bs4 import BeautifulSoup
import re

def search_google(keyword, start_page, end_page=None):
    url = "https://www.google.com/search?q={0}+magnet%3A%3Fxt%3D&oq={0}+magnet%3A%3Fxt%3D".format(keyword)
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36,gzip(gfe)"}
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, "lxml")
    divs = bs.find_all("div", attrs={"data-header-feature": True})
    results = []

    if end_page is None:
        count_div = bs.select_one("div#result-stats")
        count_txt = count_div.text
        count = int(count_txt.split("개")[0].split("약")[-1].strip().replace(",", ""))
        end_page = count / 10
        if end_page > 20:
            end_page = 20

    for d in divs:
        link = d.select_one("div > a")
        href = link.get("href")
        title = link.text
        try:
            r = requests.get(href)
            bs = BeautifulSoup(r.text, "lxml")
            magnets = bs.findAll(text=re.compile(r'magnet:\?*'))
            if len(magnets) > 0:
                magnet = "magnet:" + magnets[0].split("magnet:")[-1]
                if magnet.find("magnet:?xt=urn:btih:") >= 0:
                    results.append((title, magnet))
        except:
            pass
    
    if start_page < end_page:
        start_page += 10
        results.extend(search_google(keyword, start_page, end_page=end_page))

    return results

results = search_google("리눅스", 0)

for r in results:
    print(r)