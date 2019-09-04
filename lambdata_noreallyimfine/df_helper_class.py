import random
import pandas as pd


class Helper:
    """ DataFrame Helper Class - some useful tools for working with
    Pandas DataFrames """
    def __init__(self, df):
        self.df = df
        self.length = len(df)
        self.shape = df.shape
        self.cols = [col for col in df.columns]

    def more_rows(self, num):
        """ Function to generate more rows for DataFrame, by picking a random
        value from each column """

        for i in range(num):
            new_row = []
            for j in range(len(self.cols)):
                vals = list(self.df[self.cols[j]])
                new_row.append(random.choice(vals))
            s = pd.Series(new_row, index=self.cols)
            self.df = self.df.append(s, ignore_index=True)

        print(f'{num} rows added!')
        return self.df

    def add_list(self, l):
        """ Function to add a list to a Pandas DataFrame """

        s = pd.Series(l, index=self.cols)
        self.df = self.df.append(s, ignore_index=True)

        print("List appended to end of DataFrame!")
        return self.df

    def split_date(self, col):
        """ Function to split a date into separate components of year, month,
        and day """
        if self.df[col].dtype != 'datetime64[ns]':
            self.df[col] = pd.to_datetime(self.df[col])

        name = self.df[col].name
        self.df[f'{name}_year'] = self.df[col].dt.year
        self.df[f'{name}_month'] = self.df[col].dt.month
        self.df[f'{name}_day'] = self.df[col].dt.day

        self.df[f'{name}_month'] = self.df[f'{name}_month'].map({
            1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
            6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
            11: 'November', 12: 'December'
            })

        return self.df
