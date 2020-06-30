# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#
app = Flask(__name__)
#Create a Secret key and initialize the app
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba246'   # This is copied from tutorial change when implementing user accounts

#SQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating SQL Alchemy database instance
db = SQLAlchemy(app)

# Import routes here to avoid circular imports
from flaskblog import routes