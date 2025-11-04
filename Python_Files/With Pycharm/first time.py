#from math import sqrt

my_num1 = input("Enter a number: ")
operator = input("Operator: ")
my_num2 = input("Enter another number: ")

from math import sqrt

def max_num(my_num1, my_num2):
    if my_num1 > my_num2:
        return my_num1
    else:
        return my_num2



if operator == "+":
    ANSWER = ( int(my_num1) + int(my_num2) )
elif operator == "-":
    ANSWER = ( int(my_num1) - int(my_num2) )
elif operator == "*":
    ANSWER = ( int(my_num1) * int(my_num2) )
elif operator == "/":
    ANSWER = ( int(my_num1) / int(my_num2) )
elif operator == "^":
    ANSWER = ( int(my_num1) ** int(my_num2) )
elif operator ==  "%":
    ANSWER = ( int(my_num1) % int(my_num2) )
elif operator == "@":
    my_num2 = 1
    ANSWER = (sqrt(int(my_num1)))
#elif operator == "max":
#    ANSWER = max()
else:
     print("SYNTAX ERROR")
prints = [[]
]
ANSWER = { "print1" : int(my_num1) + int(my_num2),
    "print2" : int(my_num1) - int(my_num2),
    "print3" : int(my_num1) * int(my_num2),
    "print4" : int(my_num1) / int(my_num2),
    "print5" : int(my_num1) ** int(my_num2),
    "print6" : int(my_num1) % int(my_num2),
    "print7" : sqrt(int(my_num1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               bbbbbbbbbbbbbbbbbbbbbbbbbbb                                                   bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                                      bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                             bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                                                       bbbbbbbbbbbbb                                                                                                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                             bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                                                                                                                                                                                                              bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                           bbbbbbbbbbbbbbbbbbbbbbb                                                                                                       bbbbbbbbbbbbbbbbbbbb                                                                                               bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                              bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb            bbbbbbbbbbbbbbbbbbbbb rint7" : sqrt(int(my_num1)) 
    }


line_count = 0
line_limit = 5
out_of_steps = False
for row in ANSWER:
    line_count += 1
while line_count != line_limit and not(out_of_steps):
    line_count < line_limit:
        my_num1 = input("Enter a number: ")
        operator = input("Operator:")
        my_num2 = input("Enter another number: ")
        step_count += 1
    else:
        out_of_steps = True
        print("CLEAR MEMORY")
#        if out_of_steps != False:
#            print("CLEAR MEMORY")
#        else:
#            print(ANSWER)

        

        
 #if out_of_steps:
 #   print("CLEAR MEMORY")
 #else:
    #print(ANSWER)





#is_male = True
#is_tall = False
#if is_male or is_tall:
    #print("YOU ARE GOOD TO GO.")
#else:
    #print("GO BACK")
    #print("HAVE A NICE DAY")
