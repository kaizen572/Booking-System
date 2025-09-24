import pandas as pd
from analysis import Analyzer

def test_top_authors():
    data = {
        'author': ['A', 'A', 'B', 'C', 'C', 'C'],
        'publication date': [2022, 2023, 2023, 2021, 2022, 2023],
        'language': ['English']*6,
        'book publisher': ['P1']*6,
        'ISBN': ['1', '2', '3', '4', None, '6']
    }
    df = pd.DataFrame(data)
    analyzer = Analyzer(df)
    top = analyzer.top_authors()
    assert top.iloc[0] == 3  


