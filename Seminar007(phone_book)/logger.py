import os
from datetime import datetime


def status_log(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.txt', 'a+') as log:
        log.write(f"{[time]} - {data}\n")


def clear_log():
    os.remove('log.txt')
    with open('log.txt', 'w') as log:
        log.write("")
