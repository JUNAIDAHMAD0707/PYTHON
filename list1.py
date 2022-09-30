#lists
items=[1,2,3,4,2,"altaf"]
print(type(items))
print(items[4])
items[3]="junaid"
print(items)
print(items[3:5])
items.append(25)
print(items)
print(items.copy())
print(items.count(2))
'''items1=[3,2,5,7,4,1]
print(items1.sort())
str1=input("enter your name")
str2=input("enter your name")
str3=input("enter your name")
str4=input("enter your name")
name=[str1,str2,str3,str4] 
print(name)
name.sort()
print(name)
print(type(name))'''
# taking marks of students and sorting them
strr1=int(input("enter marks of sub1"))
strr2=int(input("enter marks of sub2"))
strr3=int(input("enter marks of sub3"))
strr4=int(input("enter marks of sub4"))
Marks =[strr1,strr2,strr3,strr4]
print(Marks)
print("marks after sorting")
Marks.sort()
print(Marks)
temp=Marks[0]
Marks[0]=Marks[-1]
Marks[-1]=temp
print(Marks)
 