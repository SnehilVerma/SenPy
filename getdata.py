import sys,time
from testrun import test
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("file1.ui")[0]


class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.input.clicked.connect(self.input_clicked)  # Bind the event handlers
        # self.train.clicked.connect(self.train_clicked)
        self.longtask=TaskThread();
        self.longtask.notifyProgress.connect(self.onProgress)

    def input_clicked(self):
        sen = self.sentence.toPlainText()
        netscore=0.0
        sen=str(sen)
        #self.tableView.insertRow(0)
        cat_score=[]
        cat_score=test(sen,netscore)
        self.textEdit.setText(str(cat_score))
        self.progressBar.setValue(0)
        self.longtask.start()

        # self.entereddata.setText(sen)

    # def train_clicked(self):

    def onProgress(self,i):
        self.progressBar.setValue(i)

class TaskThread(QtCore.QThread):
    notifyProgress=QtCore.pyqtSignal(int);
    def run(self):
        for i in range(101):
            self.notifyProgress.emit(i);
            time.sleep(0.01)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
