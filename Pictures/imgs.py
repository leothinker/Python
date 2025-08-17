import os
import re

import js2py  # 用于执行 JS 解密代码
import requests
from bs4 import BeautifulSoup
from lzstring import LZString

HEADERS = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.manhuagui.com/"}


def get_img_data_urls(chapter_url):
    resp = requests.get(chapter_url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, "html.parser")
    script = soup.find("script", text=re.compile(r"img_data"))
    if not script:
        raise Exception("未找到 img_data 脚本")
    base64_str = re.search(r'img_data\s*=\s*"([^"]+)"', script.string).group(1)
    images = LZString().decompressFromBase64(base64_str).split("|")
    chapter_url_cur = chapter_url
    return [requests.compat.urljoin(chapter_url_cur, img) for img in images]


def download_images(img_urls, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    session = requests.Session()
    session.headers.update(HEADERS)
    for idx, url in enumerate(img_urls, 1):
        # 强制使用 .png 或 .jpg 后缀
        ext = ".png" if url.lower().endswith(".png.webp") else ".jpg"
        fname = f"{idx:03d}{ext}"
        out = os.path.join(save_dir, fname)
        r = session.get(url, stream=True)
        if r.status_code == 200:
            with open(out, "wb") as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            print(f"✅ 下载: {fname}")
        else:
            print(f"⚠️ 错误状态 {r.status_code}: {url}")


def crawl_chapter(base_url, chapter_base_url, save_root):
    page = 1
    while True:
        url = f"{chapter_base_url.split('#')[0]}?p={page}"
        try:
            img_urls = get_img_data_urls(url)
        except Exception as e:
            print("🔚 结束，无法获取第", page, "页:", e)
            break
        save_dir = os.path.join(save_root, f"page_{page:03d}")
        print("➡️ 页面", page, "共", len(img_urls), "张图片")
        download_images(img_urls, save_dir)
        page += 1


if __name__ == "__main__":
    BASE = "https://www.manhuagui.com/comic/1147"
    CHAPTER = "https://www.manhuagui.com/comic/1147/10498.html"
    crawl_chapter(BASE, CHAPTER, "downloaded_chapter")
