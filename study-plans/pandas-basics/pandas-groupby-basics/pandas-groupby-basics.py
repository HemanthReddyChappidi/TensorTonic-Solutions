import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    df=pd.DataFrame(data)
    groped = df.groupby(group_col)[value_col]
    return groped.agg(['sum','mean','count']).to_dict()
    
    pass