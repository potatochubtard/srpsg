# IMPORTING RANDOM MODULE TO GET PC TO GUESS #
import random

# GREETING #
print("Welcome!")
print("This is a rock-paper-scissors game.")
print("Could you write your name so I can know you :).")

# PLAYER NAME #
name = input("YOUR NAME: ")
if (name != '' or ""):
    print("Hello " + name + "!")

elif (name == '' or ""):
    print("I see a man of privacy :).")   

# PICK LIST #
rps = ["rock", "paper", "scissors"]

# RANDOM PICK FOR COMPUTER WITH RANDOM MODULE #
random_pick = random.choice(rps)  
      
# FUNCTION TO CHECK PICKS #
# WIN-LOST-EVEN SITUATIONS #
def check_pick():
    # WIN #                                               
    pick = input("Take a pick!" + "\nYOUR PICK:").lower() # I PUT "LOWER" FUNCTION IN CASE SOMEBODY TYPE WITH CAPITAL LETTERS, IT TURNS CAPITAL LETTERS TO LOWER LETTERS #                                                         
    if (pick == rps[0] and random_pick == rps[2]) or (pick == rps[1] and random_pick == rps[0]) or (pick == rps[2] and random_pick == rps[1]):
        print("<<<You won>>>")
        print("<<<Computer picked " + random_pick + ">>>") 

    # LOST #
    elif (pick == rps[2] and random_pick == rps[0]) or (pick == rps[0] and random_pick == rps[1]) or (pick == rps[1] and random_pick == rps[2]):      
        print("<<<You lost>>>")
        print("<<<Computer picked " + random_pick + ">>>") 

    # EVEN #
    elif (pick == random_pick):
        print("<<<It is even>>>") 
        print("<<<Computer picked " + random_pick + ">>>")  

    # WHEN PICK ENTERED WRONG or ENTERED WRONG ON PURPOSE #
    else:
        print("You either typed wrong or you were EXPERIMENTING with the code!")        
        check_pick()
               
# CALLING THE FUNCTION #
check_pick()   
