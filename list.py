#List : ordered, mutable, allows duplicate elements
items=[4,2.5,"junaid","two","two","three"]
print(type(items))
print(items[2])
#length of list
leng=len(items)
print(leng)
items[0:1]="salma","hassan"
print(items)
items[0:1]="two","three"
print(items)
print(items.count("two"))
items[0]=4
#adding element at a particular index
items[1]="salma"
print(items)
#getting index of a particular element
print(items.index("two"))
k = items[-1]
print(k)
#printing every element of list
for i in items:
    print(i)
#checking whether particular element is in list or not
if "abid" in items:
    print("yes")
else:
    print("no")

items2=["one",2,3.0,"four"]
#append()= adds element at the end of the list
items2.append(5)
print(items2)
items2.insert(1,"white")
print(items2)
#pop()= removes as well as returns last element of the list
i=items2.pop()
print(i)
print(items2)
#clear()= clears the the given list
clear=items2.clear()
print(clear)

mylist=[-4,3,2,19,-5,-2,1]
print(mylist)
# sorting a list
new_list = sorted(mylist)
print(new_list)
#creating list with specified no of element
list1=[1]*5
print(list1)
list2=[2,3,4,5,6]
newlist = list1+list2
print(newlist)

#list slicing
list3=[2,3,4,5,6]
a=list3[1:4]
print(a)
list4=list3
list4.append(7)
print(list3)
print(list4)

#list comprehension
list5=[1,2,3,4,5]
b=[i*i for i in list5]
print(list5)
print(b)