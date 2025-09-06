# Quizzey  

#### Video Demo: <[URL HERE](https://youtu.be/Zvfc4p6ui0E)>  

---  

## Description  

![Home Page Screenshot](Screenshot%20(12).png)  

This is a **quiz website** built with **Flask** and **SQLite**.  
It demonstrates:  

-  User **registration** & **login** (only username & password required)  
-  **Authentication & session handling** using Flask sessions  
-  **Database integration** with SQLite (14 tables)  
-  A quiz flow where users answer **100 questions** split into **10 themed sets**  
-  Marks storage, progress tracking, and replaying completed quizzes  

I built this project to strengthen my **web development** and **database** skills.  
It’s not fully polished, but it showcases:  

- Flask Blueprints for modular routes (`views.py` for quiz logic, `auth.py` for login/register/logout)  
- Secure(ish) login and session handling  
- Dynamic question rendering and result saving  
- Replay functionality for completed quizzes  

---  

## Features  

- **User Authentication**  
  - Register with a username + password  
  - Login & logout functionality  
  - Session handling to track current user  

- **Quiz System**  
  - 100 questions total  
  - 10 sets of 10 questions (each tied to a *theme*)  
  - Multiple-choice (5 options, one correct)  
  - Instant score tracking  
  - Automatic marks saving & quiz completion logging  

- **Profile Page**  
  - View completed quizzes  
  - See marks and progress (e.g., `25/40`)  
  - Replay any completed quiz set  

- **Answers Page**  
  - Review correct answers after finishing a quiz  

---  

## Project Structure  

quiz-website/
│── main.py # Entry point (runs the app)
│── website/
│ ├── init.py # App factory, Blueprint registration
│ ├── views.py # Quiz routes
│ ├── auth.py # Authentication routes
│ ├── database.py # DB connection & helper functions
│ ├── static/ # CSS, JS, Images
│ └── templates/ # HTML templates (Jinja2)
│── README.md # Project documentation


---  

## Database Design  

There are **14 tables** in total:  

- `users` → Stores usernames, passwords, level progress  
- `marks` → Stores marks per quiz attempt  
- `completed` → Tracks completed quiz sets  
- `themes` → Stores quiz themes (10 total)  
- `quizn1` … `quizn10` → Each stores 10 questions for that set  

### Example Schemas  

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    level INTEGER DEFAULT 0
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

CREATE TABLE themes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Base schema for quizzes (quizn1 ... quizn10)
CREATE TABLE quizn1 (
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
```

### How It Works

1. A user registers or logs in.

2. They are shown a quiz set of 10 questions.

3. After answering:
   Their score is calculated.

4. The quiz is marked completed.
   Results are stored in marks.

5. On the Profile page:
   Users can see their progress.

6. Replay a quiz they already completed.

***And Answers page lets them review correct solutions.***

