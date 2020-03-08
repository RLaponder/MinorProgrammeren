import os
import requests
import xml.etree.ElementTree as ET

from flask import Flask, session, render_template, request, redirect, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/", methods=["GET", "POST"])
def index():
    # When someone tries to login, do the following.
    if request.method == "POST":
        # Check if the entered email is present in the database. If not, show error. 
        email = request.form.get("email")
        user = db.execute("SELECT id, password FROM users WHERE email= :email", {"email": email}).fetchone()
        if user is None:
            return render_template("error.html", message="There is no account with this email. Please register.")

        # Check if the entered password is correct. If not, show error. 
        password = request.form.get("password")
        password_check = db.execute("SELECT id FROM users WHERE password= :password and email= :email", {"password": password, "email": email}).fetchone()
        if password_check is None:
             return render_template("error.html", message="The entered password is incorrect. Please try again.")
        
        # Create a session for the current user. 
        session["user_email"] = email
        session["user_id"] = user.id
        return render_template("index.html", status="loggedin", email=session["user_email"])           
        
    # Check if the current user is already logged in. 
    status = "loggedout"
    try:
        user_email=session["user_email"]
        status="loggedin"
    except KeyError:
        user_email=""
    return render_template("index.html", status=status, email=user_email)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html", action="register", status="loggedout")


@app.route("/succes", methods=["POST"])
def succes():
    if request.method == "POST":
        email = request.form.get("email")
        
        # Show error when the entered e-mail adress is already present in database.
        if db.execute("SELECT id FROM users WHERE email= :email", {"email": email}).fetchone() is not None:
            return render_template("error.html", message="There is already an account with this e-mail adress. Please login.")
        
        # Add user information to database and render succes.html.
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        password = request.form.get("password1")
        db.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)", {"first_name": first_name, "last_name": last_name, "email": email, "password": password})
        db.commit()
        return render_template("succes.html", status="loggedout", message="You have succesfully registered. You can now log in.")


@app.route("/logout")
def logout():
    # Log the current user out and open the index page.
    session.clear()
    return render_template("index.html", status="loggedout")


@app.route("/results", methods=["GET", "POST"])
def results():
    # Check whether the user is logged in. If not, show error. 
    if "user_email" not in session:
        return render_template("error.html", status="loggedout", message="You need to login before you can search for books.")

    status = "loggedin"
    info_type = request.form.get("info_type")
    bookinfo = request.form.get("bookinfo")
    
    # Select the books that perfectly match the entered query. 
    if info_type == "year":
        booklist = db.execute("SELECT * FROM books WHERE year = :bookinfo", {"bookinfo": bookinfo}).fetchall()
    else:
        booklist = db.execute("SELECT * FROM books WHERE UPPER(" + info_type + ") = :bookinfo ORDER BY title", {"bookinfo": bookinfo.upper()}).fetchall()
    
    if len(booklist) != 0:
        return render_template("results.html", status=status, email=session["user_email"], booklist=booklist, message="Found something!")

    # When there is no perfect match, select the books that partially match.
    if info_type != "year":
        booklist = db.execute("SELECT * FROM books WHERE UPPER(" + info_type + ") LIKE :bookinfo ORDER BY title", {"bookinfo": "%" + bookinfo.upper() + "%"}).fetchall()
    if len(booklist) != 0:
        return render_template("results.html", status=status, email=session["user_email"], booklist=booklist, message="Were you looking for this?")
    
    # No matches were found.
    return render_template("results.html", status=status, email=session["user_email"], booklist=booklist, message="We didn't find any books :(...)")


@app.route("/bookpage/<int:book_id>", methods=["GET", "POST"])
def bookpage(book_id):
    # Check whether the user is logged in. If not, show error. 
    if "user_email" not in session:
        return render_template("error.html", message="You need to login to see any details of this book.", status="loggedout")
    
    # Select the book that the user clicked on. Show error if no book shows up.
    book = db.execute("SELECT * FROM books WHERE id = :book_id", {"book_id": book_id}).fetchone()
    if book is None:
        return render_template("error.html", message="It looks like this book does not exist. Please try again.", status="loggedin", email=session["user_email"])
    
    # User posts a review.
    if request.method == "POST":
        user_id = session["user_id"]
        rating = request.form.get("rating")
        written_review = request.form.get("written_review")

        # If the user already left a review for this book, show error.
        if db.execute("SELECT id FROM reviews WHERE user_id = :user_id AND book_id = :book_id", {"user_id": user_id, "book_id": book_id}).fetchone() is not None:
            return render_template("error.html", message="You can only leave one review for a book", status="loggedin", email=session["user_email"])

        # Add review to database.
        db.execute("INSERT INTO reviews (user_id, book_id, rating, written_review) VALUES (:user_id, :book_id, :rating, :written_review)", {"book_id": book.id, "user_id": user_id, "rating": rating, "written_review": written_review})   
        db.commit()

    # Display Goodreads review data.
    goodreads = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "K56wTDOKnTn2GR6RZO2TDw", "isbns": book.isbn}).json()["books"][0]
    ratings_count = goodreads["ratings_count"]
    average_rating = goodreads["average_rating"]

    # Display Goodreads book description.
    url = "https://www.goodreads.com/book/isbn/" + book.isbn + "?key=K56wTDOKnTn2GR6RZO2TDw"
    r = requests.get(url) 
    test = (r.text)
    root = ET.fromstring(test)
    description = root[1][16].text

    # Display own review data.
    reviews = db.execute("SELECT * FROM reviews WHERE book_id = :book_id", {"book_id": book.id}).fetchall()
    listed_reviews = []
    for review in reviews:
        first_name = db.execute("SELECT first_name FROM users WHERE id = :user_id", {"user_id": review.user_id}).fetchone().first_name
        listed_reviews.append((first_name, review))
    
    return render_template("book.html", book=book, status="loggedin", email=session["user_email"], title=book.title, ratings_count=ratings_count, average_rating=average_rating, listed_reviews=listed_reviews, description=description)


# If the user wants to logout via a bookpage, redirect to /logout.
@app.route("/bookpage/logout")
def redirect_logout():
    return redirect("/logout")


@app.route("/api/<isbn>", methods=["GET"])
def api_access(isbn):
    # Select the book and return 404 error when book is not found.
    book = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": isbn}).fetchone()
    if book is None:
        return jsonify({"error": "Invalid isbn"}), 404

    # Select the reviews for this book.
    reviews = db.execute("SELECT * FROM reviews WHERE book_id = :book_id", {"book_id": book.id}).fetchall()
    
    # Count the number of reviews and calculate the average score.
    review_count = 0
    average_score = 0
    for review in reviews:
        review_count += 1
        average_score += review.rating
    if review_count > 0:
        average_score = average_score / review_count

    # Display the JSON response.
    return jsonify(
      Title = book.title,
      Author = book.author,
      Year = book.year,
      ISBN = book.isbn,
      Review_count = review_count,
      Average_score = average_score
    )