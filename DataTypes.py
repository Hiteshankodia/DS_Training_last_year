# there are basically 4 types of Data Structures in python
''' 1. List
    2. Tuple
    3. Set
    4. Dictionary '''

# List

# empty
'''lst = []
print(type(lst))

#appending elements in a list - append
lst.append(4)
lst.append(3)
lst.append(6)
print(lst)

print(lst[1]) '''

# taking elements from user

'''lst1 = []

n = int(input("Enter the number of elements "))
print("Enter the elements one by one ")

for i in range(n):
    num = int(input())
    lst1.append(num)

print(lst1)

# updateing elements in a list
lst1[2] = 9
print(lst1) 

lst2 = [2, "Krishna", 3.5, True]
print(lst2) '''

# tuples
tup1 = ()
# print(type(tup1))

# adding only single element
'''tup2 = (1,)
print(tup2)
print(type(tup2))'''

'''tup3 = (2,5,3)
print(tup3)
print(tup3[2])'''

# returns type error
'''tup3[2] = 4
print(tup3) '''

# attribute error
'''tup3.add(4) '''

# sets

# empty set
# set1 = {} -> dict

'''set1 = set()
print(type(set1))

set2 = {4,7,8,3,4,2,7,8,4,4,4,4}
print(set2)

# adding elements
set2.add(9)
print(set2)

# we can add any type of variables in a set
set3 = {1, 5.7, "kkk", True, False}
print(set3)'''


# Dictionary

#empty dictionary
'''dict1 = {}
print(type(dict1))

# in a dictionary there are two things - 1. key, 2. value

dict2 = {"Krishna":"First Name", "kant":"Middle Name", "Singhal":"last Name"}
print(dict2)

print(dict2["kant"])

dict3 = {"A":[1,2,3,4], "B":(3,4,5,2), "C":4.3}
print(dict3)

dict4 = {"A":{"Krishna":"First Name", "kant":"Middle Name", "Singhal":"last Name"}, "B":[3,2,5]}
print(dict4)

print(dict4["A"]["Krishna"])

print(dict4["B"][2])

dict4["A"]["Krishna"] = "Name"
print(type(dict4["B"]))
dict4["B"] = 4
print(dict4)


print(type(dict4["B"]))
print(type(dict4["A"]["Krishna"]))

dict5 = {"A":{"A":{"Krishna":"First Name", "kant":"Middle Name", "Singhal":"last Name"}, "B":[3,2,5]}}
print(dict5) '''