from app import db

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email    = db.Column(db.String(100), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)


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
