"""Variables that can be accessed throughout the microservice"""
# Third party imports
from firebase_admin import credentials, initialize_app, firestore

# Initialize Firestore database client
cert_path = "firebase-sdk.json"
db_cert = credentials.Certificate(cert_path)
db_admin = initialize_app(db_cert)
DATABASE = firestore.client()
