import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cards = []
        masti = ['буби','червы','крести','пики']
        val = [6,7,8,9,10,'J', "D", "K", 'T']
        cards = []
        for j in range(4):
            for i in range(9):
                self.cards.append([masti[j],val[i]])
        self.p1_win = 0
        self.p2_win = 0
        self.turn = 0
        self.p1 = 0
        self.lcard = None
        self.suma = 0
        self.setGeometry(500,300,700,500)
        self.setWindowTitle('Black Jack')
         
        self.btnt = QPushButton('взять ещё', self)
        self.btnt.resize(90, 40)
        self.btnt.move(0, 0)
        self.btnt.clicked.connect(self.takk)
        
        self.btnz = QPushButton('закончить', self)
        self.btnz.resize(90, 40)
        self.btnz.move(100, 0)
        self.btnz.clicked.connect(self.end)

        
        self.lbll = QLabel(self)
        self.lbll.setText("Последняя взятая карта: {}          ".format(self.lcard))
        self.lbll.move(0,130)
        
        self.lbls = QLabel(self)
        self.lbls.setText("сумма: {}          ".format(self.suma))
        self.lbls.move(0,90)
        
        self.rules = QLabel(self)
        self.rules.setText("выигрывает тот, кто набирает больше очков, но если набрать больше 21 очка ты проиграешь")
        self.rules.move(0,215)
        
        self.rules2 = QLabel(self)
        self.rules2.setText("6: 6 б, 7: 7 б, 8: 8 б, 9: 9 б, 10: 10 б, J: 4 б, D: 5 б,K: 6 б, T: 1 б")
        self.rules2.move(0,230)
        
        self.btnn = QPushButton('Следующий игрок', self)
        self.btnn.resize(120, 70)
        self.btnn.move(210, 0)
        self.btnn.clicked.connect(self.next_turn)
        self.btnn.setEnabled(False)

        self.res = QPushButton('Начать сначала', self)
        self.res.resize(0, 0)
        self.res.move(100, 0)
        self.res.clicked.connect(self.again)
        
        self.btnk = QPushButton('взять ещё', self)
        self.btnk.resize(0, 0)
        self.btnk.move(0, 0)
        self.btnk.clicked.connect(self.takk2)
        

        
        self.btc = QPushButton('Подсчёт очков', self)
        self.btc.resize(0, 0)
        self.btc.move(210, 0)
        self.btc.clicked.connect(self.count)

        self.last_win_lbl = QLabel(self)
        self.last_win_lbl.setText("                                                        ")
        self.last_win_lbl.move(300,140)
        
        self.win1_lbl = QLabel(self)
        self.win1_lbl.setText("кол-во побед первого игрока:{}                                      ".format(self.p1_win))
        self.win1_lbl.move(300,165)
        
        self.win2_lbl = QLabel(self)
        self.win2_lbl.setText("кол-во побед второго игрока:{}                                      ".format(self.p2_win))
        self.win2_lbl.move(300,180)
        
    def end(self):
        if self.turn == 0:
            self.btnn.setEnabled(True)
        self.turn = 1
        
    def takk(self):
        if self.turn == 0:
            a = random.randint(0,len(self.cards) - 1)
            car = self.cards[a]
            self.cards.pop(a)
            self.lbll.setText("Последняя взятая карта: {} {}          ".format(car[1],car[0]))
            if car[1] != 'J' and car[1] != 'D' and car[1] != 'K' and car[1] != 'T':
                self.suma += car[1]
            elif car[1] == 'J':
                self.suma += 4
                
            elif car[1] == 'D':
                self.suma += 5
                
            elif car[1] == 'K':
                self.suma += 6
                
            elif car[1] == 'T':
                self.suma += 1
            self.p1score = self.suma
            self.lbls.setText("сумма: {}          ".format(self.suma))

            
    def next_turn(self):
        self.suma = 0
        self.btnn.resize(0, 0)
        self.lbll.setText("Последняя взятая карта: {}          ".format(None))
        self.lbls.setText("сумма: {}          ".format(self.suma))
        self.btnt.resize(0,0)
        self.btnk.resize(90, 40)
        self.btnz.resize(0, 0)


    def takk2(self):
        
        b = random.randint(0,len(self.cards) - 1)
        cbr = self.cards[b]
        self.cards.pop(b)
        self.lbll.setText("Последняя взятая карта: {} {}          ".format(cbr[1],cbr[0]))
        if cbr[1] != 'J' and cbr[1] != 'D' and cbr[1] != 'K' and cbr[1] != 'T':
            self.suma += cbr[1]
        elif cbr[1] == 'J':
            self.suma += 4
                
        elif cbr[1] == 'D':
            self.suma += 5
                
        elif cbr[1] == 'K':
            self.suma += 6
                
        elif cbr[1] == 'T':
            self.suma += 1
            
        self.lbls.setText("сумма: {}          ".format(self.suma))
        self.p2score = self.suma
        self.btc.resize(100,100)

    
    def count(self):
        if self.p1score > 21 and self.p2score < 21:
            self.p2_win +=1
            self.btnz.setEnabled(False)
            self.btnk.setEnabled(False)
            self.last_win_lbl.setText("Выиграл 2 Игрок")
        elif self.p2score > 21 and self.p1score < 21:
            self.p1_win +=1
            self.btnz.setEnabled(False)
            self.btnk.setEnabled(False)
            self.last_win_lbl.setText("Выиграл 1 Игрок")
        elif self.p1score > 21 and self.p2score > 21:
            self.btnz.setEnabled(False)
            self.btnk.setEnabled(False)
            self.last_win_lbl.setText("ничья")
        elif self.p1score > self.p2score:
            self.btnz.setEnabled(False)
            self.btnk.setEnabled(False)
            self.last_win_lbl.setText("Выиграл 1 Игрок")
            self.p1_win +=1
        elif self.p1score < self.p2score:
            self.p2_win += 1
            self.btnz.setEnabled(False)
            self.btnk.setEnabled(False)  
            self.last_win_lbl.setText("Выиграл 2 Игрок")
        self.res.resize(100, 60)
    
    
    def again(self):
        self.btc.resize(0,0)
        self.btnk.resize(0, 0)
        self.res.resize(0, 0)
        self.suma = 0
        self.lcard = None
        self.last_win_lbl.setText("                                           ")
        self.lbll.setText("Последняя взятая карта: None          ")
        self.lbls.setText("сумма: {}          ".format(self.suma))
        
        self.cards = []
        masti = ['буби','червы','крести','пики']
        val = [6,7,8,9,10,'J', "D", "K", 'T']
        for j in range(4):
            for i in range(9):
                self.cards.append([masti[j],val[i]])
        self.turn = 0
        self.btnt.resize(90, 40)
        self.btnz.resize(90, 40)
        self.btnz.setEnabled(True)
        self.btnn.resize(120, 70)
        self.btnn.setEnabled(False)
        self.btnk.setEnabled(True)
        self.win1_lbl.setText("кол-во побед первого игрока:{}                                      ".format(self.p1_win))
        self.win2_lbl.setText("кол-во побед второго игрока:{}                                      ".format(self.p2_win))

        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
