"""
Example code by Matthew Young August 2021

Create & delete employees from a Firestore database
"""
# Python imports
from os import makedirs

# Third party imports
from flask import Flask, jsonify
from flask_restful import Api

# Local imports
from __init__ import create_app
from apis.employees import Employees

# Instantiate app
app = create_app()
api = Api(app)
api.add_resource(Employees, "/")
