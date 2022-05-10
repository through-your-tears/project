import cgi
import cgitb
import html

from db import get_all_artists, add_album

cgitb.enable()

form = cgi.FieldStorage()
print("Content-type: text/html")
print(f'''
            <!DOCTYPE html>
            <html lang="ru">
                <head>
                    <title>Добавить песню</title>
                    <meta charset="UTF-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                </head>
                <body>
''')
if form:
    number_of_songs = form.getvalue('number')
    artist = form.getvalue('artist')
    name = html.escape(form.getvalue('name'))
    descr = html.escape(form.getvalue('descr'))

    add_album(
        number_of_songs=number_of_songs,
        artist_id=artist,
        name=name,
        descr=descr
    )
    print(f'''<h1>Альбом "{name}" добавлен </h1>''')

print('''
                <h1> Добавить альбом </h1>
                <form>
                     <label> Название альбома
                    <input type="text" name="name">
                    </label><br>
                    <label> Количество песен в альбоме
                    <input type="number" name="number"> 
                    </label><br>
                    <label> Выбрать исполнителя
                    <select name="artist">
                            ''')
for row in get_all_artists():
    print(f'<option value="{row[0]}">{row[1]}</option>')
print('''
                    </select>
                    </label><br>
                            ''')
print('''
                    <label> Описание
                    <textarea name="descr"></textarea>
                    </label><br>
                    <input class="btn btn-success" type="submit">
                    </form><br>
                    <a class="btn btn-success" href="../templates/index.html">На главную</a><br>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
                </body>
            </html>
            ''')

