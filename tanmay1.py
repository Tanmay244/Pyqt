# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import serial
ser = serial.Serial("COM7",baudrate=9600)

SPECIAL_MARKER = 253
START_MARKER = 254
END_MARKER = 255  

class Ui_PID_Tuner(object):
    def setupUi(self, PID_Tuner):
        PID_Tuner.setObjectName("PID_Tuner")
        PID_Tuner.resize(1024, 605)
        self.start = QtWidgets.QPushButton(PID_Tuner)
        self.start.setGeometry(QtCore.QRect(510, 510, 93, 28))
        self.start.setObjectName("start")
        self.kp = QtWidgets.QLabel(PID_Tuner)
        self.kp.setGeometry(QtCore.QRect(90, 120, 121, 31))
        self.kp.setObjectName("kp")
        self.ki = QtWidgets.QLabel(PID_Tuner)
        self.ki.setGeometry(QtCore.QRect(90, 250, 121, 41))
        self.ki.setObjectName("ki")
        self.kd = QtWidgets.QLabel(PID_Tuner)
        self.kd.setGeometry(QtCore.QRect(90, 390, 55, 41))
        self.kd.setObjectName("kd")
        self.kp_slider = QtWidgets.QSlider(PID_Tuner)
        self.kp_slider.setGeometry(QtCore.QRect(350, 110, 241, 41))
        self.kp_slider.setOrientation(QtCore.Qt.Horizontal)
        self.kp_slider.setObjectName("kp_slider")
        self.ki_slider = QtWidgets.QSlider(PID_Tuner)
        self.ki_slider.setGeometry(QtCore.QRect(350, 250, 241, 41))
        self.ki_slider.setOrientation(QtCore.Qt.Horizontal)
        self.ki_slider.setObjectName("ki_slider")
        self.kd_slider = QtWidgets.QSlider(PID_Tuner)
        self.kd_slider.setGeometry(QtCore.QRect(350, 380, 241, 41))
        self.kd_slider.setOrientation(QtCore.Qt.Horizontal)
        self.kd_slider.setObjectName("kd_slider")
        self.kp_box = QtWidgets.QDoubleSpinBox(PID_Tuner)
        self.kp_box.setGeometry(QtCore.QRect(730, 110, 141, 51))
        self.kp_box.setObjectName("kp_box")
        self.kp_box.setMinimum(10)
        self.kp_box.setMaximum(999)
        self.kp_box.setSingleStep(0.5)
        self.ki_box = QtWidgets.QDoubleSpinBox(PID_Tuner)
        self.ki_box.setGeometry(QtCore.QRect(730, 240, 141, 51))
        self.ki_box.setObjectName("ki_box")
        self.ki_box.setMinimum(10)
        self.ki_box.setMaximum(999)
        self.ki_box.setSingleStep(0.5)
        self.kd_box = QtWidgets.QDoubleSpinBox(PID_Tuner)
        self.kd_box.setGeometry(QtCore.QRect(730, 370, 141, 51))
        self.kd_box.setObjectName("kd_box")
        self.kd_box.setMinimum(10)
        self.kd_box.setMaximum(999)
        self.kd_box.setSingleStep(0.5)
        self.connect = QtWidgets.QPushButton(PID_Tuner)
        self.connect.setGeometry(QtCore.QRect(600, 20, 93, 28))
        self.connect.setObjectName("connect")
        self.label = QtWidgets.QLabel(PID_Tuner)
        self.label.setGeometry(QtCore.QRect(90, 60, 111, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PID_Tuner)
        self.label_2.setGeometry(QtCore.QRect(740, 60, 55, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(PID_Tuner)
        self.comboBox.setGeometry(QtCore.QRect(240, 20, 291, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.kp_min = QtWidgets.QPushButton(PID_Tuner)
        self.kp_min.setGeometry(QtCore.QRect(320, 170, 93, 28))
        self.kp_min.setObjectName("kp_min")
        self.kp_max = QtWidgets.QPushButton(PID_Tuner)
        self.kp_max.setGeometry(QtCore.QRect(560, 170, 93, 28))
        self.kp_max.setObjectName("kp_max")
        self.ki_min = QtWidgets.QPushButton(PID_Tuner)
        self.ki_min.setGeometry(QtCore.QRect(320, 310, 93, 28))
        self.ki_min.setObjectName("ki_min")
        self.ki_max = QtWidgets.QPushButton(PID_Tuner)
        self.ki_max.setGeometry(QtCore.QRect(560, 310, 93, 28))
        self.ki_max.setObjectName("ki_max")
        self.kd_min = QtWidgets.QPushButton(PID_Tuner)
        self.kd_min.setGeometry(QtCore.QRect(320, 440, 93, 28))
        self.kd_min.setObjectName("kd_min")
        self.kd_max = QtWidgets.QPushButton(PID_Tuner)
        self.kd_max.setGeometry(QtCore.QRect(560, 440, 93, 28))
        self.kd_max.setObjectName("kd_max")
        self.label_3 = QtWidgets.QLabel(PID_Tuner)
        self.label_3.setGeometry(QtCore.QRect(910, 130, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(PID_Tuner)
        self.label_4.setGeometry(QtCore.QRect(910, 260, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(PID_Tuner)
        self.label_5.setGeometry(QtCore.QRect(910, 390, 55, 16))
        self.label_5.setObjectName("label_5")
        self.send = QtWidgets.QPushButton(PID_Tuner)
        self.send.setGeometry(QtCore.QRect(350, 510, 93, 28))
        self.send.setObjectName("send")

        self.retranslateUi(PID_Tuner)
        #self.kp_slider.sliderMoved['int'].connect(self.kp_box.setValue)
        #self.ki_slider.sliderMoved['int'].connect(self.ki_box.setValue)
        #self.kd_slider.sliderMoved['int'].connect(self.kd_box.setValue)
        #self.kp_box.valueChanged['int'].connect(self.kp_slider.setValue)
        #self.ki_box.valueChanged['int'].connect(self.ki_slider.setValue)
        #self.kd_box.valueChanged['int'].connect(self.kd_slider.setValue)
        QtCore.QMetaObject.connectSlotsByName(PID_Tuner)

        
        self.kp_max.clicked.connect(self.kpmax)
        self.ki_max.clicked.connect(self.kimax)
        self.kd_max.clicked.connect(self.kdmax)
        self.kp_min.clicked.connect(self.kpmin)
        self.ki_min.clicked.connect(self.kimin)
        self.kd_min.clicked.connect(self.kdmin)
        self.connect.clicked.connect(self.call_arduino)
        self.send.clicked.connect(self.send_val)
        self.start.clicked.connect(self.start_arduino)

    def retranslateUi(self, PID_Tuner):
        _translate = QtCore.QCoreApplication.translate
        PID_Tuner.setWindowTitle(_translate("PID_Tuner", "Dialog"))
        self.start.setText(_translate("PID_Tuner", "Start"))
        self.kp.setText(_translate("PID_Tuner", "Kp"))
        self.ki.setText(_translate("PID_Tuner", "Ki"))
        self.kd.setText(_translate("PID_Tuner", "Kd"))
        self.connect.setText(_translate("PID_Tuner", "Connect"))
        self.label.setText(_translate("PID_Tuner", "Name"))
        self.label_2.setText(_translate("PID_Tuner", "Value"))
        self.comboBox.setItemText(0, _translate("PID_Tuner", "Serial Monitor"))
        self.kp_min.setText(_translate("PID_Tuner", "Min"))
        self.kp_max.setText(_translate("PID_Tuner", "Max"))
        self.ki_min.setText(_translate("PID_Tuner", "Min"))
        self.ki_max.setText(_translate("PID_Tuner", "Max"))
        self.kd_min.setText(_translate("PID_Tuner", "Min"))
        self.kd_max.setText(_translate("PID_Tuner", "Max"))
        self.label_3.setText(_translate("PID_Tuner", "TextLabel"))
        self.label_4.setText(_translate("PID_Tuner", "TextLabel"))
        self.label_5.setText(_translate("PID_Tuner", "TextLabel"))
        self.send.setText(_translate("PID_Tuner", "Send"))

  

    def send_val(self):
        kp_val=self.kp_box.text()
        ki_val=self.ki_box.text()
        kd_val=self.kd_box.text()
        print("kp=",kp_val, "kd=",kd_val, "ki=", ki_val)

        new_kp = self.ENCODE_TO_STRING(kp_val)
        #print("kp=",kp_val, "kd=",kd_val, "ki=", ki_val)
        print('Encoded')
        print(new_kp)
        #ser.write(str(kd_val).encode())
        #ser.write(str(ki_val).encode())
        #ser.write(str(kd_val).encode())
        #print("kd=",kd_val)
        #x = ser.readline()
        #y = ser.readline()
        #z = ser.readline()

        #print(x.decode())
        #print(y.decode())
        #print(z.decode())

    def call_arduino(self):
        print("Connect Arduino")

    def start_arduino(self):
        print("Start")

    def kpmax(self):
        self.kp_box.setValue(999)    
    def kimax(self):
        self.ki_box.setValue(999)
    def kdmax(self):
        self.kd_box.setValue(999)
    def kpmin(self):
        self.kp_box.setValue(10)
    def kimin(self):
        self.ki_box.setValue(10)
    def kdmin(self):
        self.kd_box.setValue(10)

    def ENCODE_TO_STRING(self,data):
        print('Encoding Now')
        global START_MARKER, SPECIAL_MARKER, END_MARKER
        o_data = ""
        o_data += chr(START_MARKER)
        for val in data:
            if val >= SPECIAL_MARKER:
                o_data += chr(SPECIAL_MARKER)
                o_data += chr(val - SPECIAL_MARKER)
            else:
                o_data += chr(val)
                
        o_data += chr(END_MARKER)
        
        return o_data
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PID_Tuner = QtWidgets.QDialog()
    ui = Ui_PID_Tuner()
    ui.setupUi(PID_Tuner)
    PID_Tuner.show()
    sys.exit(app.exec_())

