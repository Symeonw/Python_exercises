import pandas as pd
import numpy as np
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

fruits.describe()
fruits.unique()
fruits.value_counts()
s = fruits.value_counts()
s.index[-1]
fruit_count = fruits.str.count()
print(fruit_count)
