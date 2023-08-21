# Import Needed Libary's
import random
# Make Needed Variables
gameover = False
wrong = False
choose = ""
faces = [
        "⚀", # 0
        "⚁", # 1
        "⚂", # 2 
        "⚃", # 3
        "⚄", # 4
             # 5
        "⚅" ]
# Make Functions 
def init():
    choose = input("Even Or Odd: ").lower()
    if choose == "Q" or choose == "q" : exit()
    if choose != "even" or choose != "odd":
        print("Invaild Choose") ; 
    number = random.randint(0,6)
    if number == 1 : print(faces[0],number)
    elif number == 0 : print(faces[0],1)
    elif number == 6 : print(faces[5],number)
    else: print(faces[number],number)
    print("Win!") if number % 2 == 0 and choose == "even" or number % 2 != 0 and choose == "odd" else print("Lost.. Good Luck Next Time") 

while True:
    init()
