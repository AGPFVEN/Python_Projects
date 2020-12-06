from quiz import Quiz
from attempt import Attempt


quiz = Quiz()
attempt = Attempt(quiz, number_of_questions=3)
attempt.choose_category()

attempt.start()