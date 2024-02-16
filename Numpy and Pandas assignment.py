# int, str, float, bool can be used while creating a series object in pandas

import numpy as np
import pandas as pd
s = pd.Series(["1, 31 days", "2, 28 or 29 days", "3, 31 days", "4, 30 days", "5, 31 days", "6, 30 days", "7, 31 days", "8, 31 days", "9, 30 days", "10, 31 days", "11, 30 days", "12, 31 days"],
              index = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
              name = "Year")

a = pd.Series(["27", "29", "36", "33"],
              ["MatMIE", "Mat DAIS", "COMIE", "COMEC"],
              name = "Groups")

m = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']},
                index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
                
print(s, '\n')
print(a, '\n')
print(m, '\n')
print(m.loc[m.attempts >= 3], '\n')