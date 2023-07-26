from dataclasses import dataclass
from typing import List


@dataclass
class NewsData():
    title: str
    body: str
    published_original: str
    published_latest: str
    location: str
    category: List[str]
    authors: List[str]
    thumbnail_url: str
    article_url: str
    tags: List[str]
