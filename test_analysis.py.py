import pandas as pd
from analysis import Analyzer

def test_missing_isbn():
    df = pd.DataFrame({
        'ISBN': ['123', None, '456', None],
        'author': ['A', 'B', 'C', 'D'],
        'publication date': [2022, 2023, 2023, 2022],
        'language': ['English'] * 4,
        'book publisher': ['P1'] * 4
    })

    analyzer = Analyzer(df)
    missing, percent = analyzer.missing_isbn()
    assert missing == 2
    assert round(percent, 2) == 50.00

def test_top_authors():
    df = pd.DataFrame({
        'ISBN': ['111', '222', '333', '444', '555'],
        'author': ['A', 'A', 'B', 'C', 'C'],
        'publication date': [2020, 2021, 2021, 2022, 2022],
        'language': ['English'] * 5,
        'book publisher': ['P1'] * 5
    })

    analyzer = Analyzer(df)
    result = analyzer.top_authors()
    
    assert result.index[0] == 'A'
    assert result.iloc[0] == 2
    assert len(result) == 3  # Only 3 authors exist in mock data

def test_language_distribution():
    df = pd.DataFrame({
        'ISBN': ['1', '2', '3', '4'],
        'author': ['A', 'B', 'C', 'D'],
        'publication date': [2020, 2020, 2021, 2022],
        'language': ['English', 'French', 'English', 'French'],
        'book publisher': ['P1'] * 4
    })

    analyzer = Analyzer(df)
    result = analyzer.language_distribution()

    assert result['English'] == 2
    assert result['French'] == 2
    assert result.sum() == 4

def test_books_per_year():
    df = pd.DataFrame({
        'ISBN': ['x1', 'x2', 'x3', 'x4', 'x5'],
        'author': ['A', 'B', 'C', 'D', 'E'],
        'publication date': [2020, 2021, 2020, 2021, 2020],
        'language': ['English'] * 5,
        'book publisher': ['P1'] * 5
    })

    analyzer = Analyzer(df)
    result = analyzer.books_per_year()

    assert result[2020] == 3
    assert result[2021] == 2
    assert result.sum() == 5
