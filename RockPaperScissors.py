#Complete rock paper scissors game 
# Understanding the concept
import random
#importing random library
choice = random.randint(1, 3)
print("Welcome to the Game of Rock Paper Scissors")
print("Please choose the following Option In order to")
print("Proceed in the Game:")
print("1)- Rock ")
print("2)- Paper ")
print("3)- Scissors ")
usr_inp = str(input("Please Input a choice(1-3):"))
if str(usr_inp) == '1':
    print("User Picked: Rock")
elif str(usr_inp) == '2':
    print("User Picked: Paper")
elif str(usr_inp) == '3':
    print("User Picked: Scissors")
else:
    print("Invalid choice Please enter your Statement")
# assigning choice variable to the random library
# acessing the randint() member of random variable
if choice == 1:
    print("Computer Picked: Rock")
elif choice == 2:
    print("Computer Picked: Paper")
elif choice == 3:
    print("Computer Picked: Scissors")
# in case of draw
if int(usr_inp) == choice:
    print("Terrific it's a draw")
# in case if user wins
elif (int(str(usr_inp)) == int(str('1')) and choice == 3) or (int(str(usr_inp)) == int(str('2')) and choice == 1) or (int(str(usr_inp)) == int(str('3')) and choice == 2):
    print("You win!") # in case if user wins
# in case if computer wins
else:
    print("Computer wins!")
#end program
# there you have it complete game of rock paper scissors