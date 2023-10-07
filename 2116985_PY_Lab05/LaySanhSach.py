import pyodbc

connectionString = '''DRIVER={ODBC Driver 18 for SQL Server};
                        SERVER=.;DATABASE=QLSinhVien;UID=sa;Encrypto=no'''

def get_connection():
    conn = pyodbc.connect('QLSinhVien.db')
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        select_query = """select + from Lop"""
        cursor.execute(select_query)
        record = cursor.fetchall()

        print(f"Danh sach cac lop la: ")
        for row in record:
            print("*"*50)
            print("Ma lop: ", row[0])
            print("Ten lop: ", row[1])
        
        close_connection(conn)
    except (Exception, pyodbc.Error) as error:
        print("Da co loi xay ra khi thuc thi. Thong tin loi: ", error)

get_all_class()

def get_class_by_id(class_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        select_query = "select + from Lop where id = ?"
        params = (class_id,)
        cursor.execute(select_query, params)

        record = cursor.fetchone()

        print(f"Thong tin lop co id = {class_id} la: ")
        print("Ma lop: ", record[0])
        print("Ten lop: ", record[1])

        close_connection(conn)
    except (Exception, pyodbc.Error) as error:
        print("Da co loi xay ra khi thuc thi. Thong tin loi: ", error)

get_class_by_id(1)