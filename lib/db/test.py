import pandas as pd

data = pd.read_csv('books.csv', nrows= 2001)

print (data.title[1])