from mimetypes import knownfiles


var = 70
#ElSE-IF ladder statement
if(var==50):
    print("The value of expression is 50")
elif(var==60):
    print ("The value of expression is 60")
elif(var==70):
    print ("The value of expression is 70")
else:
    print("The value of expression is greater than 70")
#while loop
while(var<=75):
    print("the value of var is:",var)
    var=var+1
else:
    print(var,"value is greater than 75")
#for loop for checking whether entered number is prime or not
num = int(input("enter the number"))
for j in range(2,num):
    if(num%j==0):
        flag=0
        break
    else:
        flag=1
if(flag==0):
    print("entered number is not prime")
if(flag==1):
    print("entered number is prime")
    


    
    
