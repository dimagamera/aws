from config import *


while True:

    q = int(input(
        "1. Вивiд всiх бакетiв 2. Вивiд бакета 3. Завантажити 4. Скачати 5. Створити віртуалку  6. Видалити віртуалку 7. Список віртуалок 8. Вихiд = > "))

    if q == 1:
        show_all_bucket()

    elif q == 2:
        view_bucket()

    elif q == 3:
        upload_bucket()

    elif q == 4:
        dowload_bucket()

    elif q == 5:
        create_instance()

    elif q == 6:
        Delete()

    elif q == 7:
        show()

    elif q == 8:
        break
