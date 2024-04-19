import sqlite3


def create_connection(hw_bd):
    conn = None
    try:
        conn = sqlite3.connect(hw_bd)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_products(connection, products):
    try:
        sql = '''INSERT INTO products
                 (product_title, price, quantity)
                 VALUES (?, ?, ?)
              '''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products(connection, products):
    try:
        sql = '''UPDATE products SET quantity = ?, price = ?
         WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


# def delite_products(connection, products_id):
#     try:
#         sql = '''DELETE FROM products WHERE id = ?'''
#         cursor = connection.cursor()
#         cursor.execute(sql, products_id)
#         connection.commit()
#     except sqlite3.Error as e:
#         print(e)


def delite_products(connection, products_id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products_id)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_price(connection):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 and quantity > 5'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(e)


def select_products_by_name(connection, name):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + name + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(e)


sql_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

my_connection = create_connection("hw.db")
if my_connection:
    print("Connected.")
    # create_table(my_connection, sql_products_table)
    # insert_products(my_connection, ('Молоко', 60.50, 15))
    # insert_products(my_connection, ('Кефирfsdf', 60.50, 15))
    # insert_products(my_connection, ('Кефир', 60.50, 15))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # insert_products(my_connection, ('Кумыс', 150.50, 3))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # insert_products(my_connection, ('Сыр', 60.50, 15))
    # update_products(my_connection, (75.90, 34, 1))
    # delite_products(my_connection, [1])
    # select_all_products(my_connection)
    # select_products_by_price(my_connection)
    select_products_by_name(my_connection, 'Кумыс')

    my_connection.close()
