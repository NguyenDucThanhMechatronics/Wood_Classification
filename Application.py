from keras.models import load_model
from sklearn.metrics import accuracy_score
from tensorflow.keras.preprocessing import  image
from tensorflow.keras.preprocessing.image import load_img, img_to_array,array_to_img,ImageDataGenerator
import numpy as np
import cv2 as cv
from datetime import datetime

names = ["Anh_Dao", "Bach_Dang_NK", "Bach_xanh", "Bo_de", "Cam_Lai", "Cam_Xe","Cao_Su", "Gioi_Lua", "Hoang_Dan", "Iroko","Lim","Muong_den", "Xa_Cu","Xoan_Ta","Xoay"]

model = load_model(r'D:\AI\ProjectCK\Model_Training.h5')

from PySide2.QtMultimedia import QMediaContent, QMediaPlayer
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,QThread,Signal,Slot,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QImage,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1302, 825)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, -1, 1321, 821))
        self.widget.setMouseTracking(True)
        self.widget.setTabletTracking(True)
        self.widget.setFocusPolicy(Qt.ClickFocus)
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0.452, y1:0.108, x2:0.491525, y2:1, stop:0 rgba(161, 85, 255, 255), stop:0.864407 rgba(255, 249, 232, 255))}\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(910, 0, 501, 61))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 40, 221, 41))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 90, 711+500, 81))
        font1 = QFont()
        font1.setFamily(u"Monotype Corsiva")
        font1.setPointSize(48)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 0, 501, 61))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(80, 70, 191, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(820, 230, 20, 551))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1321, 831))
        self.label.setPixmap(QPixmap(u"backgroudWood.jpg"))
        self.label.setScaledContents(True)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 230, 791, 551))
        self.label_7.setAcceptDrops(True)
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setFrameShadow(QFrame.Plain)
        self.label_7.setLineWidth(3)
        self.label_7.setMidLineWidth(0)
        self.label_7.setPixmap(QPixmap(u"Go/Cam_lai/5762.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(False)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(850, 720, 431, 61))
        font2 = QFont()
        font2.setPointSize(28)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"background-color:qlineargradient(spread:reflect, x1:0.497, y1:0, x2:0.497, y2:0.511, stop:0 rgba(0, 161, 209, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 180, 1231, 31))
        font3 = QFont()
        font3.setFamily(u"Monotype Corsiva")
        font3.setPointSize(28)
        font3.setBold(False)
        font3.setItalic(True)
        font3.setWeight(50)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(850, 620, 141, 61))
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(850, 680, 431, 21))
        font5 = QFont()
        font5.setFamily(u"MV Boli")
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.progressBar.setFont(font5)
        self.progressBar.setStyleSheet(u"font: 20pt \"MV Boli\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(24, 255, 236)")
        self.progressBar.setValue(0)
        self.Stop = QPushButton(self.widget)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setGeometry(QRect(880, 520, 181, 71))
        font6 = QFont()
        font6.setFamily(u"Siemens Slab Black")
        font6.setPointSize(24)
        font6.setItalic(True)
        self.Stop.setFont(font6)
        self.Stop.setCursor(QCursor(Qt.OpenHandCursor))
        self.Stop.setMouseTracking(False)
        self.Stop.setTabletTracking(False)
        self.Stop.setAutoFillBackground(False)
        self.Stop.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 159, 44, 252), stop:1 rgba(255, 255, 255, 255))")
        self.clear_btn = QPushButton(self.widget)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(1080, 520, 181, 71))
        self.clear_btn.setFont(font6)
        self.clear_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.clear_btn.setMouseTracking(False)
        self.clear_btn.setTabletTracking(False)
        self.clear_btn.setAutoFillBackground(False)
        self.clear_btn.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 159, 44, 252), stop:1 rgba(255, 255, 255, 255))")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(880, 240, 381, 261))
        font7 = QFont()
        font7.setFamily(u"Siemens Serif Semibold")
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setItalic(True)
        font7.setWeight(75)
        self.tabWidget.setFont(font7)
        self.tabWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.554, y1:0, x2:0.553672, y2:1, stop:0 rgba(235, 130, 255, 255), stop:1 rgba(255, 255, 255, 255))")
        self.picture_tab = QWidget()
        self.picture_tab.setObjectName(u"picture_tab")
        self.choice_btn = QPushButton(self.picture_tab)
        self.choice_btn.setObjectName(u"choice_btn")
        self.choice_btn.setGeometry(QRect(70, 20, 251, 71))
        self.choice_btn.setFont(font6)
        self.choice_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.choice_btn.setMouseTracking(False)
        self.choice_btn.setTabletTracking(False)
        self.choice_btn.setAutoFillBackground(False)
        self.choice_btn.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 159, 44, 252), stop:1 rgba(255, 255, 255, 255))")
        self.play_btn = QPushButton(self.picture_tab)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setGeometry(QRect(70, 120, 251, 71))
        self.play_btn.setFont(font6)
        self.play_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.play_btn.setMouseTracking(False)
        self.play_btn.setTabletTracking(False)
        self.play_btn.setAutoFillBackground(False)
        self.play_btn.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 159, 44, 252), stop:1 rgba(255, 255, 255, 255))")
        self.tabWidget.addTab(self.picture_tab, "")
        self.video_tab = QWidget()
        self.video_tab.setObjectName(u"video_tab")
        self.OpenCamera = QPushButton(self.video_tab)
        self.OpenCamera.setObjectName(u"OpenCamera")
        self.OpenCamera.setGeometry(QRect(70, 20, 251, 71))
        self.OpenCamera.setFont(font6)
        self.OpenCamera.setCursor(QCursor(Qt.OpenHandCursor))
        self.OpenCamera.setMouseTracking(True)
        self.OpenCamera.setTabletTracking(False)
        self.OpenCamera.setAutoFillBackground(False)
        self.OpenCamera.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 159, 44, 252), stop:1 rgba(255, 255, 255, 255))")
        self.OpenVideo = QPushButton(self.video_tab)
        self.OpenVideo.setObjectName(u"OpenVideo")
        self.OpenVideo.setGeometry(QRect(70, 120, 251, 71))
        self.OpenVideo.setFont(font6)
        self.OpenVideo.setCursor(QCursor(Qt.OpenHandCursor))
        self.OpenVideo.setMouseTracking(False)
        self.OpenVideo.setTabletTracking(False)
        self.OpenVideo.setAutoFillBackground(False)
        self.OpenVideo.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 159, 44, 252), stop:1 rgba(255, 255, 255, 255))")
        self.tabWidget.addTab(self.video_tab, "")
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_3.raise_()
        self.progressBar.raise_()
        self.Stop.raise_()
        self.clear_btn.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        self.thread = {}

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

        #function_for_button
        self.choice_btn.clicked.connect(self.linkto)
        self.play_btn.clicked.connect(self.result)
        self.clear_btn.clicked.connect(self.clear)
        self.OpenCamera.clicked.connect(self.start_capture_video)
        self.OpenVideo.clicked.connect(self.openvideo)
        self.Stop.clicked.connect(self.stop_capture_video)#stop


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Phân loại gỗ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sinh vi\u00ean: Nguy\u1ec5n \u0110\u1ee9c Th\u00e0nh - 191463879", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Khoa C\u01a1 kh\u00ed Ch\u1ebf t\u1ea1o m\u00e1y", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"15 Woods Identification Using Machine-Learning", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ea1i h\u1ecdc S\u01b0 Ph\u1ea1m K\u1ef9 thu\u1eadt TP H\u1ed3 Ch\u00ed Minh", None))
        self.label.setText("")
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u" Result", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Your picture here", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ACCURACY:", None))
        self.Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.choice_btn.setText(QCoreApplication.translate("MainWindow", u"Open Picture", None))
        self.play_btn.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.picture_tab), QCoreApplication.translate("MainWindow", u"Picture", None))
        self.OpenCamera.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.OpenVideo.setText(QCoreApplication.translate("MainWindow", u"Open Video", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.video_tab), QCoreApplication.translate("MainWindow", u"Video", None))
    # retranslateUi

    def result(self):
        #predict
        print((cv.imread(link[0])).shape)
        img = cv.imread(link[0])
        img = img[img.shape[0]//2-250:img.shape[0]//2+250, img.shape[1]//2-250:img.shape[1]//2+250]
        img  = cv.resize(img, (128,128), interpolation=cv.INTER_AREA)
        img = img_to_array(img)
        img = img.reshape(1,128,128,3)
        img = img.astype('float32')
        img = img/255.0
        pre = model.predict(img)

        index = np.argmax(pre, axis=1)
        index = index.item() 
        accuracy = (int)(np.max(pre)*100)

        self.progressBar.setValue(accuracy)
        self.label_8.setText(QCoreApplication.translate("MainWindow", " Result: "+str(names[index]), None))
        
    def linkto(self):
        global index, link
        link = QFileDialog.getOpenFileName(filter='*.jpg *.png')
        self.label_7.setPixmap(QPixmap(link[0]))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Your picture here: "+str(link[0]), None))       

    def clear(self):
        self.label_8.setText(QCoreApplication.translate("MainWindow", " Result: ", None))
        self.label_7.setPixmap(QPixmap())
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Your picture here: ", None))
        self.progressBar.setValue(0)

    def openvideo(self):
        global link
        link = QFileDialog.getOpenFileName(filter='*.mp4')
        self.thread[2] = video(index=2)
        self.thread[2].start() # Call run fnc in capture_video
        self.thread[2].signal.connect(self.show_video)
        self.thread[2].signal.connect(self.show_webcam)
        self.thread[2].SignalAccuracy.connect(self.DisplayAcc)
        self.thread[2].SignalNamePredict.connect(self.DisplayName)

    def show_video(self, img):
        rgb_image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        vid = convert_to_Qt_format.scaled(1920, 1080, Qt.KeepAspectRatio)
        self.label_7.setPixmap(QPixmap.fromImage(vid))

    def stop(self):
        self.label_8.setText(QCoreApplication.translate("MainWindow", " Result: ", None))
        self.label_7.setPixmap(QPixmap())
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Your picture here: ", None))

    def stop_capture_video(self):
        self.thread[1].stop()
        self.thread[2].stop()
        self.label_8.setText(QCoreApplication.translate("MainWindow", " Result: ", None))
        self.label_7.setPixmap(QPixmap())
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Your picture here: ", None))
        self.progressBar.setValue(0)

    def start_capture_video(self):
        self.thread[1] = capture_video(index=1)
        self.thread[1].start() # Call run fnc in capture_video
        self.thread[1].signal.connect(self.show_webcam)
        self.thread[1].SignalAccuracy.connect(self.DisplayAcc)
        self.thread[1].SignalNamePredict.connect(self.DisplayName)

    def DisplayAcc(self, accuracy):
        self.progressBar.setValue(accuracy)
    def DisplayName(self, namePredict):
        self.label_8.setText(QCoreApplication.translate("MainWindow", " Result: "+namePredict, None))

    def show_webcam(self, cv_img):
        rgb_image = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        webcam = convert_to_Qt_format.scaled(1920, 1080, Qt.KeepAspectRatio)
        self.label_7.setPixmap(QPixmap.fromImage(webcam))


class capture_video(QThread):
    signal = Signal(np.ndarray)
    SignalAccuracy = Signal(int)
    SignalNamePredict = Signal(str)
    def __init__(self, index):
        self.index = index
        print("start threading", self.index)
        super(capture_video, self).__init__()

    def run(self):
        cap = cv.VideoCapture(0)  
        while True:
            ret, cv_img = cap.read()

            img1 = cv.flip(cv_img, 90)
            print(img1.shape)
            cv.putText(img1, str(datetime.now()), (10,30), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            img = cv.flip(cv_img, 90)
            img = self.ProcessImage(img)
            pre = model.predict(img)
            index = np.argmax(pre, axis=1)
            index = index.item() 
            namePredict = str(names[index])
 
            accuracy = (int)(np.max(pre)*100)
            if ret:
                self.signal.emit(img1)
                self.SignalAccuracy.emit(accuracy)
                self.SignalNamePredict.emit(namePredict)
            
    def ProcessImage(self, frame):
        #img = frame[40:440, 80:480]
        img = frame[ frame.shape[0]//2-200:frame.shape[0]//2+200 , frame.shape[1]//2-200:frame.shape[1]//2+200 ]
        #cv.imshow('Cam',img)
        cv.waitKey(20)
        img = cv.resize(frame, (128,128), interpolation = cv.INTER_AREA)
        img = img_to_array(img)
        img = img.reshape(1,128,128,3)
        img = img.astype('float32')
        img = img/255.0
        return img

    def stop(self):
        print("stop threading", self.index)
        self.terminate()


class video(QThread):
    signal = Signal(np.ndarray)
    SignalAccuracy = Signal(int)
    SignalNamePredict = Signal(str)
    def __init__(self, index):
        self.index = index
        print("start threading", self.index)
        super(video, self).__init__()

    def run(self):
        vid = cv.VideoCapture(link[0])  
        while True:
            ret, video = vid.read()  

            img = self.ProcessImage(video) 

            pre = model.predict(img)
            index = np.argmax(pre, axis=1)
            index = index.item() 

            namePredict = str(names[index])
            accuracy = (int)(np.max(pre)*100)
            if ret:
                self.signal.emit(video)
                self.SignalAccuracy.emit(accuracy)
                self.SignalNamePredict.emit(namePredict)

    def ProcessImage(self, img):
            
        vid = img[ img.shape[0]//2-250:img.shape[0]//2+250 , img.shape[1]//2-250:img.shape[1]//2+250 ]
        vid = cv.resize(vid, (128,128), interpolation=cv.INTER_AREA)
        vid = img_to_array(vid) 
        vid = vid.reshape(1,128,128,3)
        vid = vid.astype('float32')
        vid = vid/255.0
        return vid

    def stop(self):
        print("stop threading", self.index)
        self.terminate()

if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show() 
    sys.exit(app.exec_())