from article import Article

class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category.strip()) == 0:
            raise Exception("Category must be a non-empty string")

        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    @property
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    @property
    def contributors(self):
        return list({article.author for article in self.articles})

    def article_titles(self):
        return [article.title for article in self.articles]

    def contributing_authors(self):
        author_count = {}
        for article in self.articles:
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        return [author for author, count in author_count.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles))