class Quiz:
    questions = {}
    answers = {}

    def play_quiz(self):
        for question in self.questions:
            frage = """
            Die Frage lautet: {frage}
            """.format(frage = self.questions[question])
            print(frage)
            antwort = "Die Antwortmöglichkeiten lauten:\n"
            for answer in self.answers:
                if self.answers[answer][0] == question:
                    antwort += self.answers[answer][1]+"\n"
            print(antwort)

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
    
    def __repr__(self):
        description = """
        This is answer number {id}. It belongs to question number {question_id}.
        It reads: "{answer}"
        """.format(id = self.id, question_id = self.question_id, answer = self.answer)
        return description


question_1 = Question("Wo steht der \"schiefe Turm\"?")
#print(question_1)


answer_1 = Answer(1, "Pisa")
answer_2 = Answer(1, "Mailand")
answer_3 = Answer(1, "Rom")
answer_4 = Answer(1, "Verona")
#print(answer_1)

print(Quiz.questions)
print(Quiz.answers)

my_quiz = Quiz()

my_quiz.play_quiz()
