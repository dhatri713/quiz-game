from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")
