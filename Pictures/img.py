import os

import requests


def download_images(url_list, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    headers = {
        "Referer": "https://www.manhuagui.com/",  # 漫画柜一般需要 Referer
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    }
    for url in url_list:
        fname = os.path.basename(url).split("?")[0]
        path = os.path.join(save_dir, fname)
        try:
            resp = requests.get(url, headers=headers, stream=True)
            if resp.status_code == 200:
                with open(path, "wb") as f:
                    for chunk in resp.iter_content(1024):
                        f.write(chunk)
                print(f"✅ 下载成功: {fname}")
            else:
                print(f"⚠️ 失败状态码: {resp.status_code} → {url}")
        except Exception as e:
            print(f"❌ 下载异常: {url}，错误：{e}")


if __name__ == "__main__":
    # 示例：你已知具体图片 URLs
    urls = [
        "https://eu2.hamreus.com/ps1/h/HFLY/01/seemh-001-fe10.png.webp?e=1754755200&m=99uFlXINFVsjpF6yJaeU6g",
        # 可继续添加更多 URL...
    ]
    download_images(urls, "manhua_images")
