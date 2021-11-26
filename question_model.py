# create a question class with an __init()__ method that has two attributes namely, text & answer attributes

class Question:
    """ This class is created to model a question and answers in the quiz game. """

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


# # just to  check
# new_q = Question("starting the game", True)
# print(new_q.text)
