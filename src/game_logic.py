import numpy as np

class GameLogic:
    def __init__(self, grid_size):
        self._grid_size = grid_size
        self._grid = np.zeros((self._grid_size, self._grid_size), dtype=int)
        self._grid[2, 3], self._grid[3, 2] = 2, 2

    def move_up(self):
        self._move("up")

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def _move(self, direction, collisions_checked=False):
        match direction:
            case "up":
                for i in range(self._grid_size):
                    updated_column = list(self._grid[:, i])
                    j = 0
                    while j < (len(updated_column)):
                        if updated_column[j] == 0:
                            new_updated_column = updated_column.copy()
                            new_updated_column.append(new_updated_column.pop(j))
                            if new_updated_column != updated_column:
                                updated_column = new_updated_column.copy()
                                j -= 1
                        j += 1
                    self._grid[:, i] = updated_column

        if not collisions_checked:
            self._collisions(direction)
        else:
            self._add_piece()
                    
    def _collisions(self, direction):
        match direction:
            case "up":
                for i in range(self._grid_size):
                    updated_column = list(self._grid[:, i])
                    j = 0
                    while j < (len(updated_column) - 1):
                        if updated_column[j] == updated_column[j + 1]:
                            updated_column[j] *= 2
                            updated_column[j + 1] = 0
                            j += 1    
                        j += 1
                    self._grid[:, i] = updated_column

        self._move(direction, True)

    def _add_piece(self):
        """
        Add a piece to the grid. The piece will be
        a 2 or a 4 with 2 being more likely with a 
        probability of 0.9.
        """
        r_ind, c_ind = np.indices((self._grid_size, self._grid_size))
        indices_of_zeros = list(zip(r_ind[self._grid == 0],
                                    c_ind[self._grid == 0]))
        random_location = indices_of_zeros[np.random.choice(len(indices_of_zeros))]
        if np.random.uniform() < 0.9:
            self._grid[random_location] = 2
        else:
            self._grid[random_location] = 4

    def ret_grid(self):
        """returns the grid"""
        return self._grid
