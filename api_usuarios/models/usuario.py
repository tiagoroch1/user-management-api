from database.db import db

class Usuario(db.Model):
    id = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)