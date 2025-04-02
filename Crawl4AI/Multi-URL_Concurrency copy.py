import asyncio
import time

# from urllib.parse import urljoin, urlparse
# from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler


async def fetch_and_extract(crawler, url):
    """
    使用 Crawl4AI 爬取页面，并用 BeautifulSoup 提取所有链接
    """
    try:
        result = await crawler.arun(url=url)
        # html = result.html  # 假设返回对象中有 raw HTML
        # soup = BeautifulSoup(html, "html.parser")
        links = set([item["href"] for item in result.links["internal"]])
        # # 提取所有 <a> 标签的 href 属性
        # for a in soup.find_all("a", href=True):
        #     link = a["href"]
        #     # 将相对链接转换为绝对链接
        #     absolute_link = urljoin(url, link)
        #     # 可添加过滤条件：比如只爬取同域的链接
        #     if urlparse(absolute_link).netloc == urlparse(url).netloc:
        #         links.add(absolute_link)
        return links
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return set()


async def worker(crawler, queue, visited, max_depth):
    """
    工作协程：不断从队列取出 URL 爬取并提取新链接
    """
    while True:
        try:
            url, depth = await asyncio.wait_for(queue.get(), timeout=3)
        except asyncio.TimeoutError:
            break  # 队列暂时没有任务则退出
        if depth >= max_depth:
            queue.task_done()
            continue
        links = await fetch_and_extract(crawler, url)
        for link in links:
            if link not in visited:
                visited.add(link)
                await queue.put((link, depth + 1))
        queue.task_done()


async def bfs_crawl(start_urls, max_depth=2, max_workers=10):
    """
    主函数：初始化队列、启动 Crawl4AI 与多个 worker 协程进行并行 BFS 爬取
    """
    visited = set()
    queue = asyncio.Queue()

    # 将起始 URL 放入队列，并加入 visited 集合
    for url in start_urls:
        await queue.put((url, 0))
        visited.add(url)

    async with AsyncWebCrawler() as crawler:
        # 启动多个 worker 协程
        tasks = [
            asyncio.create_task(worker(crawler, queue, visited, max_depth))
            for _ in range(max_workers)
        ]
        # 等待队列所有任务完成
        await queue.join()
        # 取消所有工作协程
        for task in tasks:
            task.cancel()
        # 等待 worker 退出
        await asyncio.gather(*tasks, return_exceptions=True)

    return visited


if __name__ == "__main__":
    # 示例起始 URL 列表
    start_urls = ["http://info.aims.cuhk.edu.hk"]

    start_time = time.time()

    # 执行 BFS 爬取，限制最大深度为 3 层
    visited_urls = asyncio.run(bfs_crawl(start_urls, max_depth=2, max_workers=10))
    # print("爬取到的 URL：")
    # for url in visited_urls:
    #     print(url)

    print(
        f"{len(visited_urls)} web pages time costs: {int(time.time() - start_time)} seconds"
    )
    with open("visited_urls.txt", "w", encoding="utf-8") as f:
        for url in visited_urls:
            f.write(url + "\n")
