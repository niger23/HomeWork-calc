from easygui import *
import easygui

def user_input_ration():
    text = enterbox(msg='Введите выражение, которое будем считать!', title=' ', default='', strip=True, image=None, root=None)
    return text

def user_input_complex():
    text = enterbox(msg='Введите выражение, которое будем считать!\n Для комплексного числа используем только i или j!', title=' ', default='', strip=True, image=None, root=None)
    return text