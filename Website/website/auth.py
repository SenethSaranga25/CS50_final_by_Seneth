from flask import blueprints, render_template,request,redirect,session
from .database import get_all_users, insert_user,get_lvl
import sqlite3

def get_id(username):
    db = sqlite3.connect("website\database.db")
    cursor = db.cursor()
    id = session["user_id"] = cursor.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()[0]
    return id 


auth = blueprints.Blueprint('auth', __name__)
@auth.route('/login', methods=['GET','POST'])
def login():
    if "name" in session.keys():
        return redirect("/")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        all_users = get_all_users()
        for user in all_users:
            if user[0] == username and user[1] == password:
                session["name"] = username
                session['id'] =  get_id(username)
                session['level'] = get_lvl()
                return redirect("/")
        return render_template("login.html", message = "Invalid username or password")
    return render_template("login.html")

@auth.route('/register', methods = ['GET','POST'])
def register():
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmpassword")
        all_users = get_all_users()
        
        for user in all_users:
            if user[0] == username:
                return render_template("register.html", message="Username already exists")
        if not password == confirm_password:
            return render_template("register.html", message = "Passwords doesn't match")
        
        insert_user(username,password)
        return redirect("/login")
            
    return render_template("register.html")

@auth.route('/logout')
def logout(): #this function is written by AI
    session.pop('name', None)
    session.clear()
    return redirect('/login')