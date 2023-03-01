class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
 

    def still_has_questions(self):
        #gives back True or False until the end of questions
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        #pass over the user's answer and the correct answer to the function check_answer()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        #check if uswer answer and correct answer are the same, for security lower() both so that user can also type in true or false without error message
        if user_answer.lower() == correct_answer.lower():
            self.score += 1 
            print("You got it right!")
        else: 
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")

       


        