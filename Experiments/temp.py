import pandas as pd
import numpy as np


def convert_column2ints(x):
    def test(a, b):
        # Return all elements from a that are not in b, make use of the fact that both a and b are unique and sorted
        a_ix = 0
        b_ix = 0
        new_uniques = []
        while a_ix < len(a) and b_ix < len(b):
            if a[a_ix] < b[b_ix]:
                new_uniques.append(a[a_ix])
                a_ix += 1
            elif a[a_ix] > b[b_ix]:
                b_ix += 1
            else:
                a_ix += 1
                b_ix += 1
        if a_ix < len(a):
            new_uniques.extend(a[a_ix:])
        return new_uniques

    print("PREPROCESSING: Converting", x.name)
    if x.name not in self.values:
        x = x.astype("str")
        self.values[x.name], y = np.unique(x, return_inverse=True)
        return y + 1
    else:
        x = x.astype("str")
        self.values[x.name] = np.append(self.values[x.name], test(np.unique(x), self.values[x.name]))

        print("PREPROCESSING: Substituting values with ints")
        xsorted = np.argsort(self.values[x.name])
        ypos = np.searchsorted(self.values[x.name][xsorted], x)
        indices = xsorted[ypos]

    return indices + 1


df = pd.read_csv('temp.csv')
df['test'] = df['case_IDofConceptCase'].astype(str) + '-' + df['case_Includes_subCases'].astype(str)
df.to_csv('temp.csv')