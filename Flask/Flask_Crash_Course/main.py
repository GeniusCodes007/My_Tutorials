import datetime

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']= 'sqlite:///'
db= SQLAlchemy(app)

class Todo(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default= datetime.now())

    def __repr__(self):
        return '<Task %r>' % self.id_

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)