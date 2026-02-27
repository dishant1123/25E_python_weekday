# pandas :    pip install pandas
import  pandas as pd
"""
use : 
1. data cleaning  
2. data manipulation
3. data analysis

"""
# series :

"""s= pd.Series([18,12,23,56,78,90])
print(s)

s1=pd.Series([13,14,15,16,17],index=["a","b","c","d","e"])
print(s1)

s2=pd.Series({"maths":90,"english":80,"physics":70},dtype=int)
print(s2)
"""

# function  : head , tail,sample ,shape ,size,ndim ,dtype ,values , index,info : 

"""
s2=pd.Series({"maths":90,"english":80,"physics":70,"chemistry":60,"biology":50,"com":99})

print(s2)
print(s2.head(2))  # first 5 row  ==> fetch  ==> head   
print(s2.tail(3))  # last 5 row  ==> offset  ==> tail   
print(s2.sample(3))
print(s2.shape)
print(s2.size)
print(s2.ndim)
print(s2.dtype)
print(s2.values)
print(s2.index)
print(s2.info())
"""

# loc , iloc : 

"""s2=pd.Series({"maths":90,"english":80,"physics":70,"chemistry":60,"biology":50,"com":99})

print(s2)
print(s2["maths"])
print(s2[1])

print(s2.loc['maths'])
print(s2.iloc[1])

print("at",s2.at["biology"])
print("iat",s2.iat[3])

# label  based : 

print(s2["maths":"physics"])
print(s2[["maths","physics"]])

print(s2[s2>70])
"""
# aithematic : 

"""users = pd.Series([21,22,23,14,25],index=["priyanshi","krish","krishna","dev","elien"])

print(users)
print(users +1)
print(users -4)
print(users *2)
print(users /2)

match1=pd.Series([100,200,300,400,500],index=["a","b","c","d","e"],dtype=int)
match2=pd.Series([100,200,300,400,500],index=["x","b","c","d","e"],dtype=int)

print("original match 1 is : \n",match1)
print("original match 2 is : \n",match2)

# print("addition of match 1 and match 2 is : \n",match1+match2)

result =match1.add(match2, fill_value=100)
print("result is : \n",result)
"""

# statistical :

"""s=pd.Series([1,2,3,4,5,6,7,8,9,10])
print(s.mean())
print(s.median())
print(s.std())
print(s.var())
print(s.min())
print(s.max())
"""

# s2=pd.Series({"maths":90,"english":80,"physics":70,"chemistry":60,"biology":50,"com":99})

s2=pd.Series([12,14,56,99,56,34,56,78,90,12])
print(s2[3])
