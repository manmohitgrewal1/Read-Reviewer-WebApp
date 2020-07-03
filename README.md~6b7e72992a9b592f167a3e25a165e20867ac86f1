# Project 1
Completed this project in following steps:

1. Established database by installing postgresql and then creating a app on heroku.
2. Once account is made in heroku then visited adminer and entered heroku's Credentials info in it.
3. Configured my SQLAlchemy database by running "export DATABASE_URL=postgres://ikflpanwhzokex:9b2153bb8624b9de3f9ead9c2c4abfb3ef791d5bad4431be22607332083dad7d@ec2-18-206-84-251.compute-1.amazonaws.com:5432/d9v3cc6jr7gg10" in the terminal window with active pyenv manmo_codes.
4. Now every thing it up and runniing and all we need to do is create a code. Flask micro framework use application.py to do its thing. I created follloeing routes:
a. index - "/"
b. register- "/register"
c. login - "/login"
d. logout - "/logout"
e. review - "/review/<id>"
5. Stated with importing login_required method from helper.py (which is a filed I took from github open source). Helper.py provided us with decorator login_required that is sticked with every route so as to make sure when ever a user hop from a page to another he is always logied in.
6. Next step is to make register route. using post request method we get the form input of user's username and password form registed.html. Then we enterd the same into our data base using db.session.add. Also for browser to know how is logged in we updated our session['user_id']. once a user is registerd we redirect the user to login page.
  <img src="ssRegister.png" height="200">
7. Then we establish our login route. using post request method we get the form input of user's username and password from login.html. Then we match the same to our database if the same username and password exist in our database then we redirect our user to index page.
  <img src="ssLogin.png" height="200">
8. Search page is the index route. In this page a user can search any book that is in our books database (got the data from the api of goodreads) by entering either title or author or isbn number. THe user does even need to provide the full info. our code is smart enought to guess books the similar input. 
  <img src="ssHome.png" height="200">
9. When user selects a book then he can view all the details about the book and also he can leave review about it. The user can also see reviews of other users. 
  <img src="ssSearch.png" height="200">
10. User can logout by pressing logout button on the top anytime.
11. In the web application we have adopted object realation mapping method. We have created classes which creates and represents tables in the database. we have associated foreign keys to some colums and used db.relationship() so that our app can give use more functionality. 

**Go check out my YOUTUBE video that will show working of this web application <br>Link for the video: <a src="https://www.youtube.com/watch?v=7-xl-usf27s"> https://www.youtube.com/watch?v=7-xl-usf27s</a>**
