from flask import request
from flask_restful import Resource
from models import db, BookingModel

class Bookings(Resource):
    def get(self, booking_id=None):
        if booking_id:
            booking = BookingModel.query.get(booking_id)
            if booking:
                return booking.to_json(), 200
            else:
                return {'error': 'Booking not found'}, 404
        else:
            bookings = BookingModel.query.all()
            bookings_data = [booking.to_json() for booking in bookings]
            return {'bookings': bookings_data}, 200

    def post(self):
        data = request.json
        
        booking = BookingModel(**data)
        db.session.add(booking)
        db.session.commit()
        return {'message': 'Booking added successfully'}, 201

    def put(self, booking_id):
        booking = BookingModel.query.get(booking_id)
        if booking:
            data = request.json
            booking.car_id = data.get('car_id', booking.car_id)
            booking.customer_id = data.get('customer_id', booking.customer_id)
            booking.start_date = data.get('start_date', booking.start_date)
            booking.end_date = data.get('end_date', booking.end_date)
            booking.start_time = data.get('start_time', booking.start_time)
            booking.end_time = data.get('end_time', booking.end_time)
            booking.total_price = data.get('total_price', booking.total_price)
            booking.status = data.get('status', booking.status)
            db.session.commit()
            return {'message': 'Booking updated successfully'}, 200
        else:
            return {'error': 'Booking not found'}, 404

    def delete(self, booking_id):
        booking = BookingModel.query.get(booking_id)
        if booking:
            db.session.delete(booking)
            db.session.commit()
            return {'message': 'Booking deleted successfully'}, 200
        else:
            return {'error': 'Booking not found'}, 404
