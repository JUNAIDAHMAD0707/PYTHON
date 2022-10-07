#tuple: ordered, immutable, allows duplicate elements
#() are optional in tuple
import sys,timeit
myt1="junaid",       #### class tuple
print(type(myt1)) 
myt2="junaid"       #####    class string
print(type(myt2))   
mytuple=("junaid",23,"Kulgam")
print(mytuple)
print(type(mytuple))
#tuple function to create a function from a iterable
mytuple1=tuple(["junaid",12,"abid",2.2,"junaid","abid","junaid"])
print(mytuple1)
print(type(mytuple1))

# accessing tuple elements    negative indexing is also there i.e, -1 is last element
item = mytuple1[3]
print(item)
'''item assignment is not allowed in tuple because immutable
mytuple1[2]="nabiel"'''

for x in mytuple1:
    print(x)

#case of letter in provided string matters
if "Junaid" in mytuple1:
    print("yes")
else:
    print("No")
#length of tuple by len() method
#count() specifies the specified no. of time that element is in tuple
print(mytuple1.count("junaid"))
#index()  returns the first index of that element
print(mytuple1.index("abid"))
#converting the tuple into list
mylist=list(mytuple1)
print(mylist)
print(type(mylist))
#tuple slicing
a=(1,2,3,4,5,6,7,8)
b=a[0::2]  #slice for 0 till end but step condition is two ie, it takes every second element
print(b)
#####     unpacking         #####
t1= "ubaid",34,"jammu and kashmir"
name,age,address = t1
#no. of elements put here must match no. of elements in tuple
print(name)
print(age)
print(address)


t2=(0,1,2,3,4)
i1,*i2,i3 = t2  #i2 will print a list in between i1 and i3
print(i1)
print(i3)
print(i2)


# Comparision between a list and a tuple
mlist=["junaid","abid",32,2.4]
mtuple=("junaid","abid",32,2.4)
print(sys.getsizeof(mlist),"bytes")
print(sys.getsizeof(mtuple),"bytes")

#gives time required to create a tuple with specified number times
print(timeit.timeit(stmt="(0,1,2,3,4,5)" , number=10000000))

#gives time required to create a list with specified number times
print(timeit.timeit(stmt="[0,1,2,3,4,5]" , number=10000000))