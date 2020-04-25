from app import app, db, cli
from app.models import User, Ship, ShipRole

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Ship": Ship, "ShipRole": ShipRole}
