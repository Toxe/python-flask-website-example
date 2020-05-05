import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or b"\xe5\xd2\x9b\xe8\xce\xe2[_\xdf)\x0c\x96'\xc2\xc5\xbbS\xf3y\xff\x0b\xca\x18\xe9"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["your-email@example.com"]
    POSTS_PER_PAGE = 3
    LANGUAGES = ["en", "de", "es"]
    MS_TRANSLATOR_KEY = os.environ.get("MS_TRANSLATOR_KEY")
