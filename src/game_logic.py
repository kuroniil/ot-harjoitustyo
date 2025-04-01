from grid import Grid

class GameLogic:
    def __init__(self, grid_size, start_grid=[], simulate=False):
        self._grid_size = grid_size
        self.grid = Grid(self, self._grid_size, start_grid)
        self._score = 0
        self.game_over = False
        self.simulate = simulate

    def move_up(self):
        self.grid.move("up")

    def move_down(self):
        self.grid.move("down")

    def move_left(self):
        self.grid.move("left")

    def move_right(self):
        self.grid.move("right")

    def simulate_game_over(self):
        illegal_moves = 0
        for move_direction in ["left", "right", "up", "down"]:
            curr_grid = self.grid.ret_grid().copy()
            game_simulation = GameLogic(self._grid_size, curr_grid, True)
            game_simulation.grid.move(move_direction)
            illegal_moves += game_simulation.ret_game_over()
        if illegal_moves == 4:
            self.game_over = True

    def ret_score(self):
        """Returns the current score"""
        return self._score

    def ret_game_over(self):
        """Returns true if game is over, false otherwise"""
        return self.game_over
