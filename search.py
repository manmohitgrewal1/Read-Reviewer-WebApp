import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
from models import *
from helpers import login_required

app= Flask(__name__)
app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
db.init_app(app)


def main():
    rev=Reviews.query.get(1)
    print(rev)
    review_record_of_logedin_user= Reviews.query.filter(and_(Reviews.user_id== '1', Reviews.book_id== '8')).all()
    print(review_record_of_logedin_user)
    print(rev.book.title)
    print(rev.user.username)

if __name__=="__main__":
    with app.app_context():
        main()
