from sqlite3 import Error
from time import asctime
from database_connection import get_database_connection

class DatabaseConnection:
    """Class for handling initializing the database"""
    def __init__(self):
        self._connection = get_database_connection()
        self._cursor = self._connection.cursor()

    def initialize_database(self):
        """Method that initializes the database by
           first dropping tables, then creating them
           and prepopulating them with data"""
        self._drop_tables()
        self._create_tables()
        self._prepopulate()


    def _drop_tables(self):
        try:
            self._cursor.executescript("""
                DROP TABLE if exists scores;
                DROP TABLE if exists games;
                """)
        except Error as e:
            print("dropping tables failed: ", e)
        self._connection.commit()

    def _create_tables(self):
        try:
            self._cursor.executescript("""
                CREATE TABLE scores (
                id INTEGER PRIMARY KEY,
                score INTEGER,
                mode INTEGER,
                name TEXT
                );
                
                CREATE TABLE games (
                id INTEGER PRIMARY KEY,
                score INTEGER,
                mode TEXT,
                grid TEXT,
                time TEXT
                );
            """)
        except Error as e:
            print("creating tables failed: ", e)
        self._connection.commit()

    def _prepopulate(self):
        self._prepopulate_scores()
        self._prepopulate_games()

    def _prepopulate_games(self):
        grid1 = """
            [[ 2  0  0  0]
            [ 4  4  0  2]
            [32 16  2  0]
            [ 8 64 16  4]]
        """
        grid2 = """
            [[ 2  0  0  0  0]
            [ 8  2  0  0  0]
            [ 4  2  4  0  0]
            [32  4  0  0  0]
            [32 64 16  8  4]]
        """

        data = [
         (1000, grid1, 4, asctime()), (2000, grid2, 5, asctime()),
         (3000, grid1, 4, asctime()), (4000, grid2, 5, asctime()),
         (5000, grid1, 4, asctime())
        ]

        self._cursor.executemany("""
            INSERT INTO games (score, grid, mode, time)
            VALUES (?, ?, ?, ?)
        """, data)
        self._connection.commit()


    def _prepopulate_scores(self):
        data = [
         (1000, "aaa", 4), (2000, "bbb", 4),
         (3000, "ccc", 4), (4000, "ddd", 4),
         (5000, "eee", 4), (6000, "fff", 4),
         (7000, "ggg", 5), (8000, "hhh", 5)
        ]

        self._cursor.executemany("""
            INSERT INTO scores (score, name, mode)
            VALUES (?, ?, ?)
        """, data)
        self._connection.commit()

if __name__ == "__main__":
    db = DatabaseConnection()
    db.initialize_database()
    print("Database initialized")
