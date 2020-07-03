import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_session import Session
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
from sqlalchemy import *
from models import *
from helpers import login_required
app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
app.config["SQLALCHEMY_DATABASE_URI"]= os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
db.init_app(app)


@app.route("/", methods=["POST","GET"])
@login_required
def index():
    if request.method=='GET':
        return render_template("index.html")
    elif request.method=='POST':
        if not request.form.get("ISBN") and not request.form.get("Title") and not request.form.get("Author"):
            return ("Input not entered in any field! Please fill any one field.")
        if request.form.get("ISBN"):
            search_result=request.form.get("ISBN")
            query_result=Books.query.filter(Books.isbn.like(search_result+"%")).all()
            return render_template("search.html", query_result=query_result)
        elif request.form.get("Title"):
            search_result= request.form.get("Title")
            query_result= Books.query.filter(Books.title.like(search_result+"%")).all()
            return render_template("search.html", query_result=query_result)
        elif request.form.get("Author"):
            search_result= request.form.get("Author")
            query_result= Books.query.filter(Books.author.like(search_result+"%")).all()
            return render_template("search.html",query_result= query_result)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=='GET':
        return render_template("register.html")
    elif request.method=='POST':
        user_name= request.form.get("Username")
        password= request.form.get("Password")
        if Users.query.filter_by(username=user_name).all():
            return "<h1>Username already exist!</h1>"
        if request.form.get("Password")=="" or request.form.get("Username")=="":
            return "<h1>Please enter valid password/username!</h1>"
        users= Users(username=user_name, password=password)
        db.session.add(users)
        db.session.commit()
        session['user_id']= users
        flash("Registered")
        return redirect(url_for("login"))
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method=='GET':
        return render_template("login.html")
    elif request.method=='POST':
        user_name=request.form.get("Username")
        password=request.form.get("Password")
        if Users.query.filter(and_(Users.username==user_name, Users.password==password)).all():
            users= Users(username=user_name, password=password)
            session['user_id']= users
            return redirect(url_for("index"))
        else:
            return "<h1> Incorrent username or password!</h1>"
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/review/<id>", methods=["POST", "GET"])
def review(id):

    get_isbn=Books.query.get(id)
    result=requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "QQE9IXJ0UzfOuk5sIqzDQ", "isbns":get_isbn.isbn})
    dict_json=result.json()
    row=Books.query.get(id)
    title=row.title
    user=session['user_id']
    loged_in_user=Users.query.filter_by(username=user.username).all()
    record_of_logedin_user= Reviews.query.filter(and_(Reviews.user_id== loged_in_user[0].id, Reviews.book_id== id)).all()
    status=1
    if len(review_record_of_logedin_user)>=1:
        status=0
    existing_reviews=Reviews.query.filter_by(book_id=id)
    li=[]
    for run in existing_reviews:
        q=Users.query.get(run.user_id)
        li.append(q.username)
#  GET REQUEST
    if request.method=='GET':
        return render_template("review.html",get_dict=dict_json, title=title, key=id, status=status, existing_reviews=existing_reviews, user=li)

# POST REAUEST
    if request.method=='POST':
        USER=Users.query.filter_by(username=user.username).all()
        option = request.form['inlineRadioOptions']
        review=Reviews(review=request.form.get("review"), book_id= id, user_id=USER[0].id, star="4")
        db.session.add(review)
        db.session.commit()
        return option
