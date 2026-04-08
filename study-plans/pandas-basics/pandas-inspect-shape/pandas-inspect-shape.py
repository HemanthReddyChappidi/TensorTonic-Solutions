import pandas as pd

def inspect_dataframe(data):

    df=pd.DataFrame(data)

    return {
        "rows": int(df.shape[0]),
        "cols": int(df.shape[1]),
        "columns": df.columns.tolist(),
        "dtypes": {col: str(dtype) for col ,dtype in df.dtypes.items()},
        "total_values": int(df.size)
    }
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    pass