from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from models import db, CustomerModel

class Login(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')  # Retrieve the actual password

        if not email or not password:
            return {'error': 'Email and password are required'}, 400

        customer = CustomerModel.query.filter_by(email=email).first()

        if not customer or not customer.check_password(password):  # Check the password
            return {'error': 'Invalid email or password'}, 401

        # Generate access token using Flask-JWT-Extended
        access_token = create_access_token(identity=customer.id)

        # Create the Authorization header
        auth_header = f"Bearer {access_token}"

        return {'access_token': access_token, 'Authorization': auth_header}, 200
