import math
from frequents import mod_rem


def factorial(num):
    num = num
    multiplied = num

    if num == 0:
            return 1

    while num > 1 :
        num -= 1

        multiplied = multiplied * num


    if num == 1:
        return multiplied



def permutate(num1, num2):
    if num1 == num2:
        return factorial(num1)
    elif num1 > num2:
        return factorial(num1)/factorial((num1-num2))
    else:
        return "You Misplaced Your Values"


def combine(num1,num2):
    return permutate(num1, num2)/factorial(num2)

#This function converts Radian Angles to Degree Angles
def rad_to_deg(radians):
    return math.radians(radians * 180/math.pi)



#This function converts Degrees Angles to Radian Angles
def deg_to_rad(degrees):
    return math.degrees(degrees)


def Sine(num):
    if num == 30:
        return 1/2
    elif mod_rem(num,360) == 0:
        return 0.0
    elif mod_rem(num, 360) == 90:
        return 1.0
    elif mod_rem(num, 360) == 180:
        return 0.0
    elif mod_rem(num, 360) == 270:
        return -1.0
    else:
        sin = math.sin(math.pi*(num/180))
        return sin


def Cos(num):
    if mod_rem(num, 360) == 0:
        return 1.0
    elif mod_rem(num, 360) == 90:
        return 0.0
    elif mod_rem(num, 360) == 180:
        return -1.0
    elif mod_rem(num, 360) == 270:
        return 0.0
    else:
        cos = math.cos(math.pi*(num/180))
        return cos



def Tan(num):
    try:
        tan = Sine(num)/Cos(num)
        return tan
    except ZeroDivisionError:
        return "For " + str(num) + " The Result Is Undefined" + "\nDivision By Zero Is Infinite"

print(Tan(90))