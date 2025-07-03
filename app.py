from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@localhost/py_starter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def Index() :
    age = 19
    if age < 19:
        message = "young kid!"
    elif age >= 19 and age <= 25:
        message = "Hardworking phase of your life!"
    else :
        message = "Well try hard and start getting result"


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