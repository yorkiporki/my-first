# Create your models here.
import pyodbc as odbc

def querySql():
    # 定義資料庫連線參數
    driver_name='SQL SERVER'
    server_name='ROG8\MSSQLS'
    database_name='DBF1225'

    # 建立連線字串
    connection_string=f"""
    DRIVER={driver_name};
    SERVER={server_name};
    DATABASE={database_name};
    Trust_Connection=yes;
    """
    # 使用 pyodbc 進行資料庫連線
    conn=odbc.connect(connection_string,autocommit=True)

    # 建立游標物件
    cursor=conn.cursor()

    SQLcmd = "select * from customer_order_record"
    Record = conn.execute(SQLcmd)
    List1 = list(Record.fetchall())
    temp = ""
    for row in List1:
        for col in row:
            temp += col
            temp += "  "
        temp += '/n'
            
    return (temp)
    Record.close()

    conn.close()
