import unittest
from src.analysis import analyze_section_performance, analyze_overall_performance

class TestAnalysisFunctions(unittest.TestCase):
    def test_analyze_section_performance(self):
        section = {
            "questions": [
                {"timeTaken": 120, "status": "answered", "markedOptions": [{"isCorrect": True}]},
                {"timeTaken": 150, "status": "answered", "markedOptions": [{"isCorrect": False}]},
                {"timeTaken": 200, "status": "notAnswered", "markedOptions": []},
            ]
        }
        result = analyze_section_performance(section)
        self.assertEqual(result["total_questions"], 3)
        self.assertEqual(result["correct_answers"], 1)
        self.assertEqual(result["incorrect_answers"], 1)
        self.assertEqual(result["not_answered"], 1)
        self.assertEqual(result["accuracy"], 0.5)

    def test_analyze_overall_performance(self):
        test = {
            "sections": [
                {"questions": [{"timeTaken": 120, "status": "answered", "markedOptions": [{"isCorrect": True}]}]},
                {"questions": [{"timeTaken": 150, "status": "answered", "markedOptions": [{"isCorrect": False}]}]},
            ]
        }
        result = analyze_overall_performance(test)
        self.assertEqual(result["total_questions"], 2)
        self.assertEqual(result["total_correct_answers"], 1)
        self.assertEqual(result["total_incorrect_answers"], 1)
        self.assertEqual(result["overall_accuracy"], 0.5)

if __name__ == "__main__":
    unittest.main()
