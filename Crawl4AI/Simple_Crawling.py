import asyncio

from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CacheMode, CrawlerRunConfig


async def main():
    browser_config = BrowserConfig(verbose=True)  # Default browser configuration
    run_config = CrawlerRunConfig(
        # Content filtering
        word_count_threshold=10,  # Minimum words per content block
        excluded_tags=["form", "header"],
        exclude_external_links=True,  # Remove external links
        # Content processing
        process_iframes=True,  # Process iframe content
        remove_overlay_elements=True,  # Remove popups/modals
        # Cache control
        cache_mode=CacheMode.ENABLED,  # Use cache if available
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.lib.cuhk.edu.hk/en/", config=run_config
        )

        # Check success status
        if result.success:  # True if crawl succeeded
            # Print clean content
            print("Content:", result.markdown[:500])  # First 500 chars

            # Process images
            for image in result.media["images"]:
                print(f"Found image: {image['src']}")

            # Process links
            for link in result.links["internal"]:
                print(f"Internal link: {link['href']}")

        else:
            print(f"Crawl failed: {result.error_message}")


if __name__ == "__main__":
    asyncio.run(main())
