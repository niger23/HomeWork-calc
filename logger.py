from datetime import datetime as dt

def logger(data, result):
    time = dt.now().strftime('%H:%M')
    with open('logs.csv', 'a') as file:
        file.write('{} has been completed {} with the result {}\n'.format(time, data, result))

def log_user_join():
    time = dt.now().strftime('%H:%M')
    with open('logs.csv', 'a') as file:
        file.write('{} user join selection menu\n'.format(time))

def log_user_choise(data):
    time = dt.now().strftime('%H:%M')
    with open('logs.csv', 'a') as file:
        file.write('{} user choise [{}] in selection menu\n'.format(time, data))

def log_error(error):
    time = dt.now().strftime('%H:%M')
    with open('logs.csv', 'a') as file:
        file.write('{} the user has an error: {}\n'.format(time, error))