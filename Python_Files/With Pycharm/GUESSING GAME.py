#print("A GUESSING GAME")
#secret_word = "MATHS"
#guess_it = ""
#guess_it_count = 0
#guess_it_limit = 5
#out_of_guess = False

#while guess_it != secret_word and not(out_of_guess):
#    if guess_it_count < guess_it_limit:
#        guess_it = input("TELL US WHAT YOU THINK: ")
#        guess_it_count += 1
#    else:
#        out_of_guess = True
#if out_of_guess:
#    print("YOU'RE UNLUCKY, TRY HARDER NEXT TIME.")
#else:
#    print("CORRECT!!! YOU'RE A GENIUS")


print("FOR LOOPS")
for letter in "GENIUS DEXTER":
    print(letter)

rms = ["IFE", "PAUL", "MIKE", "CHRIS", "OKEY"]
len(rms)
for index in range(len(rms)):
    print(rms[index])
for rm in rms:
    print(rm)
    print(index, rm)

for index in range(15):
    print(index)

for index in range(1, 14):
    print(index)

for index in range(6):
    if index == 0:
        print("FIRST MAN!!! YOU'RE GOOD TO GO!!!")
    else:
        print("WE'RE SORRY YOU COULDN'T MAKE IT, TRY HARDER NEXT TIME.")
