class Analyzer:
    def __init__(self, df):
        self.df = df

    def books_per_year(self):
        return self.df['publication date'].value_counts().sort_index()
    # Group by year and language, reshape for plotting
    def top_authors(self):
        return self.df['author'].value_counts().head(5)

    def language_distribution(self):
        return self.df['language'].value_counts()

    def books_per_publisher(self):
        return self.df['book publisher'].value_counts()

    def missing_isbn(self):
        total = len(self.df)
        missing = self.df['ISBN'].isnull().sum()
        return missing, (missing / total) * 100

    def books_year_language(self):
        return self.df.groupby(['publication date', 'language']).size().unstack().fillna(0)
