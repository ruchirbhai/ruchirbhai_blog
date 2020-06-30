# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#
app = Flask(__name__)
#SQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating SQL Alchemy database instance
db = SQLAlchemy(app)

# Import routes here to avoid circular imports
from flaskblog import routes