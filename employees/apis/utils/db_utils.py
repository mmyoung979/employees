# Python imports
from random import randint
from typing import List

# Local imports
from settings import DATABASE
from .logging_utils import get_logger

# Global variables
LOGGER = get_logger()


def get_all_employees() -> List[dict]:
    """Query database for all employees"""
    employees = DATABASE.collection("employees").stream()
    data = [employee.to_dict() for employee in employees]
    return data


def add_employee(first_name: str, last_name: str) -> None:
    """Add employee to employee collection"""
    doc_name = f"{first_name.lower()}_{last_name.lower()}"
    doc_ref = DATABASE.collection("employees").document(doc_name)
    doc_ref.set(
        {
            "first_name": first_name,
            "last_name": last_name,
        }
    )
    LOGGER.info(f"Employee {first_name} {last_name} has been added.")


def delete_all_employees() -> None:
    """Delete all docs from employees collection in batches"""
    batch_size = 25
    deleted = 0

    employees = DATABASE.collection("employees").limit(batch_size).stream()
    for employee in employees:
        LOGGER.info(f"Deleting employee {employee.id} => {employee.to_dict()}")
        employee.reference.delete()
        deleted += 1

    if deleted >= batch_size:
        return delete_all_employees()
