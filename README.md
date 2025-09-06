# Quiz Website

#### Video Demo: <[URL HERE](https://youtu.be/Zvfc4p6ui0E))>

---

## 📖 Description

![Home Page Screenshot](Screenshot%20(12).png)

This is a simple **quiz website** built with Flask and SQLite.

- The site asks users **100 questions**.
- Users must **register and log in** (only a username and password are required).
- Questions are divided into **10 sets of 10**, each with its own **theme**.
- After completing a set, progress is stored in the database.

I built this project to strengthen my **web development** skills. It’s not feature-complete (I ran out of time), but it demonstrates authentication, session handling, and database integration.

---

## 🗂️ Table Names

There are **14 tables** in total:

- `users`
- `marks`
- `completed`
- `themes`
- `quizn1`
- `quizn2`
- `quizn3`
- `quizn4`
- `quizn5`
- `quizn6`
- `quizn7`
- `quizn8`
- `quizn9`
- `quizn10`

> The `quizn*` tables store questions; the others track users, scores, completion status, and themes.

---

## 📂 Table Schemas

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    level INTEGER DEFAULT 0
);

CREATE TABLE sqlite_sequence (
    name,
    seq
);

-- Base schema used for quiz tables (quizn1 ... quizn10)
CREATE TABLE IF NOT EXISTS quizn (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer1 TEXT NOT NULL,
    answer2 TEXT NOT NULL,
    answer3 TEXT NOT NULL,
    answer4 TEXT NOT NULL,
    answer5 TEXT NOT NULL,
    correct_answer INTEGER NOT NULL
);

CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    quiz_name TEXT NOT NULL,
    marks INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE completed (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    quiz_id INTEGER NOT NULL,
    completed INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users (id),
    UNIQUE(user_id, quiz_id)
);

-- Example of a quiz table extended with a theme reference
CREATE TABLE quizn3 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer1 TEXT NOT NULL,
    answer2 TEXT NOT NULL,
    answer3 TEXT NOT NULL,
    answer4 TEXT NOT NULL,
    answer5 TEXT NOT NULL,
    correct_answer INTEGER NOT NULL,
    theme_id INTEGER,
    FOREIGN KEY (theme_id) REFERENCES themes (id)
);

CREATE TABLE themes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);













