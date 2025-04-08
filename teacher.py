import json
Q={}

try:
    with open("FlashCards.json", "r") as file:
        Q = json.load(file)
except FileNotFoundError:
    Q = {}



class FlashCards:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def dictionary(self):
        Q[question]=answer
              
question = input("what is the question?: ")
answer = input("What is the answer?: ")
    

FlashCards1 = FlashCards(question, answer)
FlashCards1.dictionary()



# Save updated data back to file
with open("FlashCards.json", "w") as file:
    json.dump(Q, file, indent=4)