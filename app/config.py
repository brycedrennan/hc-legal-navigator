import os

# Configure the application
class Config(object):
    # Set the secret key
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret-key"

    # Set the database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")

    # Set the database to track modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
