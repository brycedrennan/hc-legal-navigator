from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Model for user accounts."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)


class LegalCase(db.Model):
    """Model for legal cases."""

    __tablename__ = "legal_cases"

    id = db.Column(db.Integer, primary_key=True)
    case_name = db.Column(db.String(64), index=True, unique=True)
    case_description = db.Column(db.String(256))
    jurisdiction = db.Column(db.String(64))
    practice_area = db.Column(db.String(64))
    legal_system = db.Column(db.String(64))

    def __repr__(self):
        return "<LegalCase {}>".format(self.case_name)
