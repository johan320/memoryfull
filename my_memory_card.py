from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QVBoxLayout,QHBoxLayout, QMessageBox, QRadioButton, QButtonGroup
from random import *

class Question():
    def __init__(self,next_question,right_ans,wr_ans1,wr_ans2,wr_ans3):
        self.next_question = next_question
        self.right_ans = right_ans
        self.wr_ans1 = wr_ans1
        self.wr_ans2 = wr_ans2
        self.wr_ans3 = wr_ans3


def show_correct(res):
    if res:
        RadioGroupBox.hide()
        AnsGroupBox.show()
        result_lable.setText('Правильно')
        main_win.score +=1
    
    else:
        RadioGroupBox.hide()
        AnsGroupBox.show()
        result_lable.setText('Неверно')
        
    otvet.setText('Следуйщий вопрос:')

def check_answer():
    if answers[0].isChecked():
        show_correct(True)
    else:
        show_correct(False)


    



def ask(q):
    AnsGroupBox.hide()
    RadioGroupBox.show()
    RadioGroup.setExclusive(False)
    ot1.setChecked(False)
    ot2.setChecked(False)
    ot3.setChecked(False)
    ot4.setChecked(False)
    RadioGroup.setExclusive(True)
    question.setText(q.next_question)
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wr_ans1)
    answers[2].setText(q.wr_ans2)
    answers[3].setText(q.wr_ans3)
    question.setText(q.next_question)
    otvet.setText('ответить')


def click_on():
    if otvet.text() == 'ответить':
        check_answer()
    else:
        next_questions()

def next_questions():

    main_win.total +=1
    sco = int(main_win.score/main_win.total*100)
    print('Твоя статистика:', sco, '%', '\n Кол-во верных ответов:', main_win.score, '\n Кол-во всех вопросов:', main_win.total)
    cur_quest = randint(0, len(question_list) - 1)
    q = question_list[cur_quest]
    ask(q)




app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
main_win.total = 0
main_win.score = 0
main_win.resize(500,500)
question = QLabel('12380198x0')
otvet = QPushButton('ответить')
RadioGroupBox = QGroupBox('Варианты ответов:')
AnsGroupBox = QGroupBox('Результат:')
result_lable = QLabel("sdasda")
result_line = QVBoxLayout()
result_line.addWidget(result_lable)
AnsGroupBox.setLayout(result_line)
AnsGroupBox.hide()
RadioGroup = QButtonGroup()
ot1 = QRadioButton('0')
ot2 = QRadioButton('21312311452315634534')
ot3 = QRadioButton('1')
ot4 = QRadioButton('01231231')
question_list = [Question('1+1','2','3','4','5'),Question('2+2x2','6','8','6','1'),Question('2+2','4','5000','1','2')]

answers = [ot1, ot2, ot3, ot4]
RadioGroup.addButton(ot1)
RadioGroup.addButton(ot2)
RadioGroup.addButton(ot3)
RadioGroup.addButton(ot4)
layouth = QHBoxLayout()
layoutv1 = QVBoxLayout()
layoutv2 = QVBoxLayout()

layoutotvet = QHBoxLayout()
mainlayout = QVBoxLayout()
mainanswerlayout = QHBoxLayout()
maingrouplayout = QHBoxLayout()
mainotvetlayout = QHBoxLayout()

mainanswerlayout.addWidget(question)
maingrouplayout.addWidget(RadioGroupBox)
maingrouplayout.addWidget(AnsGroupBox)
mainotvetlayout.addWidget(otvet)
layoutv1.addWidget(ot1)
layoutv1.addWidget(ot2)
layoutv2.addWidget(ot3)
layoutv2.addWidget(ot4)
layoutotvet.addWidget(otvet)

layouth.addLayout(layoutv1)
layouth.addLayout(layoutv2)

mainlayout.addLayout(mainanswerlayout)
mainlayout.addLayout(maingrouplayout)
mainlayout.addLayout(mainotvetlayout)
RadioGroupBox.setLayout(layouth)
main_win.setLayout(mainlayout)


otvet.clicked.connect(click_on)





main_win.show()
app.exec_()
