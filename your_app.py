# your_app.py
import mysql.connector

# Здесь параметры подключения к базе данных (замените на свои)
DB_HOST = "3306"  # Или IP-адрес, если MySQL в другом контейнере/машине
DB_NAME = "bddjango"
DB_USER = "root"
DB_PASSWORD = "1234" # **Обязательно измените!**

try:
    # Устанавливаем соединение с базой данных
    mydb = mysql.connector.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    # Создаём курсор (позволяет выполнять SQL-запросы)
    mycursor = mydb.cursor()

    # Пример SQL-запроса (выборка данных из таблицы)
    mycursor.execute("SELECT * FROM users")

    # Получаем результаты запроса
    myresult = mycursor.fetchall()

    # Выводим результаты
    for row in myresult:
        print(row)

    # Пример SQL-запроса (вставка данных)
    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    val = ("NewUser", "new.user@example.com")
    mycursor.execute(sql, val)

    # Подтверждаем изменения в базе данных (commit)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Закрываем курсор и соединение
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()