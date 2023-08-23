from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        self.color = color

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(self.color))
        self.setPalette(palette)

ball_cell_style = "font-size: 24px; padding: 4px 10px; background-color: white; color: gray; border: 1px solid gray;"

class Ball(QPushButton):
    def __init__(self,txt):
        super(Ball,self).__init__()
        self.setText(txt)
        self.setStyleSheet(ball_cell_style)

class MainWindow(QMainWindow):

    def __init__(self,projector=None):
        super(MainWindow, self).__init__()

        self.projector = None
        if projector:
            self.projector = projector

        title = "Projector"
        if self.projector:  # if projector was passed then this one is the main page
            title = "Bingo!"
        self.setWindowTitle(title)
        self.setMinimumWidth(640)
        self.setMinimumHeight(480)
        self.max_ball = 52

        self.called_numbers = []

        main_div = QVBoxLayout()
        main_div.setContentsMargins(0,0,0,0)
        main_div.setSpacing(0)

        top_half = QHBoxLayout()
        top_half_left = QVBoxLayout()
        self.previous_num_label = QLabel(self.setPreviousNumCalledText(''))
        self.previous_num_label.setStyleSheet("font-size: 12px;")
        self.previous_num_label.setAlignment(Qt.AlignCenter)
        top_half_left.addWidget(self.previous_num_label,stretch=1)
        top_half_left.addWidget(Color('black'), stretch=3)

        top_half_center = QVBoxLayout()

        # top_half_center content
        self.game_type = QLabel('Regular or 4 Corners')
        self.game_type.setStyleSheet("font-size: 18px;")
        self.game_type.setAlignment(Qt.AlignCenter)
        top_half_center.addWidget(self.game_type,stretch=1)
        
        self.called_number = QLabel('X99')
        self.called_number.setStyleSheet("font-size: 120px")
        self.called_number.setAlignment(Qt.AlignCenter)
        top_half_center.addWidget(self.called_number, stretch=4)

        top_half_right = QVBoxLayout()
        self.numbers_called = QLabel(self.getNumbersCalledText(0,52))
        self.numbers_called.setStyleSheet("font-size: 12px;")
        self.numbers_called.setAlignment(Qt.AlignCenter)
        top_half_right.addWidget(self.numbers_called,stretch=1)
        
        self.payout_number = QLabel(self.setPayoutText(15.00))
        self.payout_number.setStyleSheet("font-size: 12px;")
        self.payout_number.setAlignment(Qt.AlignCenter)
        top_half_right.addWidget(self.payout_number, stretch=1)

        self.game_number = QLabel(self.setGameNumberText(1))
        self.game_number.setStyleSheet("font-size: 12px;")
        self.game_number.setAlignment(Qt.AlignCenter)
        top_half_right.addWidget(self.game_number,stretch=1)

        top_half.addLayout(top_half_left,stretch=1)
        top_half.addLayout(top_half_center,stretch=2)
        top_half.addLayout(top_half_right,stretch=1)
        main_div.addLayout( top_half, stretch=2 )

        layout = QGridLayout()
        
        head_style = "font-size: 24px; padding: 4px 16px; background-color: black; color: white; border: 1px solid gray;"

        self.b_head = QLabel('B')
        self.b_head.setStyleSheet(head_style)
        self.b_head.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.b_head,0,0)

        self.i_head = QLabel('I')
        self.i_head.setStyleSheet(head_style)
        self.i_head.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.i_head,1,0)

        self.n_head = QLabel('N')
        self.n_head.setStyleSheet(head_style)
        self.n_head.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.n_head,2,0)

        self.g_head = QLabel('G')
        self.g_head.setStyleSheet(head_style)
        self.g_head.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.g_head,3,0)

        self.o_head = QLabel('O')
        self.o_head.setStyleSheet(head_style)
        self.o_head.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.o_head,4,0)

        # Create each ball and store for calling
        self.balls = {}
        row = 0
        col = 1
        rows = {'0': 'B', '1': 'I', '2': 'N', '3': 'G', '4': 'O'}
        for i in range(1,76):
            letter = rows[str(row)]            
            self.this_ball = Ball(str(i))
            self.balls[f'{letter}{i}'] = self.this_ball
            self.this_ball.clicked.connect(lambda checked, text=f'{letter}{i}': self.ball_clicked(text))
            layout.addWidget(self.this_ball,row,col)
            if col < 15:
                col+=1
            else:
                col=1
                row+=1
        
        main_div.addLayout( layout, stretch=2 )

        self.widget = QWidget()
        self.widget.setLayout(main_div)
        self.setCentralWidget(self.widget)

    def resizeEvent(self,event):
        pass

    def ball_clicked(self,num):
        if self.projector:
            self.projector.ball_clicked(num)
        style = ball_cell_style
        mod_name = self.balls[str(num)]
        if num not in self.called_numbers:
            style = "font-size: 24px; padding: 4px 10px; background-color: white; color: red; border: 1px solid gray;"  
            self.called_numbers.append(num)
            self.called_number.setText(num)
        else:
            while(num in self.called_numbers):
                self.called_numbers.remove(num)
        mod_name.setStyleSheet(style)

        if len(self.called_numbers) >= 2:
            self.previous_num_label.setText(self.setPreviousNumCalledText(self.called_numbers[-2]))
        else:
            self.previous_num_label.setText('')

        get_nums_called_text = self.getNumbersCalledText(len(self.called_numbers),self.max_ball)
        self.numbers_called.setText(get_nums_called_text)


    def setPayoutText(self,txt):
        return f'Payout<br><span style="color: blue; font-weight: bold;">{txt}</span>'
    
    def getNumbersCalledText(self,curr,max):
        return f'Numbers Called<br><span style="color: blue; font-weight: bold;">{curr}/{max}</span>'
    
    def setPreviousNumCalledText(self,num):
        return f'Previous Number<br><span style="color: blue; font-weight: bold; font-size: 16px;">{num}</span>'
    
    def setGameNumberText(self,num,total=None):
        show_total = ""
        if total:
            show_total = f'/{total}'
        return f'Game Number<br><span style="color: blue; font-weight: bold;">{num}{show_total}</span>'

app = QApplication([])

projector = MainWindow()
projector.show()

admin = MainWindow(projector)
admin.show()

app.exec_()