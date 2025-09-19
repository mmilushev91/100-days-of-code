from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def createQuestionBank(data):
  question_list = []
  
  for item in data:
    question = Question(q_text = item["question"], q_answer=item["correct_answer"])
    question_list.append(question)

  return question_list

question_bank = createQuestionBank(question_data)
quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()

while quiz_brain.still_has_questions():
  quiz_brain.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")
