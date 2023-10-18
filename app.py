from about_win import AboutWin
from main_win import MainWinWidgets
from PyQt6.QtCore import QSize
from PyQt6 import QtWidgets
from sys import argv
import functions


# Головне вікно 
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.widgets = MainWinWidgets()
        self.widgets.setupUi(win=self)

        # Налаштовуємо вікно так, щоб не можно було зміняти його розмір
        self.setFixedSize(QSize(637, 357))

        # Налаштування дій для кнопок
        self.widgets.about.clicked.connect(self.open_about_win)
        self.widgets.quick.clicked.connect(quit)
        self.widgets.create_arhive_btn.clicked.connect(self.new_arhive)
        self.widgets.unpack_arhive_btn.clicked.connect(self.unpack_arhive)
        self.widgets.chose_path_to_file.clicked.connect(self.get_path_to_file)
        self.widgets.chose_path_to_folder.clicked.connect(self.get_path_to_folder)

        self.path_file = None
        self.path_folder = None


    def open_about_win(self):
        self.win = AboutWin()
        self.win.show()
    

    # Получити шлях до файлу
    def get_path_to_file(self):
        self.path_file = functions.get_path_to_file(win=self)
        self.widgets.path_to_pack.setText(self.path_file)
        self.widgets.path_to_unpack.setText(self.path_file)
    

    # Получити шлях до папки
    def get_path_to_folder(self):
        self.path_folder = functions.get_path_to_folder(win=self)
        self.widgets.path_to_pack.setText(self.path_folder)
        self.widgets.path_to_unpack.setText(self.path_folder)


    # Створення нового архіва
    def new_arhive(self):
        # Отримуємо данні з віджета
        path = self.widgets.path_to_pack.text()

        # Якщо данні з віджета це не пуста строка
        if functions.is_empty(path):
            functions.create_arhive(path=path, win=self)
        
        else:
            text = 'Ви не вказали шлях до папки або файлу, яку треба запакувати'
            functions.show_message(win=self, title='Невірні данні', message=text)
    

    # Розпакування архіва
    def unpack_arhive(self):
        # Отримання данних з віджета
        path = self.widgets.path_to_unpack.text()

        # Якщо данні з віджета це не пуста строка
        if functions.is_empty(path):
            functions.unpack_arhive(path=path, win=self)
        
        else:
            text = 'Ви не вказали шлях до папки або файлу, яку треба розпакувати'
            functions.show_message(win=self, title='Невірні данні', message=text)


# Запуск программи
def start():
    app = QtWidgets.QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()
