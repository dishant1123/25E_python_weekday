# csv file  : 

import csv

"""
csv.writer(file) ==>create writer object
 writerrows() ==>writes multiple rows 
 newline "" ==>prevents blank lines in  windows 
 """

"""data = [
    ["name","age","city"],
    ["krishna",21,"ahmedabad"],
    ["aashish",22,"gandhinagar"],
    ["abhishek",23,"baroda"],
    ["aditya",24,"surat"],
]

with  open("student.csv","w",newline="")as file : 
    writer = csv.writer(file)  # writer  ==> write 
    writer.writerows(data) 
    
print("file created")
"""

# ex :2 read from  csv file  : 

"""with  open("student.csv","r") as file :
    reader =csv.reader(file)
    for i in reader:
        print(i)
"""

# ex :3 dictwriter ==>write in csv using dict 

"""with  open("student.csv","w",newline="")as file :
    fieldnames =["id","name","salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames) 
    writer.writeheader()
    writer.writerow({"id":1,"name":"krishna","salary":100000})
    writer.writerow({"id":2,"name":"krish","salary":1000000})
    writer.writerow({"id":3,"name":"sudama","salary":100})
    writer.writerow({"id":4,"name":"ravan","salary":10})
    
    
"""    
    
# ex :4 

"""
with  open("student.csv","r") as file :
    reader = csv.DictReader(file)
    for i in reader:
        print(i)
"""