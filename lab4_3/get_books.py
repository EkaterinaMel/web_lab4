from jinja2 import Template
import sqlite3
from books_model import *

amount = 6
min_price = 460
max_price = 570.2
# устанавливаем соединение с базой данных
conn = sqlite3.connect("store")

df_books = get_books(conn, amount, min_price, max_price)
df_price = get_price(conn)
df_amount = get_amount(conn)

# закрываем соединение с базой
conn.close()

f_template = open('books_templ.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
# создаем объект-шаблон
template = Template(html)
# генерируем результат на основе шаблона
result_html = template.render(
    books = df_books,
    amount = amount,
    min_price = min_price,
    max_price = max_price,
    df_price = df_price,
    df_amount = df_amount
)
#создаем файл для HTML-страницы
f = open('books.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()