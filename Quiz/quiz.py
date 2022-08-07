class Quiz:
    questions = {}
    answers = {}

class Question:
    question_id = 0

    def __init__(self, question):
        Question.question_id += 1
        self.id = Question.question_id
        self.question = question
        Quiz.questions[self.id] = self.question
    
    def __repr__(self):
        description = """
        This is question number {id}. It goes as follows:
        {question}
        """.format(id = self.id, question = self.question)
        return description

class Answer:
    answer_id = 0

    def __init__(self, question_id, answer):
        self.question_id = question_id
        self.answer = answer
        Answer.answer_id += 1
        self.id = Answer.answer_id
        Quiz.answers[self.id] = [question_id, self.answer]


question_1 = Question("Wo steht der \"schiefe Turm\"?")
print(question_1)

answer_1 = Answer(1, "Pisa")
print(answer_1)

print(Quiz.questions)
print(Quiz.answers)