import sqlite3
from flask import session

def get_lvl():
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    lvl = cursor.execute("SELECT level FROM users WHERE id = ?", (session['id'],)).fetchone()[0]
    db.close()
    return lvl

def get_all_users():
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    users = cursor.execute("SELECT username, password FROM users").fetchall()
    db.close()
    return users
    
def insert_user(username,password):
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    db.commit()
    db.close()

def get_theme():
    lvl = get_lvl()+1
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    try:
        theme = cursor.execute("SELECT name FROM themes WHERE id = ?", (lvl,)).fetchone()[0]
    except:
        theme = ""
    db.close()
    return theme

def set_marks():
    lvl = get_lvl()
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO marks (user_id, quiz_name, marks) VALUES (?, ?, ?)", (session["id"], lvl , session["score"]))
    db.commit()
    db.close()

def add_quiz_completion(lvl, db_path="website\\database.db"):
    user_id = session["id"]   #this function was created by AI (I wanted to finish the project fast so I used AI)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    lvl = get_lvl()

    cursor.execute("""
        INSERT INTO completed (user_id, quiz_id, completed)
        VALUES (?, ?, 1)
        ON CONFLICT(user_id, quiz_id) 
        DO UPDATE SET completed = 1;
    """, (user_id, lvl))

    conn.commit()
    conn.close()

def get_all_quizzes():
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    lvl = get_lvl()+1
    try:
        quizzes = cursor.execute(f"SELECT * FROM quizn{lvl}").fetchall()
    except:
        quizzes = ""
    db.close()
    return quizzes

def change_lvl(lvl):
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    lvl = cursor.execute("UPDATE users SET level = ? WHERE id = ?",(lvl ,session['id']))
    db.commit()
    db.close()

def get_quiz_answerd():
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    lvl = get_lvl()
    try:
        quizzes = cursor.execute(f"SELECT * FROM quizn{lvl}").fetchall()
    except:
        quizzes = ""
    
    db.close()
    return quizzes

def get_completed_quizes():
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    quizzes = cursor.execute("SELECT quiz_name, marks FROM marks WHERE user_id = ?", (session['id'],)).fetchall()
    db.close()
    return quizzes

def get_theme_of_one_quiz(i):
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    theme = cursor.execute("SELECT name FROM themes WHERE id = ?", (i,)).fetchall()
    db.close()
    return theme

def ged_id(name):
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    try:
        id = cursor.execute("SELECT id FROM themes WHERE name = ?", (name,)).fetchone()[0]
    except:
        id = 1
    db.close()
    return id

def get_quiz_replay(lvl):
    db = sqlite3.connect('website\\database.db')
    cursor = db.cursor()
    try:
        quizzes = cursor.execute(f"SELECT * FROM quizn{lvl}").fetchall()
    except:
        quizzes = ""
    
    db.close()
    return quizzes
