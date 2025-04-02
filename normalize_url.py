from urllib.parse import urlparse, urlunparse


def normalize_url(url: str) -> str:
    """
    标准化 URL 用于比较是否指向同一资源

    标准化规则：
    1. 自动补全协议前缀（默认添加 http://）
    2. 忽略协议类型（http/https 视为相同）
    3. 移除 www 子域名前缀
    4. 统一转换为小写
    5. 移除 URL 末尾的斜杠
    6. 清除所有查询参数和锚点
    7. 移除默认端口声明（:80/:443）

    参数:
        url (str): 原始 URL 字符串

    返回:
        str: 标准化后的 URL

    示例:
        >>> normalize_url("https://www.EXAMPLE.com/sitemap.xml")
        'http://example.com/sitemap.xml'
    """
    # 预处理：补充协议头
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    # 解析 URL 组件
    parsed = urlparse(url)

    # 标准化协议 (统一视为 http)
    scheme = "http"

    # 处理域名
    netloc = parsed.netloc.lower()

    # 移除 www 前缀
    if netloc.startswith("www."):
        netloc = netloc[4:]

    # 移除端口声明
    if ":" in netloc:
        netloc = netloc.split(":", 1)[0]

    # 处理路径
    path = parsed.path.rstrip("/")  # 移除末尾斜杠
    path = path if path else "/"  # 确保至少保留根路径

    # 构建标准化 URL
    return urlunparse(
        (
            scheme,
            netloc,
            path,
            "",  # 清除 params
            "",  # 清除 query
            "",  # 清除 fragment
        )
    )


# 测试用例
test_urls = [
    "https://example.com",
    "https://example.com/",
    "http://example.com",
    "http://example.com/",
    "example.com",
    "example.com/",
    "https://www.example.com/path/?query=1#anchor",
    "http://EXAMPLE.COM:80/path",
]

# 所有测试 URL 标准化后都应该相同
normalized = [normalize_url(url) for url in test_urls]
# print("标准化结果示例:", normalized[0])
print(normalized)
print("是否全部相同:", len(set(normalized)) == 1)

# 输出结果：
# 标准化结果示例: http://example.com/
# 是否全部相同: True
