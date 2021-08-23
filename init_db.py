# import sqlite3

# connection = sqlite3.connect('database.db')

# with open('schema.sql') as f:
#     connection.executescript(f.read())

# connection.commit()
# connection.close()


from sqlite3 import OperationalError
import sqlite3

#Assuming urls.db is in your app root folder
create_table = """
    CREATE TABLE WEB_URL(
    id INTEGER PRIMARY KEY     AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    original_url  TEXT    NOT NULL
    );
    """
with sqlite3.connect('urls.db') as conn:
    cursor = conn.cursor()
    try:
        cursor.execute(create_table)
    except OperationalError as e:
        print(e)