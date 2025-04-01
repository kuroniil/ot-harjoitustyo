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
