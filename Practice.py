# write a program to print whether a year is leap or not

'''year = int(input("Enter the year: "))

if(year%4 == 0):

    if(year%100 == 0):
        if(year%400 == 0):
            print("Leap Year")
        else:
            print("Not A Leap Year")
    
    print("Leap Year")

else:
    print("Not a Leap Year") '''

# To print odd numbers till n

'''n = int(input("Enter the number: "))

for i in range(n+1):
    if(i%2 == 1):
        print(i) '''

# To print even numbers till n

'''n = int(input("Enter the number: "))

for i in range(n+1):
    if(i%2 == 0):
        print(i) '''

# using while loop
'''n = int(input("Enter the number: "))
i = 0
while(i<=n):
    if(i%2 == 0):
        print(i)
    i = i+1 '''

# Write a program to print table of a number
'''n = int(input("Enter the number: "))

for i in range(1,11):
    print(n," X ",i," = ", n*i) '''


# Functions 

# c++ -> return_type function_name(return_type arguments){}
# python -> def function_name(arguments)

# write a program to print sum of two numbers
'''def func(a,b):
    print("The sum of two numbers is: ", a+b)

# Calling Function
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

func(x,y) '''

# write a program to print factorial series

'''def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    print(fact)

n = int(input("Enter the number: "))
factorial(n) '''