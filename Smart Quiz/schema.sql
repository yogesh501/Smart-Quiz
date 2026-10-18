-- ===================================================
-- Smart Quiz Database Schema
-- Database Name: smart_quiz
-- Suitable for 11th-Standard School Project
-- ===================================================

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS smart_quiz CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE smart_quiz;

-- ---------------------------------------------------
-- 1. Table: categories
-- Stores quiz subject categories (Java, Python, MySQL, DBMS, History, Science)
-- ---------------------------------------------------
DROP TABLE IF EXISTS quiz_results;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    code VARCHAR(50) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    icon VARCHAR(50) NOT NULL DEFAULT 'book',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ---------------------------------------------------
-- 2. Table: questions
-- Stores multiple-choice questions belonging to a category
-- ---------------------------------------------------
CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    question_text TEXT NOT NULL,
    option_a VARCHAR(255) NOT NULL,
    option_b VARCHAR(255) NOT NULL,
    option_c VARCHAR(255) NOT NULL,
    option_d VARCHAR(255) NOT NULL,
    correct_option CHAR(1) NOT NULL, -- 'A', 'B', 'C', or 'D'
    explanation TEXT,
    difficulty VARCHAR(20) DEFAULT 'Easy',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_questions_category FOREIGN KEY (category_id) 
        REFERENCES categories(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ---------------------------------------------------
-- 3. Table: users
-- Stores simple student registrations (name only)
-- ---------------------------------------------------
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ---------------------------------------------------
-- 4. Table: quiz_results
-- Stores quiz score, percentage, user and category references
-- ---------------------------------------------------
CREATE TABLE quiz_results (
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

-- Indexes for performance optimization
CREATE INDEX idx_questions_category ON questions(category_id);
CREATE INDEX idx_results_user ON quiz_results(user_id);
CREATE INDEX idx_results_category ON quiz_results(category_id);
CREATE INDEX idx_results_date ON quiz_results(completion_date);
