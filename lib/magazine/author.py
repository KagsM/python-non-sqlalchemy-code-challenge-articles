from article import Article
from magazine import Magazine

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Author name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return [article for article in Article.all if article.author == self]

    @property
    def magazines(self):
        return list({article.magazine for article in self.articles})

    def write_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({article.magazine.category for article in self.articles if article.magazine})