# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bingo_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from helpers import *


class Ui_Form(object):
    def setupUi(self, Form, game_type_name, pattern, readOnly=True, fn=False):
        self.readOnly = readOnly
        self.game_type_name = game_type_name
        self.pattern = pattern
        self.game_types = loadJSONFromFile(game_types_file)
        self.Form = Form
        self.fn = fn

        self.Form.setObjectName("Form")
        self.Form.resize(365, 352)
        self.Form.setAutoFillBackground(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.o_1 = QtWidgets.QLabel(self.Form)
        self.o_1.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.o_1.setText("")
        self.o_1.setObjectName("o_1")
        self.gridLayout.addWidget(self.o_1, 1, 4, 1, 1)
        self.b_0 = QtWidgets.QLabel(self.Form)
        self.b_0.setAutoFillBackground(False)
        self.b_0.setStyleSheet("background-color: black; color: white; border: 1px solid gray;")
        self.b_0.setAlignment(QtCore.Qt.AlignCenter)
        self.b_0.setObjectName("b_0")
        self.gridLayout.addWidget(self.b_0, 0, 0, 1, 1)
        self.i_2 = QtWidgets.QLabel(self.Form)
        self.i_2.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.i_2.setText("")
        self.i_2.setObjectName("i_2")
        self.gridLayout.addWidget(self.i_2, 2, 1, 1, 1)
        self.i_3 = QtWidgets.QLabel(self.Form)
        self.i_3.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.i_3.setText("")
        self.i_3.setObjectName("i_3")
        self.gridLayout.addWidget(self.i_3, 3, 1, 1, 1)
        self.n_4 = QtWidgets.QLabel(self.Form)
        self.n_4.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.n_4.setText("")
        self.n_4.setObjectName("n_4")
        self.gridLayout.addWidget(self.n_4, 4, 2, 1, 1)
        self.b_5 = QtWidgets.QLabel(self.Form)
        self.b_5.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.b_5.setText("")
        self.b_5.setObjectName("b_5")
        self.gridLayout.addWidget(self.b_5, 5, 0, 1, 1)
        self.o_3 = QtWidgets.QLabel(self.Form)
        self.o_3.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.o_3.setText("")
        self.o_3.setObjectName("o_3")
        self.gridLayout.addWidget(self.o_3, 3, 4, 1, 1)
        self.b_1 = QtWidgets.QLabel(self.Form)
        self.b_1.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.b_1.setText("")
        self.b_1.setObjectName("b_1")
        self.gridLayout.addWidget(self.b_1, 1, 0, 1, 1)
        self.i_4 = QtWidgets.QLabel(self.Form)
        self.i_4.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.i_4.setText("")
        self.i_4.setObjectName("i_4")
        self.gridLayout.addWidget(self.i_4, 4, 1, 1, 1)
        self.n_0 = QtWidgets.QLabel(self.Form)
        self.n_0.setAutoFillBackground(False)
        self.n_0.setStyleSheet("background-color: black; color: white; border: 1px solid gray;")
        self.n_0.setAlignment(QtCore.Qt.AlignCenter)
        self.n_0.setObjectName("n_0")
        self.gridLayout.addWidget(self.n_0, 0, 2, 1, 1)
        self.b_4 = QtWidgets.QLabel(self.Form)
        self.b_4.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.b_4.setText("")
        self.b_4.setObjectName("b_4")
        self.gridLayout.addWidget(self.b_4, 4, 0, 1, 1)
        self.n_2 = QtWidgets.QLabel(self.Form)
        self.n_2.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.n_2.setText("")
        self.n_2.setObjectName("n_2")
        self.gridLayout.addWidget(self.n_2, 2, 2, 1, 1)
        self.n_3 = QtWidgets.QLabel(self.Form)
        self.n_3.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.n_3.setText("")
        self.n_3.setObjectName("n_3")
        self.gridLayout.addWidget(self.n_3, 3, 2, 1, 1)
        self.o_2 = QtWidgets.QLabel(self.Form)
        self.o_2.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.o_2.setText("")
        self.o_2.setObjectName("o_2")
        self.gridLayout.addWidget(self.o_2, 2, 4, 1, 1)
        self.i_1 = QtWidgets.QLabel(self.Form)
        self.i_1.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.i_1.setText("")
        self.i_1.setObjectName("i_1")
        self.gridLayout.addWidget(self.i_1, 1, 1, 1, 1)
        self.o_4 = QtWidgets.QLabel(self.Form)
        self.o_4.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.o_4.setText("")
        self.o_4.setObjectName("o_4")
        self.gridLayout.addWidget(self.o_4, 4, 4, 1, 1)
        self.g_3 = QtWidgets.QLabel(self.Form)
        self.g_3.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.g_3.setText("")
        self.g_3.setObjectName("g_3")
        self.gridLayout.addWidget(self.g_3, 3, 3, 1, 1)
        self.i_5 = QtWidgets.QLabel(self.Form)
        self.i_5.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.i_5.setText("")
        self.i_5.setObjectName("i_5")
        self.gridLayout.addWidget(self.i_5, 5, 1, 1, 1)
        self.o_5 = QtWidgets.QLabel(self.Form)
        self.o_5.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.o_5.setText("")
        self.o_5.setObjectName("o_5")
        self.gridLayout.addWidget(self.o_5, 5, 4, 1, 1)
        self.b_3 = QtWidgets.QLabel(self.Form)
        self.b_3.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.b_3.setText("")
        self.b_3.setObjectName("b_3")
        self.gridLayout.addWidget(self.b_3, 3, 0, 1, 1)
        self.n_1 = QtWidgets.QLabel(self.Form)
        self.n_1.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.n_1.setText("")
        self.n_1.setObjectName("n_1")
        self.gridLayout.addWidget(self.n_1, 1, 2, 1, 1)
        self.g_4 = QtWidgets.QLabel(self.Form)
        self.g_4.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.g_4.setText("")
        self.g_4.setObjectName("g_4")
        self.gridLayout.addWidget(self.g_4, 4, 3, 1, 1)
        self.g_5 = QtWidgets.QLabel(self.Form)
        self.g_5.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.g_5.setText("")
        self.g_5.setObjectName("g_5")
        self.gridLayout.addWidget(self.g_5, 5, 3, 1, 1)
        self.g_2 = QtWidgets.QLabel(self.Form)
        self.g_2.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.g_2.setText("")
        self.g_2.setObjectName("g_2")
        self.gridLayout.addWidget(self.g_2, 2, 3, 1, 1)
        self.n_5 = QtWidgets.QLabel(self.Form)
        self.n_5.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.n_5.setText("")
        self.n_5.setObjectName("n_5")
        self.gridLayout.addWidget(self.n_5, 5, 2, 1, 1)
        self.g_1 = QtWidgets.QLabel(self.Form)
        self.g_1.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.g_1.setText("")
        self.g_1.setObjectName("g_1")
        self.gridLayout.addWidget(self.g_1, 1, 3, 1, 1)
        self.i_0 = QtWidgets.QLabel(self.Form)
        self.i_0.setAutoFillBackground(False)
        self.i_0.setStyleSheet("background-color: black; color: white; border: 1px solid gray;")
        self.i_0.setAlignment(QtCore.Qt.AlignCenter)
        self.i_0.setObjectName("i_0")
        self.gridLayout.addWidget(self.i_0, 0, 1, 1, 1)
        self.g_0 = QtWidgets.QLabel(self.Form)
        self.g_0.setAutoFillBackground(False)
        self.g_0.setStyleSheet("background-color: black; color: white; border: 1px solid gray;")
        self.g_0.setAlignment(QtCore.Qt.AlignCenter)
        self.g_0.setObjectName("g_0")
        self.gridLayout.addWidget(self.g_0, 0, 3, 1, 1)
        self.o_0 = QtWidgets.QLabel(self.Form)
        self.o_0.setAutoFillBackground(False)
        self.o_0.setStyleSheet("background-color: black; color: white; border: 1px solid gray;")
        self.o_0.setAlignment(QtCore.Qt.AlignCenter)
        self.o_0.setObjectName("o_0")
        self.gridLayout.addWidget(self.o_0, 0, 4, 1, 1)
        self.b_2 = QtWidgets.QLabel(self.Form)
        self.b_2.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.b_2.setText("")
        self.b_2.setObjectName("b_2")
        self.gridLayout.addWidget(self.b_2, 2, 0, 1, 1)
        
        
        if not self.readOnly:
            self.delete_button = QtWidgets.QPushButton(self.Form)
            self.delete_button.clicked.connect(self.delete_pattern)
            self.delete_button.setObjectName("delete_button")
            self.gridLayout.addWidget(self.delete_button, 6, 3, 1, 1)
            self.save_button = QtWidgets.QPushButton(self.Form)
            self.save_button.clicked.connect(self.save_pattern)
            self.save_button.setObjectName("save_button")
            self.gridLayout.addWidget(self.save_button, 6, 4, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        # ADDITIONS
        
        self.selected = 'background-color: red; border: 1px solid gray;'
        self.deselected = 'background-color: white; border: 1px solid gray'

        # Change background if selected

        # B
        if "b_1" in pattern: self.b_1.setStyleSheet(self.selected)
        if "b_2" in pattern: self.b_2.setStyleSheet(self.selected)
        if "b_3" in pattern: self.b_3.setStyleSheet(self.selected)
        if "b_4" in pattern: self.b_4.setStyleSheet(self.selected)
        if "b_5" in pattern: self.b_5.setStyleSheet(self.selected)
        # I
        if "i_1" in pattern: self.i_1.setStyleSheet(self.selected)
        if "i_2" in pattern: self.i_2.setStyleSheet(self.selected)
        if "i_3" in pattern: self.i_3.setStyleSheet(self.selected)
        if "i_4" in pattern: self.i_4.setStyleSheet(self.selected)
        if "i_5" in pattern: self.i_5.setStyleSheet(self.selected)
        # N
        if "n_1" in pattern: self.n_1.setStyleSheet(self.selected)
        if "n_2" in pattern: self.n_2.setStyleSheet(self.selected)
        if "n_3" in pattern: self.n_3.setStyleSheet(self.selected)
        if "n_4" in pattern: self.n_4.setStyleSheet(self.selected)
        if "n_5" in pattern: self.n_5.setStyleSheet(self.selected)
        # G
        if "g_1" in pattern: self.g_1.setStyleSheet(self.selected)
        if "g_2" in pattern: self.g_2.setStyleSheet(self.selected)
        if "g_3" in pattern: self.g_3.setStyleSheet(self.selected)
        if "g_4" in pattern: self.g_4.setStyleSheet(self.selected)
        if "g_5" in pattern: self.g_5.setStyleSheet(self.selected)
        # O
        if "o_1" in pattern: self.o_1.setStyleSheet(self.selected)
        if "o_2" in pattern: self.o_2.setStyleSheet(self.selected)
        if "o_3" in pattern: self.o_3.setStyleSheet(self.selected)
        if "o_4" in pattern: self.o_4.setStyleSheet(self.selected)
        if "o_5" in pattern: self.o_5.setStyleSheet(self.selected)

        if not self.readOnly:
            # Toggle style when selected
            # B
            self.b_1.mouseReleaseEvent=lambda event, location=self.b_1 :self.toggle_select(location)
            self.b_2.mouseReleaseEvent=lambda event, location=self.b_2 :self.toggle_select(location)
            self.b_3.mouseReleaseEvent=lambda event, location=self.b_3 :self.toggle_select(location)
            self.b_4.mouseReleaseEvent=lambda event, location=self.b_4 :self.toggle_select(location)
            self.b_5.mouseReleaseEvent=lambda event, location=self.b_5 :self.toggle_select(location)

            # I
            self.i_1.mouseReleaseEvent=lambda event, location=self.i_1 :self.toggle_select(location)
            self.i_2.mouseReleaseEvent=lambda event, location=self.i_2 :self.toggle_select(location)
            self.i_3.mouseReleaseEvent=lambda event, location=self.i_3 :self.toggle_select(location)
            self.i_4.mouseReleaseEvent=lambda event, location=self.i_4 :self.toggle_select(location)
            self.i_5.mouseReleaseEvent=lambda event, location=self.i_5 :self.toggle_select(location)

            # N
            self.n_1.mouseReleaseEvent=lambda event, location=self.n_1 :self.toggle_select(location)
            self.n_2.mouseReleaseEvent=lambda event, location=self.n_2 :self.toggle_select(location)
            self.n_3.mouseReleaseEvent=lambda event, location=self.n_3 :self.toggle_select(location)
            self.n_4.mouseReleaseEvent=lambda event, location=self.n_4 :self.toggle_select(location)
            self.n_5.mouseReleaseEvent=lambda event, location=self.n_5 :self.toggle_select(location)

            # G
            self.g_1.mouseReleaseEvent=lambda event, location=self.g_1 :self.toggle_select(location)
            self.g_2.mouseReleaseEvent=lambda event, location=self.g_2 :self.toggle_select(location)
            self.g_3.mouseReleaseEvent=lambda event, location=self.g_3 :self.toggle_select(location)
            self.g_4.mouseReleaseEvent=lambda event, location=self.g_4 :self.toggle_select(location)
            self.g_5.mouseReleaseEvent=lambda event, location=self.g_5 :self.toggle_select(location)

            # O
            self.o_1.mouseReleaseEvent=lambda event, location=self.o_1 :self.toggle_select(location)
            self.o_2.mouseReleaseEvent=lambda event, location=self.o_2 :self.toggle_select(location)
            self.o_3.mouseReleaseEvent=lambda event, location=self.o_3 :self.toggle_select(location)
            self.o_4.mouseReleaseEvent=lambda event, location=self.o_4 :self.toggle_select(location)
            self.o_5.mouseReleaseEvent=lambda event, location=self.o_5 :self.toggle_select(location)

        # END ADDITIONS

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
    
    def save_pattern(self):
        # Get the new pattern
        index = self.gridLayout.count()
        checked_boxes = []
        for i in range(index):
            try:
                if 'background-color: red;' in self.gridLayout.itemAt(i).widget().styleSheet():
                    checked_boxes.append(self.gridLayout.itemAt(i).widget().objectName())
            except:
                pass
        # Look for and replace the previous pattern
        for i in range(len(self.game_types)):
            if self.game_types[i]['name'] == self.game_type_name:
                if len(self.pattern) > 0:
                    for ii in range(len(self.game_types[i]['patterns'])):
                        if self.game_types[i]['patterns'][ii] == self.pattern:
                            self.game_types[i]['patterns'][ii] = checked_boxes
                            break
                else:
                    self.game_types[i]['patterns'].append(checked_boxes)
        saveJSONToFile(game_types_file, self.game_types)
        self.fn(self.game_type_name)
        self.Form.close()

    def delete_pattern(self):
        for i in range(len(self.game_types)):
                    if self.game_types[i]['name'] == self.game_type_name:
                        if len(self.pattern) > 0:
                            for ii in range(len(self.game_types[i]['patterns'])):
                                if self.game_types[i]['patterns'][ii] == self.pattern:
                                    del self.game_types[i]['patterns'][ii]
                                    print('deleted ok')
                                    break
        saveJSONToFile(game_types_file, self.game_types)
        self.fn(self.game_type_name)
        self.Form.close()                            

    def toggle_select(self,location):
        current_style = location.styleSheet()
        if 'background-color: white;' in current_style:
            location.setStyleSheet(self.selected)
        else:
            location.setStyleSheet(self.deselected)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b_0.setText(_translate("Form", "B"))
        self.n_0.setText(_translate("Form", "N"))
        self.i_0.setText(_translate("Form", "I"))
        self.g_0.setText(_translate("Form", "G"))
        self.o_0.setText(_translate("Form", "O"))
        if not self.readOnly:
            self.delete_button.setText(_translate("Form", "Delete"))
            self.save_button.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form, game_type_name="None", pattern=[], readOnly=True)
    Form.show()
    sys.exit(app.exec_())
