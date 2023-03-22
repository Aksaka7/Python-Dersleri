# Question Soru vevap GEliştirme

class Question():
    def __init__(self, text, choice, answer):
        self.text = text
        self.choice = choice
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# Quiz
class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru{self.questionIndex + 1}: {question.text}")

        for q in question.choice:
            print('-' + q)

        answer = input("Cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Score: {self.score}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Sorular Bitti    ")
        else:
            print(
                f'Question {questionNumber} of {totalQuestion}'.center(100, '*'))


q1 = Question('En iyi programlama Dili hangisidir.', [
              'C#', 'Python', 'C++', 'Java'], 'Python')
q2 = Question('En popüler programlama Dili hangisidir.',
              ['C#',  'C++', 'Java', 'Python'], 'Python')
q3 = Question('En çok kazandıran programlama Dili hangisidir.',
              ['Java', 'C#', 'Python', 'C++'], 'Python')

questions = [q1, q2, q3]

quiz = Quiz(questions)
question = quiz.getQuestion()

quiz.loadQuestion()
# print(q1.checkAnswer('Python'))
# print(q2.checkAnswer('C++'))
# print(q3.checkAnswer('Mehmet'))
