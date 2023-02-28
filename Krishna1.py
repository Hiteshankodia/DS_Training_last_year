# print statement
'''print("Hello World!")'''

# taking variables
'''a = "Krishna"
b = 4.5
c = 5
d = True

print(a)
print(b)
print(c)
print(d)

'''

# type casting

'''
print(int(b))
print(float(c))

e = int(b)'''

# type of variable
'''print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
'''

# taking input along with type cast
'''f = float(input())
print(f)
print(type(f)) '''


# taking input with some pre written string after that string concatination for output
'''g = input("Enter your name : ")
print("Your name is: " + g)

h = int(input("Enter your age: "))
print("The age is: " , h)

print(type(g))
print(type(h))'''

# looping in python
# three basic things in a loop - initialization , condition, increement/decreement
# for loop
# range(n) = values from 0 to n-1
'''for i in range(6):
    print(i) '''

'''for i in range(6,20):
    print(i) '''

'''for i in range(3,20,3):
    print(i) '''

#while loop
'''i=0
while(i<=5):
    print(i)
    i = i+1 '''

# conditional statements
'''a = 8
if(a>5):
    print("Valid") '''

# else
'''b = 8
if(b>9):
    print("valid")

else:
    print("Invalid") '''

# elif
# write a program to print largest number among three numbers

'''a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if(a>b and a>c):
    print(a," is largest")

elif(b>a and b>c):
    print(b, " is largest")

else:
    print(c," is largest") '''