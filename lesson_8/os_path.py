# 1. os.chdir(path) - Змінює поточний робочий каталог на вказаний шлях.
# 2. os.getcwd() - Повертає рядок, що представляє поточний робочий каталог.
# 3. os.listdir(path='.') - Повертає список усіх файлів та каталогів у вказаному каталозі.
# 4. os.mkdir(path, mode=0o777) - Створює каталог за вказаним шляхом.
# 5. os.makedirs(name, mode=0o777, exist_ok=False) - Рекурсивно створює каталоги вказані в шляху; створює всі проміжні каталоги,
# необхідні для створення кінцевого каталогу.
# 6. os.remove(path) - Видаляє файл за вказаним шляхом.
# 7. os.rename(src, dst) - Перейменовує файл або каталог з src на dst.
# 8. os.rmdir(path) - Видаляє пустий каталог.
# 9. os.removedirs(name) - Рекурсивно видаляє каталоги, закінчуючи вказаним іменем; продовжує видалення вгору по дереву, поки не зустріне непустий каталог.
# 10. os.system(command) - Виконує системну команду.
# 11. os.path.join(path, *paths) - Об'єднує один або декілька компонентів шляху з урахуванням особливостей операційної системи.
# 12. os.path.split(path) - Розділяє шлях на кортеж, що складається з двох частин: голови та хвоста, де хвіст - останній компонент шляху.
# 13. os.path.dirname(path) - Повертає директорію, що містить файл або кінцеву директорію в шляху.
# 14. os.path.basename(path) - Повертає базове ім'я шляху (останній компонент шляху).
# 15. os.path.exists(path) - Перевіряє, чи існує вказаний шлях або об'єкт.
# 16. os.path.isfile(path) - Перевіряє, чи є вказаний шлях файлом.
# 17. os.path.isdir(path) - Перевіряє, чи є вказаний шлях директорією.
# 18. os.getenv(key, default=None) - Повертає значення змінної оточення або default, якщо змінна не встановлена.
# 19. os.putenv(key, value) - Встановлює значення змінної оточення.
# 20. os.rename() - Зміна імена та можливість перести файл
# 21. os.replace()
# 22. os.path.abspath(path)


import os
#
#
# print(os.getcwd())
#
# print(os.chdir('../))

# print(os.listdir('./'))

# os.mkdir('temp/temp_1')

# os.rmdir()#для директорій
#
# os.remove() #для файликів
#
# os.unlink()

# os.removedirs('temp/temp1')

# PATH
#
# res = str(__file__)[::-1].split('/', 1)
# print(res[1][::-1])

# def install_app():
#     print('App is installing..')
#
# app_name = 'app.ipa'
# #download_app() we are gonna download to dir with our file
#
# dir_name = os.path.dirname(__file__)
#
# print('dir name: ', dir_name)
#
# full_path = os.path.join(dir_name, app_name)
#
# if os.path.exists(full_path):
#     install_app()
#
# else:
#     print('not found')

# def install_app():
#     print('App is installing..')
#
# dir_name = os.path.dirname(__file__)
#
# jks_file = os.path.join(dir_name, 'config.jsk')
# aab_file = os.path.join(dir_name, 'aab.jsk')
# apk_file = os.path.join(dir_name, 'apk.jsk')
#
#
# if os.path.exists(apk_file):
#     install_app()
# elif os.path.exists(aab_file):
#     print('Prepare app convert from aab to apk')
#     install_app()
# else:
#     print('Download aab')
#     print('Prepare app convert from aab to apk')
#     install_app()


# print(os.getenv('key'))
#
# print(os.putenv('key', 'value'))
#
# print(os.getenv('key'))

# print(list(os.walk(os.path.dirname(__file__))))

# for dirpath, dirnames, filenames in os.walk('../../'):
#     if 'venv' not in dirpath:
#         print(dirpath)
#         print(dirnames)
#         print(filenames)