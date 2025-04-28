from sqlite3 import Error
from database_connection import get_database_connection

class Scores:
    """Class for the game score database operations"""
    def __init__(self, mode):
        self._mode = mode
        self._db_connection = get_database_connection()
        self._cursor = self._db_connection.cursor()
        self._scores = []

    def get_all_scores(self):
        """Gets all scores from the database, sorts
           them by their score and returns them"""
        self._scores = self._scores_by_mode()
        self._sort_scores()
        complete_scores = []
        for s in self._scores:
            complete_scores.append(
                Score(
                    s[0],
                    s[1],
                    s[2]
                )
            )
        return complete_scores

    def add_new_score(self, name, score, mode):
        """Method for adding new score into the
           database"""
        try:
            Score(name, score, mode).add_new_score()
        except Error as e:
            print("Something went wrong: ", e)
            return False
        return True

    def _scores_by_mode(self):
        self._cursor.execute(
            """
            SELECT name, score, mode
            FROM scores
            WHERE mode = ?;
            """, (self._mode, ))

        return self._cursor.fetchall()

    def _sort_scores(self):
        self._scores = sorted(
            self._scores,
            key=lambda score: score[1],
            reverse=True
        )

class Score:
    """Class for the database score objects"""
    def __init__(self, name, score, mode):
        self.name = name
        self.score = int(score)
        self.mode = mode
        self._db_connection = get_database_connection()
        self._cursor = self._db_connection.cursor()

    def add_new_score(self):
        """Adds a new score into the database using
           the intialization details"""
        if not self._validate():
            raise ValueError("Name must be 1-20 characters long")
        self._cursor.execute("""
            INSERT INTO scores (name, score, mode)
            VALUES (?, ?, ?);
            """, (self.name, self.score, self.mode))
        self._db_connection.commit()

    def display(self):
        name_spaces = 23 - len(self.name)
        return f"{' ' * 11}{self.name}{name_spaces*' '}{self.score}"

    def _validate(self):
        if 0 < len(self.name) <= 20:
            return True
        return False
