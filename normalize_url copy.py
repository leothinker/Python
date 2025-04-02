from urllib.parse import urlparse, urlunparse


def normalize_url(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Parse the URL
    parsed_url = urlparse(url)

    # Ensure the scheme and netloc are in lowercase
    scheme = parsed_url.scheme.lower() if parsed_url.scheme else "http"
    netloc = parsed_url.netloc.lower()

    # Remove trailing slashes from netloc and path
    netloc = netloc.rstrip("/")
    path = parsed_url.path.rstrip("/")

    # Rebuild the normalized URL
    return urlunparse(
        (scheme, netloc, path, parsed_url.params, parsed_url.query, parsed_url.fragment)
    )


print(normalize_url("https://technovationchallenge.org/sitemap.xml"))
