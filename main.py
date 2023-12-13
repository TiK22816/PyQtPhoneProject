import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTableWidget, \
    QTableWidgetItem, QDialog, QMessageBox, QHBoxLayout
from PyQt5 import QtGui
import sqlite3
import random

class AuthorizationWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.setWindowTitle("Авторизация")
        self.setGeometry(200, 200, 300, 200)
        self.username_label = QLabel("Имя пользовотеля:")
        self.username_label.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        stud = StudentApp()
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)
        stud.pepa = self.username_input
        self.password_label = QLabel("Пароль:")
        self.password_label.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)

        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.login)

        self.q_label = QLabel("Нет аккаунта?  Зарегестрируйся")
        self.q_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: black;
                                                }
                                                """)
        self.reg_button = QPushButton("Register")
        self.reg_button.clicked.connect(self.regis)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.q_label)
        layout.addWidget(self.reg_button)
        self.setLayout(layout)

        self.login_button.setStyleSheet("""
                QPushButton{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid red;
                    border-radius: 15px;
                    color: white;
                    background-color: red;
                }
                """)

        self.reg_button.setStyleSheet("""
                        QPushButton{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid grey;
                            border-radius: 15px;
                            color: black;
                            background-color: white;
                        }
                        """)


        self.status = None
        self.user_name = None

    def regis(self):
        ex = PeopleWindow()
        ex.exec()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()
        conn.close()

        if user:
            self.status = user[6]
            self.user_name = user[4]
            self.accept()
        else:
            err = ErrorWin()
            err.exec()


class ErrorWin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Ошибка")
        self.setFixedSize(333,150)
        self.subject_label = QLabel("Неправильное имя пользователя или пароль!")
        self.subject_label.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.submit_button = QPushButton("Назад")
        self.submit_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid black;
                                    border-radius: 15px;
                                    color: white;
                                    background-color: grey;
                                }
                                """)
        self.submit_button.clicked.connect(self.go_to_login1)

        layout = QVBoxLayout()
        layout.addWidget(self.subject_label)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def go_to_login1(self):
        while True:
            self.close()
            break

class AddPairWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))

        self.setWindowTitle("Добавить тариф")
        self.setGeometry(200, 200, 400, 200)

        self.kategory = QLabel("Категория(Основной или Дополнительный)")
        self.kategory.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.kategory_input = QLineEdit()
        self.kategory_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)



        self.tarif = QLabel("Название тарифа:")
        self.tarif.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.tarif_input = QLineEdit()
        self.tarif_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)

        self.gigs_mins = QLabel("Сколько гигабайт и минут:")
        self.gigs_mins.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.gigs_mins_input = QLineEdit()
        self.gigs_mins_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid grey;
                            border-radius: 15px;
                            color: black;
                            background-color: white;
                        }
                        """)

        self.price = QLabel("Цена")
        self.price.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.price_input = QLineEdit()
        self.price_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)

        self.submit_button = QPushButton("Добавить тариф")
        self.submit_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid black;
                                    border-radius: 15px;
                                    color: white;
                                    background-color: grey;
                                }
                                """)
        self.submit_button.clicked.connect(self.add_pair)

        layout = QVBoxLayout()
        layout.addWidget(self.kategory)
        layout.addWidget(self.kategory_input)
        layout.addWidget(self.tarif)
        layout.addWidget(self.tarif_input)
        layout.addWidget(self.gigs_mins)
        layout.addWidget(self.gigs_mins_input)
        layout.addWidget(self.price)
        layout.addWidget(self.price_input)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def add_pair(self):
        kategory = self.kategory_input.text()
        tarif = self.tarif_input.text()
        gig = self.gigs_mins_input.text()
        price = self.price_input.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarif (kategory, name, gigs_mins, price) VALUES (?, ?, ?, ?)",
                       (kategory, tarif, gig, price))
        conn.commit()

        conn.close()

        self.close()


class RedPairWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))

        self.setWindowTitle("Изменить тариф")
        self.setGeometry(200, 200, 400, 200)

        self.last_name = QLabel("Название прошлого тарифа")
        self.last_name.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.last_input = QLineEdit()
        self.last_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)

        self.kategory = QLabel("Новая категория(Основной или Дополнительный)")
        self.kategory.setStyleSheet("""
                                               QLabel{
                                                   font-style: classic;
                                                   font-weight: bold;
                                                   color: black;
                                               }
                                               """)
        self.kategory_input = QLineEdit()
        self.kategory_input.setStyleSheet("""
                       QLineEdit{
                           font-style: classic;
                           font-weight: bold;
                           border: 3px solid grey;
                           border-radius: 15px;
                           color: grey;
                       }
                       """)



        self.new_tarif = QLabel("Новое название тарифа:")
        self.new_tarif.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.new_tarif_input = QLineEdit()
        self.new_tarif_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)

        self.gigs_mins = QLabel("Сколько гигабайт и минут:")
        self.gigs_mins.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.gigs_mins_input = QLineEdit()
        self.gigs_mins_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid grey;
                            border-radius: 15px;
                            color: black;
                            background-color: white;
                        }
                        """)

        self.price = QLabel("Цена")
        self.price.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.price_input = QLineEdit()
        self.price_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)

        self.submit_button = QPushButton("Добавить тариф")
        self.submit_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid black;
                                    border-radius: 15px;
                                    color: white;
                                    background-color: grey;
                                }
                                """)
        self.submit_button.clicked.connect(self.add_pair)

        layout = QVBoxLayout()
        layout.addWidget(self.last_name)
        layout.addWidget(self.last_input)
        layout.addWidget(self.kategory)
        layout.addWidget(self.kategory_input)
        layout.addWidget(self.new_tarif)
        layout.addWidget(self.new_tarif_input)
        layout.addWidget(self.gigs_mins)
        layout.addWidget(self.gigs_mins_input)
        layout.addWidget(self.price)
        layout.addWidget(self.price_input)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def add_pair(self):
        last = self.last_input.text()
        kategory = self.kategory_input.text()
        new_name = self.new_tarif_input.text()
        gigs_mins = self.gigs_mins_input.text()
        price = self.price_input.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        sql = f"UPDATE tarif SET kategory = ?, name = ?, gigs_mins = ?, price = ? \
                                    WHERE name = ?"
        val = (f"{kategory}", f"{new_name}",f"{gigs_mins}",f"{price}", f"{last}")
        cursor.execute(sql, val)

        conn.commit()
        conn.close()
        self.close()


class TarifWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.setWindowTitle("Оценки учащихся")
        self.setGeometry(200, 200, 600, 400)


        self.assessment_table = QTableWidget()
        self.assessment_table.setColumnCount(4)
        self.assessment_table.setHorizontalHeaderLabels(["Категория", "Название", "Гиг. и минуты", "Цена"])

        self.assessment_table.setStyleSheet("""
                                            QTableWidget{
                                                font-style: classic;
                                                font-weight: bold;
                                                color: black;
                                                background-color: white;
                                            }
                                            """)

        layout = QVBoxLayout()
        layout.addWidget(self.assessment_table)
        self.setLayout(layout)

    def view_assessments(self):
        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()

        user_type = authorization_window.status
        if user_type:
            cursor.execute(f"SELECT * FROM tarif ")
        else:
            cursor.execute(f"SELECT * FROM tarif")
        assessments = cursor.fetchall()
        conn.close()
        self.assessment_table.setRowCount(0)
        for row_num, assessment in enumerate(assessments):
            self.assessment_table.insertRow(row_num)
            for col_num, data in enumerate(assessment):
                self.assessment_table.setItem(row_num, col_num , QTableWidgetItem(str(data)))







class PeopleWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.setWindowTitle("Зарегестрироваться")
        self.setGeometry(200, 200, 600, 400)

        self.setWindowTitle("Регистрация")
        self.setGeometry(200, 200, 300, 150)
        self.name = QLabel("Ваше Имя:")
        self.name.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: black;
                                                }
                                                """)
        self.name_l = QLineEdit()
        self.name_l.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid grey;
                            border-radius: 15px;
                            color: grey;
                        }
                        """)
        self.fam = QLabel("Ваша Фамилия:")
        self.fam.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: black;
                                                }
                                                """)
        self.fam_l = QLineEdit()
        self.fam_l.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid grey;
                            border-radius: 15px;
                            color: grey;
                        }
                        """)
        self.th_name = QLabel("Ваше Отчество:")
        self.th_name.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: black;
                                                }
                                                """)
        self.th_name_l = QLineEdit()
        self.th_name_l.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid grey;
                            border-radius: 15px;
                            color: grey;
                        }
                        """)
        self.email = QLabel("Ваш Email:")
        self.email.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.email_l = QLineEdit()
        self.email_l.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)
        self.user_label = QLabel("Логин:")
        self.user_label.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)
        self.passw_label = QLabel("Пароль:")
        self.passw_label.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.passw_input = QLineEdit()
        self.passw_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)
        self.passw_input.setEchoMode(QLineEdit.Password)

        self.reg_button = QPushButton("Зарегестрироваться")
        self.reg_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid black;
                                    border-radius: 15px;
                                    color: white;
                                    background-color: grey;
                                }
                                """)
        self.reg_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.name_l)
        layout.addWidget(self.fam)
        layout.addWidget(self.fam_l)
        layout.addWidget(self.th_name)
        layout.addWidget(self.th_name_l)
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.passw_label)
        layout.addWidget(self.passw_input)
        layout.addWidget(self.email)
        layout.addWidget(self.email_l)
        layout.addWidget(self.reg_button)
        self.setLayout(layout)

        layout = QVBoxLayout()
        self.setLayout(layout)

    def register(self):
        name = self.name_l.text()
        fam = self.fam_l.text()
        th_name = self.th_name_l.text()
        email = self.email_l.text()
        username = self.user_input.text()
        password = self.passw_input.text()
        usertype = "user"

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, fam, th_name, username, password, user_type, email) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, fam, th_name, username, password, usertype, email))
        conn.commit()
        conn.close()

        self.close()



class DeletePair(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Удалить Тариф")
        self.setGeometry(200, 200, 600, 400)

        self.setWindowTitle("Удаление")
        self.setGeometry(200, 200, 300, 150)
        self.user_label = QLabel("Название Тарифа:")
        self.user_label.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: black;
                                        }
                                        """)
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid grey;
                    border-radius: 15px;
                    color: grey;
                }
                """)
        self.del_button = QPushButton("Удалить")
        self.del_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid black;
                                    border-radius: 15px;
                                    color: white;
                                    background-color: grey;
                                }
                                """)
        self.del_button.clicked.connect(self.del_pair)

        layout = QVBoxLayout()
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.del_button)
        self.setLayout(layout)

        layout = QVBoxLayout()
        self.setLayout(layout)

    def del_pair(self):
        id = self.user_input.text()
        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM tarif WHERE name = '{id}'")
        conn.commit()
        conn.close()

        self.close()




class TeacherApp(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Админская панель")
        self.setFixedSize(900,800)


        self.go_to_login_button = QPushButton("Назад")
        self.go_to_login_button.setStyleSheet("""
                QPushButton{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid black;
                    border-radius: 15px;
                    color: white;
                    background-color: red;
                }
                """)
        self.go_to_login_button.setFixedSize(150, 35)
        self.go_to_login_button.clicked.connect(self.go_to_login1)

        self.add_tarif = QPushButton("Добавить тариф")
        self.add_tarif.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid black;
                                    border-radius: 15px;
                                    color: white;
                                    background-color: grey;
                                }
                                """)
        self.add_tarif.setFixedSize(500, 35)
        self.add_tarif.clicked.connect(self.open_add_tarif_window)

        self.red_tarif = QPushButton("Редактировать тариф")
        self.red_tarif.setStyleSheet("""
                                        QPushButton{
                                            font-style: classic;
                                            font-weight: bold;
                                            border: 3px solid black;
                                            border-radius: 15px;
                                            color: white;
                                            background-color: grey;
                                        }
                                        """)
        self.red_tarif.setFixedSize(500, 35)
        self.red_tarif.clicked.connect(self.open_red_tarif_window)



        self.del_tarif = QPushButton("Удалить тариф")
        self.del_tarif.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid black;
                                    border-radius: 15px;
                                    color: white;
                                    background-color: grey;
                                }
                                """)
        self.del_tarif.setFixedSize(500, 35)
        self.del_tarif.clicked.connect(self.delete_tarif)





        self.view_tarif = QPushButton("Посмотреть тариф")
        self.view_tarif.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid black;
                                    border-radius: 15px;
                                    color: white;
                                    background-color: grey;
                                }
                                """)
        self.view_tarif.setFixedSize(500, 35)
        self.view_tarif.clicked.connect(self.open_assessment_window)



        layout = QVBoxLayout()
        layout.addWidget(self.go_to_login_button)
        layout.addWidget(self.add_tarif)
        layout.addWidget(self.red_tarif)
        layout.addWidget(self.del_tarif)
        layout.addWidget(self.view_tarif)



        self.tarif_window = TarifWindow()
        layout.addWidget(self.tarif_window)




        self.setLayout(layout)



    def delete_tarif(self):
        del_p_win = DeletePair()
        del_p_win.exec()




    def open_add_tarif_window(self):
        add_pair_window = AddPairWindow()
        add_pair_window.exec()


    def open_red_tarif_window(self):
        add_pair_window = RedPairWindow()
        add_pair_window.exec()



    def open_assessment_window(self):
        self.tarif_window.view_assessments()

    def go_to_login1(self):
        while True:
            self.close()
            os.system("python main.py")
            break


class ChBalanceWin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.setWindowTitle("Баланс")
        self.setFixedSize(300,200)

        self.go_back_button = QPushButton("Назад")
        self.go_back_button.setStyleSheet("""
                               QPushButton{
                                   font-style: classic;
                                   font-weight: bold;
                                   border: 3px solid grey;
                                   border-radius: 15px;
                                   color: black;
                                   background-color: grey;
                               }
                               """)
        self.go_back_button.clicked.connect(self.go_to_login2)

        self.subm = QPushButton("Узнать баланс")
        self.subm.setStyleSheet("""
                                       QPushButton{
                                           font-style: classic;
                                           font-weight: bold;
                                           border: 3px solid black;
                                           border-radius: 15px;
                                           color: white;
                                           background-color: red;
                                       }
                                       """)
        self.subm.clicked.connect(self.go_subm)
        self.user_label = QLabel("Логин:")
        self.user_label.setStyleSheet("""
                                               QLabel{
                                                   font-style: classic;
                                                   font-weight: bold;
                                                   color: black;
                                               }
                                               """)
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("""
                       QLineEdit{
                           font-style: classic;
                           font-weight: bold;
                           border: 3px solid grey;
                           border-radius: 15px;
                           color: grey;
                       }
                       """)
        self.passw_label = QLabel("Пароль:")
        self.passw_label.setStyleSheet("""
                                               QLabel{
                                                   font-style: classic;
                                                   font-weight: bold;
                                                   color: black;
                                               }
                                               """)
        self.passw_input = QLineEdit()
        self.passw_input.setStyleSheet("""
                       QLineEdit{
                           font-style: classic;
                           font-weight: bold;
                           border: 3px solid grey;
                           border-radius: 15px;
                           color: grey;
                       }
                       """)
        self.passw_input.setEchoMode(QLineEdit.Password)

        self.m_l = QLabel("Тут будет баланс после ввода данных:)")
        self.m_l.setStyleSheet("""
                                                       QLabel{
                                                           font-style: classic;
                                                           font-weight: bold;
                                                           color: black;
                                                       }
                                                       """)


        layout = QVBoxLayout()
        layout.addWidget(self.go_back_button)
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.passw_label)
        layout.addWidget(self.passw_input)
        layout.addWidget(self.m_l)

        layout.addWidget(self.subm)
        self.setLayout(layout)

    def go_to_login2(self):
        self.close()

    def go_subm(self):
        try:
            username = self.user_input.text()
            password = self.passw_input.text()

            conn = sqlite3.connect('pairs_users.db')
            cursor = conn.cursor()

            cursor.execute(f"SELECT balance FROM users WHERE username='{username}' AND password='{password}'")
            user = cursor.fetchone()
            user = list(user)
            m = user[0]
            if m == None:
                self.m_l.setText(f"Ваш баланс = 0")
            else:
                self.m_l.setText(f"Ваш баланс = {m}")
            conn.close()
        except:
            pass


class PBalanceWin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.setWindowTitle("Баланс")
        self.setFixedSize(400,300)

        self.go_back_button = QPushButton("Назад")
        self.go_back_button.setStyleSheet("""
                               QPushButton{
                                   font-style: classic;
                                   font-weight: bold;
                                   border: 3px solid grey;
                                   border-radius: 15px;
                                   color: black;
                                   background-color: grey;
                               }
                               """)
        self.go_back_button.clicked.connect(self.go_to_login2)

        self.subm = QPushButton("Пополнить баланс")
        self.subm.setStyleSheet("""
                                       QPushButton{
                                           font-style: classic;
                                           font-weight: bold;
                                           border: 3px solid black;
                                           border-radius: 15px;
                                           color: white;
                                           background-color: red;
                                       }
                                       """)
        self.subm.clicked.connect(self.go_subm)
        self.user_label = QLabel("Логин:")
        self.user_label.setStyleSheet("""
                                               QLabel{
                                                   font-style: classic;
                                                   font-weight: bold;
                                                   color: black;
                                               }
                                               """)
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("""
                       QLineEdit{
                           font-style: classic;
                           font-weight: bold;
                           border: 3px solid grey;
                           border-radius: 15px;
                           color: grey;
                       }
                       """)
        self.passw_label = QLabel("Пароль:")
        self.passw_label.setStyleSheet("""
                                               QLabel{
                                                   font-style: classic;
                                                   font-weight: bold;
                                                   color: black;
                                               }
                                               """)
        self.passw_input = QLineEdit()
        self.passw_input.setStyleSheet("""
                       QLineEdit{
                           font-style: classic;
                           font-weight: bold;
                           border: 3px solid grey;
                           border-radius: 15px;
                           color: grey;
                       }
                       """)
        self.passw_input.setEchoMode(QLineEdit.Password)

        self.card = QLabel("Номер вашей карты(средства будут списаны)")
        self.card.setStyleSheet("""
                                                       QLabel{
                                                           font-style: classic;
                                                           font-weight: bold;
                                                           color: black;
                                                       }
                                                       """)
        self.card_input = QLineEdit()
        self.card_input.setStyleSheet("""
                               QLineEdit{
                                   font-style: classic;
                                   font-weight: bold;
                                   border: 3px solid grey;
                                   border-radius: 15px;
                                   color: grey;
                               }
                               """)
        self.num = QLabel("Cумма")
        self.num.setStyleSheet("""
                                                               QLabel{
                                                                   font-style: classic;
                                                                   font-weight: bold;
                                                                   color: black;
                                                               }
                                                               """)
        self.num_input = QLineEdit()
        self.num_input.setStyleSheet("""
                                       QLineEdit{
                                           font-style: classic;
                                           font-weight: bold;
                                           border: 3px solid grey;
                                           border-radius: 15px;
                                           color: grey;
                                       }
                                       """)



        layout = QVBoxLayout()
        layout.addWidget(self.go_back_button)
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.passw_label)
        layout.addWidget(self.passw_input)
        layout.addWidget(self.card)
        layout.addWidget(self.card_input)
        layout.addWidget(self.num)
        layout.addWidget(self.num_input)

        layout.addWidget(self.subm)
        self.setLayout(layout)

    def go_to_login2(self):
        self.close()

    def go_subm(self):
        username = self.user_input.text()
        num = self.num_input.text()
        num_int = int(num)
        password = self.passw_input.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        a = cursor.execute(f"SELECT balance FROM users WHERE username='{username}'")
        b = list(a.fetchone())
        c = b[0]
        l = int(c)
        sql = "UPDATE users SET balance = ? \
                            WHERE username = ? and password = ?"
        val = (f"{l + num_int}", f"{username}", f"{password}")
        cursor.execute(sql, val)

        conn.commit()
        conn.close()
        self.close()

class TarBuyWin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.setWindowTitle("Баланс")
        self.setFixedSize(400,300)

        self.go_back_button = QPushButton("Назад")
        self.go_back_button.setStyleSheet("""
                               QPushButton{
                                   font-style: classic;
                                   font-weight: bold;
                                   border: 3px solid grey;
                                   border-radius: 15px;
                                   color: black;
                                   background-color: grey;
                               }
                               """)
        self.go_back_button.clicked.connect(self.go_to_login2)

        self.subm = QPushButton("Купить тариф")
        self.subm.setStyleSheet("""
                                       QPushButton{
                                           font-style: classic;
                                           font-weight: bold;
                                           border: 3px solid black;
                                           border-radius: 15px;
                                           color: white;
                                           background-color: red;
                                       }
                                       """)
        self.subm.clicked.connect(self.go_subm)
        self.user_label = QLabel("Логин:")
        self.user_label.setStyleSheet("""
                                               QLabel{
                                                   font-style: classic;
                                                   font-weight: bold;
                                                   color: black;
                                               }
                                               """)
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("""
                       QLineEdit{
                           font-style: classic;
                           font-weight: bold;
                           border: 3px solid grey;
                           border-radius: 15px;
                           color: grey;
                       }
                       """)
        self.passw_label = QLabel("Пароль:")
        self.passw_label.setStyleSheet("""
                                               QLabel{
                                                   font-style: classic;
                                                   font-weight: bold;
                                                   color: black;
                                               }
                                               """)
        self.passw_input = QLineEdit()
        self.passw_input.setStyleSheet("""
                       QLineEdit{
                           font-style: classic;
                           font-weight: bold;
                           border: 3px solid grey;
                           border-radius: 15px;
                           color: grey;
                       }
                       """)
        self.passw_input.setEchoMode(QLineEdit.Password)

        self.card = QLabel("Название тарифа")
        self.card.setStyleSheet("""
                                                       QLabel{
                                                           font-style: classic;
                                                           font-weight: bold;
                                                           color: black;
                                                       }
                                                       """)
        self.card_input = QLineEdit()
        self.card_input.setStyleSheet("""
                               QLineEdit{
                                   font-style: classic;
                                   font-weight: bold;
                                   border: 3px solid grey;
                                   border-radius: 15px;
                                   color: grey;
                               }
                               """)

        self.ex = QLabel("")
        self.ex.setStyleSheet("""
                                                       QLabel{
                                                           font-style: classic;
                                                           font-weight: bold;
                                                           color: black;
                                                       }
                                                       """)

        layout = QVBoxLayout()
        layout.addWidget(self.go_back_button)
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.passw_label)
        layout.addWidget(self.passw_input)
        layout.addWidget(self.card)
        layout.addWidget(self.card_input)
        layout.addWidget(self.ex)


        layout.addWidget(self.subm)
        self.setLayout(layout)

    def go_to_login2(self):
        self.close()

    def go_subm(self):
        username = self.user_input.text()
        password = self.passw_input.text()
        tarif_name = self.card_input.text()


        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        try:
            a = cursor.execute(f"SELECT balance FROM users WHERE username='{username}'")
            b = list(a.fetchone())
            c = b[0]
            p_bal = int(c)
            g = cursor.execute(f"SELECT price FROM tarif WHERE name='{tarif_name}'")
            s = list(g.fetchone())
            l = s[0]
            p_price = int(l)

            if p_bal > p_price:
                sql = "UPDATE users SET tarif_name = ? \
                                        WHERE username = ? and password = ?"
                val = (f"{tarif_name}", f"{username}", f"{password}")
                cursor.execute(sql, val)
                dsql = "UPDATE users SET balance = ? \
                                        WHERE username = ? and password = ?"
                dval = (f"{p_bal - p_price}", f"{username}", f"{password}")
                cursor.execute(sql, val)
                cursor.execute(dsql, dval)
                conn.commit()
                conn.close()
                self.close()
            else:
                self.ex.setText("Не достаточно средств")
        except:
            self.ex.setText("Введены неправильные данные")

class Phone(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.setWindowTitle("Номера")
        self.setFixedSize(400,330)

        self.go_back_button = QPushButton("Назад")
        self.go_back_button.setStyleSheet("""
                               QPushButton{
                                   font-style: classic;
                                   font-weight: bold;
                                   border: 3px solid grey;
                                   border-radius: 15px;
                                   color: black;
                                   background-color: grey;
                               }
                               """)
        self.go_back_button.clicked.connect(self.go_to_login2)

        self.login = QLabel("                                     Ваш Логин")
        self.login.setStyleSheet("""
                                                              QLabel{
                                                                  font-style: classic;
                                                                  font-weight: bold;
                                                                  color: black;
                                                              }
                                                              """)
        self.login_input = QLineEdit()
        self.login_input.setStyleSheet("""
                                      QLineEdit{
                                          font-style: classic;
                                          font-weight: bold;
                                          border: 3px solid grey;
                                          border-radius: 15px;
                                          color: grey;
                                      }
                                      """)

        self.user_label = QLabel("                    Введите номер который выбрали")
        self.user_label.setStyleSheet("""
                                                      QLabel{
                                                          font-style: classic;
                                                          font-weight: bold;
                                                          color: black;
                                                      }
                                                      """)
        self.user_sss = QLineEdit()
        self.user_sss.setStyleSheet("""
                              QLineEdit{
                                  font-style: classic;
                                  font-weight: bold;
                                  border: 3px solid grey;
                                  border-radius: 15px;
                                  color: grey;
                              }
                              """)

        self.subm = QPushButton("Подтвердить номер")
        self.subm.setStyleSheet("""
                                       QPushButton{
                                           font-style: classic;
                                           font-weight: bold;
                                           border: 3px solid black;
                                           border-radius: 15px;
                                           color: white;
                                           background-color: red;
                                       }
                                       """)
        self.subm.clicked.connect(self.go_subm)

        num_list = []
        while len(num_list) < 3:
            lnum = str(random.randint(0, 999999999)).zfill(9)
            if not lnum in num_list:
                num_list.append(lnum)



        self.f_num = QLabel(f"+7{str(num_list[0])}")
        self.f_num.setStyleSheet("""
                                                     QLabel{
                                                         font-style: classic;
                                                         font-weight: bold;
                                                         color: black;
                                                     }
                                                     """)


        self.s_num = QLabel(f"+7{str(num_list[1])}")
        self.s_num.setStyleSheet("""
                                                     QLabel{
                                                         font-style: classic;
                                                         font-weight: bold;
                                                         color: black;
                                                     }
                                                     """)



        self.t_num = QLabel(f"+7{str(num_list[2])}")
        self.t_num.setStyleSheet("""
                                                     QLabel{
                                                         font-style: classic;
                                                         font-weight: bold;
                                                         color: black;
                                                     }
                                                     """)

        self.exe = QLabel("")
        self.exe.setStyleSheet("""
                                                             QLabel{
                                                                 font-style: classic;
                                                                 font-weight: bold;
                                                                 color: black;
                                                             }
                                                             """)





        layout = QVBoxLayout()
        layout.addWidget(self.go_back_button)
        layout.addWidget(self.login)
        layout.addWidget(self.login_input)
        layout.addWidget(self.f_num)
        layout.addWidget(self.s_num)
        layout.addWidget(self.t_num)
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_sss)

        layout.addWidget(self.subm)
        self.setLayout(layout)

    def go_to_login2(self):
        self.close()

    def go_subm(self):
        login = self.login_input.text()
        nomer = self.user_sss.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        a = cursor.execute(f"SELECT phone FROM users WHERE username='{login}'")
        b = list(a.fetchone())
        c = b[0]
        if c == None:
            sql = "UPDATE users SET phone = ? \
                                        WHERE username = ?"
            val = (f"{nomer}", f"{login}")
            cursor.execute(sql, val)
            conn.commit()
            conn.close()
            self.close()
        else:
            self.exe.setText("Ваш номер уже зарегестрирован")


class ChDannie(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.setWindowTitle("Данные")
        self.setFixedSize(500,400)

        self.go_back_button = QPushButton("Назад")
        self.go_back_button.setStyleSheet("""
                               QPushButton{
                                   font-style: classic;
                                   font-weight: bold;
                                   border: 3px solid grey;
                                   border-radius: 15px;
                                   color: black;
                                   background-color: grey;
                               }
                               """)
        self.go_back_button.clicked.connect(self.go_to_login2)

        self.subm = QPushButton("Узнать данные")
        self.subm.setStyleSheet("""
                                       QPushButton{
                                           font-style: classic;
                                           font-weight: bold;
                                           border: 3px solid black;
                                           border-radius: 15px;
                                           color: white;
                                           background-color: red;
                                       }
                                       """)
        self.subm.clicked.connect(self.go_subm)
        self.user_label = QLabel("Логин:")
        self.user_label.setStyleSheet("""
                                               QLabel{
                                                   font-style: classic;
                                                   font-weight: bold;
                                                   color: black;
                                               }
                                               """)
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("""
                       QLineEdit{
                           font-style: classic;
                           font-weight: bold;
                           border: 3px solid grey;
                           border-radius: 15px;
                           color: grey;
                       }
                       """)
        self.passw_label = QLabel("Пароль:")
        self.passw_label.setStyleSheet("""
                                               QLabel{
                                                   font-style: classic;
                                                   font-weight: bold;
                                                   color: black;
                                               }
                                               """)
        self.passw_input = QLineEdit()
        self.passw_input.setStyleSheet("""
                       QLineEdit{
                           font-style: classic;
                           font-weight: bold;
                           border: 3px solid grey;
                           border-radius: 15px;
                           color: grey;
                       }
                       """)
        self.passw_input.setEchoMode(QLineEdit.Password)

        self.name = QLabel("")
        self.name.setStyleSheet("""
                                                       QLabel{
                                                           font-style: classic;
                                                           font-weight: bold;
                                                           color: black;
                                                       }
                                                       """)

        self.fam = QLabel("")
        self.fam.setStyleSheet("""
                                                       QLabel{
                                                           font-style: classic;
                                                           font-weight: bold;
                                                           color: black;
                                                       }
                                                       """)
        self.th_name = QLabel("")
        self.th_name.setStyleSheet("""
                                                       QLabel{
                                                           font-style: classic;
                                                           font-weight: bold;
                                                           color: black;
                                                       }
                                                       """)
        self.email = QLabel("")
        self.email.setStyleSheet("""
                                                       QLabel{
                                                           font-style: classic;
                                                           font-weight: bold;
                                                           color: black;
                                                       }
                                                       """)

        self.tarif = QLabel("")
        self.tarif.setStyleSheet("""
                                                       QLabel{
                                                           font-style: classic;
                                                           font-weight: bold;
                                                           color: black;
                                                       }
                                                       """)




        layout = QVBoxLayout()
        layout.addWidget(self.go_back_button)
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.passw_label)
        layout.addWidget(self.passw_input)
        layout.addWidget(self.name)
        layout.addWidget(self.fam)
        layout.addWidget(self.th_name)
        layout.addWidget(self.email)
        layout.addWidget(self.tarif)
        layout.addWidget(self.subm)
        self.setLayout(layout)

    def go_to_login2(self):
        self.close()

    def go_subm(self):
        username = self.user_input.text()
        password = self.passw_input.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()

        all = cursor.execute(f"SELECT name,fam,th_name,email,tarif_name FROM users WHERE username = '{username}'")
        b = all.fetchone()
        b = list(b)
        if b[4] == None:
            self.name.setText(f"Ваше Имя: {b[0]}")
            self.fam.setText(f"Ваша Фамилия: {b[1]}")
            self.th_name.setText(f"Ваше Отчество: {b[2]}")
            self.email.setText(f"Ваш Gmail: {b[3]}")
            self.tarif.setText(f"Нет Тарифа!")
        else:
            self.name.setText(f"Ваше Имя: {b[0]}")
            self.fam.setText(f"Ваша Фамилия: {b[1]}")
            self.th_name.setText(f"Ваше Отчество: {b[2]}")
            self.email.setText(f"Ваш Gmail: {b[3]}")
            self.tarif.setText(f"Ваш тариф: {b[4]}")




        conn.commit()
        conn.close()

class StudentApp(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.setWindowTitle("Пользовательское окно")
        self.setFixedSize(600,600)

        self.go_back_button = QPushButton("Назад")
        self.go_back_button.setStyleSheet("""
                QPushButton{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid black;
                    border-radius: 15px;
                    color: white;
                    background-color: red;
                }
                """)
        self.go_back_button.clicked.connect(self.go_to_login2)

        self.chek_balance = QPushButton("Проверить баланс")
        self.chek_balance.setStyleSheet("""
                                        QPushButton{
                                            font-style: classic;
                                            font-weight: bold;
                                            border: 3px solid black;
                                            border-radius: 15px;
                                            color: white;
                                            background-color: grey;
                                        }
                                        """)
        self.chek_balance.clicked.connect(self.balance)

        self.push_balance = QPushButton("Пополнить баланс")
        self.push_balance.setStyleSheet("""
                                                QPushButton{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    border: 3px solid black;
                                                    border-radius: 15px;
                                                    color: white;
                                                    background-color: grey;
                                                }
                                                """)
        self.push_balance.clicked.connect(self.p_b)

        self.tarifs = QPushButton("Посмотреть тарифы")
        self.tarifs.setStyleSheet("""
                                        QPushButton{
                                            font-style: classic;
                                            font-weight: bold;
                                            border: 3px solid black;
                                            border-radius: 15px;
                                            color: white;
                                            background-color: grey;
                                        }
                                        """)
        self.tarifs.clicked.connect(self.open_assessment_window)

        self.tar_buy = QPushButton("Приобрести тариф")
        self.tar_buy.setStyleSheet("""
                                                QPushButton{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    border: 3px solid black;
                                                    border-radius: 15px;
                                                    color: white;
                                                    background-color: grey;
                                                }
                                                """)
        self.tar_buy.clicked.connect(self.tarif_buyer)

        self.phone = QPushButton("Выбрать номер")
        self.phone.setStyleSheet("""
                                                        QPushButton{
                                                            font-style: classic;
                                                            font-weight: bold;
                                                            border: 3px solid black;
                                                            border-radius: 15px;
                                                            color: white;
                                                            background-color: grey;
                                                        }
                                                        """)
        self.phone.clicked.connect(self.phone_1)

        self.chek_dannie = QPushButton("Посмотреть свои данные")
        self.chek_dannie.setStyleSheet("""
                                                        QPushButton{
                                                            font-style: classic;
                                                            font-weight: bold;
                                                            border: 3px solid black;
                                                            border-radius: 15px;
                                                            color: white;
                                                            background-color: grey;
                                                        }
                                                        """)
        self.chek_dannie.clicked.connect(self.chek_dannie_1)

        layout = QVBoxLayout()
        layout.addWidget(self.go_back_button)
        layout.addWidget(self.chek_balance)
        layout.addWidget(self.push_balance)
        layout.addWidget(self.tar_buy)
        layout.addWidget(self.tarifs)
        layout.addWidget(self.chek_dannie)
        layout.addWidget(self.phone)

        self.tarif_window = TarifWindow()
        self.p_balance = PBalanceWin()
        layout.addWidget(self.tarif_window)

        self.setLayout(layout)

    def tarif_buyer(self):
        a = TarBuyWin()
        a.exec()

    def chek_dannie_1(self):
        d = ChDannie()
        d.exec()

    def phone_1(self):
        p = Phone()
        p.exec()

    def balance(self):
        niga = ChBalanceWin()
        niga.exec()

    def p_b(self):
        self.p_balance.exec()

    def open_assessment_window(self):
        self.tarif_window.view_assessments()

    def go_to_login2(self):
        while True:
            self.close()
            os.system("python main.py")
            break

if __name__ == '__main__':

    conn = sqlite3.connect('pairs_users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    fam TEXT,
                    th_name TEXT,
                    username TEXT UNIQUE,
                    password TEXT,
                    user_type TEXT,
                    email TEXT,
                    balance INTEGER,
                    tarif_name TEXT,
                    phone TEXT)''')


    cursor.execute('''CREATE TABLE IF NOT EXISTS tarif
                    (
                    kategory TEXT,
                    name TEXT,
                    gigs_mins TEXT,
                    price INTEGER)''')

    conn.commit()
    conn.close()

    app = QApplication(sys.argv)
    mainapp = None
    authorization_window = AuthorizationWindow()
    if authorization_window.exec() == QDialog.Accepted:
        if authorization_window.status == 'user':
            mainapp = StudentApp()
        else:
            mainapp = TeacherApp()

    mainapp.show()
    sys.exit(app.exec())