import sys
import sqlite3

from PIL import Image, ImageEnhance, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog
from basee import Ui_Base
from menuu import Ui_Menu
from historyy import Ui_MainWindow


class Menu(QMainWindow, Ui_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.begin.clicked.connect(self.begining)
        self.settings.clicked.connect(self.changecolor)
        self.pbcontinue.clicked.connect(self.continuee)
        self.w = Base()
        self.h = WHistory()
        self.changepbcolor.clicked.connect(self.colorofpb)
        self.con = sqlite3.connect('history.db')
        self.cur = self.con.cursor()
        self.setcolors()
        self.pbreset.clicked.connect(self.reset)
        self.pbhistory.clicked.connect(self.openwhistory)
        self.hnames = [self.h.name1, self.h.name2, self.h.name3, self.h.name4, self.h.name5]

    def reset(self):
        self.cur.execute(f"""UPDATE colors
                    SET bg = '#e6e5ff'""")
        self.cur.execute(f"""UPDATE colors
                   SET pb = '#e6e5ff'""")
        self.setcolors()
        self.con.commit()

    def setcolors(self):
        self.setStyleSheet("QPushButton { background-color: " +
                           str(self.cur.execute("""SELECT pb FROM colors""").fetchone())[2: -3] +
                           "} QMainWindow { background-color: " +
                           str(self.cur.execute("""SELECT bg FROM colors""").fetchone())[2: -3] + "}")
        self.w.setStyleSheet("QPushButton { background-color: " +
                             str(self.cur.execute("""SELECT pb FROM colors""").fetchone())[2: -3] +
                             "} QMainWindow { background-color: " +
                             str(self.cur.execute("""SELECT bg FROM colors""").fetchone())[2: -3] + "}")
        self.h.setStyleSheet("QPushButton { background-color: " +
                             str(self.cur.execute("""SELECT pb FROM colors""").fetchone())[2: -3] +
                             "} QMainWindow { background-color: " +
                             str(self.cur.execute("""SELECT bg FROM colors""").fetchone())[2: -3] + "}")

    def colorofpb(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.cur.execute(f"""UPDATE colors
            SET pb = '{color.name()}'""")
            self.setcolors()
            self.con.commit()

    def changecolor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.cur.execute(f"""UPDATE colors
            SET bg = '{color.name()}'""")
            self.setcolors()
            self.con.commit()

    def continuee(self):
        try:
            self.begining()
            self.w.fname = 'new.png'
            self.w.open()
        except:
            pass

    def begining(self):
        self.w.show()
        self.hide()

    def openwhistory(self):
        self.h.show()
        for i in range(1, 6):
            self.hnames[i - 1].setText(str(self.cur.execute(f"""SELECT file FROM files WHERE id = {i}""").fetchone())[2: -3])


class WHistory(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open1.clicked.connect(self.opening1)
        self.open2.clicked.connect(self.opening2)
        self.open3.clicked.connect(self.opening3)
        self.open4.clicked.connect(self.opening4)
        self.open5.clicked.connect(self.opening5)

    def closing(self, fname):
        wm.w.fname = fname
        wm.w.open()
        wm.w.show()
        wm.h.hide()
        wm.hide()

    def opening1(self):
        self.closing(self.name1.text())

    def opening2(self):
        self.closing(self.name2.text())

    def opening3(self):
        self.closing(self.name3.text())

    def opening4(self):
        self.closing(self.name4.text())

    def opening5(self):
        self.closing(self.name5.text())


class Base(QMainWindow, Ui_Base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname = ''
        #открытие и сохранение
        self.pbopen.clicked.connect(self.open1)
        self.pbsave.clicked.connect(self.save)
        #cохранение несохранение изменений
        self.yes.clicked.connect(self.savechanges)
        self.no.clicked.connect(self.noo)
        self.yes.hide()
        self.no.hide()
        #контрастность
        self.pbcontrast.clicked.connect(self.contrast)
        self.rofcontrast.hide()
        self.rofcontrast.valueChanged.connect(self.changecontrast)
        #яркость
        self.rofbright.hide()
        self.pbbright.clicked.connect(self.bright)
        self.rofbright.valueChanged.connect(self.changebright)
        #насыщенность
        self.rofsat.hide()
        self.pbsaturation.clicked.connect(self.saturation)
        self.rofsat.valueChanged.connect(self.changesaturation)
        #резкость
        self.rofsharpness.hide()
        self.pbsharpness.clicked.connect(self.sharpness)
        self.rofsharpness.valueChanged.connect(self.changesharpness)
        #цвета
        self.rofblue.hide()
        self.rofred.hide()
        self.rofgreen.hide()
        self.textred.hide()
        self.textblue.hide()
        self.textgreen.hide()
        self.pbred.clicked.connect(self.red)
        self.pbblue.clicked.connect(self.blue)
        self.pbgreen.clicked.connect(self.green)
        self.rofred.valueChanged.connect(self.changered)
        self.rofgreen.valueChanged.connect(self.changegreen)
        self.rofblue.valueChanged.connect(self.changeblue)
        #обрезать
        self.pbsize.clicked.connect(self.sizee)
        self.left.hide()
        self.right.hide()
        self.top.hide()
        self.bottom.hide()
        self.ok.hide()
        self.ok.clicked.connect(self.changesize)
        #отразить
        self.horizontal.hide()
        self.vertical.hide()
        self.pbreflect.clicked.connect(self.reflect)
        self.horizontal.clicked.connect(self.reflecthorizontal)
        self.vertical.clicked.connect(self.reflectvertical)
        #повернуть
        self.turnr.hide()
        self.turnl.hide()
        self.pbturn.clicked.connect(self.turn)
        self.turnr.clicked.connect(self.turnright)
        self.turnl.clicked.connect(self.turnleft)
        #фильтр
        self.pbfilters.clicked.connect(self.filters)
        self.filterbw.hide()
        self.filterbw.clicked.connect(self.bw)
        self.stf.hide()
        self.stf.clicked.connect(self.strangefilter)
        self.fcontour.hide()
        self.fcontour.clicked.connect(self.contour)
        self.femboss.hide()
        self.femboss.clicked.connect(self.emboss)
        self.frank.hide()
        self.frank.clicked.connect(self.rank)
        self.funsharp.hide()
        self.funsharp.clicked.connect(self.unsharp)
        self.fmode.hide()
        self.fmode.clicked.connect(self.mode)
        self.linef.hide()
        self.linef.clicked.connect(self.lines)

        self.back.clicked.connect(self.backk)

        self.con = sqlite3.connect('history.db')
        self.cur = self.con.cursor()

    def open1(self):
        self.fname = QFileDialog.getOpenFileName(self, '', 'выберите')[0]
        self.open()


    def open(self):
        #открытие изображения
        try:
            im = Image.open(self.fname)
            x, y = im.size
            if x > y:
                im = im.resize((631, round(y / (x / 631))))
            elif y > x:
                im = im.resize((round(x / (y / 631)), 631))
            else:
                im = im.resize((631, 631))
            im.save('new.png')
            self.img = QPixmap('new.png')
            self.photo.setPixmap(self.img)
            Image.open('new.png').save('new2.png')
        except:
            pass

    def save(self):
        #сохранение итога
        try:
            if self.fname:
                self.f2name = QFileDialog.getSaveFileName(self, 'Выбрать картинку', '', '(*.jpg);;(*.png);;(*)')[0]
                Image.open('new.png').save(self.f2name)
                self.savenewfile(self.f2name)
        except:
            pass

    def hideallpb(self):
        #убирание всего
        self.pbred.hide()
        self.pbgreen.hide()
        self.pbblue.hide()
        self.pbfilters.hide()
        self.pbcontrast.hide()
        self.pbbright.hide()
        self.pbsaturation.hide()
        self.pbsize.hide()
        self.pbsharpness.hide()
        self.pbturn.hide()
        self.pbreflect.hide()
        self.pbfilters.hide()

    def showallpb(self):
        #появление всего
        self.pbred.show()
        self.pbgreen.show()
        self.pbblue.show()
        self.pbfilters.show()
        self.pbcontrast.show()
        self.pbbright.show()
        self.pbsaturation.show()
        self.pbsize.show()
        self.pbsharpness.show()
        self.pbturn.show()
        self.pbreflect.show()
        self.pbfilters.show()

    def yesorno(self):
        #появление выбора: отмена или сохранение изменений
        self.yes.show()
        self.no.show()

    def savechanges(self):
        #при сохранении изменений
        if self.fname:
            Image.open('new2.png').save('new.png')
        self.noo()

    def noo(self):
        #при отмене изменений
        self.yes.hide()
        self.no.hide()
        if self.fname:
            self.img = QPixmap('new.png')
            self.photo.setPixmap(self.img)
        if self.n == 1:
            self.notcontrast()
        if self.n == 2:
            self.notbright()
        if self.n == 3:
            self.notsaturation()
        if self.n == 4:
            self.notcolor()
        if self.n == 5:
            self.notsize()
        if self.n == 6:
            self.notsharpness()
        if self.n == 7:
            self.notreflect()
        if self.n == 8:
            self.notturn()
        if self.n == 9:
            self.notfilters()
        self.showallpb()

    def backk(self):
        self.hide()
        self.photo.setPixmap(QPixmap(""))
        wm.show()

    def savenewfile(self, f):
        for i in range(1, 5):
            nm = str(self.cur.execute(f"""SELECT file FROM files WHERE id = {i + 1}""").fetchone())[2: -3]
            self.cur.execute(f"""UPDATE files
                                SET file = '{nm}'
                                WHERE id = {i}""")
            self.con.commit()
        self.cur.execute(f"""DELETE FROM files WHERE id = 5""")
        self.cur.execute(f"""INSERT INTO files VALUES (5, '{f}')""")

        self.con.commit()

    #КОНТРАСТ
    def contrast(self):
        #появление
        self.n = 1
        self.nameofr.setText('Контрастность')
        self.rofcontrast.show()
        self.rofcontrast.setValue(100)
        self.yesorno()
        self.hideallpb()

    def notcontrast(self):
        #убирание
        self.nameofr.setText('')
        self.rofcontrast.hide()

    def changecontrast(self):
        #изменение
        if self.fname:
            im = Image.open('new.png')
            ImageEnhance.Contrast(im).enhance(int(self.rofcontrast.value()) / 100).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    #ЯРКОСТЬ
    def bright(self):
        # появление
        self.n = 2
        self.nameofr.setText('Яркость')
        self.rofbright.show()
        self.rofbright.setValue(100)
        self.yesorno()
        self.hideallpb()

    def notbright(self):
        #убирание
        self.nameofr.setText('')
        self.rofbright.hide()

    def changebright(self):
        #изменение
        if self.fname:
            im = Image.open('new.png')
            ImageEnhance.Brightness(im).enhance(int(self.rofbright.value()) / 100).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    #НАСЫЩЕННОСТЬ
    def saturation(self):
        # появление
        self.n = 3
        self.nameofr.setText('Насыщенность')
        self.rofsat.show()
        self.rofsat.setValue(100)
        self.yesorno()
        self.hideallpb()

    def notsaturation(self):
        # убирание
        self.nameofr.setText('')
        self.rofsat.hide()

    def changesaturation(self):
        #изменение
        if self.fname:
            im = Image.open('new.png')
            ImageEnhance.Color(im).enhance(int(self.rofsat.value()) / 100).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    #ЦВЕТА
    def blue(self):
        # появление
        self.n = 4
        self.rofblue.show()
        self.textblue.show()
        self.rofblue.setValue(0)
        self.yesorno()
        self.hideallpb()

    def red(self):
        self.rofred.show()
        self.n = 4
        self.textred.show()
        self.rofred.setValue(0)
        self.yesorno()
        self.hideallpb()

    def green(self):
        self.rofgreen.show()
        self.n = 4
        self.textgreen.show()
        self.rofgreen.setValue(0)
        self.yesorno()
        self.hideallpb()

    def notcolor(self):
        # убирани
        self.rofblue.hide()
        self.rofred.hide()
        self.rofgreen.hide()
        self.textred.hide()
        self.textblue.hide()
        self.textgreen.hide()

    def changered(self):
        #изменение красного
        try:
            if self.fname:
                im = Image.open('new.png')
                p = im.load()
                x, y = im.size
                for i in range(x):
                    for j in range(y):
                        r, g, b = p[i, j]
                        if r + int(self.rofred.value()) < 0:
                            r = 0
                        if r + int(self.rofred.value()) > 255:
                            r = 255
                        else:
                            r += int(self.rofred.value())
                        p[i, j] = r, g, b
                im.save('new2.png')
                self.img = QPixmap('new2.png')
                self.photo.setPixmap(self.img)
        except:
            pass

    def changeblue(self):
        #изменение синего
        try:
            if self.fname:
                im = Image.open('new.png')
                p = im.load()
                x, y = im.size
                for i in range(x):
                    for j in range(y):
                        r, g, b = p[i, j]
                        if b + self.rofblue.value() < 0:
                            b = 0
                        if b + self.rofblue.value() > 255:
                            b = 255
                        else:
                            b += self.rofblue.value()
                        p[i, j] = r, g, b
                im.save('new2.png')
                self.img = QPixmap('new2.png')
                self.photo.setPixmap(self.img)
        except:
            pass

    def changegreen(self):
        #изменение зеленого
        if self.fname:
            try:
                im = Image.open('new.png')
                p = im.load()
                x, y = im.size
                for i in range(x):
                    for j in range(y):
                        r, g, b = p[i, j]
                        if g + self.rofgreen.value() < 0:
                            g = 0
                        if g + self.rofgreen.value() > 255:
                            g = 255
                        else:
                            g += self.rofgreen.value()
                        p[i, j] = r, g, b
                im.save('new2.png')
                self.img = QPixmap('new2.png')
                self.photo.setPixmap(self.img)
            except:
                pass

    #обрезать
    def sizee(self):
        # появление
        self.n = 5
        self.left.show()
        self.right.show()
        self.top.show()
        self.bottom.show()
        self.ok.show()
        im = Image.open('new.png')
        x, y = im.size
        self.yesorno()
        self.hideallpb()

        self.left.setText('0')
        self.right.setText(str(x))
        self.top.setText('0')
        self.bottom.setText(str(y))

    def notsize(self):
        # убирание
        self.left.hide()
        self.right.hide()
        self.top.hide()
        self.bottom.hide()
        self.ok.hide()

    def changesize(self):
        #изменение
        if self.fname:
            im = Image.open('new.png')
            try:
                im.crop((int(self.left.text()), int(self.top.text()),
                         int(self.right.text()), int(self.bottom.text()))).save('new2.png')
            except:
                pass
            im = Image.open('new2.png')
            x, y = im.size
            if x > y:
                im = im.resize((631, round(y / (x / 631))))
            elif y > x:
                im = im.resize((round(x / (y / 631)), 631))
            else:
                im = im.resize((631, 631))
            im.save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    #РЕЗКОСТЬ
    def sharpness(self):
        # появление
        self.n = 6
        self.nameofr.setText('Резкость')
        self.rofsharpness.show()
        self.rofsharpness.setValue(100)
        self.yesorno()
        self.hideallpb()

    def notsharpness(self):
        # убирание
        self.nameofr.setText('')
        self.rofsharpness.hide()

    def changesharpness(self):
        # изменение
        if self.fname:
            im = Image.open('new.png')
            ImageEnhance.Sharpness(im).enhance(int(self.rofsharpness.value()) / 100).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    #ОТРАЗИТЬ
    def reflect(self):
        # появление
        self.n = 7
        self.horizontal.show()
        self.vertical.show()
        self.yesorno()
        self.hideallpb()

    def notreflect(self):
        # убирание
        self.horizontal.hide()
        self.vertical.hide()

    def reflecthorizontal(self):
        # изменение
        if self.fname:
            im = Image.open('new2.png')
            im.transpose(Image.FLIP_LEFT_RIGHT).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    def reflectvertical(self):
        # изменение
        if self.fname:
            im = Image.open('new2.png')
            im.transpose(Image.FLIP_TOP_BOTTOM).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    #ПОВЕРНУТЬ
    def turn(self):
        # появление
        self.n = 8
        self.turnr.show()
        self.turnl.show()
        self.yesorno()
        self.hideallpb()

    def notturn(self):
    # убирание
        self.turnr.hide()
        self.turnl.hide()

    def turnright(self):
        # изменение
        if self.fname:
            im = Image.open('new2.png')
            im.transpose(Image.ROTATE_270).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    def turnleft(self):
        # изменение
        if self.fname:
            im = Image.open('new2.png')
            im.transpose(Image.ROTATE_90).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)


    #фильтры
    def filters(self):
        # появление
        self.n = 9
        self.nameofr.setText('Фильтры')
        self.filterbw.show()
        self.stf.show()
        self.fcontour.show()
        self.femboss.show()
        self.frank.show()
        self.funsharp.show()
        self.fmode.show()
        self.linef.show()
        self.yesorno()
        self.hideallpb()

    def notfilters(self):
        # убирание
        self.nameofr.setText('')
        self.filterbw.hide()
        self.stf.hide()
        self.fcontour.hide()
        self.femboss.hide()
        self.fmode.hide()
        self.frank.hide()
        self.linef.hide()
        self.funsharp.hide()

    def bw(self):
        # изменение
        if self.fname:
            im = Image.open('new.png')
            im.convert("L").save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    def strangefilter(self):
        # изменение
        if self.fname:
            im = Image.open('new.png')
            im.filter(ImageFilter.EDGE_ENHANCE).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    def contour(self):
        # изменение
        if self.fname:
            im = Image.open('new.png')
            im.filter(ImageFilter.CONTOUR).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    def emboss(self):
        # изменение
        if self.fname:
            im = Image.open('new.png')
            im.filter(ImageFilter.EMBOSS).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    def rank(self):
        # изменение
        if self.fname:
            im = Image.open('new.png')
            im.filter(ImageFilter.RankFilter(size=3, rank=2)).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    def unsharp(self):
        # изменение
        if self.fname:
            im = Image.open('new.png')
            im.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3)).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    def mode(self):
        # изменение
        if self.fname:
            im = Image.open('new.png')
            im.filter(ImageFilter.ModeFilter(size=9)).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)

    def lines(self):
        # изменение
        if self.fname:
            im = Image.open('new.png')
            im.filter(ImageFilter.EDGE_ENHANCE_MORE).save('new2.png')
            self.img = QPixmap('new2.png')
            self.photo.setPixmap(self.img)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wm = Menu()
    wm.show()
    sys.exit(app.exec_())