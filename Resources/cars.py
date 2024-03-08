from flask import request
from flask_restful import Resource
from models import db, CarModel

class Cars(Resource):
    def get(self, car_id=None):
        try:
            if car_id:
                car = CarModel.query.get(car_id)
                if car:
                    return car.to_json(), 200
                else:
                    return {'error': 'Car not found'}, 404
            else:
                cars = CarModel.query.all()
                cars_data = [car.to_json() for car in cars]
                return {'cars': cars_data}, 200
        except Exception as e:
            return {'error': str(e)}, 500

    def post(self):
        data = request.json
        car = CarModel(**data)
        db.session.add(car)
        db.session.commit()
        return {'message': 'Car added successfully'}, 201

    def put(self, car_id):
        car = CarModel.query.get(car_id)
        if car:
            data = request.json
            car.make = data.get('make', car.make)
            car.model = data.get('model', car.model)
            car.year = data.get('year', car.year)
            car.color = data.get('color', car.color)
            car.licence_plate = data.get('licence_plate', car.licence_plate)
            car.rental_rate = data.get('rental_rate', car.rental_rate)
            car.image_url = data.get('image_url', car.image_url)
            car.availability_status = data.get('availability_status', car.availability_status)
            car.category_id = data.get('category_id', car.category_id)
            db.session.commit()
            return {'message': 'Car updated successfully'}, 200
        else:
            return {'error': 'Car not found'}, 404

    def delete(self, car_id):
        car = CarModel.query.get(car_id)
        if car:
            db.session.delete(car)
            db.session.commit()
            return {'message': 'Car deleted successfully'}, 200
        else:
            return {'error': 'Car not found'}, 404
