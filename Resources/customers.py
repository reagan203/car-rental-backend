from flask_restful import Resource
from models import db, CustomerModel

class Customers(Resource):
    def get(self):
        # Query all customers
        customers = CustomerModel.query.all()

        # Serialize customers data to JSON
        customers_data = [customer.to_json() for customer in customers]

        return {'customers': customers_data}, 200
