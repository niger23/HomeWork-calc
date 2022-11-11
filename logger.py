from datetime import datetime as dt

def logger(data):
    time = dt.now().strftime('%H:%M')
    with open('Seminars\Seminar007\calc\log.csv', 'a') as file:
        file.write(''.format(time, data))