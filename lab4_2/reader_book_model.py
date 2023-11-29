import pandas as pd
def get_reader(conn):
    return pd.read_sql("SELECT * FROM reader", conn)
def get_book_reader(conn, id):
    return pd.read_sql('''
    SELECT title AS "Название", GROUP_CONCAT(author_name) AS "Авторы", 
    borrow_date AS "Дата_выдачи", return_date AS "Дата_возврата" FROM book_reader
    JOIN book ON book.book_id = book_reader.book_id
    JOIN book_author ON book_author.book_id = book.book_id
    JOIN author ON author.author_id = book_author.author_id
    WHERE reader_id = '''+str(id)
    +'''\nGROUP BY book.book_id, borrow_date, return_date
    ORDER BY title''', conn)
#
#
#