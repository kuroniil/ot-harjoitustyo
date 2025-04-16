from sqlite3 import Error
from time import asctime
import numpy as np
from database_connection import get_database_connection

class Games:
    """Class for interacting with the database for
       tasks such as getting games from the database
       and adding new games into the database"""
    def __init__(self, mode):
        self._mode = mode
        self._db_connection = get_database_connection()
        self._cursor = self._db_connection.cursor()
        self._games = []

    def get_all_games(self):
        """Gets all games by mode from the database
          and returns them as Game objects sorted by id"""
        self._games = self._games_by_mode()
        complete_games = []
        for g in self._games:
            complete_games.append(
                Game(
                    g[0],
                    g[1],
                    g[2],
                    g[3],
                    g[4]
                )
            )
        return sorted(complete_games, key=lambda g: g.id, reverse=True)

    def _games_by_mode(self):
        self._cursor.execute("""
            SELECT score, grid, mode, time, id
            FROM games
            WHERE mode = ?;
            """, (self._mode, ))
        return self._cursor.fetchall()

    def add_new_game(self, score, grid, mode):
        """Tries to add a new game into the database,
           returns True if succesful, returns False
           otherwise"""
        try:
            Game(score, grid, mode).add_new_game()
        except Error as e:
            print("Something went wrong: ", e)
            return False
        return True

    def get_game_by_id(self, game_id):
        self._cursor.execute("""
            SELECT score, grid, mode, time, id
            FROM games
            WHERE id = ?;
            """, (game_id, ))
        game = Game(*self._cursor.fetchone())
        return game.details()

class Game:
    """Class for database game objects"""
    def __init__(self, score, grid, mode, creation_time=None, game_id=-1):
        self.grid = grid
        self.score = int(score)
        self.mode = mode
        self._time = creation_time
        if creation_time is None:
            self._time = asctime()
        self.id = game_id
        self._db_connection = get_database_connection()
        self._cursor = self._db_connection.cursor()

    def add_new_game(self):
        """Method for adding a game into the database
           after initialization"""
        self._cursor.execute("""
            INSERT INTO games (score, grid, mode, time)
            VALUES (?, ?, ?, ?)
            RETURNING id
            """, (self.score, self.grid, self.mode, self._time))
        self.id = self._cursor.fetchone()[0]
        self._db_connection.commit()

    def details(self):
        """Returns all the details of the object
           as a dictionary"""
        return {
            "grid": self._parse_grid(),
            "score": self.score,
            "mode": self.mode,
            "time": self._time,
            "id": self.id
        }

    def _parse_grid(self):
        """Method for parsing the string grid of a saved
           game stored in the database and returning it as
           a numpy array"""
        res = []
        i = 0
        while i < len(self.grid):
            curr_number = ""
            if self.grid[i].isdigit():
                curr_number += self.grid[i]
                while i + 1 < len(self.grid) and self.grid[i + 1].isdigit():
                    i += 1
                    curr_number += self.grid[i]
            i += 1
            if curr_number != "":
                res.append(int(curr_number))
        return np.array(res).reshape(int(self.mode), int(self.mode))

    def display(self):
        time_spaces = 42 - len(self._time)
        return f" {self._time}{time_spaces*' '}{self.score}"
