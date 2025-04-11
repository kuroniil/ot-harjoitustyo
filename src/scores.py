from sqlite3 import Error
from database_connection import get_database_connection

class Scores:
    def __init__(self, mode):
        self._mode = mode
        self._db_connection = get_database_connection()
        self._cursor = self._db_connection.cursor()
        self._scores = []

    def get_all_scores(self):
        self._scores = self._scores_by_mode()
        self._sort_scores()
        complete_scores = []
        for s in self._scores:
            complete_scores.append(Score(
                s[0],
                s[1],
                s[2]
            ))
        return complete_scores

    def _scores_by_mode(self):
        self._cursor.execute("""
                SELECT name, score, mode
                FROM scores
                WHERE mode = ?;
            """, (self._mode, ))

        return self._cursor.fetchall()

    def _sort_scores(self):
        self._scores = sorted(self._scores, key=lambda x: x[1], reverse=True)

    def add_new_score(self, name, score, mode):
        try:
            Score(name, score, mode).add_new_score()
        except Error as e:
            print("Something went wrong: ", e)
            return False
        return True

class Score:
    def __init__(self, name, score, mode):
        self.name = name
        self.score = int(score)
        self.mode = mode
        self._db_connection = get_database_connection()
        self._cursor = self._db_connection.cursor()

    def add_new_score(self):
        self._cursor.execute("""
            INSERT INTO scores (name, score, mode)
            VALUES (?, ?, ?);
            """, (self.name, self.score, self.mode))
        self._db_connection.commit()

    def display(self):
        name_spaces = 23 - len(self.name)
        return f"{' ' * 11}{self.name}{name_spaces*' '}{self.score}"
