import sqlite3

def get_connection():
    connection = sqlite3.connect('QLSinhVien.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select sqlite_version();")
        db_version = cursor.fetchone()
        print("Ban dang su dung SQLite phien ban: ", db_version)
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Da co loi xay ra. Thong tin loi: ", error)

read_database_version()