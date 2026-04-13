import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    frames=[pd.DataFrame(d) for d in dfs]
    con=pd.concat(frames, ignore_index=True)
    return [list(con.shape),con.to_dict("list")]
    pass