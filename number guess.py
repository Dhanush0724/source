#Number guessing using python


import random 
print("Welcome to number guessing game")
range = input("Type a number to guess:  ")
  
if range.isdigit():  
    range  = int(range)

    if range <= 0:
        print("please type a positive number greater than zero ")
        quit()

else:
    print("oops!! you are not in the game , type a number")
    quit()        

random_number = random.randint(0, range)
attempt = 0

while True:
    attempt += 1
    user_guess = input(" Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
         print("enter a number next time within the limit. ")   
         continue


    if user_guess == range:
        print("you got this right guess")
        break

    elif user_guess < range:
        print("try with the larger one ")

    else:
        print("try with the smaller number")

         
    print("you guessed", attempt , "attempt")      
        

