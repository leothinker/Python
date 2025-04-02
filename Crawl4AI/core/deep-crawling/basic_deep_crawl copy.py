import asyncio
import json
import time

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy


async def main():
    # Configure a 2-level deep crawl
    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=2, include_external=False),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True,
    )

    time_start = time.time()
    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun("https://medium.com/", config=config)
    time_end = time.time()

    sublinks = []
    # Access individual results
    for result in results:  # Show first 3 results
        sublinks.append(result.url)

    print(f"Crawled {len(results)} pages in total")
    print(f"Crawled {len(set(sublinks))} different html pages in total")
    print("total time cost:", time_end - time_start)
    sublinks.sort()
    with open("medium_crawl4ai_depth2.json", "w") as final:
        json.dump(sublinks, final)


if __name__ == "__main__":
    asyncio.run(main())
