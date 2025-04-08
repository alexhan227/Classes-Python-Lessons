import json

points = 0
streak = 0

try:
    with open("FlashCards.json", "r") as file:
        Flash_data = json.load(file)
except FileNotFoundError:
    Flash_data = []

for question, answer in Flash_data.items():
    test = input(f"What is the Answer to {question}?  ")
    if streak >= 3:
        points += 3
    if test == answer:
        print("correct")
        points += 1
        streak +=1
        
    elif test != answer:
        print("you're dumb")
        points -= 1
        streak = 0 

        
print(f"You have points:{points} and steak:{streak}. ")