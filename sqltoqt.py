import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QRadioButton, QPushButton
from PyQt5.QtGui import QFont
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.con=sqlite3.connect("Meva.db")
        self.k=self.con.cursor()
        self.setWindowTitle("Database and PyQt5")
        self.setGeometry(200,200,1100,800)
        self.start()
    def font(self,ob,x,y):
        ob.setFont(QFont("Times",30))
        ob.move(x,y)
    def start(self):
        self.create()
        self.l1=QLabel("Id",self)
        self.font(self.l1,50,50)
        self.l2=QLabel("Name",self)
        self.font(self.l2,50,120)
        self.l3=QLabel("Price",self)
        self.font(self.l3,50,190)
        self.k1=QLineEdit(self)
        self.font(self.k1,250,50)
        self.k1.setPlaceholderText("Id...")
        self.k2=QLineEdit(self)
        self.font(self.k2,250,120)
        self.k2.setPlaceholderText("Name...")
        self.k3=QLineEdit(self)
        self.font(self.k3,250,190)
        self.add=QPushButton("ADD",self)
        self.font(self.add,50,260)
        self.delete=QPushButton("DELETE",self)
        self.font(self.delete,170,260)
        self.update=QPushButton("UPDATE",self)
        self.font(self.update,355,260)
        self.k3.setPlaceholderText("Price...")
        self.v1=QRadioButton("Id",self)
        self.font(self.v1,750,50)
        self.v2=QRadioButton("Name",self)
        self.font(self.v2,750,120)
        self.v3=QRadioButton("Price",self)
        self.font(self.v3,750,190)
        self.s=QLineEdit(self)
        self.font(self.s,750,260)
        self.s.setPlaceholderText("Searching...")
    def create(self):
        self.k.execute("""CREATE TABLE IF NOT EXISTS meva(id NUMERIC,
                          name TEXT, price REAL, PRIMARY KEY(id) )""")
        self.con.commit()
    def insert(self):
        self.k.execute("""INSERT INTO meva VALUES
                        (1,"Olma",12000),
                        (2,"Anor",25000),
                        (3,"Shaftoli",45000),
                        (4,"Banan",20000),
                        (5,"Gilos",35000),
                        (6,"Qulupnay",85000),
                        (7,"Uzum",36000),
                        (8,"Avakado",75000)""")
        self.con.commit()
app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())