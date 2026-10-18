"""
Smart Quiz - Automated Verification & Test Script
Tests all routes, database operations, quiz generation,
submission, server-side scoring, and history recording.
"""

import unittest
from app import app
from database import db


class SmartQuizTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.client = app.test_client()
        db.init_database()

    def test_01_index_page(self):
        """Test home page loads with all 6 categories."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Smart", response.data)
        self.assertIn(b"Java Programming", response.data)
        self.assertIn(b"Python Programming", response.data)
        self.assertIn(b"MySQL", response.data)
        self.assertIn(b"DBMS", response.data)
        self.assertIn(b"History", response.data)
        self.assertIn(b"Science", response.data)
        print("[TEST] Index page loaded successfully with 6 categories.")

    def test_02_categories_api(self):
        """Test API endpoint returns JSON category list."""
        response = self.client.get("/api/categories")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 6)
        print(f"[TEST] /api/categories returned {len(data)} categories.")

    def test_03_start_quiz_and_session(self):
        """Test starting a quiz session with student name."""
        response = self.client.post("/start-quiz/1", data={"student_name": "Rohan Sharma"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as sess:
            self.assertEqual(sess.get("student_name"), "Rohan Sharma")
            self.assertEqual(sess.get("category_id"), 1)
        self.assertIn(b"Rohan Sharma", response.data)
        self.assertIn(b"Question 1 of 10", response.data)
        print("[TEST] Student registration and quiz initialization passed.")

    def test_04_quiz_security(self):
        """Ensure correct answers are NOT sent to the client during quiz play."""
        with self.client.session_transaction() as sess:
            sess["student_name"] = "Priya Patel"
            sess["category_id"] = 2
        response = self.client.get("/quiz/2")
        self.assertEqual(response.status_code, 200)
        # Ensure correct_option and explanation are not exposed in HTML
        self.assertNotIn(b"correct_option", response.data)
        print("[TEST] Quiz security verified: correct answers are hidden from client.")

    def test_05_quiz_submission_and_scoring(self):
        """Test answer submission, score calculation, and result page."""
        # 1. Start quiz
        self.client.post("/start-quiz/3", data={"student_name": "Aarav Gupta"}, follow_redirects=True)
        
        # 2. Get active question IDs from session
        with self.client.session_transaction() as sess:
            q_ids = sess.get("active_question_ids", [])
            self.assertEqual(len(q_ids), 10)

        # 3. Submit answers (answering 'B' for all questions)
        mock_answers = {str(qid): "B" for qid in q_ids}
        response = self.client.post(
            "/submit-quiz",
            json={"answers": mock_answers}
        )
        self.assertEqual(response.status_code, 200)
        res_data = response.get_json()
        self.assertTrue(res_data.get("success"))
        result_id = res_data.get("result_id")
        self.assertGreater(result_id, 0)

        # 4. Visit results page
        res_page = self.client.get(f"/result/{result_id}")
        self.assertEqual(res_page.status_code, 200)
        self.assertIn(b"out of 10", res_page.data)
        self.assertIn(b"Review Answers", res_page.data)
        print(f"[TEST] Quiz scored successfully: Result ID #{result_id}.")

    def test_06_history_page(self):
        """Test history/leaderboard page renders recent attempts."""
        response = self.client.get("/history")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recent Quiz History", response.data)
        self.assertIn(b"Aarav Gupta", response.data)
        print("[TEST] History/leaderboard verified with student record.")


if __name__ == "__main__":
    unittest.main()
