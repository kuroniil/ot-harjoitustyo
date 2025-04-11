from sqlite3 import Error
from database_connection import get_database_connection

class DatabaseConnection:
    def __init__(self):
        self._connection = get_database_connection()
        self._cursor = self._connection.cursor()

    def _drop_tables(self):
        try:
            self._cursor.execute("DROP TABLE if exists scores;")
        except Error as e:
            print("dropping tables failed: ", e)
        self._connection.commit()

    def _create_tables(self):
        try:
            self._cursor.execute("""
                CREATE TABLE scores (
                id INTEGER PRIMARY KEY,
                score INTEGER,
                mode INTEGER,
                name TEXT)
                """)
        except Error as e:
            print("creating tables failed: ", e)
        self._connection.commit()

    def _prepopulate(self):
        data = [
         (1000, "aaa", 4), (2000, "bbb", 4),
         (3000, "ccc", 4), (4000, "ddd", 4),
         (5000, "eee", 4), (6000, "fff", 4)
        ]

        self._cursor.executemany("""
            INSERT INTO scores (score, name, mode)
            VALUES (?, ?, ?)
        """, data)
        self._connection.commit()

    def initialize_database(self):
        self._drop_tables()
        self._create_tables()
        self._prepopulate()

if __name__ == "__main__":
    db = DatabaseConnection()
    db.initialize_database()
    print("Database initialized")
