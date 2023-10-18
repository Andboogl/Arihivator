from about_win.about_win_design import AboutWinWidgets
from PyQt6 import QtWidgets


# Вікно 'Про программу'
class AboutWin(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        # Додаємо віджети
        self.widgets = AboutWinWidgets()
        self.widgets.setupUi(win=self)

        # Налаштовуємо вікно так, щоб не можна було змінювати його розмір
        self.setFixedSize(426, 215)
