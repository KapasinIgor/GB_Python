import os
import logger

path = "phone_book.csv"


def clear_db():
    os.remove(path)
    with open(path, 'w') as db:
        db.write("")
    logger.status_log("- Очистка базы данных")

