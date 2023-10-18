from PyQt6.QtWidgets import QMessageBox, QFileDialog
from datetime import datetime
import shutil
import random
import os


# Вивести QMessageBox
def show_message(win, title, message):
    m = QMessageBox(win)
    m.setWindowTitle(title)
    m.setText(message)
    m.exec()


# Створити новий архів
def create_arhive(path, win):
    try:
        # Переходимо у дерикторію, де знаходиться path,
        # для того щоб архів створився саме там
        p = os.path.dirname(path)
        os.chdir(p)
        print(os.getcwd())

        # Створюємо архів
        shutil.make_archive(
            base_name=f'Arhive{datetime.now()}',
            format='zip',
            base_dir=os.path.basename(path)
        )


    # Якщо виникла помилка
    except:
        text = 'Виникла помилка. Перевірте правильність ввода данних.'
        show_message(win=win, message=text, title='Помилка')


# Розпакувати архів
def unpack_arhive(path, win):
    try:
        # Переходимо у дерикторію, де знаходиться path,
        # для того щоб розпакований файл створився саме там
        p = os.path.dirname(path)
        os.chdir(p)

        # Архівація файлу/папки
        arhive_name = f'Unpack{random.randint(1, 500)}'
        shutil.unpack_archive(
            path,
            arhive_name,
            'zip'
    )

    # Якщо шлях невірний або виникла помилка
    except:
        text = 'Виникла помилка. Перевірте правильність ввода данних.'
        show_message(win=win, message=text, title='Помилка')


# Попросити користувача вибрати шлях до папки (використовується у app.py)
def get_path_to_folder(win):
    path = QFileDialog.getExistingDirectory(win,
                       'Виберіть папку',
                       '/')
    return path


# Попросити користувача вибрати шлях до файлу (використовується у app.py)
def get_path_to_file(win):
    path = QFileDialog.getOpenFileName(win,
                       'Виберіть файл',
                       '/')[0]
    return path


# Чи пуста строка (використовується у app.py)
def is_empty(string): return True if string.strip() else False
