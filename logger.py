from datetime import datetime as dt

def logger(data, result):
    time = dt.now().strftime('%H:%M')
    with open('logs.csv', 'a') as file:
        file.write('{} has been completed {} with the result {}\n'.format(time, data, result))