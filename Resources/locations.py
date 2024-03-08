from flask import request
from flask_restful import Resource
from models import db, LocationModel

class Locations(Resource):
    def get(self, location_id=None):
        if location_id:
            location = LocationModel.query.get(location_id)
            if location:
                return location.to_json(), 200
            else:
                return {'error': 'Location not found'}, 404
        else:
            locations = LocationModel.query.all()
            locations_data = [location.to_json() for location in locations]
            return {'locations': locations_data}, 200

    def post(self):
        data = request.json
        location = LocationModel(**data)
        db.session.add(location)
        db.session.commit()
        return {'message': 'Location added successfully'}, 201

    def put(self, location_id):
        location = LocationModel.query.get(location_id)
        if location:
            data = request.json
            location.location_name = data.get('location_name', location.location_name)
            location.contact_person = data.get('contact_person', location.contact_person)
            location.contact_number = data.get('contact_number', location.contact_number)
            location.contact_email = data.get('contact_email', location.contact_email)
            location.image_url = data.get('image_url', location.image_url)
            db.session.commit()
            return {'message': 'Location updated successfully'}, 200
        else:
            return {'error': 'Location not found'}, 404

    def delete(self, location_id):
        location = LocationModel.query.get(location_id)
        if location:
            db.session.delete(location)
            db.session.commit()
            return {'message': 'Location deleted successfully'}, 200
        else:
            return {'error': 'Location not found'}, 404
