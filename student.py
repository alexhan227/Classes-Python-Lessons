import json

try:
    with open("FlashCards.json", "r") as file:
        Flash_data = json.load(file)
except FileNotFoundError:
    Flash_data = []

for data in Flash_data:
    for question, answer in data:
        print(question)
