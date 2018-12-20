from PyQt5 import QtCore
from PyQt5.Qt import Qt,QRectF,QRect,QPoint,QSize,QSizeF
from PyQt5.QtGui import *#QFont,QTextDocument,QTextCursor
from PyQt5.QtWidgets import *#QApplication, QMainWindow, QLabel, QSizePolicy, QAction,QDialog
from PyQt5.QtPrintSupport import *#QPrinter, QPrintDialog,QPrintPreviewDialog
import sys

################################################
#######打印文本---《心经》
################################################
# the_text = '''
# 观自在菩萨，行深般若波罗蜜多时，照见五蕴皆空，度一切苦厄。
# 舍利子，色不异空，空不异色，色即是空，空即是色，受想行识亦复如是。
# 舍利子，是诸法空相，不生不灭，不垢不净，不增不减。
# 是故空中无色，无受想行识，无眼耳鼻舌身意，无色声香味触法，无眼界乃至无意识界，无无明亦无无明尽，乃至无老死，亦无老死尽，无苦集灭道，无智亦无得。
# 以无所得故，菩提萨埵，依般若波罗蜜多故，心无挂碍；无挂碍故，无有恐怖，远离颠倒梦想，究竟涅槃。
# 三世诸佛，依般若波罗蜜多故，得阿耨多罗三藐三菩提。
# 故知般若波罗蜜多，是大神咒，是大明咒，是无上咒，是无等等咒，能除一切苦，真实不虚。
# 故说般若波罗蜜多咒，即说咒曰：揭谛揭谛，波罗揭谛，波罗僧揭谛，菩提萨婆诃。
# '''
the_text = '0000101010000'
################################################
#######创建主窗口
################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(self.tr("打印功能"))

        # 创建文本框
        self.image = QImage()
        self.label = QLabel()
        '''
        if self.image.load('00001010100000001.png'):

            self.image = self.image.scaled(self.image.width()/4,self.image.height()/4,Qt.IgnoreAspectRatio)
            # self.label.setPicture(QPicture.load(self.image))
            self.label.setPixmap(QPixmap.fromImage(self.image))
            # self.label
            # self.image.scaled(self.image.width()/4,self.image.height()/4)
            self.resize(self.image.width()/4,self.image.height()/4)
            # self.label.frameGeometry()
        self.label.setFont(QFont("Roman times",12,QFont.Bold))
        self.label.setText("00001010100000001")
        
        self.setCentralWidget(self.label)
        # self.setCentralWidget(self.image)
        '''


        # 创建菜单栏
        self.createMenus()



    def createMenus(self):
        # 创建动作一
        self.printAction1 = QAction(self.tr("打印无预留"), self)
        self.printAction1.triggered.connect(self.on_printAction1_triggered)

        # 创建动作二
        self.printAction2 = QAction(self.tr("打印有预留"), self)
        self.printAction2.triggered.connect(self.on_printAction2_triggered)

        # 创建动作三
        self.printAction3 = QAction(self.tr("直接打印"), self)
        self.printAction3.triggered.connect(self.on_printAction3_triggered)

        # 创建动作四
        self.printAction4 = QAction(self.tr("打印到PDF"), self)
        self.printAction4.triggered.connect(self.on_printAction4_triggered)


        # 创建菜单，添加动作
        self.printMenu = self.menuBar().addMenu(self.tr("打印"))
        self.printMenu.addAction(self.printAction1)
        self.printMenu.addAction(self.printAction2)
        self.printMenu.addAction(self.printAction3)
        self.printMenu.addAction(self.printAction4)



    # 动作一：打印，无预览
    def on_printAction1_triggered(self):
        self.printer = QPrinter()
        printDialog = QPrintDialog(self.printer, self)
        if printDialog.exec_() == QDialog.Accepted:
            self.handlePaintRequest(self.printer)


    # 动作二：打印，有预览
    def on_printAction2_triggered(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()


    # 动作三：直接打印
    def on_printAction3_triggered(self):
        printer = QPrinter()


        image = QPixmap()
        image.load("0.png")

        font = QFont()
        font.setBold(True)
        font.setPixelSize(50)

        textsize = QSize()
        # textsize.setHeight()
        pen = QPen()
        pen.setColor(Qt.black)



        pagesize = QSizeF()

        print(image.width())
        print(image.height())

        pagesize.setWidth(60)
        pagesize.setHeight(40)




        printer.setPaperSize(pagesize,QPrinter.Millimeter)



        print(printer.pageSize())
        printDialog = QPrintDialog(printer, self)
        printDialog.setWindowTitle("打印二维码")
        if printDialog.exec_() == QDialog.Accepted:
            painter = QPainter(printer)




            painter.setPen(pen)
            painter.setFont(font)


            painter.begin(printer)

            picsize = image.size()
            size = QSize()
            # size.setHeight(picsize.height())
            # size.setWidth(picsize.width())

            # size.setWidth(60)
            # size.setHeight(40)
            #
            #
            #
            # image = image.scaled(size, Qt.KeepAspectRatio)

            rectdest = QRect()
            rectdest.setX(25)
            rectdest.setY(0)
            rectdest.setWidth(175)
            rectdest.setHeight(150)

            print(image.rect())
            # rectsrc = QRect()
            # image.rect()
            # rectsrc.setX(0)
            # rectsrc.setY(0)
            # rectsrc.setX(image.width())
            # rectsrc.setY(image.height())


            painter.drawPixmap(rectdest, image, image.rect())

            # rect.setX(10 + picsize.width()/10)
            # rect.setY(12 + picsize.height()/2.5)
            # painter.drawText(50, 120, "10001491274")

            # preview = QPrintPreviewDialog()
            # preview.paintRequested(printer)
            # preview.exec()

            painter.end()




        #self.handlePaintRequest(printer)


    # 动作四：打印到pdf
    def on_printAction4_triggered(self):
        printer = QPrinter()

        printer.setPageSize(QPrinter.A4)
        view = QPrintPreviewDialog(printer)


        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("xxx.pdf")

        painter = QPainter(printer)
        painter.begin(printer)

        image = QPixmap()
        image.load("00001010100000001.png")
        picsize = image.size()
        size = QSize()
        size.setHeight(picsize.height() / 2.5)
        size.setWidth(picsize.width() / 2.5)

        image = image.scaled(size, Qt.KeepAspectRatio)
        rect = QRect()
        rect.setX(10)
        rect.setY(10)
        painter.drawPixmap(rect, image)

        print(10 + picsize.width()/5)
        print(12 + picsize.height())


        # rect.setX(10 + picsize.width()/10)
        # rect.setY(12 + picsize.height()/2.5)
        painter.drawText(50, 200, "10001491274")

        painter.layoutDirection()
        # self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        # self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        painter.end()
        #self.handlePaintRequest(printer)


    ## 打印函数
    def handlePaintRequest(self, printer):
        sizef = QSize()
        #printer.setPageSize(sizef.scale(40,40,Qt.AspectRatioMode))
        '''
        document = QTextDocument()
        cursor = QTextCursor(document)
        # self.image
        cursor.insertImage(self.image)

        # cursor.insertText(self.label.text())
        document.print(printer)
        '''


'''            # rectf = QRectF()
            # rect = QRect()
            rect = painter.viewport()
            # print(type(rect))
            size = self.image.size()
            size.scale(size,Qt.KeepAspectRatio)
            painter.setViewport(rect.x(),rect.y(),size.width(),size.height())
            painter.setWindow(self.rect())
            # painter.drawImage(rect/4,self.image)'''


################################################
#######程序入门
################################################
if __name__ == "__main__":
    #run()

    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
