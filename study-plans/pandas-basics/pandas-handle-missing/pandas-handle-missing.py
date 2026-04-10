import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """

    df=pd.DataFrame(data)
    null_counts=df.isna().sum().to_dict()
    df_filled = df.fillna(fill_value)
    cleaned_data = df_filled.to_dict(orient="list")

    return {
        "null_counts": null_counts,
        "cleaned_data": cleaned_data
    }
    
    pass