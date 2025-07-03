import os

import requests


def download_images(base_url, start, end, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    exts = ["jpg", "png", "gif"]
    for i in range(start, end + 1):
        num = f"{i:03d}"
        try:
            for ext in exts:
                filename = f"{num}.{ext}"
                url = f"{base_url}/{filename}"
                resp = requests.get(url, stream=True)
                if resp.status_code == 200:
                    file_path = os.path.join(save_dir, filename)
                    with open(file_path, "wb") as f:
                        for chunk in resp.iter_content(1024):
                            f.write(chunk)
                    print(f"✅ 下载成功: {filename}")
                    break
            else:
                print(f"⚠️ 未找到: {num}.[jpg/png/gif]")
        except Exception as e:
            print(f"❌ 失败: {filename}，错误: {e}")


if __name__ == "__main__":
    download_images(
        base_url="https://example.com/images",
        start=1,
        end=100,
        save_dir="downloaded_images",
    )
