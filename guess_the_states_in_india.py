#import random

# List of African countries
india_states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
    

# Shuffle the list for a random order
#random.shuffle(india_states)
length = len(india_states)
print("--------Guess the India States Quiz--------")
print("Try to guess as India states as possible. Enter 'exit' to end the quiz.")

score = 0
ans = []

while True:
    print("\nScore:", score)
    guess = input("Enter the name of an india state: ").strip().title()  # Capitalize input

    if guess.lower() == 'exit':
        break  # End the quiz if the user enters 'exit'

    if guess in india_states:
        print("Correct! +1 point")
        score += 1
        india_states.remove(guess)
        ans.append(guess)
        print(ans)
        print("Still"+(length-ans)+"left to guess")
    else:
        if guess in ans :
            print("You already guessed this state try Different")
        else :
            print("Incorrect. Try again!")

print("\nQuiz ended. Your final score is:", score)
