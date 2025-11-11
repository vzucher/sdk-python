"""Bright Data Python SDK - Modern async-first SDK for Bright Data APIs."""

__version__ = "2.0.0"

# Export result models
from .models import (
    BaseResult,
    ScrapeResult,
    SearchResult,
    CrawlResult,
    Result,
)

__all__ = [
    "__version__",
    "BaseResult",
    "ScrapeResult",
    "SearchResult",
    "CrawlResult",
    "Result",
]

