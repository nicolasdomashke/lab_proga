import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                             QTableWidgetItem, QPushButton, QMessageBox)

week = "Нечетная"
day = "Четверг"
Weeks = ["Нечетная", "Четная"]
Days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Schedule")

        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_weeks_tab()
        self._create_schedule_tab()
        self._create_subjects_tab()
        self._create_teachers_tab()


    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="schedule_db",
                                     user="postgres",
                                     password="1234",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_weeks_tab(self):
        self.weeks_tab = QWidget()
        self.tabs.addTab(self.weeks_tab, "Weeks")

        self.weeks_gbox = QGroupBox("Weeks")

        self.svbox0 = QVBoxLayout()
        self.shbox10 = QHBoxLayout()
        self.shbox20 = QHBoxLayout()

        self.svbox0.addLayout(self.shbox10)
        self.svbox0.addLayout(self.shbox20)

        self.shbox10.addWidget(self.weeks_gbox)

        self._create_weeks_table()


        self.weeks_tab.setLayout(self.svbox0)


    def _create_schedule_tab(self):
        self.schedule_tab = QWidget()
        self.tabs.addTab(self.schedule_tab, "Schedule")

        self.monday_gbox = QGroupBox("Schedule")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.monday_gbox)

        #self._create_monday_table()

        self.update_schedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_schedule_button)
        self.update_schedule_button.clicked.connect(self._update_schedule)

        self.schedule_tab.setLayout(self.svbox)

    def _create_subjects_tab(self):
        self.subjects_tab = QWidget()
        self.tabs.addTab(self.subjects_tab, "Subjects")

        self.subjects_gbox = QGroupBox('Subjects')

        self.svbox3 = QVBoxLayout()
        self.shbox4 = QHBoxLayout()
        self.shbox5 = QHBoxLayout()

        self.svbox3.addLayout(self.shbox4)
        self.svbox3.addLayout(self.shbox5)

        self.shbox4.addWidget(self.subjects_gbox)

        #self._create_subjects_table()

        self.update_subjects_button = QPushButton("Update")
        self.shbox5.addWidget(self.update_subjects_button)
        self.update_subjects_button.clicked.connect(self._update_subjects_table)

        self.subjects_tab.setLayout(self.svbox3)

    def _create_teachers_tab(self):
        self.teachers_tab = QWidget()
        self.tabs.addTab(self.teachers_tab, "Teachers")

        self.teachers_gbox = QGroupBox('Teachers')

        self.svbox6 = QVBoxLayout()
        self.shbox7 = QHBoxLayout()
        self.shbox8 = QHBoxLayout()

        self.svbox6.addLayout(self.shbox7)
        self.svbox6.addLayout(self.shbox8)

        self.shbox7.addWidget(self.teachers_gbox)

        #self._create_teachers_table()

        self.update_teachers_button = QPushButton("Update")
        self.shbox8.addWidget(self.update_teachers_button)
        self.update_teachers_button.clicked.connect(self._update_teachers_table)

        self.teachers_tab.setLayout(self.svbox6)

    def _create_weeks_table(self):
        self.weeks_table = QTableWidget()
        self.weeks_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.weeks_table.setColumnCount(7)
        self.weeks_table.setHorizontalHeaderLabels(
            ["понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Нечетная", "Четная"])

        mondayButton = QPushButton("Понедельник")
        tueButton = QPushButton("Вторник")
        wedButton = QPushButton("Среда")
        thuButton = QPushButton("Четверг")
        friButton = QPushButton("Пятница")
        oddButton = QPushButton("Нечетная")
        evenButton = QPushButton("Четная")

        self.weeks_table.setRowCount(1)

        self.weeks_table.setCellWidget(0, 0, mondayButton)
        self.weeks_table.setCellWidget(0, 1, tueButton)
        self.weeks_table.setCellWidget(0, 2, wedButton)
        self.weeks_table.setCellWidget(0, 3, thuButton)
        self.weeks_table.setCellWidget(0, 4, friButton)
        self.weeks_table.setCellWidget(0, 5, oddButton)
        self.weeks_table.setCellWidget(0, 6, evenButton)

        mondayButton.clicked.connect(lambda ch: self._monday())
        tueButton.clicked.connect(lambda ch: self._tue())
        wedButton.clicked.connect(lambda ch: self._wed())
        thuButton.clicked.connect(lambda ch: self._thu())
        friButton.clicked.connect(lambda ch: self._fri())
        oddButton.clicked.connect(lambda ch: self._odd())
        evenButton.clicked.connect(lambda ch: self._even())


        self.mvbox10 = QVBoxLayout()
        self.mvbox10.addWidget(self.weeks_table)
        self.weeks_gbox.setLayout(self.mvbox10)

    def _monday(self):
        global day
        day = "Понедельник"
        self._update_schedule()
    def _tue(self):
        global day
        day = "Вторник"
        self._update_schedule()
    def _wed(self):
        global day
        day = "Среда"
        self._update_schedule()
    def _thu(self):
        global day
        day = "Четверг"
        self._update_schedule()
    def _fri(self):
        global day
        day = "Пятница"
        self._update_schedule()
    def _odd(self):
        global week
        week = "Нечетная"
        self._update_schedule()
    def _even(self):
        global week
        week = "Четная"
        self._update_schedule()
    def _create_subjects_table(self):
        self.subjects_table = QTableWidget()
        self.subjects_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subjects_table.setColumnCount(4)
        self.subjects_table.setHorizontalHeaderLabels(
            ["id", "Subject", "Save row", "Delete row"])

        self._update_subjects_table()

        self.mvbox1 = QVBoxLayout()
        self.mvbox1.addWidget(self.subjects_table)
        self.subjects_gbox.setLayout(self.mvbox1)

    def _create_teachers_table(self):
        self.teachers_table = QTableWidget()
        self.teachers_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teachers_table.setColumnCount(5)
        self.teachers_table.setHorizontalHeaderLabels(
            ["id", "Full name", "Subject", "Save row", "Delete row"])

        self._update_teachers_table()

        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.teachers_table)
        self.teachers_gbox.setLayout(self.mvbox2)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(8)
        self.monday_table.setHorizontalHeaderLabels(["id", "Day", "Subject", "Auditorium", "Time", "Week", "Save row", "Delete row"])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _update_monday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day=%s AND week=%s", (day, week))
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            deleteRowButton = QPushButton("Delete row")
            saveRowButton = QPushButton("Save row")

            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[1])))
            self.monday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 4,
                                      QTableWidgetItem(str(r[4])))
            self.monday_table.setItem(i, 5,
                                      QTableWidgetItem(str(r[5])))
            self.monday_table.setCellWidget(i, 6, saveRowButton)
            self.monday_table.setCellWidget(i, 7, deleteRowButton)

            saveRowButton.clicked.connect(lambda ch, num=i: self._save_changes_to_row(num))
            deleteRowButton.clicked.connect(lambda ch, id=r[0]: self._delete_row_from_table(id))

        self.monday_table.setItem(len(records), 0,
                                  QTableWidgetItem(''))
        self.monday_table.setItem(len(records), 1,
                                  QTableWidgetItem(''))
        self.monday_table.setItem(len(records), 2,
                                  QTableWidgetItem(''))
        self.monday_table.setItem(len(records), 3,
                                  QTableWidgetItem(''))
        self.monday_table.setItem(len(records), 4,
                                  QTableWidgetItem(''))
        self.monday_table.setItem(len(records), 5,
                                  QTableWidgetItem(''))

        addRowButton = QPushButton("Add row")
        self.monday_table.setCellWidget(len(records), 6, addRowButton)
        addRowButton.clicked.connect(lambda ch, num=len(records): self._add_row_to_table(num))

        changeDayButton = QPushButton("Delete row")
        self.monday_table.setCellWidget(len(records), 7, changeDayButton)
        #changeDayButton.clicked.connect(lambda ch, num=len(records): self._change_day(num))

        self.monday_table.resizeRowsToContents()

    def _update_subjects_table(self):
        self.cursor.execute("SELECT * FROM subject")
        records = list(self.cursor.fetchall())

        self.subjects_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            deleteRowButton = QPushButton("Delete row")
            saveRowButton = QPushButton("Save row")

            self.subjects_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.subjects_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[1])))
            self.subjects_table.setCellWidget(i, 2, saveRowButton)
            self.subjects_table.setCellWidget(i, 3, deleteRowButton)

            saveRowButton.clicked.connect(lambda ch, num=i: self._save_changes_to_row_subjects(num))
            deleteRowButton.clicked.connect(lambda ch, id=r[0]: self._delete_row_from_table_subjects(id))

        self.subjects_table.setItem(len(records), 0,
                                  QTableWidgetItem(''))
        self.subjects_table.setItem(len(records), 1,
                                  QTableWidgetItem(''))

        addRowButton = QPushButton("Add row")
        self.subjects_table.setCellWidget(len(records), 2, addRowButton)
        addRowButton.clicked.connect(lambda ch, num=len(records): self._add_row_to_table_subjects(num))

        deleteRowButton = QPushButton("Delete row")
        self.subjects_table.setCellWidget(len(records), 3, deleteRowButton)

        self.subjects_table.resizeRowsToContents()

    def _update_teachers_table(self):
        self.cursor.execute("SELECT * FROM teacher")
        records = list(self.cursor.fetchall())

        self.teachers_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            deleteRowButton = QPushButton("Delete row")
            saveRowButton = QPushButton("Save row")

            self.teachers_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.teachers_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[1])))
            self.teachers_table.setItem(i, 2,
                                        QTableWidgetItem(str(r[2])))
            self.teachers_table.setCellWidget(i, 3, saveRowButton)
            self.teachers_table.setCellWidget(i, 4, deleteRowButton)

            saveRowButton.clicked.connect(lambda ch, num=i: self._save_changes_to_row_teachers(num))
            deleteRowButton.clicked.connect(lambda ch, id=r[0]: self._delete_row_from_table_teachers(id))

        self.teachers_table.setItem(len(records), 0,
                                  QTableWidgetItem(''))
        self.teachers_table.setItem(len(records), 1,
                                  QTableWidgetItem(''))
        self.teachers_table.setItem(len(records), 2,
                                    QTableWidgetItem(''))

        addRowButton = QPushButton("Add row")
        self.teachers_table.setCellWidget(len(records), 3, addRowButton)
        addRowButton.clicked.connect(lambda ch, num=len(records): self._add_row_to_table_teachers(num))

        deleteRowButton = QPushButton("Delete row")
        self.teachers_table.setCellWidget(len(records), 4, deleteRowButton)

        self.teachers_table.resizeRowsToContents()

    def _add_row_to_table(self, num):
        if self.monday_table.item(num, 2).text() == '' or self.monday_table.item(num, 3).text() == '' or self.monday_table.item(num, 4).text() == '':
            QMessageBox.about(self, "Error", "Enter all fields")
        try:
            self.cursor.execute("INSERT INTO timetable (day, subject, room_numb, start_time, week) VALUES (%s, %s, %s, %s, %s)", (day, self.monday_table.item(num, 2).text(), self.monday_table.item(num, 3).text(), self.monday_table.item(num, 4).text(), week))
            self.conn.commit()
            self._update_schedule()
        except:
            QMessageBox.about(self, "Error", "No such subject")

    def _add_row_to_table_subjects(self, num):
        try:
            self.cursor.execute("INSERT INTO subject (name) VALUES (%s)", (self.subjects_table.item(num, 1).text(),))
            self.conn.commit()
            self._update_subjects_table()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _add_row_to_table_teachers(self, num):
        if self.teachers_table.item(num, 1).text() == '' or self.teachers_table.item(num, 2).text() == '':
            QMessageBox.about(self, "Error", "Enter all fields")
        else:
            try:
                self.cursor.execute("INSERT INTO teacher (full_name, subject) VALUES (%s, %s)", (self.teachers_table.item(num, 1).text(), self.teachers_table.item(num, 2).text()))
                self.conn.commit()
                self._update_teachers_table()
            except:
                QMessageBox.about(self, "Error", "No such subject")

    def _delete_row_from_table(self, id):
        self.cursor.execute("DELETE FROM timetable WHERE id=%s", (id,))
        self.conn.commit()
        self._update_schedule()

    def _delete_row_from_table_subjects(self, id):
        try:
            self.cursor.execute("DELETE FROM subject WHERE id=%s", (id,))
            self.conn.commit()
            self._update_subjects_table()
        except:
            QMessageBox.about(self, "Error", "Can't delete subject because of refs")

    def _delete_row_from_table_teachers(self, id):
        self.cursor.execute("DELETE FROM teacher WHERE id=%s", (id,))
        self.conn.commit()
        self._update_teachers_table()

    def _save_changes_to_row(self, rowNum):
        id = self.monday_table.item(rowNum, 0).text()
        try:
            self.cursor.execute("UPDATE timetable SET subject=%s WHERE id=%s",
                                (self.monday_table.item(rowNum, 2).text(), id))
            self.cursor.execute("UPDATE timetable SET room_numb=%s WHERE id=%s",
                                (self.monday_table.item(rowNum, 3).text(), id))
            self.cursor.execute("UPDATE timetable SET start_time=%s WHERE id=%s",
                                (self.monday_table.item(rowNum, 4).text(), id))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _save_changes_to_row_subjects(self, rowNum):
        id = self.subjects_table.item(rowNum, 0).text()
        try:
            self.cursor.execute("UPDATE subject SET name=%s WHERE id=%s",
                                (self.subjects_table.item(rowNum, 1).text(), id))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _save_changes_to_row_teachers(self, rowNum):
        id = self.teachers_table.item(rowNum, 0).text()
        try:
            self.cursor.execute("UPDATE teacher SET full_name=%s WHERE id=%s",
                                (self.teachers_table.item(rowNum, 1).text(), id))
            self.cursor.execute("UPDATE teacher SET subject=%s WHERE id=%s",
                                (self.teachers_table.item(rowNum, 2).text(), id))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _change_day(self, rowNum):
        global day
        global week
        if self.monday_table.item(rowNum, 5).text() in Weeks:
            week = self.monday_table.item(rowNum, 5).text()
        if self.monday_table.item(rowNum, 1).text() in Days:
            day = self.monday_table.item(rowNum, 1).text()
        self.monday_table.setItem(rowNum, 1,
                                  QTableWidgetItem(''))
        self.monday_table.setItem(rowNum, 5,
                                  QTableWidgetItem(''))
        self._update_schedule()


    def _update_schedule(self):
        self._update_monday_table()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
