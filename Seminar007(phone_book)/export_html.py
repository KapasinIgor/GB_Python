from database import path


def create_html():
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '<table>'
    html += '<colgroup><col span="2" style="background:Khaki"><col style="background-color:LightCyan"></colgroup>'
    html += '<tr><th>Фамилия</th><th>Имя</th><th>Номер телефона</th></tr>'
    with open(path, 'r') as file:
        for line in file:
            temp = line.strip().split(' ')
            html += f'<tr><td>{temp[0]}</td><td>{temp[1]}</td><td>{temp[2]}</td></tr>'
    html += '</table>'
    html += '  </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)
