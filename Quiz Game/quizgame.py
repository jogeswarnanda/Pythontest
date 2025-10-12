from questionmodel import Question
from question_data import question_data
from quiz_brain import Quizbrain
question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)
while quiz.still_has_question():
    print(quiz.question_number)
    quiz.next_question()

print(f"You have completed the Quiz.Your final score is {quiz.score}.")
#quu.next_question(question_bank)
#print(question_bank)
