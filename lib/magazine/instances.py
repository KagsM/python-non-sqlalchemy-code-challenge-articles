from author import Author
from magazine import Magazine
from article import Article

print("\n--- AUTHOR TESTS ---")
# Create authors
author1 = Author("Malcolm")
author2 = Author("Caren")
print(f"Author 1: {author1.name}")
print(f"Author 2: {author2.name}")

try:
    author1.name = "New Name"
except AttributeError:
    print("Author name is immutable")

print("\n--- MAGAZINE TESTS ---")
# Create magazines
mag1 = Magazine("Tech Today", "Technology")
mag2 = Magazine("Code Life", "Programming")

print(f"Magazine 1: {mag1.name}, Category: {mag1.category}")
print(f"Magazine 2: {mag2.name}, Category: {mag2.category}")

# Test setters
mag1.name = "AI Monthly"
mag1.category = "AI"
print(f"Updated Magazine 1: {mag1.name}, Category: {mag1.category}")

print("\n--- ARTICLE TESTS ---")
# Create articles
article1 = Article(author1, mag1, "The Rise of AI")
article2 = Article(author1, mag2, "Python Tips")
article3 = Article(author1, mag2, "Decorators Explained")
article4 = Article(author1, mag2, "Advanced Python")

print(f"Article 1 Title: {article1.title}")
try:
    article1.title = "New Title"
except AttributeError:
    print("Article title is immutable")

# Test author/magazine mutability
article1.author = author2
article1.magazine = mag2
print(f"Article 1 New Author: {article1.author.name}")
print(f"Article 1 New Magazine: {article1.magazine.name}")

print("\n--- AUTHOR METHODS ---")
# Test articles and magazines
print("Author 1 Articles:", [a.title for a in author1.articles])
print("Author 1 Magazines:", [m.name for m in author1.magazines])
print("Author 1 Topic Areas:", author1.topic_areas())

print("\n--- MAGAZINE METHODS ---")
# Test magazine's articles and contributors
print("Mag2 Articles:", [a.title for a in mag2.articles])
print("Mag2 Contributors:", [a.name for a in mag2.contributors])
print("Mag2 Article Titles:", mag2.article_titles())
print("Mag2 Contributing Authors:", [a.name for a in mag2.contributing_authors() or []])

print("\n--- BONUS: TOP PUBLISHER ---")
top_mag = Magazine.top_publisher()
if top_mag:
    print("Top Publisher:", top_mag.name)
else:
    print("No top publisher yet")