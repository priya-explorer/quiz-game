# todo - create a class named quiz_brain

# this takes the question bank as a parameter - question_list
import self as self


class QuizBrain:
    """ This class manages the quiz game!"""

    # todo: Attributes of the class - question_number, question_list, score
    def __init__(self, q_list):
        self.question_number = 0  # default attribute
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        """This function is going to retrieve the  item at the current question number from the question list."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False?)")
        self.check_answer(user_answer, current_question.answer)

    # todo: method - to check the number of question to complete
    def still_has_questions(self):
        """This function returns a boolean depending on the value of the question number"""
        return self.question_number < len(self.question_list)  # using expression inplace of if-else statement

    # todo : A function to check the answer and keep track of score
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("Wrong answer")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print()




