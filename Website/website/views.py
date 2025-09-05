from flask import blueprints, render_template, request,redirect, session
import sqlite3
from .database import get_theme, set_marks, add_quiz_completion,get_all_quizzes,get_lvl,change_lvl,get_quiz_answerd,get_completed_quizes,get_theme_of_one_quiz,ged_id,get_quiz_replay


views = blueprints.Blueprint('views', __name__)
@views.route('/')
def home():
    if 'counter' in session.keys():
        session['ans_num'] = 0
        session['counter'] = 0
        session['score'] = 0
        session['level'] = get_lvl()+1
        session["play_again_id"] = 0
    return render_template("index.html")

@views.route('/quiz', methods=['GET','POST'])
def quiz():
    value = 0
    if "ans_num" in session.keys():
        session['ans_num'] = 0
    if "counter" not in session.keys():
        session["counter"] = 0
        session['score'] = 0
        

    if request.method == "POST":
        value = request.form["answer"]
        session['counter'] += 1

    lvl = get_lvl() + 1
    theme = get_theme() 
    counter = session['counter']
    quizes = get_all_quizzes()
    try:
        if value == str(quizes[counter - 1][7]):
            session['score'] += 1
    except:
        pass

    if counter <  len(quizes):
        return render_template("quiz.html",
            number=counter + 1,
            theme = theme,
            question=quizes[counter][1],
            Answer1=quizes[counter][2],
            Answer2=quizes[counter][3],
            Answer3=quizes[counter][4],
            Answer4=quizes[counter][5],
            Answer5=quizes[counter][6]
        )
    else:
        set_marks()                            
        add_quiz_completion(lvl)                
        change_lvl(lvl)
        session["counter"] = 0
        return redirect("/quiz/marks")

        
@views.route('/quiz/marks')
def marks():
    temp = session['score']
    session['score'] = 0
    return render_template("marks.html", mark = temp)

@views.route('/quiz/answers', methods = ['GET', "POST"])
def answers():
    quize =  get_quiz_answerd()
    if "ans_num" not in session.keys():
            session['ans_num'] = 0
    if request.method == "POST": 

        session['ans_num'] += 1
    if session['ans_num'] < len(quize):
        return render_template("answers.html", question = quize[session['ans_num']][1], answer = quize[session['ans_num']][(quize[session['ans_num']][7]) + 1], number = session["ans_num"]+1 )
    else:
        session['ans_num'] = 0
        return redirect("/")
    
@views.route("/profile", methods = {"GET", "POST"})
def profile():
    if request.method == "POST":
        value = request.form["quiz"]
        id  =  ged_id(value)
        session["play_again_id"]  = id
        return redirect("/profile/play")
    quizez = get_completed_quizes()
    quiz_d = []
    total = 0
    count = 0
    try:
        for quiz in quizez:
            quiz_theme = get_theme_of_one_quiz(int(quiz[0])+1)
            quiz_theme = quiz_theme[0]
            temp = [quiz_theme[0], quiz[-1]]
            quiz_d.append(temp)
            total += quiz[-1]
            count += 1
    except:
        pass
    total = f"{total}/{10*count}"
    return render_template("profile.html", quizzes = quiz_d, total_marks = total)

@views.route("/done")
def done():
    return render_template("done.html")


@views.route("/profile/play", methods = {"GET", "POST"})
def play_again():
    if "ans_num" in session.keys():
        session['ans_num'] = 0
    if "play_again_id" in session.keys():
        if "counter" not in session.keys():
            session["counter"] = 0
            session['score'] = 0
            

        if request.method == "POST":
            value = request.form["answer"]
            session['counter'] += 1

        lvl = get_lvl() + 1
        theme = get_theme_of_one_quiz(session['play_again_id'])[0][0]
        counter = session['counter']
        quizes = get_quiz_replay(session['play_again_id'])
        try:
            if value == str(quizes[counter - 1][7]):
                session['score'] += 1
        except:
            pass

        try:
            return render_template("quiz.html",
                number=counter + 1,
                theme = theme,
                question=quizes[counter][1],
                Answer1=quizes[counter][2],
                Answer2=quizes[counter][3],
                Answer3=quizes[counter][4],
                Answer4=quizes[counter][5],
                Answer5=quizes[counter][6]
            )
        except:                                         
            session["counter"] = 0
            return redirect("/profile/play/marks")
    else:
        return redirect("/")
        
@views.route('/profile/play/marks')
def marks_again():
    temp = session['score']
    session['score'] = 0
    if "ans_num" in session.keys():
        session["ans_num"] = 0
    return render_template("marks.html", mark = temp)

@views.route('/profile/play/answers', methods = ['GET', "POST"])
def answers_again():
    quize =  get_quiz_replay(session["play_again_id"])
    print(quize)
    print(len(quize))
    if "ans_num" not in session.keys():
            session['ans_num'] = 0
    if request.method == "POST":
        print(session['ans_num']) 
        print(len(quize))
        session['ans_num'] += 1
    if session['ans_num'] < len(quize):
        print(session['ans_num'])
        return render_template("answers.html", question = quize[session['ans_num']][1], answer = quize[session['ans_num']][(quize[session['ans_num']][7]) + 1], number = session["ans_num"]+1 )
    else:
        session['ans_num'] = 0
        session['play_again_id'] = 0
        return redirect("/")