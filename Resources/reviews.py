from flask import request
from flask_restful import Resource
from models import db, ReviewModel

class Reviews(Resource):
    def post(self):
        data = request.json
        rating = data.get('rating')
        comment = data.get('comment')

        # Validate required fields
        if not all([rating, comment]):
            return {'error': 'Rating and comment are required'}, 400

        # Create a new review object
        review = ReviewModel(
            rating=rating,
            comment=comment
        )

        # Save the new review to the database
        db.session.add(review)
        db.session.commit()

        return {'message': 'Review added successfully'}, 201

    def get(self):
        reviews = ReviewModel.query.all()
        reviews_data = [review.to_json() for review in reviews]
        return {'reviews': reviews_data}, 200
    
    
