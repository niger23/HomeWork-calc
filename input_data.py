from easygui import *
import easygui

def user_input():
    text = enterbox(msg='Введите выражение, которое будем считать!\n Для комплексного числа используем только i или j!', title=' ', default='', strip=True, image=None, root=None)
    return text
