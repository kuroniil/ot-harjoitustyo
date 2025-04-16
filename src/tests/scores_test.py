import unittest
from scores import Scores
from initialize_database import DatabaseConnection

class TestScores(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseConnection()
        self.db.initialize_database()
        self.scores = Scores(4)

    def test_adding_score(self):
        start_scores = self.scores.get_all_scores()
        self.scores.add_new_score("test123", 2562, 4)
        
        scores_after_adding = self.scores.get_all_scores()
        self.assertEqual(len(scores_after_adding), len(start_scores) + 1)
        
        score_names = list(map(lambda score: score.name, scores_after_adding))
        self.assertTrue("test123" in score_names)
