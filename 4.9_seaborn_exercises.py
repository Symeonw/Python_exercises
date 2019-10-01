import seaborn as sns
import pydataset as py
import pandas as pd
import matplotlib.pyplot as plt
iris = data("iris")
iris = sns.load_dataset("iris")
sns.pairplot(iris)
sns.distplot(iris.petal_length)
sns.relplot(x="petal_length", y="petal_width", data=iris)
sns.regplot(x="sepal_length",y="sepal_width", data=iris)

ans = sns.load_dataset("anscombe")
df = pd.DataFrame(ans)
df.groupby("dataset").describe()
sns.stripplot(x="x", y="y", data=df)
sns.regplot(x="x", y="y",data=df)
sns.lmplot(x="x", y="y", data=df)


