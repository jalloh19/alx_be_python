class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # Human-readable string (e.g., for print(book))
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    def __repr__(self):
        # Unambiguous string for debugging
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"

