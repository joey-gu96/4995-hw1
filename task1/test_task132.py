import pandas as pd
def test_task132():
    data = pd.read_csv("input.txt", encoding = 'UTF-16',  index_col = 0, escapechar = '\\')
    data['2010'] = data['2010'].replace('--', 0)
    data.fillna(0)
    data['2010'] = pd.to_numeric(data['2010'])
    total = data['2010'].sum()
    assert round(total) == 7065
