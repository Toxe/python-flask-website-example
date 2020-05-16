# Flask Website Example/Test

A simple Flask website example/test based mostly on [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg.

## Dependencies

- Python 3
- SQLAlchemy
- SQLite
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-Mail
- Flask-Bootstrap
- Flask-Moment
- Flask-Babel
- Flask-HTTPAuth
- PyJWT
- python-dotenv
- pylint
- pylint-flask
- pylint-flask-sqlalchemy
- Click
- Requests
- guess_language-spirit

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

## Import ships example data

```
sqlite3 app.db < ships.sql
```

## Running

```
flask run
```

## Translation

### Add a new language

For example add support for German (`de`):

```
flask translate init de
```

### Update all languages

```
flask translate update
```

### Compile translation files

```
flask translate compile
```
