import numpy as np

class Grid():
    """Class for handling the grid of the game and its
       operations. Takes as parameters the game that the
       grid is a part of, the size of the grid and optional
       starting point start_grid"""
    def __init__(self, game, size, start_grid=[]):
        self._game = game
        if len(start_grid) == 0:
            self._grid = np.zeros((size, size), dtype=int)
            self._grid[2, 3], self._grid[3, 2] = 2, 2
        else:
            self._grid = start_grid
        self._grid_before_move = self._grid
        self._size = size

    def add_piece(self):
        """Add a piece to the grid. The piece will be
        a 2 or a 4 with 2 being more likely with a 
        probability of 0.9"""
        indices_of_zeros = self.find_all_zeros()
        random_location = indices_of_zeros[np.random.choice(len(indices_of_zeros))]
        if np.random.uniform() < 0.9:
            self._grid[random_location] = 2
        else:
            self._grid[random_location] = 4

    def find_all_zeros(self):
        """"Return the indices of zeros from the grid"""
        r_ind, c_ind = np.indices((self._size, self._size))
        indices_of_zeros = list(zip(r_ind[self._grid == 0],
                                    c_ind[self._grid == 0]))
        return indices_of_zeros

    def ret_grid(self):
        """Returns the grid"""
        return self._grid

    def save_grid(self):
        """Forms the grid into a string
           that can be saved in the database"""
        return str(self._grid)

    def move(self, direction, collisions_checked=False):
        """Method for moving the grid into a direction.
           Along with the other internal methods, all
           zeros are moved in a direction, after which
           the collisions are checked. Next all zeros 
           are moved again and a new piece is added to
           the grid"""
        if not collisions_checked:
            self._grid_before_move = self._grid.copy()
        self._move_zeros(direction)
        if not collisions_checked:
            self._collisions(direction)
        else:
            grid_changed = self._grid != self._grid_before_move
            if grid_changed.any():
                self.add_piece()
            elif len(self.find_all_zeros()) == 0 and not self._game.simulate:
                self._game.simulate_game_over()
            elif len(self.find_all_zeros()) == 0 and self._game.simulate:
                self._game.game_over = True

    def _move_zeros(self, direction):
        if direction in set(("up", "left")):
            for i in range(self._size):
                updated = list(self._grid[:, i]) if direction == "up" else list(self._grid[i, :])
                self._move_zeros_right(updated, direction, i)

        elif direction in set(("down", "right")):
            for i in range(self._size):
                updated = list(self._grid[i, :]) if direction == "right" else list(self._grid[:, i])
                self._move_zeros_left(updated, direction, i)

    def _move_zeros_right(self, updated, direction, i):
        j = 0
        swaps = self._size - 1
        while j < (len(updated)):
            if updated[j] == 0 and swaps > 0:
                updated.append(updated.pop(j))
                j -= 1
                swaps -= 1
            j += 1
            if direction == "up":
                self._grid[:, i] = updated
            else:
                self._grid[i, :] = updated

    def _move_zeros_left(self, updated, direction, i):
        j = self._size - 1
        swaps = self._size - 1
        while j > 0:
            if updated[j] == 0 and swaps > 0:
                updated.insert(0, updated.pop(j))
                j += 1
                swaps -= 1
            j -= 1
        if direction == "down":
            self._grid[:, i] = updated
        else:
            self._grid[i, :] = updated

    def _collisions(self, direction):
        if direction in set(("up", "left")):
            for i in range(self._size):
                updated = list(self._grid[:, i]) if direction == "up" else list(self._grid[i, :])
                self._left_collisions(updated, direction, i)
        elif direction in set(("down", "right")):
            for i in range(self._size):
                updated = list(self._grid[i, :]) if direction == "right" else list(self._grid[:, i])
                self._right_collisions(updated, direction, i)

        self.move(direction, True)

    def _left_collisions(self, updated, direction, i):
        j = 0
        while j < (len(updated) - 1):
            if updated[j] == updated[j + 1]:
                self._game._score += updated[j]
                updated[j] *= 2
                updated[j + 1] = 0
                j += 1
            j += 1
            if direction == "up":
                self._grid[:, i] = updated
            else:
                self._grid[i, :] = updated

    def _right_collisions(self, updated, direction, i):
        j = len(updated) - 1
        while j > 0:
            if updated[j] == updated[j - 1]:
                self._game._score += updated[j]
                updated[j] *= 2
                updated[j - 1] = 0
                j -= 1
            j -= 1
        if direction == "down":
            self._grid[:, i] = updated
        else:
            self._grid[i, :] = updated
