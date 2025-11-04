is_male = True
is_female = True
is_boulder = True
is_slender = True
is_fair = True
is_dark = True
is_tall = True
if is_fair and is_tall and not(is_female):
    print("She is " + "elegant.".upper())
else:
    print("She is ugly.")

if is_dark and is_boulder or (is_tall):
    print("She is " + "ugly and a dwarf.".upper())
elif is_male and not (is_dark):
    print("He is an Albino.")
elif not(is_male) and not(is_boulder):
    print("She is slender.")
else:
    print("She is ugly.".upper())



def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print(max_num(4500,23, 9))



print("while loops".upper())
u = 4
while u <= 72:
    print(u)
    u +=3


print("I am done")

i = 6
while i < 35:
    i += 3
    print(i)

print("FINISHED")



print("guessing game".upper())

from math import sqrt
num1 = input("Put a number: ")
#num2 = input("Put another number: ")
#print(float(num2)//float(num1))
print(sqrt(float(num1)))
print(49//2)
