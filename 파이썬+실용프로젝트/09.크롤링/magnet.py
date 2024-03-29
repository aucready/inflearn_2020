import requests
from bs4 import BeautifulSoup
import re

"리눅스 magent:?xt="

def search_google(keyword, start_page, end_page=None):
    url = "https://www.google.com/search?q={0}+magnet%3A%3Fxt%3D&oq={0}+magnet%3A%3Fxt%3D".format(keyword)
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36,gzip(gfe)"}
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, "lxml")
    links = bs.select("div.g > div > div.rc > div.r > a")

    results = []

    if end_page is None:
        counts = bs.select("div#resultStats")[0].text.replace("검색결과 약", "").replace("개", "").replace(",", "").split("(")[0].strip()
        end_page = int(int(counts) / 10)
        if end_page > 20:
            end_page = 20

    for a in links:
        href = a["href"]
        text = a.select("h3")
        if len(text) <= 0:
            continue
        title = text[0].text

        try:
            r = requests.get(href)
            bs = BeautifulSoup(r.text, "lxml")
            magnets = bs.find_all("a", href=re.compile(r'magnet:\?xt=*'))

            if len(magnets) > 0:
                magnet = magnets[0]["href"]
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