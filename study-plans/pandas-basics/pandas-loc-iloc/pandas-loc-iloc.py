import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """

    df=pd.DataFrame(data)
    element=df.iloc[row,col]
    row_val=df.iloc[row, :].tolist()
    col_val=df.iloc[:,col].tolist()

    return [element,row_val,col_val]
    


    
    pass