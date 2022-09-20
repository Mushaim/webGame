from cs50 import SQL
from flask import Flask, render_template, request

from templates.Question import Question

app = Flask(__name__)

db = SQL("sqlite:///quiz.db")
q1_db = {
    "q_id": 1,
    "question":db.execute("SELECT question FROM quizMaterial WHERE q_id = ?",1),
    "option1":db.execute("SELECT option1 FROM quizMaterial WHERE q_id = ?",1),
    "option2":db.execute("SELECT option2 FROM quizMaterial WHERE q_id = ?",1),
    "option3":db.execute("SELECT option3 FROM quizMaterial WHERE q_id = ?",1),
    "option4":db.execute("SELECT option4 FROM quizMaterial WHERE q_id = ?",1),
    "correctOption":db.execute("SELECT correctOption FROM quizMaterial WHERE q_id = ?",1),
}

q1 = Question(q1_db["q_id"],q1_db["question"],q1_db["option1"],q1_db["option2"],q1_db["option3"],q1_db["option4"],q1_db["correctOption"])

question_list = [q1]
@app.route("/")
def index():
    return render_template("index.html",question_list= question_list)

@app.route("/submitQuiz",methods=['POST','GET'])
def submit():
    value = request.form['option']
    return value