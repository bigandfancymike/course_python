# 1. Path.cwd() Повертає об'єкт Path, що представляє поточний робочий каталог.
# 2. Path.home() Повертає об'єкт Path, що представляє домашній каталог користувача.
# 3. Path.joinpath(*other) Об'єднує шляхи з поточним шляхом та повертає новий об'єкт Path. Може приймати один або кілька аргументів.
# 4. Path.exists() Перевіряє, чи існує файл або каталог за цим шляхом.
# 5. Path.is_dir() Перевіряє, чи є об'єкт каталогом.
# 6. Path.is_file() Перевіряє, чи є об'єкт файлом.
# 7. Path.mkdir(mode=0o777, parents=False, exist_ok=False) Створює новий каталог за цим шляхом.
# 8. Path.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None) Відкриває файл за цим шляхом та повертає файловий об'єкт.
# 9. Path.read_text(encoding=None, errors=None) Відкриває файл у текстовому режимі, читає його та повертає вміст як рядок.
# 10. Path.write_text(data, encoding=None, errors=None) Відкриває файл у текстовому режимі та записує в нього дані.
# 11. Path.unlink(missing_ok=False) Видаляє файл або символічне посилання.
# 12. Path.rename(target) Перейменовує файл або каталог на новий шлях або ім'я.
# 13. Path.resolve(strict=False) Перетворює шлях на абсолютний шлях, розв'язуючи будь-які символічні посилання.