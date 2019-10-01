import pandas as pd 
from pydataset import data

mpg= data("mpg")

mpg["highest_mean_mpg"] = mpg.hwy + mpg.cty / 2
mpg
mpg[["trans", "highest_mean_mpg"]].groupby("trans", as_index=False).mean()
mpg[["manufacturer", 'highest_mean_mpg']].groupby("manufacturer").mean().idxmax() #Manufacturer with highest mean mpg(between highway and city)
mpg.model.nunique() #count of unique models
mpg.manufacturer.nunique() #count of unique manufacturers
pre_auto = mpg[["trans", "highest_mean_mpg"]].groupby("trans",as_index=False).mean() #places all unique transmission types and their respective mean_mpg's into a dataframe
pre_auto
pre_auto.loc[pre_auto["trans"].str.contains("auto"), "trans"] = "auto"#changes all values which contain "auto" to just "auto" by itself within the trans column
pre_auto.loc[pre_auto["trans"].str.contains("manual"), "trans"] = "manual"#changes all values which contain "manual" to just "manual" by itself within the trans column
pre_auto.groupby("trans",as_index=False).mean()

from env import host, user, password
def get_db_url(user,host,password,database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url

df = get_db_url(user, host, password, "employees")
df_t = pd.read_sql('select * from titles', url)
df_e = df.read_sql('select * from employees', url)
unique_titles = df_t.groupby(df_t).count()
unique_titles.rename(columns={"emp_no":"number_with_title"}, inplace=True)
unique_titles = unique_titles.drop()

df = df_t.groupby("emp_no").count()
#group by employee number


