import ssl
import urllib.request as rq
import xml.dom.minidom as xmldom
from urllib.parse import urljoin, urlparse

# import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
}
url = "https://cpii.hk/"
# response = requests.get(
#     url,
#     headers=headers,
#     timeout=16,
#     allow_redirects=True,
#     verify=False,
# )
# url_startings = response.url.strip("/").lower()

sitemap_url = urljoin(url, "/sitemap.xml")
print(url)
print(sitemap_url)

try:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    http = rq.Request(url=sitemap_url, headers=headers)
    http_run = rq.urlopen(http, context=ctx)
    dom = xmldom.parse(http_run)
    print(http_run.read())
except Exception as e:
    print(e)


# # print(dom.documentElement.getElementsByTagName("sitemap"))
# xmls = dom.documentElement.getElementsByTagName("sitemap")

# for url_xml in xmls:
#     url = url_xml.getElementsByTagName("loc")[0]
#     print(url.firstChild.data)
# # x = requests.get(sitemap_url)
# # print(x.text)


# # print(urlparse("https://www.lib.cuhk.edu.hk/en/"))


# assert True
# print("hello")
