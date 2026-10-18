"""
Smart Quiz - Database Operations Module
Handles MySQL connections, schema execution, parameterized queries,
and includes a transparent SQLite fallback for immediate testing/demonstration
if MySQL server is not locally running.
"""

import os
import sqlite3
import pymysql
from pymysql.cursors import DictCursor
from seed_data import seed_database

# Configuration - can be overridden via environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "smart_quiz")

if os.getenv("VERCEL"):
    SQLITE_DB_PATH = "/tmp/smart_quiz.db"
    _source_db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "smart_quiz.db")
    if os.path.exists(_source_db) and not os.path.exists(SQLITE_DB_PATH):
        import shutil
        try:
            shutil.copy2(_source_db, SQLITE_DB_PATH)
        except Exception as _e:
            print(f"[DATABASE] Notice: Could not copy seed db to /tmp ({_e})")
else:
    SQLITE_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "smart_quiz.db")


class DatabaseManager:
    def __init__(self):
        self.engine = None  # 'mysql' or 'sqlite'
        self.mysql_error = None
        self._test_connection()
        self.init_database()

    def _test_connection(self):
        """Attempts to connect to MySQL; falls back to SQLite if unreachable."""
        try:
            conn = pymysql.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD,
                cursorclass=DictCursor,
                connect_timeout=3
            )
            conn.close()
            self.engine = "mysql"
            print(f"[DATABASE] Connected successfully to MySQL at {DB_HOST}:{DB_PORT}.")
        except Exception as e:
            self.engine = "sqlite"
            self.mysql_error = str(e)
            print(f"[DATABASE] MySQL not reachable ({e}). Switching seamlessly to SQLite mode ({SQLITE_DB_PATH}).")

    def get_connection(self):
        """Returns an active database connection based on the chosen engine."""
        if self.engine == "mysql":
            try:
                return pymysql.connect(
                    host=DB_HOST,
                    port=DB_PORT,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    database=DB_NAME,
                    cursorclass=DictCursor,
                    autocommit=True
                )
            except pymysql.err.OperationalError as e:
                # Database might not exist yet; connect to root to create it
                if e.args[0] == 1049:  # Unknown database
                    return pymysql.connect(
                        host=DB_HOST,
                        port=DB_PORT,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        cursorclass=DictCursor,
                        autocommit=True
                    )
                raise
        else:
            conn = sqlite3.connect(SQLITE_DB_PATH)
            conn.row_factory = sqlite3.Row  # Enables dict-like row access
            conn.execute("PRAGMA foreign_keys = ON;")
            return conn

    def init_database(self):
        """Initializes tables and seeds initial data if empty."""
        if self.engine == "mysql":
            self._init_mysql()
        else:
            self._init_sqlite()

        # Seed categories and questions if database is empty
        cat_count = self.execute_query("SELECT COUNT(*) AS count FROM categories", fetch_one=True)
        count_val = cat_count.get("count", 0) if isinstance(cat_count, dict) else (cat_count[0] if cat_count else 0)
        if count_val == 0:
            print("[DATABASE] No categories found. Automatically seeding questions...")
            seed_database(self)
        else:
            print(f"[DATABASE] Database ready with {count_val} categories.")

    def _init_mysql(self):
        """Creates smart_quiz database and MySQL schema."""
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            cursorclass=DictCursor,
            autocommit=True
        )
        try:
            with conn.cursor() as cur:
                cur.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
                cur.execute(f"USE `{DB_NAME}`;")
                
                cur.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL UNIQUE,
                    code VARCHAR(50) NOT NULL UNIQUE,
                    description TEXT NOT NULL,
                    icon VARCHAR(50) NOT NULL DEFAULT 'book',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                """)

                cur.execute("""
                CREATE TABLE IF NOT EXISTS questions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    category_id INT NOT NULL,
                    question_text TEXT NOT NULL,
                    option_a VARCHAR(255) NOT NULL,
                    option_b VARCHAR(255) NOT NULL,
                    option_c VARCHAR(255) NOT NULL,
                    option_d VARCHAR(255) NOT NULL,
                    correct_option CHAR(1) NOT NULL,
                    explanation TEXT,
                    difficulty VARCHAR(20) DEFAULT 'Easy',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    CONSTRAINT fk_questions_category FOREIGN KEY (category_id) 
                        REFERENCES categories(id) ON DELETE CASCADE ON UPDATE CASCADE
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                """)

                cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    student_name VARCHAR(100) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                """)

                cur.execute("""
                CREATE TABLE IF NOT EXISTS quiz_results (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT NOT NULL,
                    category_id INT NOT NULL,
                    score INT NOT NULL,
                    total_questions INT NOT NULL,
                    percentage DECIMAL(5,2) NOT NULL,
                    completion_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    CONSTRAINT fk_results_user FOREIGN KEY (user_id) 
                        REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    CONSTRAINT fk_results_category FOREIGN KEY (category_id) 
                        REFERENCES categories(id) ON DELETE CASCADE ON UPDATE CASCADE
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                """)
        finally:
            conn.close()

    def _init_sqlite(self):
        """Initializes tables for SQLite fallback mode."""
        conn = sqlite3.connect(SQLITE_DB_PATH)
        conn.execute("PRAGMA foreign_keys = ON;")
        cur = conn.cursor()
        
        cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            code TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL,
            icon TEXT NOT NULL DEFAULT 'book',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER NOT NULL,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL,
            explanation TEXT,
            difficulty TEXT DEFAULT 'Easy',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            percentage REAL NOT NULL,
            completion_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
        );
        """)
        conn.commit()
        conn.close()

    def _adapt_query(self, query):
        """Adapts MySQL parameterized syntax (%s) for SQLite (?) if needed."""
        if self.engine == "sqlite":
            return query.replace("%s", "?")
        return query

    def execute_query(self, query, params=None, fetch_one=False, fetch_all=True):
        """Executes a SELECT query and returns dictionary rows."""
        conn = self.get_connection()
        adapted_query = self._adapt_query(query)
        params = params or ()
        try:
            if self.engine == "mysql":
                with conn.cursor() as cur:
                    cur.execute(adapted_query, params)
                    if fetch_one:
                        return cur.fetchone()
                    if fetch_all:
                        return cur.fetchall()
                    return None
            else:
                cur = conn.cursor()
                cur.execute(adapted_query, params)
                if fetch_one:
                    row = cur.fetchone()
                    return dict(row) if row else None
                if fetch_all:
                    rows = cur.fetchall()
                    return [dict(r) for r in rows]
                return None
        finally:
            conn.close()

    def execute_insert(self, query, params=None):
        """Executes an INSERT query and returns the newly generated ID."""
        conn = self.get_connection()
        adapted_query = self._adapt_query(query)
        params = params or ()
        try:
            if self.engine == "mysql":
                with conn.cursor() as cur:
                    cur.execute(adapted_query, params)
                    return cur.lastrowid
            else:
                cur = conn.cursor()
                cur.execute(adapted_query, params)
                conn.commit()
                return cur.lastrowid
        finally:
            conn.close()

    def execute_non_query(self, query, params=None):
        """Executes an UPDATE, DELETE, or DDL query."""
        conn = self.get_connection()
        adapted_query = self._adapt_query(query)
        params = params or ()
        try:
            if self.engine == "mysql":
                with conn.cursor() as cur:
                    return cur.execute(adapted_query, params)
            else:
                cur = conn.cursor()
                result = cur.execute(adapted_query, params)
                conn.commit()
                return result.rowcount
        finally:
            conn.close()

    # --- High Level Data Access Functions ---

    def get_all_categories_with_count(self):
        """Retrieves all categories along with question counts."""
        sql = """
        SELECT c.id, c.name, c.code, c.description, c.icon,
               COUNT(q.id) AS question_count
        FROM categories c
        LEFT JOIN questions q ON c.id = q.category_id
        GROUP BY c.id, c.name, c.code, c.description, c.icon
        ORDER BY c.id ASC;
        """
        return self.execute_query(sql)

    def get_category_by_id(self, category_id):
        """Retrieves a single category by its ID."""
        sql = "SELECT * FROM categories WHERE id = %s"
        return self.execute_query(sql, (category_id,), fetch_one=True)

    def get_random_questions(self, category_id, limit=10):
        """
        Retrieves random questions for a quiz attempt.
        Crucial: Excludes correct_option and explanation to prevent frontend cheating!
        """
        order_clause = "RAND()" if self.engine == "mysql" else "RANDOM()"
        sql = f"""
        SELECT id, category_id, question_text, option_a, option_b, option_c, option_d
        FROM questions
        WHERE category_id = %s
        ORDER BY {order_clause}
        LIMIT {limit};
        """
        return self.execute_query(sql, (category_id,))

    def get_questions_for_scoring(self, question_ids):
        """Retrieves full question data (with correct options) for server-side score calculation."""
        if not question_ids:
            return []
        placeholders = ", ".join(["%s"] * len(question_ids))
        sql = f"""
        SELECT id, category_id, question_text, option_a, option_b, option_c, option_d, correct_option, explanation
        FROM questions
        WHERE id IN ({placeholders});
        """
        return self.execute_query(sql, tuple(question_ids))

    def get_or_create_user(self, student_name):
        """Finds or registers a student by name."""
        student_name = student_name.strip()
        user = self.execute_query(
            "SELECT id, student_name FROM users WHERE student_name = %s ORDER BY id DESC",
            (student_name,),
            fetch_one=True
        )
        if user:
            return user["id"]
        
        return self.execute_insert(
            "INSERT INTO users (student_name) VALUES (%s)",
            (student_name,)
        )

    def save_quiz_result(self, user_id, category_id, score, total_questions, percentage):
        """Saves a completed quiz result into quiz_results table."""
        sql = """
        INSERT INTO quiz_results (user_id, category_id, score, total_questions, percentage)
        VALUES (%s, %s, %s, %s, %s)
        """
        return self.execute_insert(sql, (user_id, category_id, score, total_questions, percentage))

    def get_result_by_id(self, result_id):
        """Retrieves full result details joined with user and category names."""
        sql = """
        SELECT r.id, r.score, r.total_questions, r.percentage, r.completion_date,
               u.student_name,
               c.name AS category_name, c.code AS category_code
        FROM quiz_results r
        JOIN users u ON r.user_id = u.id
        JOIN categories c ON r.category_id = c.id
        WHERE r.id = %s;
        """
        return self.execute_query(sql, (result_id,), fetch_one=True)

    def get_recent_results(self, limit=25):
        """Retrieves the most recent quiz attempts for the history / leaderboard."""
        sql = f"""
        SELECT r.id, r.score, r.total_questions, r.percentage, r.completion_date,
               u.student_name,
               c.name AS category_name, c.code AS category_code
        FROM quiz_results r
        JOIN users u ON r.user_id = u.id
        JOIN categories c ON r.category_id = c.id
        ORDER BY r.completion_date DESC
        LIMIT {limit};
        """
        return self.execute_query(sql)

    def get_system_stats(self):
        """Calculates dashboard summary statistics."""
        sql = """
        SELECT 
            COUNT(id) AS total_quizzes,
            COALESCE(AVG(percentage), 0) AS average_score,
            COALESCE(MAX(score), 0) AS highest_score
        FROM quiz_results;
        """
        stats = self.execute_query(sql, fetch_one=True)
        
        user_count = self.execute_query("SELECT COUNT(id) AS total_students FROM users;", fetch_one=True)
        q_count = self.execute_query("SELECT COUNT(id) AS total_questions FROM questions;", fetch_one=True)
        
        return {
            "total_quizzes": stats.get("total_quizzes", 0) if stats else 0,
            "average_score": round(stats.get("average_score", 0), 1) if stats else 0.0,
            "highest_score": stats.get("highest_score", 0) if stats else 0,
            "total_students": user_count.get("total_students", 0) if user_count else 0,
            "total_questions": q_count.get("total_questions", 0) if q_count else 0,
            "database_engine": self.engine
        }


# Singleton database manager instance
db = DatabaseManager()
