import sqlite3

conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()
# Вопрос 1. Информация о скольких художниках представлена в базе данных? 
# cursor.execute('select * from artists')
# data = cursor.fetchall()
# conn.commit()
# cursor.execute('SELECT COUNT(*) FROM artists')
# cursor.execute('SELECT * FROM artists')
# print(len(cursor.fetchall()))
# conn.commit()

# Вопрос 2. Сколько женщин (Female) в базе?
# cursor.execute('SELECT COUNT(*) FROM artists WHERE Gender="Female"')
# print(cursor.fetchall())


# Вопрос 3. Сколько человек в базе данных родились до 1900 года?
# cursor.execute('SELECT COUNT(*) FROM artists WHERE "Birth Year" < 1900')
# print(cursor.fetchall())

# Вопрос 4*. Как зовут самого пожилого художника?
cursor.execute('SELECT * FROM artists ORDER BY "Birth Year"')
print(cursor.fetchall())