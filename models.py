from app import db

class Blogpost(db.model):

	_tablename_ = "posts"

	id = db.column(db.integer, primary_key=True)