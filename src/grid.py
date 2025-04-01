import numpy as np

class Grid():
    def __init__(self, game, size, start_grid):
        self._game = game
        if len(start_grid) == 0:
            self._grid = np.zeros((size, size), dtype=int)
            self._grid[2, 3], self._grid[3, 2] = 2, 2
        else:
            self._grid = start_grid
        self._grid_before_move = self._grid
        self._size = size

    def add_piece(self):
        """
        Add a piece to the grid. The piece will be
        a 2 or a 4 with 2 being more likely with a 
        probability of 0.9.
        """
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

    def move(self, direction, collisions_checked=False):
        if not collisions_checked:
            self._grid_before_move = self._grid.copy()
        match direction:
            case "up":
                for i in range(self._size):
                    updated_column = list(self._grid[:, i])
                    j = 0
                    swaps = self._size - 1
                    while j < (len(updated_column)):
                        if updated_column[j] == 0 and swaps > 0:
                            updated_column.append(updated_column.pop(j))
                            j -= 1
                            swaps -= 1
                        j += 1
                    self._grid[:, i] = updated_column
            case "right":
                for i in range(self._size):
                    updated_row = list(self._grid[i, :])
                    j = self._size - 1
                    swaps = self._size - 1
                    while j > 0:
                        if updated_row[j] == 0 and swaps > 0:
                            updated_row.insert(0, updated_row.pop(j))
                            j += 1
                            swaps -= 1
                        j -= 1
                    self._grid[i, :] = updated_row
            case "left":
                for i in range(self._size):
                    updated_row = list(self._grid[i, :])
                    j = 0
                    swaps = self._size - 1
                    while j < (len(updated_row)):
                        if updated_row[j] == 0 and swaps > 0:
                            updated_row.append(updated_row.pop(j))
                            j -= 1
                            swaps -= 1
                        j += 1
                    self._grid[i, :] = updated_row
            case "down":
                for i in range(self._size):
                    updated_column = list(self._grid[:, i])
                    j = self._size - 1
                    swaps = self._size - 1
                    while j > 0:
                        if updated_column[j] == 0 and swaps > 0:
                            updated_column.insert(0, updated_column.pop(j))
                            j += 1
                            swaps -= 1
                        j -= 1
                    self._grid[:, i] = updated_column

        if not collisions_checked:
            self._collisions(direction)
        else:
            # Don't even try to add piece if the move doesn't change the grid
            grid_changed = self._grid != self._grid_before_move
            if grid_changed.any():
                self.add_piece()
            elif len(self.find_all_zeros()) == 0 and not self._game.simulate:
                # Simulate if the game is actually over
                self._game.simulate_game_over()
            elif len(self.find_all_zeros()) == 0 and self._game.simulate:
                self._game.game_over = True

    def _collisions(self, direction):
        match direction:
            case "up":
                for i in range(self._size):
                    updated_column = list(self._grid[:, i])
                    j = 0
                    while j < (len(updated_column) - 1):
                        if updated_column[j] == updated_column[j + 1]:
                            self._game._score += updated_column[j]
                            updated_column[j] *= 2
                            updated_column[j + 1] = 0
                            j += 1
                        j += 1
                    self._grid[:, i] = updated_column
            case "right":
                for i in range(self._size):
                    updated_row = list(self._grid[i, :])
                    j = len(updated_row) - 1
                    while j > 0:
                        if updated_row[j] == updated_row[j - 1]:
                            self._game._score += updated_row[j]
                            updated_row[j] *= 2
                            updated_row[j - 1] = 0
                            j -= 1
                        j -= 1
                    self._grid[i, :] = updated_row
            case "left":
                for i in range(self._size):
                    updated_row = list(self._grid[i, :])
                    j = 0
                    while j < len(updated_row) - 1:
                        if updated_row[j] == updated_row[j + 1]:
                            self._game._score += updated_row[j]
                            updated_row[j] *= 2
                            updated_row[j + 1] = 0
                            j += 1
                        j += 1
                    self._grid[i, :] = updated_row
            case "down":
                for i in range(self._size):
                    updated_column = list(self._grid[:, i])
                    j = len(updated_column) - 1
                    while j > 0:
                        if updated_column[j] == updated_column[j - 1]:
                            self._game._score += updated_column[j]
                            updated_column[j] *= 2
                            updated_column[j - 1] = 0
                            j -= 1
                        j -= 1
                    self._grid[:, i] = updated_column

        self.move(direction, True)
