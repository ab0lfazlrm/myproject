from random import choice
import random
import string

def passgen(lenght):
    letters = string.ascii_letters
    # joining = ""
    for i in range(lenght):
        joining += "".join(str(random.choice(letters)))
    return joining


if __name__ ==  "__main__":
    lenght = int(input("Enter the lenght: "))
    last = passgen(lenght)
    print(last)








