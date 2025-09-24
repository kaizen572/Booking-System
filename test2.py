import pandas as pd
import pandas.testing as pdt
from analysis import Analyzer

# Sample DataFrame for testing
sample_data = {
    'book': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E', 'Book F'],
    'author': ['Author 1', 'Author 2', 'Author 1', 'Author 3', 'Author 2', 'Author 1'],
    'publication date': ['2020', '2021', '2022', '2020', '2021', '2022'],
    'language': ['English', 'English', 'French', 'French', 'English', 'English'],
    'book publisher': ['Pub A', 'Pub B', 'Pub A', 'Pub C', 'Pub B', 'Pub A'],
    'ISBN': ['123', None, '789', '456', '012', None],
    'bnb id': ['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6']
}

df = pd.DataFrame(sample_data)
analyzer = Analyzer(df)

def test_books_per_year():
    result = analyzer.books_per_year()
    expected = pd.Series({'2020': 2, '2021': 2, '2022': 2})
    expected.index.name = 'publication date'
    expected.name = 'count'
    pdt.assert_series_equal(result, expected)

def test_top_authors():
    result = analyzer.top_authors()
    expected = pd.Series({'Author 1': 3, 'Author 2': 2, 'Author 3': 1})
    expected.index.name = 'author'  # <-- fix
    expected.name = 'count'
    pdt.assert_series_equal(result, expected)

def test_language_distribution():
    result = analyzer.language_distribution()
    expected = pd.Series({'English': 4, 'French': 2})
    expected.index.name = 'language'  # <-- fix
    expected.name = 'count'
    pdt.assert_series_equal(result, expected)

def test_books_per_publisher():
    result = analyzer.books_per_publisher()
    expected = pd.Series({'Pub A': 3, 'Pub B': 2, 'Pub C': 1})
    expected.index.name = 'book publisher'  # <-- fix
    expected.name = 'count'
    pdt.assert_series_equal(result, expected)

def test_missing_isbn():
    missing, percent = analyzer.missing_isbn()
    assert missing == 2
    assert round(percent, 2) == 33.33

def test_books_year_language_structure():
    result = analyzer.books_year_language()
    expected = pd.DataFrame({
        'English': {'2020': 1.0, '2021': 1.0, '2022': 1.0},
        'French': {'2020': 1.0, '2021': 1.0, '2022': 0.0}
    }).fillna(0)
    expected.index.name = 'publication date'
    expected.columns.name = 'language'  # <-- fix
    pdt.assert_frame_equal(result, expected)
