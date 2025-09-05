# YOUR PROJECT TITLE
#### Video Demo:  <URL HERE>
#### Description:

this is a website that asks **100** questions from the person they have to register and log in to use it mainly giving a name and a password that is it then they will be able to complete the 100 questions 10 by 10 and they each **10** questions have a **theme** assigned to them I felt I was weak in **web development** so I made this project. It is not that good and lacks many features but I was out of time and had to end the project fast.

#### Database:

the **database** consists of ***14*** tables 10 of them are used in setting the ***questions*** and the others are used in keeping track of **players ,player scores** and **themes** of each quiz

this is the sql ***.schema*** for the tables and all the table names

#### Table Names: 
*completed  
*quizn1     
*quizn2     
*quizn4     
*quizn6    
*quizn8          
*quizn10    
*quizn3     
*quizn5     
*quizn7    
*quizn9 
*marks     
*users
*themes

all the numberd ***quizn*** files are created to store the quizes
and ***completed** stores witch user completed witch quiz
also ***users*** stores the user data and gives them a id and stores their name and password
    ***marks*** stores the marks each user has in each quiz
    ***themes*** as the name suggests it stores the themes of the quizes

these are __.schema__ of the database

CREATE TABLE **users** (/
    id INTEGER PRIMARY KEY AUTOINCREMENT,/
    username TEXT NOT NULL,/
    password TEXT NOT NULL/
, level INTEGER DEFAULT 0);/

CREATE TABLE **sqlite_sequence**(name,seq); /

CREATE TABLE IF NOT EXISTS **quizn** ( /   
    id INTEGER PRIMARY KEY AUTOINCREMENT,/
    question TEXT NOT NULL,/
    answer1 TEXT NOT NULL,/
    answer2 TEXT NOT NULL,/
    answer3 TEXT NOT NULL,/
    answer4 TEXT NOT NULL,/
    answer5 TEXT NOT NULL,/
    correct_answer INTEGER NOT NULL /    
);/

CREATE TABLE **marks** (/
    id INTEGER PRIMARY KEY AUTOINCREMENT,/
    user_id INTEGER NOT NULL,/
    quiz_name TEXT NOT NULL,/
    marks INTEGER NOT NULL,/
    FOREIGN KEY (user_id) REFERENCES users (id)/     
);/
CREATE TABLE **completed** (/
    id INTEGER PRIMARY KEY AUTOINCREMENT,/
    user_id INTEGER NOT NULL,/
    quiz_id INTEGER NOT NULL,/
    completed INTEGER DEFAULT 0,/
    FOREIGN KEY (user_id) REFERENCES users (id),/      
    UNIQUE(user_id, quiz_id)/
);/
CREATE TABLE **quizn3** (/
    id INTEGER PRIMARY KEY AUTOINCREMENT,/
    question TEXT NOT NULL,/
    answer1 TEXT NOT NULL,/
    answer2 TEXT NOT NULL,/
    answer3 TEXT NOT NULL,/
    answer4 TEXT NOT NULL,/
    answer5 TEXT NOT NULL,/
    correct_answer INTEGER NOT NULL,/
    theme_id INTEGER,/
    FOREIGN KEY (theme_id) REFERENCES themes (id)/    
);/
CREATE TABLE **themes** (/
    id INTEGER PRIMARY KEY AUTOINCREMENT,/
    name TEXT NOT NULL/
);/

#### CODE

The ***main.py*** file is the file that we need to run to get the website
AND it uses website file as a python package

The **__init__.py** is the file that combines all the files in the package namely **views.py** and **auth.py**

The **auth.py** file takes care of the autharization of any user and its the file with the login, logout and register functions

Then **views.py** is the file that takes care of the main functionality of the website it takes care of everythin other than login,logout and register functions in the ***website***

At Last the ***database.py*** takes care of the database functionality needed for the website

#### Style

some style code is in the html files but most of it is inside the ***styles.css***

#### Libraries in Use

this simple website uses ***flask*** and ***sqlite3*** *note that **sqlite3** is build into python





