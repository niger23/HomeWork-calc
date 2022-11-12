from easygui import *
import easygui
import os

import input_data as id
import calc_complex as cc
import calc_ration as cr
import logger as log
import user_interface as ui

def interface():
    choise_user = buttonbox(msg='Введите:\nComplex - для решения с комплексными числами, \nRational - для решения с рациональными числами, \nLogs - для просмотра логов, \nExit - если хотите выйти', title="Выберите что будем делать!", choices=('Complex', 'Rational', 'Logs', 'Exit'),)
    print(choise_user)

    if choise_user == 'Complex':
        data = id.user_input()
        result = cc.test(data)
        log.logger(data, result)
        msgbox(f'{data} = {result}', 'Выполнено решение')
        ui.interface()

    elif choise_user == 'Rational':
        data = id.user_input()
        result = cr.simple_calc(data)
        log.logger(data, result)
        msgbox(f'{data} = {result}', 'Выполнено решение')
        ui.interface()

    elif choise_user == 'Logs':
        file_path = 'logs.csv'
        with open(file_path) as f:
            title = os.path.basename(file_path)
            msg = 'Содержимое файла [% s] выглядит следующим образом:' % title
            text = f.read()
            easygui.textbox(msg, title, text)

    elif choise_user == 'Exit':
        msgbox('Возвращайтесь поскорее, мы будем скучать)', 'Выход')
        exit()

interface()