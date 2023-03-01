from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

#first tap into the list
for question in question_data:
    #assign the key and value of each dictionary to a variable
    question_text = question["text"]
    question_answer = question["answer"]
    #create a new object for each question
    new_question = Question(text = question_text, answer = question_answer)
    #append the newly created object to the formerly empty list "question_bank"
    question_bank.append(new_question)
                   
#access the values of each object with the .answer or .text attribute 
#print(question_bank[0].answer)


#run the quiz til the end of all questions
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

#giving feedback at the end of the quiz
print("You've completed the quiz")
print(f"You're final score was: {quiz.score}/{quiz.question_number}.")