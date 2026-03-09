# matplotlib :  pip install  matplotlib 
"""
use  : 
1. data visualization
"""
import matplotlib.pyplot as plt

# line  graph : 

"""x=[1,2,3,4,5,6,7,8,9,10]
y=[23,45,67,89,10,12,14,19,90,44]

plt.plot(x,y,color="red",linewidth=2)
plt.figure(figsize=(10,5))
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("line graph")
# plt.grid(True)
plt.show()
"""

# bar graph :

"""x=["a","b","c","d","e","f","g","h","i","j"]
y=[23,45,67,89,10,12,14,19,90,44]

plt.bar(x,y,color="red",width=0.5,edgecolor="black",linewidth=2)
plt.xlabel("name")
plt.ylabel("marks")
plt.title("bar graph")
plt.show()
"""

# pie graph : 

"""x=["india","usa","china","japan"]
y=[190,200,350,170]

plt.pie(y,labels=x,autopct="%1.1f%%",shadow=True)
plt.title("pie graph")
plt.show()

"""

# histogram :

"""x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y=[23,45,67,89,10,12,14,19,90,44,23,45,67,89,10]

plt.hist(x, weights=y,bins=6, color="red", edgecolor="black", linewidth=2)
plt.xlabel("days")
plt.ylabel("temprature")
plt.title("histogram")
plt.show()
"""

# scatter plot :

"""
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,3,2.5,6.7,0.2,0.1,0.3,0.4,0.5,0.6]

plt.scatter(x,y,color="red",s=100,linewidth=2)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("scatter plot")
plt.show()
"""