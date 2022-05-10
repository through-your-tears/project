import sqlite3
import cgitb

from adapter import export_to_xml
from db import sqlite_connection

PATH = 'songs.xml'

cgitb.enable()

@sqlite_connection
def sql_to_xml(con: sqlite3.Connection):
    cur = con.cursor()
    cur.execute("select * from songs;")
    rows = cur.fetchall()
    export_to_xml(rows, PATH)


sql_to_xml()
print("Content-type: text/html")
print(f'''
            <!DOCTYPE html>
            <html lang="ru">
                <head>
                    <title>БД</title>
                    <meta charset="UTF-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                </head>
                <body>
                <h1>Экспорт БД в xml файл выполнен</h1><br>
                <a class="btn btn-success" href="../templates/index.html">На главную</a><br>
        </body>
        </html>

    ''')