import unittest
import numpy as np
from game_logic import GameLogic

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic(4)    
        np.random.seed(1)

    def test_game_creates_correct_grid(self):
        correct_grid = np.array([[0,0,0,0],
                                 [0,0,0,0],
                                 [0,0,0,2],
                                 [0,0,2,0]], dtype=int)
        
        equal_values = self.game.grid.ret_grid() == correct_grid
        self.assertTrue(equal_values.all())
        self.assertEqual(self.game.grid.ret_grid().shape, correct_grid.shape)

    def test_game_move_up_works_correctly(self):
        self.game.move_up()
        
        correct_grid = np.array([[0,0,2,2],
                                 [0,0,0,4],
                                 [0,0,0,0],
                                 [0,0,0,0]], dtype=int)
        
        equal_values = self.game.grid.ret_grid() == correct_grid
        self.assertTrue(equal_values.all())

    def test_game_move_down_works_correctly(self):
        self.game.move_down()
        
        correct_grid = np.array([[0,0,0,0],
                                 [0,4,0,0],
                                 [0,0,0,0],
                                 [0,0,2,2]], dtype=int)
        equal_values = self.game.grid.ret_grid() == correct_grid
        self.assertTrue(equal_values.all())

    def test_game_move_right_works_correctly(self):
        self.game.move_right()
        
        correct_grid = np.array([[0,0,0,0],
                                 [0,4,0,0],
                                 [0,0,0,2],
                                 [0,0,0,2]], dtype=int)
        equal_values = self.game.grid.ret_grid() == correct_grid
        self.assertTrue(equal_values.all())

    def test_game_move_left_works_correctly(self):
        self.game.move_left()
        
        correct_grid = np.array([[0,0,0,0],
                                 [0,4,0,0],
                                 [2,0,0,0],
                                 [2,0,0,0]], dtype=int)
        equal_values = self.game.grid.ret_grid() == correct_grid
        self.assertTrue(equal_values.all())

    def test_starting_with_saved_grid_works(self):
        start_grid = np.array([[0,   0,    0,  0],
                               [0,   4,    4,  8],
                               [2,   256,  16, 0],
                               [512, 1024, 32, 4]], dtype=int)

        correct_grid = np.array([[0,   0,    0,  0],
                                 [0,   4,    4,  4],
                                 [2,   256,  16, 8],
                                 [512, 1024, 32, 4]], dtype=int)
        game = GameLogic(4, start_grid, 0)
        game.move_down()
        equal_values = game.grid.ret_grid() == correct_grid
        self.assertTrue(equal_values.all())
