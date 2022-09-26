from array import *
arrayName=array('i',[10,21,13,14,54])
# Accessing elements at particular indexes
print("element at index[3] is:",arrayName[3])
print("element at index[3] is:",arrayName[2])
for x in arrayName:
    print(x)
# Inserting elements at particular indexes
arrayName.insert(1,33)
arrayName.insert(4,99)
print("Array after insertion of elements at index 1 and 4")
for y in arrayName:
    print(y)
#deleting elements from Array
arrayName.remove(99)
arrayName.remove(10)
arrayName.remove(21)
print("array after deleting of elements")
for z in arrayName:
    print(z)
#search operation in an array
print("the index of 13 in array is:",arrayName.index(13))
#updating an element at particular index
arrayName[1]=75
for a in arrayName:
    print(a)