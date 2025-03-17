import asyncio

from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig
from crawl4ai.content_filter_strategy import BM25ContentFilter, PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def main():
    browser_config = BrowserConfig(
        headless=True,
        verbose=True,
    )
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.ENABLED,
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(
                threshold=0.48, threshold_type="fixed", min_word_threshold=0
            )
        ),
        # markdown_generator=DefaultMarkdownGenerator(
        #     content_filter=BM25ContentFilter(
        #         user_query="WHEN_WE_FOCUS_BASED_ON_A_USER_QUERY", bm25_threshold=1.0
        #     )
        # ),
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://docs.micronaut.io/4.7.6/guide/", config=run_config
        )
        print(len(result.markdown.raw_markdown))
        print(len(result.markdown.fit_markdown))


if __name__ == "__main__":
    asyncio.run(main())
