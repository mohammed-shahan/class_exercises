from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from werkzeug.security import generate_password_hash
import auth
from flask import redirect, url_for




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.sqlite3'

db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

    def __init__(self, title, subtitle, author, date_posted, content) -> None:
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date_posted = date_posted
        self.content = content



class Users(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    firstName   = db.Column(db.String(20), nullable=False)
    lastName    = db.Column(db.String(20), nullable=False)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    phone       = db.Column(db.String(13))
    password    = db.Column(db.String(300), nullable=False)

    def __init__(self, firstName, lastName, password, email, phone) -> None:
        self.firstName  = firstName
        self.lastName   = lastName
        self.password   = password
        self.email      = email
        self.phone      = phone

          
# def dummy():
#     db.session.add(Users('user', 'abc',generate_password_hash('user123'),'user@foo','6846435465'))
#     db.session.commit()

  

@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)




@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))





def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

if __name__ == '__main__':
    db.create_all(app=app)
    # dummy()
    app.run(debug=True)
    