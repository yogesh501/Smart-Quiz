"""
Smart Quiz - Sample Student Records Generator
Generates realistic initial quiz attempt records for demonstration.
"""

from database import db

SAMPLE_STUDENTS = [
    {"name": "Priya Patel", "cat_id": 2, "score": 10, "pct": 100.0},
    {"name": "Rohan Sharma", "cat_id": 1, "score": 9, "pct": 90.0},
    {"name": "Ananya Iyer", "cat_id": 4, "score": 9, "pct": 90.0},
    {"name": "Aarav Gupta", "cat_id": 3, "score": 8, "pct": 80.0},
    {"name": "Diya Mehta", "cat_id": 6, "score": 10, "pct": 100.0},
    {"name": "Siddharth Rao", "cat_id": 5, "score": 7, "pct": 70.0},
    {"name": "Tanvi Joshi", "cat_id": 1, "score": 8, "pct": 80.0},
    {"name": "Kabir Verma", "cat_id": 2, "score": 9, "pct": 90.0}
]

def add_sample_records():
    print("[INFO] Adding sample student records for demonstration...")
    count = 0
    for s in SAMPLE_STUDENTS:
        user_id = db.get_or_create_user(s["name"])
        db.save_quiz_result(
            user_id=user_id,
            category_id=s["cat_id"],
            score=s["score"],
            total_questions=10,
            percentage=s["pct"]
        )
        count += 1
    print(f"[SUCCESS] Added {count} sample student quiz records.")

if __name__ == "__main__":
    add_sample_records()
