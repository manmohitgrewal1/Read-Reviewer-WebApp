from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()

class Books(db.Model):
     __tablename__="books"
     id=db.Column(db.Integer, primary_key=True)
     isbn=db.Column(db.String, nullable=False)
     title=db.Column(db.String, nullable=False)
     author=db.Column(db.String, nullable=False)
     year=db.Column(db.Integer, nullable=False)

class Users(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, nullable=False)
    password=db.Column(db.String,nullable=False)

class Reviews(db.Model):
    __tablename__="reviews"
    id= db.Column(db.Integer, primary_key=True)
    review= db.Column(db.Text, nullable=False)
    book_id= db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    star=db.Column(db.Integer, nullable=False)
    book=db.relationship("Books", backref="reviews", lazy=True)
    user=db.relationship("Users", backref="users", lazy=True)
