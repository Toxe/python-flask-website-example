# Flask SQLAlchemy

## Dependencies

- Python 3.8
- SQLAlchemy
- SQLite
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-RESTful
- python-dotenv
- pylint
- pylint-flask
- pylint-flask-sqlalchemy

## Configuration

### Visual Studio Code

#### `.vscode/settings.json`

```json
{
    "python.linting.pylintArgs": [
        "--load-plugins",
        "pylint-flask",
        "pylint-flask-sqlalchemy"
    ]
}
```

## Running

```
flask run
```
