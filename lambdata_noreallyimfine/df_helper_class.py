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
        s = pd.Series(l, index=self.cols)
        self.df = self.df.append(s, ignore_index=True)

        print("List appended to end of DataFrame!")
        return self.df
