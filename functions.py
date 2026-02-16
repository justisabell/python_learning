# ex1
# name = "Iza"
# age = 24

# def greeting():
#     print("My name is " + name + " and I am " + str(age))

# def bye():
#     print("Byeee")

# greeting()
# bye()

# ex2
# def multiply(num):
#     print(int(num) * 3 + 9)

# def exponent(base, power):
#     print(int(base)** int(power))

# question = input("What numbers would you like to multiply by 3 and add 9 to? \n")

# multiply(question)

# userbase = input("Input a base: ")
# userpower = input("Input a power: ")

# exponent(userbase, userpower)

# ex3

# def times3plus2(num):
#     print(num*3 +2)

# times3plus2(1)
# times3plus2(2)
# times3plus2(3)

# variable = 6

# times3plus2(variable)

# def twotimespowerof(base, exponent):
#     print(2* int(base)**int(exponent))

# userbase = input("Input the base: ")
# userexponent = input("Input the exponent: ")

# twotimespowerof(userbase, userexponent)

# ex4

# def luckify(string):
#     return string + "777"

# print(luckify("hey "))

# luckyname = luckify("hey ")
# print(luckyname)
# luckyname = luckify(luckyname)
# print(luckyname)

# ex5

# def printname(name = "Bob"):
#     return "My name is " + name

# username = input("What is your name? ")

# if username:
#     print(printname(username))

# else:
#     print(printname)

# ex6

# globe = "Iza"

# def friends(name):
#     local = "Iza"
#     return local + " and " + name + " are friends"

# print(friends("Bob"))
# print(local)

# project1 - calculator
import math

def add(a,b):
    return a + b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def exponent(base,power):
    return base ** power

def remainder_division(a,b):
    answer = a/b
    answer = math.floor(answer)
    remainder = a % b
    return str(answer) + " remainder " + str(remainder)

def square_root(a):
    return math.sqrt(a)

print("Welcome to the calculator app, we will help you solve even the toughest equestions!")
user_input = input("What function would you like to use?\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponent\n6. Remainder\n7. Square root\n\n")

if user_input == "1":
    num = input("What two numbers would you like to add?\n")
    num2 = input("And?\n")
    print ("The answer is: " + str(add(int(num), int(num2))))
    
elif user_input == "2":
    num = input("What two numbers would you like to substract?\n")
    num2 = input("And?\n")
    print ("The answer is: " + str(substract(int(num), int(num2))))

elif user_input == "3":
    num = input("What two numbers would you like to multiply?\n")
    num2 = input("And?\n")
    print ("The answer is: " + str(multiply(int(num), int(num2))))

elif user_input == "4":
    num = input("What two numbers would you like to divide?\n")
    num2 = input("And?\n")
    print ("The answer is: " + str(divide(int(num), int(num2))))

elif user_input == "5":
    num = input("What two numbers would you like to exponent?\n")
    num2 = input("And?\n")
    print ("The answer is: " + str(exponent(int(num), int(num2))))

elif user_input == "6":
    num = input("Of which two numbers would you like to find a remainder?\n")
    num2 = input("And?\n")
    print ("The answer is: " + str(remainder_division(int(num), int(num2))))

elif user_input == "7":
    num = input("What number would you like to take the square root of?\n")
    print ("The answer is: " + str(square_root(float(num))))

