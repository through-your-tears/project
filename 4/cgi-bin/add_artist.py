import cgi
import cgitb
import html

from db import get_all_countries, add_artist

cgitb.enable()

form = cgi.FieldStorage()
print("Content-type: text/html")
print(f'''
            <!DOCTYPE html>
            <html lang="ru">
                <head>
                    <title>Добавить Исполнителя</title>
                    <meta charset="UTF-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                </head>
                <body>
''')
if form:
    name = html.escape(form.getvalue('name'))
    country = form.getvalue('country')

    add_artist(
        name=name,
        country_id=country
    )
    print('''<h1>Исполнитель(группа) добавлен </h1>''')

print('''
                <h1> Добавить исполнителя(группу) </h1>
                <form>
                    <label> Имя исполнителя(название группы)
                    <input type="text" name="name">
                    </label><br>
                    <label> Выбрать страну 
                    <select name="country">''')
for row in get_all_countries():
    print(f'<option value="{row[0]}">{row[1]}</option>')
print('''
                    </select>
                    </label><br>
                    <input class="btn btn-success" type="submit">
                    </form><br>
                    <a class="btn btn-success" href="../templates/index.html">На главную</a><br>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
                </body>
            </html>
            ''')

