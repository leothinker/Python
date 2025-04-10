import asyncio

from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig


async def main():
    urls = ["https://example1.com", "https://example2.com", "https://example3.com"]

    config = CrawlerRunConfig(
        cache_mode=CacheMode.ENABLED,
        check_robots_txt=True,  # Will respect robots.txt for each URL
        semaphore_count=3,  # Max concurrent requests
    )

    async with AsyncWebCrawler() as crawler:
        async for result in crawler.arun_many(urls, config=config):
            if result.success:
                print(f"Successfully crawled {result.url}")
            elif result.status_code == 403 and "robots.txt" in result.error_message:
                print(f"Skipped {result.url} - blocked by robots.txt")
            else:
                print(f"Failed to crawl {result.url}: {result.error_message}")


if __name__ == "__main__":
    asyncio.run(main())
