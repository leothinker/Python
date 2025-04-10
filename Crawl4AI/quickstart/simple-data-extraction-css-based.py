from crawl4ai import LLMConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

# Generate a schema (one-time cost)
html = "<div class='product'><h2>Gaming Laptop</h2><span class='price'>$999.99</span></div>"

# Using OpenAI (requires API token)
schema = JsonCssExtractionStrategy.generate_schema(
    html,
    llm_config=LLMConfig(
        provider="openai/gpt-4o", api_token="your-openai-token"
    ),  # Required for OpenAI
)

# Or using Ollama (open source, no token needed)
schema = JsonCssExtractionStrategy.generate_schema(
    html,
    llm_config=LLMConfig(
        provider="ollama/llama3.3", api_token=None
    ),  # Not needed for Ollama
)

# Use the schema for fast, repeated extractions
strategy = JsonCssExtractionStrategy(schema)
