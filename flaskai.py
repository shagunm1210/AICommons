from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Base
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/shagun'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Companies(Base):
	id = db.Column(db.Integer, primary_key=True)
	company_name = db.Column(db.String(80), unique=True)
	category = db.Column(db.String(50))
	mission = db.Column(db.String(10000))
	product = db.Column(db.String(10000))




@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)

