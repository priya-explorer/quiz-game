from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# todo : Create a Question bank
# create an empty list
question_bank = []

# 1st, create a for loop to iterate over the question_data
# next, create a question object(called new question) for each entry in question_data
# then, append question object to the question_bank list
for que in question_data:
    question_text = que['question']
    question_answer = que['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# to check if code is running
# print(question_bank)


# todo: Creating and instance of the class QuizBrain
quiz = QuizBrain(question_bank)

# todo: Run the quiz
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")