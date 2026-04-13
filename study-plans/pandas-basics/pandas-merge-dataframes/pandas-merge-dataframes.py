import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    left=pd.DataFrame(left)
    right=pd.DataFrame(right)
    merge=pd.merge(left,right,on=on,how=how)
    return merge.to_dict("list")
    pass