dict1={
    "Name":"junaid",
    "Course":"MCA",
    "Roll no.":7,
    "Address":"Kulgam"
}
print(dict1)
print(type(dict1))
print(dict1["Course"])
print(dict1.get("Address"))
dict1.update({"Name":"Javid","Address":"Pakistan"})
print(dict1)
dict1["cell"]=979797
print(dict1)
mydict={
    "gindun":"play",
    "thapaer":"slap",
    "madad":"help"
}
print("kashmiri words whose english translation is available are:", mydict.keys())
a = input("enter kashmiri word to find english meaning\n")
print("meaning of entered kashmiri word is ", mydict[a])