from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from helpers import *
import sys

stylesheet = """
    MainWindow {
        background-image: url("images/background.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""
ball_cell_style = "font-size: 24px; padding: 4px 10px; background-color: white; color: gray; border: 1px solid gray;"


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        self.color = color

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(self.color))
        self.setPalette(palette)


class Ball(QPushButton):
    def __init__(self, txt):
        super(Ball, self).__init__()
        self.setText(txt)
        self.setStyleSheet(ball_cell_style)


class MainWindow(QMainWindow):
    def __init__(self, projector=None):
        super(MainWindow, self).__init__()

        # Set minimum display size
        self.setMinimumSize(800, 600)
        self.blackout = False
        if self.blackout:
            self.max_ball = 52
        else:
            self.max_ball = False

        self.projector = projector
        if projector:
            self.projector = projector
            self.showHomePage()
        else:
            self.showPlay()

        title = "Projector"
        if self.projector:  # if projector was passed then this one is the main page
            title = "Bingo!"
        self.setWindowTitle(title)

    def showHomePage(self):
        self.setStyleSheet(stylesheet)
        # if projector:
        # If projector was passed then setup start page to begin with
        home_page = QVBoxLayout()
        home_page.setContentsMargins(0, 0, 0, 0)
        home_page.setSpacing(0)

        bingo_label = QLabel("BINGO")
        bingo_label.setStyleSheet("font-size: 240px;")
        bingo_label.setAlignment(Qt.AlignCenter)
        home_page.addWidget(bingo_label)

        button_grid = QGridLayout()
        # l, t, r, b
        button_grid.setContentsMargins(100, 20, 100, 100)
        button_grid.setSpacing(20)

        self.create_session_button = QPushButton("Create Session")
        self.create_session_button.setMinimumHeight(50)
        self.create_session_button.clicked.connect(lambda: self.create_session())
        button_grid.addWidget(self.create_session_button, 0, 0)

        self.edit_session_button = QPushButton("Edit Sessions")
        self.edit_session_button.setMinimumHeight(50)
        self.edit_session_button.clicked.connect(lambda: self.select_session())
        button_grid.addWidget(self.edit_session_button, 0, 1)

        self.load_session_button = QPushButton("Load Session")
        self.load_session_button.setMinimumHeight(50)
        self.load_session_button.clicked.connect(lambda: self.load_session())
        button_grid.addWidget(self.load_session_button, 0, 2)

        self.about_button = QPushButton("About")
        self.about_button.setMinimumHeight(50)
        self.about_button.clicked.connect(lambda: self.show_about())
        button_grid.addWidget(self.about_button, 0, 3)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setMinimumHeight(50)
        self.exit_button.clicked.connect(lambda: self.exit_app())
        button_grid.addWidget(self.exit_button, 0, 4)

        home_page.addLayout(button_grid)

        widget = QWidget()
        widget.setLayout(home_page)
        self.setCentralWidget(widget)

    def show_about(self):
        print("awwww, you care?")

    def exit_app(self):
        sys.exit()

    def load_all_sessions(self):
        return loadJSONFromFile(sessions_file)

    def load_session(self):
        sessions = self.load_all_sessions()
        has_games = []
        for s in range(len(sessions)):
            if len(sessions[s]["games"]) > 0:
                has_games.append(sessions[s])

        if not has_games:
            msg = QMessageBox()
            msg.setWindowTitle("No games available")
            msg.setText(f"No sessions available with games.")
            msg.setInformativeText("You must first add games to a created session.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            self.showHomePage()
        else:
            print("load selection window with list of sessions that have games")
        # for now just load the play window
        # self.showPlay()

    def select_session(self):
        # First pop up a window to select which session
        window = QWidget()
        self.listWidget = QListWidget()

        sessions = self.load_all_sessions()
        for session in range(len(sessions)):
            name = sessions[session]["name"]
            item = QListWidgetItem(name, self.listWidget)
            self.listWidget.addItem(item)

        self.listWidget.itemDoubleClicked.connect(lambda: self.edit_session())
        window_layout = QVBoxLayout(window)
        window_layout.addWidget(self.listWidget)
        window.setLayout(window_layout)

        self.setCentralWidget(window)

    def edit_session(self):
        session_name = self.listWidget.selectedItems()[0].text()
        # Retrieve session with session_name
        sessions = self.load_all_sessions()
        selected_session = False
        for session in range(len(sessions)):
            if sessions[session]["name"] == session_name:
                selected_session = sessions[session]
                break

        # Populate selected session to page
        self.setStyleSheet("")
        edit_session_page = QVBoxLayout()
        edit_session_page.setContentsMargins(0, 0, 0, 0)
        edit_session_page.setSpacing(0)

        # Content
        # creating a group box
        self.formGroupBox = QGroupBox("Edit Session")

        # adding items to the combo box
        self.nameLineEdit = QLineEdit()
        self.nameLineEdit.setText(session_name)
        # creating a form layout
        update_form = QFormLayout()
        self.new_name = QLabel("Name")
        self.game_typeList = QListWidget()

        update_form.addRow(self.new_name, self.nameLineEdit)

        self.formGroupBox.setLayout(update_form)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        #self.buttonBox.accepted.connect(lambda checked, sessions=sessions: saveJSONToFile(sessions_file,sessions))

        self.buttonBox.rejected.connect(self.showHomePage)
        edit_session_page.addWidget(self.formGroupBox)
        edit_session_page.addWidget(self.buttonBox)

        ## end Content ##

        widget = QWidget()
        widget.setLayout(edit_session_page)
        self.setCentralWidget(widget)

    def create_session(self):
        self.setStyleSheet("")
        create_session_page = QVBoxLayout()
        create_session_page.setContentsMargins(0, 0, 0, 0)
        create_session_page.setSpacing(0)

        bingo_label = QLabel("BINGO")
        bingo_label.setStyleSheet("font-size: 120px;")
        bingo_label.setAlignment(Qt.AlignCenter)
        create_session_page.addWidget(bingo_label)

        # creating a group box
        self.formGroupBox = QGroupBox("Create Session")

        # creating spin box to select age
        self.numGamesSpinBar = QSpinBox()
        self.numGamesSpinBar.setMinimum(1)
        self.numGamesSpinBar.setValue(16)

        # creating combo box to select degree
        self.degreeComboBox = QComboBox()

        # adding items to the combo box
        self.nameLineEdit = QLineEdit()
        self.createForm()
        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.saveNewSession)

        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)

        # adding form group box to the layout
        create_session_page.addWidget(self.formGroupBox)

        # adding button box to the layout
        create_session_page.addWidget(self.buttonBox)


        widget = QWidget()
        widget.setLayout(create_session_page)
        self.setCentralWidget(widget)

    def reject(self):
        self.showHomePage()

    # create form method
    def createForm(self):
        # creating a form layout
        layout = QFormLayout()

        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Name"), self.nameLineEdit)

        # for age and adding spin box
        layout.addRow(QLabel("Games"), self.numGamesSpinBar)

        # setting layout
        self.formGroupBox.setLayout(layout)

    def saveNewSession(self):
        sessions_list = loadJSONFromFile(sessions_file)
        found = False
        session_name = self.nameLineEdit.text()
        num_games = int(self.numGamesSpinBar.text())
        msg = QMessageBox()
        for i in range(len(sessions_list)):
            if sessions_list[i]["name"] == session_name:
                found = True
                msg.setWindowTitle("Warning")
                msg.setText(f"Session '{session_name}' already exists!")
                msg.setIcon(QMessageBox.Warning)
                break

        if not found:
            sessions_list.append(
                {"name": session_name, "num_games": num_games, "games": []}
            )
            try:
                saveJSONToFile(sessions_file, sessions_list)
                msg.setWindowTitle("Session Saved")
                msg.setText(f"New session '{session_name}' successfully saved")
                msg.setIcon(QMessageBox.Information)
            except Exception as e:
                msg.setWindowTitle("Critical")
                msg.setText(f"Failed to save session!")
                msg.setInformativeText(f"{e}")
                msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    def showPlay(self):
        self.letters = {"0": "B", "1": "I", "2": "N", "3": "G", "4": "O"}
        self.called_numbers = []

        main_div = QVBoxLayout()
        main_div.setContentsMargins(0, 0, 0, 0)
        main_div.setSpacing(0)

        top_half = QHBoxLayout()
        top_half_left = QVBoxLayout()
        self.previous_num_label = QLabel(self.setPreviousNumCalledText("None"))
        self.previous_num_label.setStyleSheet("font-size: 12px;")
        self.previous_num_label.setAlignment(Qt.AlignCenter)
        top_half_left.addWidget(self.previous_num_label, stretch=1)

        # TODO: Replace this with animaged demo card
        top_half_left.addWidget(Color("#f0f0f0"), stretch=3)

        top_half_center = QVBoxLayout()

        # top_half_center content
        self.game_type = QLabel("Regular or 4 Corners")
        self.game_type.setStyleSheet("font-size: 18px;")
        self.game_type.setAlignment(Qt.AlignCenter)
        top_half_center.addWidget(self.game_type, stretch=1)

        self.called_number = QLabel("")
        self.called_number.setStyleSheet("font-size: 120px")
        self.called_number.setAlignment(Qt.AlignCenter)
        top_half_center.addWidget(self.called_number, stretch=4)

        top_half_right = QVBoxLayout()
        self.numbers_called = QLabel(self.getNumbersCalledText(0, self.max_ball))
        self.numbers_called.setStyleSheet("font-size: 12px;")
        self.numbers_called.setAlignment(Qt.AlignCenter)
        top_half_right.addWidget(self.numbers_called, stretch=1)

        self.payout_number = QLabel(self.setPayoutText(15.00))
        self.payout_number.setStyleSheet("font-size: 12px;")
        self.payout_number.setAlignment(Qt.AlignCenter)
        top_half_right.addWidget(self.payout_number, stretch=1)

        self.game_number = QLabel(self.setGameNumberText(1))
        self.game_number.setStyleSheet("font-size: 12px;")
        self.game_number.setAlignment(Qt.AlignCenter)
        top_half_right.addWidget(self.game_number, stretch=1)

        top_half.addLayout(top_half_left, stretch=1)
        top_half.addLayout(top_half_center, stretch=2)
        top_half.addLayout(top_half_right, stretch=1)
        main_div.addLayout(top_half, stretch=2)

        layout = QGridLayout()

        head_style = "font-size: 24px; padding: 4px 16px; background-color: black; color: white; border: 1px solid gray;"

        letter_row = 0
        for key in self.letters.keys():
            self.head = QLabel(self.letters[str(key)])
            self.head.setStyleSheet(head_style)
            self.head.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.head, letter_row, 0)
            letter_row += 1

        # Create each ball and store for calling
        self.balls = {}
        row = 0
        col = 1

        for i in range(1, 76):
            letter = self.letters[str(row)]
            self.this_ball = Ball(str(i))
            self.balls[f"{letter}{i}"] = self.this_ball
            self.this_ball.clicked.connect(
                lambda checked, text=f"{letter}{i}": self.ball_clicked(text)
            )
            layout.addWidget(self.this_ball, row, col)
            if col < 15:
                col += 1
            else:
                col = 1
                row += 1

        main_div.addLayout(layout, stretch=2)

        button_grid = QGridLayout()
        # l, t, r, b
        button_grid.setContentsMargins(10, 5, 10, 10)
        button_grid.setSpacing(10)

        self.change_payout_button = QPushButton("Change Payout")
        self.change_payout_button.setMinimumHeight(50)
        self.change_payout_button.clicked.connect(lambda: self.payout_dialog())
        button_grid.addWidget(self.change_payout_button, 0, 0)

        self.change_max_button = QPushButton("Change Max Ball")
        self.change_max_button.setMinimumHeight(50)
        self.change_max_button.clicked.connect(lambda: self.maxball_dialog())
        button_grid.addWidget(self.change_max_button, 0, 1)

        self.claim_bingo_button = QPushButton("Claim Bingo")
        self.claim_bingo_button.setMinimumHeight(50)
        self.claim_bingo_button.clicked.connect(lambda: self.edit_session())
        button_grid.addWidget(self.claim_bingo_button, 0, 2)

        self.next_game_button = QPushButton("Next Game")
        self.next_game_button.setMinimumHeight(50)
        self.next_game_button.clicked.connect(lambda: self.next_game())
        button_grid.addWidget(self.next_game_button, 0, 3)

        self.back_button = QPushButton("Back")
        self.back_button.setMinimumHeight(50)
        self.back_button.clicked.connect(lambda: self.confirm_back())
        button_grid.addWidget(self.back_button, 0, 4)

        main_div.addLayout(button_grid)

        self.widget = QWidget()
        self.widget.setLayout(main_div)
        self.setCentralWidget(self.widget)

    def payout_dialog(self):
        text, ok = QInputDialog.getText(self, "Change Payout", "Enter new payout")
        if ok:
            self.payout_number.setText(self.setPayoutText(text))

    def maxball_dialog(self):
        text, ok = QInputDialog.getText(self, "Change Max Ball", "Enter new maximum")
        called = (
            self.numbers_called.text().split("</span>")[0].split(">")[-1].split("/")[0]
        )
        if ok:
            self.numbers_called.setText(self.getNumbersCalledText(called, text))

    def confirm_back(self):
        msg = QMessageBox()
        msg.setWindowTitle("Abandon Session")
        msg.setText(f"Abandon session and return to title page?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setIcon(QMessageBox.Warning)
        response = msg.exec_()
        if response == QMessageBox.Yes:
            self.showHomePage()

    def resizeEvent(self, event):
        pass

    def ball_clicked(self, num):
        if self.projector:
            self.projector.ball_clicked(num)
        style = ball_cell_style
        mod_name = self.balls[str(num)]
        if num not in self.called_numbers:
            style = "font-size: 24px; padding: 4px 10px; background-color: white; color: red; border: 1px solid gray;"
            self.called_numbers.append(num)
            self.called_number.setText(num)
        else:
            while num in self.called_numbers:
                self.called_numbers.remove(num)
        mod_name.setStyleSheet(style)

        if len(self.called_numbers) >= 2:
            self.previous_num_label.setText(
                self.setPreviousNumCalledText(self.called_numbers[-2])
            )
        else:
            self.previous_num_label.setText(self.setPreviousNumCalledText("None"))

        get_nums_called_text = self.getNumbersCalledText(
            len(self.called_numbers), self.max_ball
        )
        self.numbers_called.setText(get_nums_called_text)

    def setPayoutText(self, txt):
        return f'Payout<br><span style="color: blue; font-weight: bold;">{txt}</span>'

    def getNumbersCalledText(self, curr, max=None):
        show_max = ""
        if max:
            show_max = f"/{max}"
        return f'Numbers Called<br><span style="color: blue; font-weight: bold;">{curr}{show_max}</span>'

    def setPreviousNumCalledText(self, num):
        return f'Previous Number<br><span style="color: blue; font-weight: bold; font-size: 16px;">{num}</span>'

    def setGameNumberText(self, num, total=None):
        show_total = ""
        if total:
            show_total = f"/{total}"
        return f'Game Number<br><span style="color: blue; font-weight: bold;">{num}{show_total}</span>'


app = QApplication([])

projector = MainWindow()
projector.show()
# We don't need the projector right now, close it
projector.close()

admin = MainWindow(projector)
admin.show()

app.exec_()
