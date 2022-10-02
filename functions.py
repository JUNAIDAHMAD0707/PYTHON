def oddeven(num):
    if (num%2==0):
        print("even")
    else:
        print("odd")
n=int(input(" enter number to find whether it is odd or even \n"))
oddeven(n)

def lists(mylist):
    mylist.append([1,3,5,7])
    print("list values inside function are:",mylist)
    print(type(mylist))
mylist=[20,30,40]
lists(mylist)
print("list values outside function are:",mylist)

#### Function with required arguments
def lists1(mylists):
    mylists=[1,3,5,7]
    print("\n\nlist values inside function are:",mylists)
mylists=[20,30,40]
lists1(mylists)
print("list values outside function are:",mylists)

### Function with keyword arguments
def info(name,age,address):
    print("name:",name)
    print("age:",age)
    print("address:",address)
info(name="junaid",age=23,address="Kulgam")

### Function with default agrument
def info1(name,age=23):
    print("name:",name)
    print("age:",age)
info1(name="Aabid",age=24)
info1(name="junaid" )


### Function with variable length arguments

def vla(arg1, *arglen):
    print("arguments is/are:")
    print(arg1)
    for i in arglen:
        print(i)
vla(11)
vla(10,12,23,34)

#variable local and global scope
sum=0
def add(i,j):
    sum = i+j
    print("sum of two numbers is:",sum)
    return sum
add(10,32)
print("sum of two numbers outside function is:",sum)