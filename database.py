import psycopg2
from config import host, database, user, password


connection = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)


with connection:
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS birthdays (
        id SERIAL,
        name TEXT,
        month INTEGER,
        day INTEGER
        )
    ''')


def get_all_birthdays():
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, month, day FROM birthdays")
        return cursor.fetchall()


def add_entry(name, month, day):
    with connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO birthdays (name, month, day) VALUES (%s, %s, %s)
        ''', (name, month, day))
    

def remove_birthday(id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(''' DELETE FROM birthdays WHERE id = %s
        ''', (id, ))
        
# print(remove_birthday('1'))
# print(get_all_birthdays())
