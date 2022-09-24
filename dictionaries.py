students={
    'name':'junaid',
    'classs':'10th',
    'address':'kulgam',
    'course':['python','machine learning']
}
print(type(students))
print(students['course'])
#getting values and keys
print(students.items())
#getting keys
print(students.keys())
#getting values
print(students.values())
print(students.get('address'))
print(students.get('cell','not found'))
students['cell']='9682545053'
students['age']= 23
print(students)
students.update({'name':'Junaid ahmad','class':'11th','age':'17'})
print("updated student record below")
print(students)
del students['cell']   #delete
age=students.pop('age')
print(students)
print(age)
#looping through values and keys
for key,value in students.items():
    print(key,value)


