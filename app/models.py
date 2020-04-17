from datetime import datetime
from hashlib import md5
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


followers = db.Table("followers",
    db.Column("follower_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("followed_id", db.Integer, db.ForeignKey("user.id")),
)


class User(UserMixin, db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(64), index=True, unique=True)
    email     = db.Column(db.String(100), index=True, unique=True)
    password  = db.Column(db.String(128))
    about_me  = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed  = db.relationship("User",
        secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref("followers", lazy="dynamic"),
        lazy="dynamic",
    )

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return "https://www.gravatar.com/avatar/{}?d=identicon&s={}".format(digest, size)


class Post(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    body      = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id   = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "<Post {}>".format(self.body)


class Ship(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    length       = db.Column(db.Integer)
    crew         = db.Column(db.Integer)
    affiliation  = db.Column(db.String(100))
    category     = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    model        = db.Column(db.String(100))
    ship_class   = db.Column(db.String(100))
    roles        = db.relationship("ShipRole", backref="ship", lazy="dynamic")

    def __repr__(self):
        return "<Ship {}>".format(self.model)


class ShipRole(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    ship_id = db.Column(db.Integer, db.ForeignKey("ship.id"))
    role    = db.Column(db.String(100))

    def __repr__(self):
        return "<ShipRole {}>".format(self.role)
