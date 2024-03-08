from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from models import db, CustomerModel

class Signup(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.pop('password')  # Remove password from data

        # Check if the email is already registered
        if CustomerModel.query.filter_by(email=email).first():
            return {'error': 'Email is already registered'}, 400

        # Create a new customer object
        customer = CustomerModel(**data)

        # Hash the password before saving
        customer.set_password(password)

        # Save the new customer to the database
        db.session.add(customer)
        db.session.commit()

        # Generate access token using Flask-JWT-Extended
        access_token = create_access_token(identity=customer.id)

        return {'access_token': access_token}, 201
