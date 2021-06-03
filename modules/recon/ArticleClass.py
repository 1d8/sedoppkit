class Article:
    def __init__(self, publishDate, articleTitle, articleShort, articleURL):
        self.publishDate = publishDate
        self.articleTitle = articleTitle
        self.articleShort = articleShort
        self.articleURL = articleURL
    def Date(self):
        return self.publishDate
    def Title(self):
        return self.articleTitle
    def Description(self):
        return self.articleShort
    def URL(self):
        return self.articleURL