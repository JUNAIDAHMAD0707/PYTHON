set1={1,5,3,4,}
set2={2,3,9}
print(type(set1))
print(set1)
set1.add(32)
set2.add("abd")
print(set2)
print("Union of set1 and set2:",set1.union(set2))
print("intersection of set1 and set2:",set1.intersection(set2))
set3=set()
print(set3)

mydict={
    "gindun":"play",
    "thapaer":"slap",
    "madad":"help"
}
print("kashmiri words whose english translation is available are:", mydict.keys())
a = input("enter kashmiri word to find english meaning\n")
print("meaning of entered kashmiri word is ", mydict[a])
