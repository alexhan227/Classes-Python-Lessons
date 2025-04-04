import json
Q={}
p=[]

try:
    with open("FlashCards.json", "r") as file:
        p = json.load(file)
except FileNotFoundError:
    p = []



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


p.append(Q)
print(p)

# Save updated data back to file
with open("FlashCards.json", "w") as file:
    json.dump(p, file, indent=4)