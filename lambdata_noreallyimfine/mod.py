### lambdata-noreallyimfine module

### Methods to build

# train_val_test split
# generate more data for df
# add list to df by changing into Series
# split dates into multiple columns

import random
import pandas as pd 
from sklearn.model_selection import train_test_split

def three_way_split(df, test_size=0.2, val_size=0.2):
    
    """
    Function: takes in dataframe
    and splits into 3 for train, val,
    test split. 

    Arguments: 
    df - Pandas DataFrame
    test_size - float(0-1). Size of test and val sets.
    Default 0.2 for 60/20/20 split.
    val_size - float(0-1). Size of test and val sets.
    Default 0.2 for 60/20/20 split.

    Returns:
    List of 3 dfs. Default 60/20/20 split.
    """

    train, test = train_test_split(df, test_size=test_size)

    train, val = train_test_split(train, test_size=val_size)

    return train, val, test

def more_data(df):
    """
    Function: Create new rows for df from
    existing values in the columns of df
	
    Arguments: 
    df - Pandas Dataframe

    Returns:
    DataFrame with 1 row added.
    """
    cols = [col for col in df.columns]
    new_row = []
    
    for i in range(len(cols)):
        vals = list(df[cols[i]])
        new_row.append(random.choice(vals))
    
    s = pd.Series(new_row, index=cols)
    df = df.append(s, ignore_index=True)

    return df


