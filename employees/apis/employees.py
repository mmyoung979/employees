"""
Create & delete employee records in a Firestore database
"""
# Third party imports
from flask import jsonify, request
from flask_restful import Resource

# Local imports
from settings import DATABASE
from .utils.db_utils import add_employee, delete_all_employees, get_all_employees


class Employees(Resource):
    def get(self):
        """Return a list of all employees"""
        return jsonify(
            {
                "description": "List of employees",
                "employees": get_all_employees(),
            }
        )

    def post(self):
        """Create new employee doc in the employees collection"""
        # Parse URL parameters
        args = request.args
        first_name = args.get("first_name")
        last_name = args.get("last_name")

        # Create record in database
        add_employee(first_name, last_name)
        data = {
            "message": f"Employee {first_name} {last_name} has been added.",
        }
        return jsonify(data)

    def delete(self):
        """Wipe database"""
        delete_all_employees()
