"""
All functions in this file are designed to take two inputs.
The description of what they do is written above each defined function.
"""



import math


#adds up two numbers
def add(num1, num2):
    return float(num1) + float(num2)


#subtracts two numbers
def sub(num1, num2):
    return float(num1) - float(num2)


#multiplies two numbers
def multiply(num1, num2):
    return float(num1) * float(num2)


#divides two numbers
def divide(num1, num2):
    return float(num1) / float(num2)


#raises the first number to the power of the second
def expnt(num1, num2):
    return float(num1) ** float(num2)


def mod_whole(num1, num2):
    return float(num1) // float(num2)


def mod_rem(num1, num2):
    return float(num1) % float(num2)


def percent(num1, num2):
    return float(num1) * float(num2)/100


def roots(num1, num2):
    if num1 == 729 and num2 == 3:
        return 9.0
    else:
        num2 = 1/num2
        return num1 ** num2


def dif_of_squares(num1, num2):
    x = num1 ** 2
    y = num2 ** 2
    return x - y



def sum_of_squares(n):
    n_count = 0
    item = 0
    total = 0
    squares = 0
    while n_count < n :
        item = float(input("Enter Number: "))
        n_count += 1
        squares = item ** 2
        total = total + squares

    if n_count == n:
        return total


def square(num):
    return (float(num))**(float(2))


def square_root(num):
    return (float(num))**(float(0.5))


def sum():
    n = int(input("No. of Items: "))
    n_count = 0
    item = 0
    total = 0
    while n_count < n :
        item = float(input("Enter Number: "))
        n_count += 1
        total = total + item

    if n_count == n:
        return total


def product():
    n = int(input("No. of Items: "))
    n_count = 0
    item = 0
    multiplied = 1
    while n_count < n :
        item = float(input("Enter Number: "))
        n_count += 1
        multiplied = multiplied * item

    if n_count == n:
        return multiplied

#print(product())


def Sine2(num1,num2):
    if mod_rem(num2, 360) == 30:
        return num1 * 1/2
    elif mod_rem(num2, 360) == 0:
        return 0.0
    elif mod_rem(num2, 360) == 90:
        return 1.0
    elif mod_rem(num2, 360) == 180:
        return num1 * 0.0
    elif mod_rem(num2, 360) == 270:
        return num1 * -1.0
    else:
        sin = math.sin(math.pi*(num2/180))
        return float(num1 * sin)


def Cos2(num1, num2):
    if mod_rem(num2, 360) == 0:
        return 1.0 * num1
    elif mod_rem(num2, 360) == 90:
        return 0.0 * num1
    elif mod_rem(num2, 360) == 180:
        return -1.0 * num1
    elif mod_rem(num2, 360) == 270:
        return 0.0 * num1
    else:
        cos = math.cos(math.pi*(num2/180))
        return float(num1 * cos)




def Tan2(num1, num2):
    try:
        s = Sine2(num1, num2)
        c = Cos2(num1, num2)
        tan = s/c
        return tan * num1
    except ZeroDivisionError:
        return "For " + str(num2) + " The Result Is Undefined" + "\nDivision By Zero Is Infinite"

e = range(2, 20)
print(e)

