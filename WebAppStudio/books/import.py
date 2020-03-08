import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://rxdnjvfyrasdzq:ecf7437abe99a4d96dec6549d26525a00063150ca2972b03d3bcf5047aafbf00@ec2-54-247-189-1.eu-west-1.compute.amazonaws.com:5432/ddfn94a62l37c0')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv", "r")
    reader = csv.reader(f)
    next(reader)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
               {"isbn": isbn, "title": title, "author": author, "year": year})
        db.commit()
    print("done")
if __name__ == '__main__':
    main()