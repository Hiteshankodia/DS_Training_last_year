# write a program to print ascii value of a character

'''n = input("Enter the input: ")
print("The ascii value of a character given is: ", ord(n)) '''

# swapping first and last elements in a list
'''lst = []
lst.append(3)
lst.append(5)
lst.append(6)
lst.append(8)
lst.append(1)

print(lst)

temp = lst[0]
lst[0] = lst[4]
lst[4] = temp

print(lst) '''

# to reverse the list
'''lst = []
lst.append(3)
lst.append(5)
lst.append(6)
lst.append(8)
lst.append(1)

print(lst)

lst2 = []

# lst.reverse()
# print(lst)

for i in range(4, -1, -1):
    lst2.append(lst[i])

print(lst2) '''

# to sort the list
'''
lst = []
lst.append(3)
lst.append(5)
lst.append(6)
lst.append(8)
lst.append(1)
print(lst)

# lst.sort()
# print(lst)

for i in range(5):
    for j in range(i, 5):
        if(lst[i]>=lst[j]):
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp

print(lst) '''

# to find the length of list
'''
lst = []
lst.append(3)
lst.append(5)
lst.append(6)
lst.append(8)
lst.append(1)
print(lst)

# print(len(lst))

count = 0

for i in lst:
    print(i)
    count = count+1

print(count) '''

# print the largest number in a list
'''lst = []
lst.append(3)
lst.append(5)
lst.append(6)
lst.append(8)
lst.append(1)
print(lst)

print("The maximum element in the list is: ")
max = lst[0]

for i in range(len(lst)):
    if(lst[i]>max):
        max = lst[i]

print(max)


print("The minimum element of the list: ")
min = lst[0]

for i in range(len(lst)):
    if(lst[i]<min):
        min = lst[i]

print(min) '''

# Print the median of the list
'''
lst = []
lst.append(3)
lst.append(5)
lst.append(6)
lst.append(8)
lst.append(1)
lst.append(4)
lst.append(9)
print(lst)


lst.sort()
print(lst)

# length of list
n = int(len(lst))

if(n%2 == 0):
    print(lst[int(n/2) -1])

else:
    print(lst[int(n/2)]) '''

# mode of the list
'''
lst = []
lst.append(3)
lst.append(5)
lst.append(6)
lst.append(5)
lst.append(3)
lst.append(5)
lst.append(9)
print(lst)

maxV = lst[0]
maxC = 0

for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):

        if(lst[i] == lst[j]):
            count = count+1
        
        if(count>maxC):
            maxC = count
            maxV = lst[i]

            
print(maxC)
print(maxV) '''