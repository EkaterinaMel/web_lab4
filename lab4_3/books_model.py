import pandas as pd
def get_price(conn):
    return pd.read_sql("SELECT DISTINCT price FROM book\nORDER BY price", conn)
def get_amount(conn):
    return pd.read_sql("SELECT DISTINCT amount FROM book\nORDER BY amount", conn)
def get_books(conn, amount, min_price, max_price):
    return pd.read_sql('''
    SELECT title AS "Название", name_author AS "Автор", name_genre AS "Жанр", amount AS "Количество", price AS "Цена"
    FROM book
    JOIN author ON author.author_id = book.author_id
    JOIN genre ON genre.genre_id = book.genre_id
    WHERE amount > '''+str(amount)+''' AND 
    (price >= '''+str(min_price)+''' AND price <= '''+str(max_price)+''')
    ORDER BY title, name_author
    ''', conn)