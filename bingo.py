from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from helpers import *
import sys

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

        settings = loadJSONFromFile(settings_file)

        # Set minimum display size
        self.setMinimumSize(800, 600)

        self.max_ball = False

        self.projector = projector
        if projector:
            self.projector = projector
            self.showHomePage()
        else:
            self.showPlay()

        title = settings["secondary_window_name"]
        if self.projector:  # if projector was passed then this one is the main page
            title = settings["primary_window_name"]
        self.setWindowTitle(title)

    def showHomePage(self):
        # Allow for updating the background image without restart
        settings = loadJSONFromFile(settings_file)
        stylesheet = f"""
    MainWindow {{
        background-image: url("{settings['background']}"); 
        background-repeat: no-repeat; 
        background-position: center;
    }}
"""
        self.setStyleSheet(stylesheet)
        # if projector:
        # If projector was passed then setup start page to begin with
        home_page = QVBoxLayout()
        home_page.setContentsMargins(0, 0, 0, 0)
        home_page.setSpacing(0)

        bingo_label = QLabel("pyBINGO")
        bingo_label.setStyleSheet("font-size: 120px;")
        bingo_label.setAlignment(Qt.AlignCenter)
        home_page.addWidget(bingo_label)

        button_grid = QGridLayout()
        # l, t, r, b
        button_grid.setContentsMargins(60, 0, 60, 60)
        button_grid.setSpacing(20)

        self.create_session_button = QPushButton("Create Session")
        self.create_session_button.setMinimumHeight(50)
        self.create_session_button.clicked.connect(self.create_session)
        button_grid.addWidget(self.create_session_button, 0, 0)

        self.edit_session_button = QPushButton("Edit Sessions")
        self.edit_session_button.setMinimumHeight(50)
        self.edit_session_button.clicked.connect(self.select_session)
        button_grid.addWidget(self.edit_session_button, 0, 1)

        self.load_session_button = QPushButton("Load Session")
        self.load_session_button.setMinimumHeight(50)
        self.load_session_button.clicked.connect(self.load_session)
        button_grid.addWidget(self.load_session_button, 0, 2)

        self.about_button = QPushButton("About")
        self.about_button.setMinimumHeight(50)
        self.about_button.clicked.connect(self.show_about)
        button_grid.addWidget(self.about_button, 1, 0)

        self.settings_button = QPushButton("Settings")
        self.settings_button.setMinimumHeight(50)
        self.settings_button.clicked.connect(self.show_settings)
        button_grid.addWidget(self.settings_button, 1, 1)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setMinimumHeight(50)
        self.exit_button.clicked.connect(self.exit_app)
        button_grid.addWidget(self.exit_button, 1, 2)

        home_page.addLayout(button_grid)

        widget = QWidget()
        widget.setLayout(home_page)
        self.setCentralWidget(widget)

    def show_settings(self):
        settings = loadJSONFromFile(settings_file)
        self.setStyleSheet("")
        settings_page = QVBoxLayout()
        settings_page.setContentsMargins(30, 30, 30, 30)
        settings_page.setSpacing(10)

        # creating a group box
        self.settingsFormBox = QGroupBox("Settings")
        self.settingsFormBox.setStyleSheet("font-size: 14px; font-weight: bold;")
        regular_font = "font-size: 11px; font-weight: normal;"
        # adding items to the combo box
        self.primary_window_name = QLineEdit(settings["primary_window_name"])
        self.primary_window_name.setStyleSheet(regular_font)
        self.secondary_window_name = QLineEdit(settings["secondary_window_name"])
        self.secondary_window_name.setStyleSheet(regular_font)
        # creating a form layout
        layout = QFormLayout()

        background_button = QPushButton("Select")
        background_button.setStyleSheet(regular_font)
        background_button.clicked.connect(self.dialog)
        self.home_page_background = QLineEdit(settings["background"])
        self.home_page_background.setStyleSheet(regular_font)

        # adding rows
        # for name and adding input text
        titles_style = "font-size: 12px; font-weight: bold;"
        name_titles = QLabel("Window names")
        name_titles.setStyleSheet(titles_style)
        layout.addRow(name_titles)

        self.primary_window_label = QLabel("Primary window")
        self.primary_window_label.setStyleSheet(regular_font)
        layout.addRow(self.primary_window_label, self.primary_window_name)

        secondary_window_label = QLabel("Secondary window")
        secondary_window_label.setStyleSheet(regular_font)
        layout.addRow(secondary_window_label, self.secondary_window_name)

        background_title = QLabel("Background")
        background_title.setStyleSheet(titles_style)

        layout.addRow(background_title)
        layout.addRow(background_button, self.home_page_background)
        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(
            lambda form=self.settingsFormBox: self.saveSettings(form)
        )

        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.showHomePage)

        layout.addRow(self.buttonBox)

        # setting layout
        self.settingsFormBox.setLayout(layout)

        # adding form group box to the layout
        settings_page.addWidget(self.settingsFormBox)

        # adding button box to the layout
        settings_page.addWidget(self.buttonBox)

        widget = QWidget()
        widget.setLayout(settings_page)
        self.setCentralWidget(widget)

    def dialog(self):
        file, check = QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py);;Text Files (*.txt)",
        )
        if check:
            self.home_page_background.setText(file)

    def saveSettings(self, form):
        settings = loadJSONFromFile(settings_file)
        new_primary_name = self.primary_window_name.text()
        new_secondary_name = self.secondary_window_name.text()
        new_background_image = self.home_page_background.text()
        settings["primary_window_name"] = new_primary_name
        settings["secondary_window_name"] = new_secondary_name
        settings["background"] = new_background_image
        msg = QMessageBox()
        try:
            saveJSONToFile(settings_file, settings)
            msg.setWindowTitle("Settings Saved")
            msg.setText(f"Settings successfully saved")
            msg.setIcon(QMessageBox.Information)
        except Exception as e:
            msg.setWindowTitle("Critical")
            msg.setText(f"Failed to save settings!")
            msg.setInformativeText(f"{e}")
            msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    def show_about(self):
        self.setStyleSheet("")

        container = QVBoxLayout()

        about_page = QHBoxLayout()

        about_developer = QVBoxLayout()
        about_developer.setContentsMargins(0, 0, 0, 0)

        # image path
        imgpath = "images/developer_scott_rowley.png"

        # loading image
        imgdata = open(imgpath, "rb").read()

        # calling the function
        pixmap = mask_image(imgdata, size=200)

        # creating label
        self.developer_img = QLabel("Image Label")
        self.developer_img.setStyleSheet("background-color: lightgray;")

        # putting image on label
        self.developer_img.setPixmap(pixmap)

        # moving the label
        self.developer_img.setAlignment(Qt.AlignCenter)

        # another label to put text
        developer_name = "Scott Rowley"
        name_styled = f'<span style="font-size: 32px;">{developer_name}</span>'
        developer_bio = f"""{name_styled}<br><a href="mailto:scott.m.rowley@gmail.com?subject='pyBingo Contact'">scott.m.rowley@gmail.com</a><br><br>
        Scott first started programming with QBasic in 1993
        and has since moved on to learn HTML, CSS, JavaScript/JQuery, SQL, PHP, BASH (Bourne-Again Shell), SAS, and Python.<br><br<br>
        Use the email address above to suggest updates or to contact Scott for your development needs.
        <br><br>View more of Scotts recent development work on <a href='http://github.com/SoftwareMods'>GitHub</a>"""
        self.developer_info = QLabel(developer_bio, self)
        self.developer_info.setOpenExternalLinks(True)
        self.developer_info.setWordWrap(True)
        self.developer_info.setStyleSheet(
            "background-color: lightgray; padding: 10px 60px;"
        )
        self.developer_info.setAlignment(Qt.AlignHCenter)

        about_developer.addWidget(self.developer_img)
        about_developer.addWidget(self.developer_info)

        about_software = QVBoxLayout()

        about_software_top = QHBoxLayout()
        software_name = "pyBingo"
        software_name_label = QLabel(software_name)
        software_name_label.setStyleSheet("font-size: 60px;")
        software_name_label.setAlignment(Qt.AlignCenter)
        about_software_top.addWidget(software_name_label)

        about_software_bottom = QVBoxLayout()
        software_title = "Software"
        software_name_styled = f'<span style="font-size: 32px;">{software_title}</span>'
        software_bio = f"""{software_name_styled}<br><br>
        pyBingo: 1.0.0<br>
        Windows 10 Pro: 19045.3324<br>
        Visual Studio Code: 1.81.1<br>
        Python: 3.11.4<br>
        PyQt5: 5.15.9"""
        self.software_info = QLabel(software_bio, self)
        self.software_info.setWordWrap(True)
        self.software_info.setStyleSheet("padding: 10px 80px;")
        self.software_info.setAlignment(Qt.AlignHCenter)
        about_software_bottom.addWidget(self.software_info)

        buttons_grid = QGridLayout()
        buttons_grid.setContentsMargins(0, 0, 0, 0)
        buttons_grid.setSpacing(5)
        buttons_grid.setAlignment(Qt.AlignRight)

        self.cancel_button = QDialogButtonBox(QDialogButtonBox.Cancel)

        # adding action when form is rejected
        self.cancel_button.rejected.connect(self.showHomePage)

        buttons_grid.addWidget(self.cancel_button, 0, 1)
        about_software.addLayout(about_software_top)
        about_software.addLayout(about_software_bottom)

        about_page.addLayout(about_developer)
        about_page.addLayout(about_software)

        container.addLayout(about_page)
        container.addLayout(buttons_grid)
        widget = QWidget()
        widget.setLayout(container)

        self.setCentralWidget(widget)

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
            self.select_session(showPlay=True)

    def select_session(self, showPlay=False):
        # First pop up a window to select which session
        window = QWidget()
        self.listWidget = QListWidget()

        sessions = self.load_all_sessions()
        for session in range(len(sessions)):
            name = sessions[session]["name"]
            if showPlay:
                if len(sessions[session]["games"]) == 0:
                    continue
            item = QListWidgetItem(name, self.listWidget)
            self.listWidget.addItem(item)

        if not showPlay:
            self.listWidget.itemDoubleClicked.connect(self.edit_session)
        else:
            self.listWidget.itemDoubleClicked.connect(
                lambda doCheck=True: self.showPlay(doCheck)
            )
        window_layout = QVBoxLayout(window)
        window_layout.addWidget(self.listWidget)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel)

        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.showHomePage)

        # adding button box to the layout
        window_layout.addWidget(self.buttonBox)
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
        self.edit_session_page = QVBoxLayout()
        self.edit_session_page.setContentsMargins(0, 0, 0, 0)
        self.edit_session_page.setSpacing(0)

        # Content
        # creating a group box
        self.formGroupBox = QGroupBox("Edit Session")

        # adding items to the combo box
        self.nameLineEdit = QLineEdit()
        self.nameLineEdit.setText(session_name)
        # creating a form layout
        self.update_form = QFormLayout()
        self.new_name = QLabel("Name")
        game_types = loadJSONFromFile(game_types_file)

        self.update_form.addRow(self.new_name, self.nameLineEdit)
        self.update_form.addRow(QLabel("Games"))
        self.cb_boxes = {}

        for i in range(selected_session["num_games"]):
            self.this_combo = QComboBox()
            self.cb_boxes[i] = self.this_combo
            for type in range(len(game_types)):
                self.cb_boxes[i].addItem(game_types[type]["name"])
                try:
                    if selected_session["games"][i]:
                        if selected_session["games"][i] == game_types[type]["name"]:
                            self.this_combo.setCurrentText(game_types[type]["name"])
                except:
                    pass
            self.update_form.addRow(QLabel(str(i + 1)), self.cb_boxes[i])

        self.formGroupBox.setLayout(self.update_form)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(
            lambda form=self.formGroupBox, id=selected_session["id"]: self.getForm(
                form, id
            )
        )

        self.buttonBox.rejected.connect(self.showHomePage)
        self.edit_session_page.addWidget(self.formGroupBox)
        self.edit_session_page.addWidget(self.buttonBox)

        ## end Content ##

        widget = QWidget()
        widget.setLayout(self.edit_session_page)
        self.setCentralWidget(widget)

    def getForm(self, form, id):
        game_types = []
        for widget in form.children():
            if isinstance(widget, QLineEdit):
                new_session_name = widget.text()

            if isinstance(widget, QComboBox):
                game_types.append(widget.currentText())

        saved_sessions = loadJSONFromFile(sessions_file)
        for n in range(len(saved_sessions)):
            if saved_sessions[n]["id"] == id:
                saved_sessions[n]["name"] = new_session_name
                saved_sessions[n]["games"] = game_types
                break
        msg = QMessageBox()
        try:
            saveJSONToFile(sessions_file, saved_sessions)
            msg.setWindowTitle("Session Saved")
            msg.setText(f"Session '{new_session_name}' successfully saved")
            msg.setIcon(QMessageBox.Information)
        except Exception as e:
            msg.setWindowTitle("Critical")
            msg.setText(f"Failed to save session!")
            msg.setInformativeText(f"{e}")
            msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()
        self.showHomePage()

    def create_session(self):
        self.setStyleSheet("")
        create_session_page = QVBoxLayout()
        create_session_page.setContentsMargins(0, 0, 0, 0)
        create_session_page.setSpacing(0)

        # creating a group box
        self.formGroupBox = QGroupBox("Create Session")

        # creating spin box to select age
        self.numGamesSpinBar = QSpinBox()
        self.numGamesSpinBar.setMinimum(1)
        self.numGamesSpinBar.setValue(16)

        # adding items to the combo box
        self.nameLineEdit = QLineEdit()

        # creating a form layout
        layout = QFormLayout()

        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Name"), self.nameLineEdit)

        # for age and adding spin box
        layout.addRow(QLabel("Games"), self.numGamesSpinBar)

        # setting layout
        self.formGroupBox.setLayout(layout)
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

    def saveNewSession(self):
        found = False
        saved = False
        sessions_list = loadJSONFromFile(sessions_file)
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
            id = getNewId(sessions_list)
            sessions_list.append(
                {"id": id, "name": session_name, "num_games": num_games, "games": []}
            )
            try:
                saveJSONToFile(sessions_file, sessions_list)
                msg.setWindowTitle("Session Saved")
                msg.setText(f"New session '{session_name}' successfully saved")
                msg.setIcon(QMessageBox.Information)
                saved = True
            except Exception as e:
                msg.setWindowTitle("Critical")
                msg.setText(f"Failed to save session!")
                msg.setInformativeText(f"{e}")
                msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()
        if saved:
            self.showHomePage()

    def showPlay(self, doCheck=False, game_index=0, **kwargs):
        self.setStyleSheet("")
        sessions = loadJSONFromFile(sessions_file)
        self.session = False
        self.payout = 0.0
        game_number = game_index + 1
        if doCheck:
            session_name = self.listWidget.selectedItems()[0].text()
            for i in range(len(sessions)):
                if sessions[i]["name"] == session_name:
                    self.session = sessions[i]
                    break
        else:
            try:
                self.session = kwargs["session"]
                game_number = game_index + 1
                self.payout = kwargs["payout"]
                self.projector.previous_num_label.setText(
                    setPreviousNumCalledText("None")
                )
                self.projector.called_number.setText("")
                self.projector.numbers_called.setText(getNumbersCalledText(0))
                for ball in self.projector.balls:
                    self.projector.balls[ball].setStyleSheet(ball_cell_style)
            except:
                pass

        self.letters = {"0": "B", "1": "I", "2": "N", "3": "G", "4": "O"}
        self.called_numbers = []

        main_div = QVBoxLayout()
        main_div.setContentsMargins(0, 0, 0, 0)
        main_div.setSpacing(0)

        top_half = QHBoxLayout()
        top_half_left = QVBoxLayout()
        self.previous_num_label = QLabel(setPreviousNumCalledText("None"))
        self.previous_num_label.setStyleSheet("font-size: 12px;")
        self.previous_num_label.setAlignment(Qt.AlignCenter)
        top_half_left.addWidget(self.previous_num_label, stretch=1)

        # TODO: Replace this with animated demo card
        top_half_left.addWidget(Color("#f0f0f0"), stretch=3)

        top_half_center = QVBoxLayout()

        # top_half_center content
        self.game_type = QLabel("")

        if self.session:
            self.game_type.setText(self.session["games"][game_index])
            self.projector.game_type.setText(self.session["games"][game_index])
        self.game_type.setStyleSheet("font-size: 18px;")
        self.game_type.setAlignment(Qt.AlignCenter)
        top_half_center.addWidget(self.game_type, stretch=1)

        self.called_number = QLabel("")
        self.called_number.setStyleSheet("font-size: 120px")
        self.called_number.setAlignment(Qt.AlignCenter)
        top_half_center.addWidget(self.called_number, stretch=4)

        top_half_right = QVBoxLayout()
        self.numbers_called = QLabel(getNumbersCalledText(0, self.max_ball))
        self.numbers_called.setStyleSheet("font-size: 12px;")
        self.numbers_called.setAlignment(Qt.AlignCenter)
        top_half_right.addWidget(self.numbers_called, stretch=1)

        self.payout_number = QLabel(setPayoutText(self.payout))
        if self.session:
            self.payout_number.setText(setPayoutText(self.payout))
        self.payout_number.setStyleSheet("font-size: 12px;")
        self.payout_number.setAlignment(Qt.AlignCenter)
        top_half_right.addWidget(self.payout_number, stretch=1)

        self.game_number = QLabel(setGameNumberText(game_number))
        if self.session:
            total_games = self.session["num_games"]
            self.game_number.setText(setGameNumberText(game_number, total_games))
            self.projector.game_number.setText(
                setGameNumberText(game_number, total_games)
            )
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
            if self.projector:
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

        if self.projector:
            button_grid = QGridLayout()
            # l, t, r, b
            button_grid.setContentsMargins(10, 5, 10, 10)
            button_grid.setSpacing(10)

            self.change_payout_button = QPushButton("Change Payout")
            self.change_payout_button.setMinimumHeight(50)
            self.change_payout_button.clicked.connect(self.payout_dialog)
            button_grid.addWidget(self.change_payout_button, 0, 0)

            self.change_max_button = QPushButton("Change Max Ball")
            self.change_max_button.setMinimumHeight(50)
            self.change_max_button.clicked.connect(self.maxball_dialog)
            button_grid.addWidget(self.change_max_button, 0, 1)

            self.next_end_button = QPushButton("Next Game")
            self.next_end_button.setMinimumHeight(50)
            if game_number < total_games:
                self.next_end_button.clicked.connect(
                    lambda session=self.session, game_index=game_index + 1: self.next_game(
                        session, game_index
                    )
                )
            else:
                self.next_end_button.setText("End Session")
                # For now, just go back to the home page.
                self.next_end_button.clicked.connect(self.showHomePage)
            button_grid.addWidget(self.next_end_button, 0, 2)

            self.back_button = QPushButton("Back")
            self.back_button.setMinimumHeight(50)
            self.back_button.clicked.connect(self.confirm_back)
            button_grid.addWidget(self.back_button, 0, 3)

            main_div.addLayout(button_grid)

        self.widget = QWidget()
        self.widget.setLayout(main_div)
        self.setCentralWidget(self.widget)

    def next_game(self, session, game_index):
        # session variable is not used here but must be passed to save self.session
        msg = QMessageBox()
        msg.setWindowTitle("Continue Session")
        msg.setText(f"Proceed to next game?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setIcon(QMessageBox.Question)
        response = msg.exec_()
        if response == QMessageBox.Yes:
            self.showPlay(
                doCheck=False,
                game_index=game_index,
                session=self.session,
                payout=self.payout,
            )

    def payout_dialog(self):
        text, ok = QInputDialog.getText(self, "Change Payout", "Enter new payout")
        if ok:
            self.payout = text
            self.payout_number.setText(setPayoutText(text))
            self.projector.payout_number.setText(setPayoutText(text))

    def maxball_dialog(self):
        text, ok = QInputDialog.getText(self, "Change Max Ball", "Enter new maximum")
        called = (
            self.numbers_called.text().split("</span>")[0].split(">")[-1].split("/")[0]
        )
        if ok:
            self.numbers_called.setText(getNumbersCalledText(called, text))
            self.projector.numbers_called.setText(getNumbersCalledText(called, text))

    def confirm_back(self):
        msg = QMessageBox()
        msg.setWindowTitle("Abandon Session")
        msg.setText(f"Abandon session and return to title page?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setIcon(QMessageBox.Warning)
        response = msg.exec_()
        if response == QMessageBox.Yes:
            self.showHomePage()

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
                setPreviousNumCalledText(self.called_numbers[-2])
            )
        else:
            self.previous_num_label.setText(setPreviousNumCalledText("None"))

        get_nums_called_text = getNumbersCalledText(
            len(self.called_numbers), self.max_ball
        )
        self.numbers_called.setText(get_nums_called_text)


app = QApplication([])
projector = MainWindow()
projector.show()

admin = MainWindow(projector)
admin.show()

app.exec_()
