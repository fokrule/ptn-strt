from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Encapsulation
class AgeAdvisor:
    def __init__(self, age):
        self._age = age #protected variable

    def get_message(self):
        if self._age < 19:
            return "Young Kid!"
        elif self._age <=25:
            return "Hardworking phase"
        else:
            return "Result phase"
        
# Inheritance
class TeenAdvisor(AgeAdvisor):
    def get_message(self):
        return "You are a tennager."
    
# Polumorphism
def get_advice(age):
    if 13 <= age <= 17:
        advisor = TeenAdvisor(age)
    else:
        advisor = AgeAdvisor(age)
    return advisor.get_message()

@app.route('/')
def Index() :
    age = 19
    message = get_advice(age)


    # Match section
    match(age):
        case 18:
            caseMessage = "This is from case and age is 18"
        case  _ if age >=19 and age <= 25:
            caseMessage = "This is from case and age is 19"
        case _:
            caseMessage = "Nothing mathced"
    return render_template('index.html',message = message, caseMessage = caseMessage)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        title = request.form['title']
        post = request.form['post']
        status = request.form['status']

        sql = text("INSERT INTO posts (title, post, status) VALUES (:title, :post, :status)")
        db.session.execute(sql, {'title': title, 'post': post, 'status': status})
        db.session.commit()
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)