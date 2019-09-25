import pandas as pd
import numpy as np
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

fruits.describe()


fruits.unique()


fruits.value_counts()


s = fruits.value_counts()


s.index[0]


s.index[-1]

ftnu = fruits.unique()
ftn = pd.Series(ftnu)
length_of_longest = ftn.str.len().max()
index_of_long = ftn.str.len().idxmax()
ftn[index_of_long]

fruits_count = lambda x: fruits.count()
print (fruits[fruit_count >= 5])


fruits_cap = fruits.str.capitalize()


fruits.apply(lambda x: x.count("a")
count_a = fruits.str.count("a")
list(zip(fruits, count_a))

count_o = lambda x: x.count("o")
fruits[fruits.apply(count_o)]

def count_vowels(x):
    vowels = "aeiouAEIOU"
    count = 0
    for n in x:
        count += n in vowels
    return count

fruits.apply(count_vowels)
fruits[fruits.str.contains("berry")]
fruits[fruits.str.contains("apple")]
fruits[fruits.apply(count_vowels).idxmax]


f = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
f = pd.Series(f)
#What is the data type of the series?
#dtype: object

f = f.replace('[\$,]', '', regex=True).astype(float)

f.max()
f.min()
pd.cut(f, [1000000,2000000,3000000,40000000])
f.plot.hist()
e = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
e = pd.Series(e)
e.min()
e.max()
e.mean()
e.median()
e.plot.hist()
def grade(x):
    if x > 89:
        return "A"
    elif x >79:
        return "B"
    elif x >69:
        return "C"
    else:
        return "F"

e.apply(grade)

e = pd.Series([n + 100 - e.max() for n in list(e)])


x = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
x = pd.Series(x)
x.mode()[0]
x.apply(count_vowels)






x = lambda x, func: x + func(x)
x(3, lambda x: x * x)


