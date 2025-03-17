import asyncio
import os
import sys
import time
from pathlib import Path

from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig


async def test_news_crawl():
    # Create a persistent user data directory
    user_data_dir = os.path.join(Path.home(), ".crawl4ai", "browser_profile")
    os.makedirs(user_data_dir, exist_ok=True)

    browser_config = BrowserConfig(
        verbose=True,
        headless=True,
        user_data_dir=user_data_dir,
        use_persistent_context=True,
    )
    run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        url = "ADDRESS_OF_A_CHALLENGING_WEBSITE"

        result = await crawler.arun(
            url,
            config=run_config,
            magic=True,
        )

        print(f"Successfully crawled {url}")
        print(f"Content length: {len(result.markdown)}")
