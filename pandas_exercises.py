import pandas as pd 
from pydataset import data

mpg= data("mpg")

mpg["highest_mean_mpg"] = mpg.hwy + mpg.cty / 2
mpg[["manufacturer", 'highest_mean_mpg']].groupby("manufacturer").mean().idxmax() #Manufacturer with highest mean mpg(between highway and city)
mpg.model.nunique() #count of unique models
mpg.manufacturer.nunique() #count of unique manufacturers
pre_auto = mpg[["trans", "highest_mean_mpg"]].groupby("trans",as_index=False).agg('mean')#places all unique transmission types and their respective mean_mpg's into a dataframe
def replace_auto():
    for x in x:
        if x = 
auto =