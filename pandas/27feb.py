import pandas as pd
import numpy as np
"""
df = pd.read_csv("pandas\mckinsey.csv")
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
print(df.isnull().sum())  # check  null value for  count  
print(df.size)
print(df.values)
print(df.keys())
"""

# dataframe create manually :  add , rename , drop  

"""df =pd.DataFrame([
    ["priyanshi",10000,25],
    ["krish",20000,22],
    ["krishna",30000,23],
    ["dev",40000,14]
],columns=["name","salary","age"])

print(df)
print(df.rename(columns={"name":"first_name"}))
"""

"""df1=pd.DataFrame({
    "name" : ["priyanshi","krish","krishna","dev"],
    "salary" : [10000,20000,30000,40000],
    "age" : [25,22,23,14]
})
print(df1)

df1["gender"]=['f','m','f','m']
df1 = df1.rename(columns={"name":"first_name"})
df1.rename(columns={"name":"first_name"},inplace=True)

df1.drop(columns=["age"],inplace=True)
print(df1)
"""

# read csv : 

"""
df = pd.read_csv("pandas\mckinsey.csv")

print(df)
df=df['year']
df = df[["year","continent"]]
df["next_survey_year"] = df["year"] +3 

df = df["country"].unique()
df = df['country'].nunique()
df =df['country'].value_counts()
df['GDP'] =df["gdp_cap"] * df['population']

df['new_index']=np.arange(5,1709)
df.index= np.arange(1,1705)
print(df.head())
"""

# implicit index  vs explicit index :
"""
implicit  index : always start with 0 . 

explicit index : we can define it as we want (what is seen in output of a dataframe). 
it can be string , float whatever we want. 

"""

# df = pd.read_csv("pandas\mckinsey.csv")

"""print(df.head(20))
print(df['country'][16])
print(df['country'][17])

"""
# pandas give  two method : 
"""
1. loc : explict index
2. iloc : implicit index
"""
# print(df.loc[1])
# print(df.iloc[1])

# print(df.loc[5 :13])
# print(df.iloc[5 :13])  # last  value  excluded 

# print(df.iloc[2 :5,1:4])
# print(df.loc[2 :5,"year" :"continent"])

# print(df.loc[2 :5,["country","year","continent"]])

# print(df.iloc[[1,4,6,7],[0,3,4]])

# print(df.iloc[-1])
# print(df.loc[-1])

"""
que : give me year =2002 
"""

# print(df.loc[df['year']==2002])  # give  output  year =2002 
# print(df.iloc[df['year']==2002])  # error 

"""
df = df.drop([2,3,6,8]).head(20)
print(df)
"""

# sort in data frame  : 

"""
df = df.sort_values(by="life_exp")  # sort  ==> asc to desc 
df =df.sort_values(by="gdp_cap",ascending=False)

df = df.sort_values(['year',"life_exp"])
df = df.sort_values(['year',"life_exp"],ascending=[False,False])
df = df.sort_values(['year',"life_exp"],ascending=[True,False])

print(df.head(100))
"""

# join  :  join , concat , merge 

users =pd.DataFrame({
    "user_id" :[1,2,3],
    "name" : ["priyanshi","krish","krishna"],
})

# print(users)

msgs = pd.DataFrame({
  "user_id" :[1,1,2,4], 
  "message" : ["hi","hello","hmm","ok"]
})
# print(msgs)

# df =pd.concat([users,msgs])
# df =pd.concat([users,msgs],axis=0)  # axis =0  rows 
# df =pd.concat([users,msgs],axis=1)   # axis =1  columns

# df =users.merge(msgs)  # inner join  

users.rename(columns={"user_id":"id"},inplace=True)

# df =users.merge(msgs,left_on="id",right_on="user_id")
# df =users.merge(msgs,left_on="id",right_on="user_id",how="left")
# df =users.merge(msgs,left_on="id",right_on="user_id",how="right")
df = users.merge(msgs,left_on="id",right_on="user_id",how="outer")

print(df)

"""
153 : left 
1. 
   id       name  user_id message
0   1  priyanshi      1.0      hi
1   1  priyanshi      1.0   hello
2   2      krish      2.0     hmm
3   3    krishna      NaN     NaN

154 : right 
   id       name  user_id message
0  1.0  priyanshi        1      hi
1  1.0  priyanshi        1   hello
2  2.0      krish        2     hmm
3  NaN        NaN        4      ok

155 : outer 
    id       name  user_id message
0  1.0  priyanshi      1.0      hi
1  1.0  priyanshi      1.0   hello
2  2.0      krish      2.0     hmm
3  3.0    krishna      NaN     NaN
4  NaN        NaN      4.0      ok
"""