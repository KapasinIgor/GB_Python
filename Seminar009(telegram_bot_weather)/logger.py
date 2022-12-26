from datetime import datetime


def add_log(operation, summary):
    time = datetime.now().strftime('%m.%d.%Y - %H:%M')
    with open('log.txt', 'a+') as log:
        log.write(f"{[time]} - {operation}\n{summary}\n")
