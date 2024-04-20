#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from random import shuffle

####
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
#####

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(True)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)
    btn_OK.setText('Ответить')

def test():
    if btn_OK.text()=='Ответить':
        show_result()
    else:
        show_question()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос') 

app = QApplication([])

lb_Question = QLabel('Как по тувински называют Йети?')

# создание кнопок переключения
answer1 = QRadioButton('Ак-кижи')
answer2 = QRadioButton('Хар-кижи')
answer3 = QRadioButton('Кижи-бурус')
answer4 = QRadioButton('Кижи-адыг')

RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)
btn_OK = QPushButton('Ответить')

lb_Question.setFont(QFont('Times New Roman',25))
answer1.setFont(QFont('Times New Roman',15))
answer2.setFont(QFont('Times New Roman',15))
answer3.setFont(QFont('Times New Roman',15))
answer4.setFont(QFont('Times New Roman',15))
btn_OK.setFont(QFont('Times New Roman',15))
RadioGroupBox.setFont(QFont('Times New Roman',12))

layout_main = QVBoxLayout()
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()

layout_ans1.addWidget(answer1, alignment = Qt.AlignLeft)
layout_ans1.addWidget(answer2, alignment = Qt.AlignLeft)
layout_ans2.addWidget(answer3, alignment = Qt.AlignLeft)
layout_ans2.addWidget(answer4, alignment = Qt.AlignLeft)

layout_main.addLayout(layout_ans1)
layout_main.addLayout(layout_ans2)
RadioGroupBox.setLayout(layout_main)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

# область ответа (начало)
AnsGroupBox=QGroupBox('Результат теста')
lb_Result=QLabel('Прав ты или нет?')
lb_Correct=QLabel('Ответ будет тут')

layout_Res=QVBoxLayout()
layout_Res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_Res.addWidget(lb_Correct, alignment=Qt.AlignCenter)

AnsGroupBox.setLayout(layout_Res)
AnsGroupBox.hide()
# область ответа(конец)

layout_line1.addWidget(lb_Question,alignment = Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addWidget(btn_OK)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

##########
answers = [answer1, answer2, answer3, answer4]


def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ 
    show_question() # показываем панель вопросов 


def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()

def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        ###
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
        ###
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')


def next_question():
    ''' задает следующий вопрос из списка '''
    window.total += 1
    
    if window.total > len(questions_list):
        exit()
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    q = questions_list[window.total-1] # взяли вопрос
    ask(q) # спросили


def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос


########

#main_window = QWidget() #главное окно
#main_window.setWindowTitle('Memory Card') #заголовок
#main_window.resize(450, 250) #размер окна
#main_window.setLayout(layout_card)
#button.clicked.connect(test)

#main_window.show()
#app.exec_()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
# текущий вопрос из списка сделаем свойством объекта "окно", так мы сможем спокойно менять его из функции:
window.cur_question = -1    # по-хорошему такие переменные должны быть свойствами, 
                            # только надо писать класс, экземпляры которого получат такие свойства, 
                            # но python позволяет создать свойство у отдельно взятого экземпляра


btn_OK.clicked.connect(click_OK) # по нажатии на кнопку выбираем, что конкретно происходит

window.score = 0
window.total = 0
# все настроено, осталось задать вопрос и показать окно:
next_question()
window.resize(400, 300)
window.show()
app.exec()