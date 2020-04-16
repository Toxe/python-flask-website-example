import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or b"\xe5\xd2\x9b\xe8\xce\xe2[_\xdf)\x0c\x96'\xc2\xc5\xbbS\xf3y\xff\x0b\xca\x18\xe9"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False