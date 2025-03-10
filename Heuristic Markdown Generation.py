import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import PruningContentFilter, BM25ContentFilter
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
        #     content_filter=BM25ContentFilter(user_query="WHEN_WE_FOCUS_BASED_ON_A_USER_QUERY", bm25_threshold=1.0)
        # ),
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://docs.micronaut.io/4.7.6/guide/", config=run_config
        )
        # print(len(result.markdown.raw_markdown))
        # print(len(result.markdown.fit_markdown))
        with open("raw_output.md", "w", encoding="utf-8") as file:
            file.write(result.markdown.raw_markdown)
        with open("fit_output.md", "w", encoding="utf-8") as file:
            file.write(result.markdown.fit_markdown)


if __name__ == "__main__":
    asyncio.run(main())
