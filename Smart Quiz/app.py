"""
Smart Quiz - Flask Web Application
Backend application for 11th-Standard School Project.
Provides routing, session management, secure server-side scoring,
and integrates with MySQL / database module.
"""

import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    jsonify
)
from database import db

app = Flask(__name__)
# Secret key for secure session cookies
app.secret_key = os.getenv("SECRET_KEY", "smart-quiz-school-project-secret-key-2026")


@app.context_processor
def inject_global_data():
    """Injects database status and common variables to all templates."""
    return {
        "db_engine": db.engine,
        "current_student": session.get("student_name", "")
    }


@app.route("/")
def index():
    """Home Page: displays title, subtitle, welcome message, stats, and 6 category cards."""
    try:
        categories = db.get_all_categories_with_count()
        stats = db.get_system_stats()
    except Exception as e:
        flash(f"Error loading categories: {str(e)}", "danger")
        categories = []
        stats = {}
    return render_template("index.html", categories=categories, stats=stats)


@app.route("/start-quiz/<int:category_id>", methods=["POST"])
def start_quiz(category_id):
    """
    Validates student name from modal/form, saves in session,
    and initiates the quiz session.
    """
    student_name = request.form.get("student_name", "").strip()
    if not student_name:
        flash("Please enter your name to start the quiz.", "warning")
        return redirect(url_for("index"))

    # Validate category exists
    category = db.get_category_by_id(category_id)
    if not category:
        flash("Invalid category selected.", "danger")
        return redirect(url_for("index"))

    # Store student details in session
    session["student_name"] = student_name
    session["category_id"] = category_id
    session["current_quiz_review"] = None  # Clear past review data

    return redirect(url_for("quiz", category_id=category_id))


@app.route("/quiz/<int:category_id>")
def quiz(category_id):
    """
    Quiz Interface:
    Renders 10 randomly selected questions for the selected category.
    CRITICAL SECURITY RULE: Correct answers are NOT exposed to the client!
    """
    student_name = session.get("student_name") or request.args.get("demo_student")
    if student_name and not session.get("student_name"):
        session["student_name"] = student_name
    if not student_name:
        flash("Please enter your name on the home page before taking a quiz.", "info")
        return redirect(url_for("index"))

    category = db.get_category_by_id(category_id)
    if not category:
        flash("Category not found.", "danger")
        return redirect(url_for("index"))

    # Fetch 10 random questions (without correct_option and without explanation)
    questions = db.get_random_questions(category_id, limit=10)
    if not questions:
        flash(f"No questions currently available in '{category['name']}'.", "warning")
        return redirect(url_for("index"))

    # Store question IDs in session to prevent client manipulation upon submission
    session["active_question_ids"] = [q["id"] for q in questions]
    session["active_category_id"] = category_id

    return render_template(
        "quiz.html",
        category=category,
        questions=questions,
        total_questions=len(questions),
        student_name=student_name
    )


@app.route("/submit-quiz", methods=["POST"])
def submit_quiz():
    """
    Submits student answers, calculates score on server side,
    stores result in MySQL/SQLite database, and prepares review data.
    """
    student_name = session.get("student_name")
    if not student_name:
        if request.is_json:
            return jsonify({"success": False, "error": "Session expired. Please start again from Home."}), 400
        flash("Session expired. Please enter your name again.", "warning")
        return redirect(url_for("index"))

    category_id = session.get("active_category_id")
    question_ids = session.get("active_question_ids", [])

    if not category_id or not question_ids:
        if request.is_json:
            return jsonify({"success": False, "error": "No active quiz session found."}), 400
        flash("No active quiz found. Please choose a category to begin.", "warning")
        return redirect(url_for("index"))

    # Parse submitted answers (supports both JSON fetch and traditional Form submission)
    if request.is_json:
        payload = request.get_json() or {}
        submitted_answers = payload.get("answers", {})
    else:
        submitted_answers = {}
        for q_id in question_ids:
            key = f"q_{q_id}"
            if key in request.form:
                submitted_answers[str(q_id)] = request.form[key]

    # Fetch authentic question records (including correct_option and explanation)
    full_questions = db.get_questions_for_scoring(question_ids)
    q_dict = {str(q["id"]): q for q in full_questions}

    score = 0
    total_questions = len(question_ids)
    review_list = []

    for q_id in question_ids:
        str_id = str(q_id)
        q_data = q_dict.get(str_id)
        if not q_data:
            continue

        selected_opt = submitted_answers.get(str_id, "").strip().upper()
        correct_opt = q_data["correct_option"].strip().upper()
        is_correct = (selected_opt == correct_opt)

        if is_correct:
            score += 1

        review_list.append({
            "id": q_data["id"],
            "question_text": q_data["question_text"],
            "option_a": q_data["option_a"],
            "option_b": q_data["option_b"],
            "option_c": q_data["option_c"],
            "option_d": q_data["option_d"],
            "selected_option": selected_opt or "Unanswered",
            "correct_option": correct_opt,
            "is_correct": is_correct,
            "explanation": q_data["explanation"]
        })

    percentage = round((score / total_questions) * 100, 2) if total_questions > 0 else 0.0

    # Save to database (users and quiz_results tables)
    try:
        user_id = db.get_or_create_user(student_name)
        result_id = db.save_quiz_result(
            user_id=user_id,
            category_id=category_id,
            score=score,
            total_questions=total_questions,
            percentage=percentage
        )
    except Exception as e:
        print(f"[ERROR] Failed to save quiz result: {e}")
        result_id = 0

    # Save detailed review in session for the results page
    session["current_quiz_review"] = review_list

    if request.is_json:
        return jsonify({
            "success": True,
            "result_id": result_id,
            "redirect_url": url_for("result", result_id=result_id)
        })

    return redirect(url_for("result", result_id=result_id))


@app.route("/result/<int:result_id>")
def result(result_id):
    """
    Results Page:
    Displays score, percentage, correct/incorrect counters,
    motivational message, and full answer review with explanations.
    """
    result_data = None
    if result_id > 0:
        result_data = db.get_result_by_id(result_id)

    # Fallback to session values if direct record lookup fails
    student_name = session.get("student_name", "Student")
    review_list = session.get("current_quiz_review", [])
    
    if result_data:
        score = result_data["score"]
        total = result_data["total_questions"]
        percentage = float(result_data["percentage"])
        category_name = result_data["category_name"]
        category_code = result_data.get("category_code", "general")
        student_name = result_data["student_name"]
    else:
        # Compute from review_list if available
        total = len(review_list) or 10
        score = sum(1 for r in review_list if r["is_correct"])
        percentage = round((score / total) * 100, 2) if total > 0 else 0.0
        cat_id = session.get("active_category_id", 1)
        cat_obj = db.get_category_by_id(cat_id)
        category_name = cat_obj["name"] if cat_obj else "Quiz"
        category_code = cat_obj["code"] if cat_obj else "general"

    incorrect = total - score

    # Performance-based motivational message
    if percentage >= 90:
        badge_title = "Outstanding Performance! 🌟"
        badge_message = "Brilliant job! You demonstrated complete mastery of this subject."
        badge_class = "result-excellent"
    elif percentage >= 70:
        badge_title = "Great Effort! 👍"
        badge_message = "Well done! You have a solid grasp of key concepts."
        badge_class = "result-good"
    elif percentage >= 50:
        badge_title = "Good Attempt! 📚"
        badge_message = "Nice try! Review the explanations below and give it another shot."
        badge_class = "result-average"
    else:
        badge_title = "Keep Practicing! 💪"
        badge_message = "Don't be discouraged! Check the detailed explanations below to learn and retake the quiz."
        badge_class = "result-needs-improvement"

    category_id = session.get("active_category_id", 1)

    return render_template(
        "result.html",
        result_id=result_id,
        student_name=student_name,
        category_name=category_name,
        category_id=category_id,
        category_code=category_code,
        score=score,
        total=total,
        incorrect=incorrect,
        percentage=percentage,
        badge_title=badge_title,
        badge_message=badge_message,
        badge_class=badge_class,
        review_list=review_list
    )


@app.route("/history")
def history():
    """Displays recent quiz history, leaderboard, and overall statistics."""
    recent_results = db.get_recent_results(limit=30)
    stats = db.get_system_stats()
    return render_template("history.html", results=recent_results, stats=stats)


@app.route("/about")
def about():
    """
    Project documentation page explaining DBMS concepts, SQL schema,
    Python Flask structure, and Java topics for school project evaluation.
    """
    return render_template("about.html")


@app.route("/api/categories")
def api_categories():
    """JSON API to fetch all categories."""
    categories = db.get_all_categories_with_count()
    return jsonify(categories)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", error=str(e)), 500


import socket


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


if __name__ == "__main__":
    local_ip = get_local_ip()
    print("=" * 60)
    print(" Smart Quiz Web Application")
    print(f" Database Engine: {db.engine.upper()}")
    print(f" Local (PC/Desktop):      http://127.0.0.1:5000")
    print(f" Android / Mobile Device: http://{local_ip}:5000")
    print("=" * 60)
    port = int(os.environ.get("PORT", 5000))
    # Bind to 0.0.0.0 so phones and tablets on the same network or cloud routers can access it
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
