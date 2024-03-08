from flask_restful import Resource, reqparse
from models import db, CustomerModel

class CustomerProfile(Resource):
    def get(self, user_id=None):
        if user_id:
            customer = CustomerModel.get_by_id(user_id)
            if customer:
                return customer.to_json(), 200
            else:
                return {'error': 'Customer not found'}, 404
        else:
            return {'error': 'User ID not provided'}, 400

    def put(self, user_id):
        customer = CustomerModel.get_by_id(user_id)
        if customer:
            parser = reqparse.RequestParser()
            parser.add_argument('first_name', type=str)
            parser.add_argument('last_name', type=str)
            parser.add_argument('email', type=str)
            parser.add_argument('phone', type=str)
            parser.add_argument('location', type=str)
            parser.add_argument('age', type=int)
            parser.add_argument('role', type=str)
            parser.add_argument('gender', type=str)
            parser.add_argument('national_id', type=str)
            parser.add_argument('nationality', type=str)
            parser.add_argument('image_url', type=str)
            parser.add_argument('password_hash', type=str)  # Add password field
            args = parser.parse_args()

            # Check if password field is provided and update password if necessary
            if args['password']:
                customer.set_password_hash(args['password_hash'])

            self.update_profile(customer, args)  # Call the update_profile method
            return {'message': 'Customer profile updated successfully'}, 200
        else:
            return {'error': 'Customer not found'}, 404

    def update_profile(self, customer, args):
        """Update the customer's profile with the provided arguments."""
        if args.get('first_name'):
            customer.first_name = args['first_name']
        if args.get('last_name'):
            customer.last_name = args['last_name']
        if args.get('email'):
            customer.email = args['email']
        if args.get('phone'):
            customer.phone = args['phone']
        if args.get('location'):
            customer.location = args['location']
        if args.get('age'):
            customer.age = args['age']
        if args.get('role'):
            customer.role = args['role']
        if args.get('gender'):
            customer.gender = args['gender']
        if args.get('national_id'):
            customer.national_id = args['national_id']
        if args.get('nationality'):
            customer.nationality = args['nationality']
        if args.get('image_url'):
            customer.image_url = args['image_url']
        if args.get('password_hash'):
            customer.set_password_hash(args['password_hash'])    
        
        db.session.commit()
