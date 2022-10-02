''' Anonymous functions are created using lambda keyword.
    cannot be a direct call to print because lambda requires an expression.
    Lambda's are a one line version of a function but not equivalent to inline statements in c or c++
'''
sub=lambda arg1,arg2:arg1-arg2;
print("subtration of 23 and 12 is :",sub(23,12))
## filter() function with lambda function:

num=[1,3,5,8,6]
even=filter(lambda n:n%2==0,num)
odd=filter(lambda n:n%2==1,num)
print(list(even))
print(list(odd))
print(type(even))


sum=0
def add(i,j):
    sum = i+j
    print("sum of two numbers is:",sum)
    return sum
add(10,32)
print("sum of two numbers outside function is:",sum)