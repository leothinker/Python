import asyncio
import time

from crawl4ai import *


async def main():
    time_start = time.time()
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.innohk.gov.hk/",
        )
    time_end = time.time()

    sublinks = []
    for link in result.links["internal"]:
        sublinks.append(link["href"])

    sublinks.sort()
    print(sublinks)
    print(len(sublinks))
    print("total time cost:", time_end - time_start)


if __name__ == "__main__":
    asyncio.run(main())
