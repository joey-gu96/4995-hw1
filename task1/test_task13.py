import pandas as pd
def test_task13():
    data = pd.read_csv("task1/input.txt", encoding = 'UTF-16',  index_col = 0, escapechar = '\\')
    assert data.shape[0] == 225
    assert data.shape[1] == 31
