class FlashCards:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_question(self):
        print(self.question)

    def the_answer(self):
        print(self.answer)
            
question = input("what is the question?: ")
answer = input("What is the answer?: ")
    

FlashCards1 = FlashCards(question, answer)

FlashCards1.ask_question()
FlashCards1.the_answer()
