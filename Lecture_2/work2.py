# -*- coding: utf-8 -*-
listM = [12, 4, 5, 5]
print(listM)
print(listM[1])
listM[2] = 23
print(listM)
print("===================")
tupleM = (12, 4, 5, 5)
print(tupleM)
print(tupleM[1])
#tupleM[1] = 23
print(tupleM)
print("===================")
setM = {12, 4, 5, 5, 5, 4}
print(setM)
#print(setM[0])
print("===================")
dictionaryM = {
        "name":"dato",
        "age":20,
        "merried":False
    }
print(dictionaryM)
print(dictionaryM["name"])
for item in dictionaryM:
    print(item)