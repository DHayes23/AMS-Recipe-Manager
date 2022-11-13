from flask import Flask
from application import app
from application.models import User


if __name__ == '__main__':
    app.run(debug=True)