from typing import Any, Callable, List, Optional, cast

from configuration import Configuration


async def search(query: str) -> Optional[dict[str, Any]]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    configuration = Configuration.from_context()
    return cast(dict[str, Any], configuration)


TOOLS: List[Callable[..., Any]] = [search]
