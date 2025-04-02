import asyncio
import json

from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def main():
    md_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.4, threshold_type="fixed")
    )

    browser_conf = BrowserConfig(headless=True)  # or False to see the browser
    run_conf = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS, markdown_generator=md_generator
    )

    async with AsyncWebCrawler(config=browser_conf) as crawler:
        result = await crawler.arun(url="https://cuhk.edu.hk/", config=run_conf)

        with open("output.md", "w", encoding="utf-8") as file:
            file.write(result.markdown)
        with open("raw_output.md", "w", encoding="utf-8") as file:
            file.write(result.markdown.raw_markdown)
        with open("fit_output.md", "w", encoding="utf-8") as file:
            file.write(result.markdown.fit_markdown)
        with open("links.json", "w", encoding="utf-8") as file:
            print(len(result.links["internal"]))
            json.dump(result.links, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    asyncio.run(main())
