#edited by josiah
#dice roll program
#the purpose of this program is to roll the dice to display a number to the user and as a addition it will ask the user if they woule like to keep rolling the dice untill they get a 6, this is made using funtions.

import random
import time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"
x = 0
def roll():
    print("rolling.....")
    roll = random.randint(1,6)
    return roll

    

def show_dice(roll):
    global x
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    else:
        print(s6)
        x = x + 10
    return myroll
    return x

User_Input = input("if you would like to roll the dice please type roll?")
if User_Input == "roll":
    myroll = roll()
else:
    print("this Program will now end")
    quit

    
def Rolling6():
    global x
    ask6 = input("would you like to run this program until you get a 6?\n"
                 "Y = Yes\n"
                 "N = No\n")

    if ask6 == "Y":
        while x == 0 :
            roll = random.randint(1,6)
            time.sleep(0.5)
            show_dice(roll)
        if x == 10:
            print("you have rolled a 6")
            quit

        else:
            print("this Program will now end")
            quit
                
    


time.sleep(1)

show_dice(myroll)

Rolling6()

