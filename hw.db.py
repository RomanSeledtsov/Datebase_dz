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
        sql = '''UPDATE products SET price = ?, quantity = ?
         WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)




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
        sql = '''SELECT * FROM products WHERE price = ?, quantity = ?'''
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
    # insert_products(my_connection, ('Лейка', 15, 15))
    # insert_products(my_connection, ('Губка', 30.15, 12))
    # insert_products(my_connection, ('Мыло банное', 45.50, 22))
    # insert_products(my_connection, ('Мыло хозяйственное', 17, 55))
    # insert_products(my_connection, ('Стекломой', 55.99, 10))
    # insert_products(my_connection, ('Туалетная бумага', 14, 34))
    # insert_products(my_connection, ('Зубная паста', 75, 8))
    # insert_products(my_connection, ('Стиральный порошок', 120, 19))
    # insert_products(my_connection, ('Коврик', 150.50, 3))
    # insert_products(my_connection, ('Зубная щётка', 60.50, 15))
    # insert_products(my_connection, ('WD-40', 90, 15))
    # insert_products(my_connection, ('Туалетный утенок', 120.50, 5))
    # insert_products(my_connection, ('Антинакипин', 32.00, 36))
    # insert_products(my_connection, ('Моющий порошок', 73.50, 20))
    # insert_products(my_connection, ('Гвозди', 3.50, 500))
    update_products(my_connection, (999.90, 22, 55))
    delite_products(my_connection, [48])
    # select_all_products(my_connection)
    # select_products_by_price(my_connection)
    select_products_by_name(my_connection, 'Мыло')

    my_connection.close()
