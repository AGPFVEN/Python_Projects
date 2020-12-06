

class Attempt:
    def __init__(self, quiz, number_of_questions):
        self.quiz = quiz
        self.number_of_questions = number_of_questions

    
    def choose_category(self):
        category_name = input("Enter desired category: ")
        self.category = self.quiz.get_category(category_name)


    def answer_question(self):
        question = self.category.pick_random_question()
        print(question)
        answer = int(input("Answer: "))
        if question.check_answer(answer):
            print("Correct")
        else:
            print("Wrong")


    def start(self):
        for i in range(self.number_of_questions):
            self.answer_question()