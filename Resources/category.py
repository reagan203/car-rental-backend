from flask import request
from flask_restful import Resource
from models import db, CategoryModel

class CategoryList(Resource):
    def get(self):
        categories = CategoryModel.query.all()
        categories_data = [category.to_json() for category in categories]
        return {'categories': categories_data}, 200

    def post(self):
        data = request.json
        name = data.get('name')
        image_url = data.get('image_url')
        description = data.get('description')

        # Validate required fields
        if not all([name, image_url, description]):
            return {'error': 'All fields are required'}, 400

        # Check if category with the same name already exists
        existing_category = CategoryModel.query.filter_by(name=name).first()
        if existing_category:
            return {'error': 'Category with this name already exists'}, 409

        # Create a new category object
        category = CategoryModel(name=name, image_url=image_url, description=description)

        # Save the new category to the database
        db.session.add(category)
        db.session.commit()

        return {'message': 'Category added successfully'}, 201


class Category(Resource):
    def get(self, category_id):
        category = CategoryModel.query.get(category_id)
        if category:
            return category.to_json(), 200
        else:
            return {'error': 'Category not found'}, 404

    def put(self, category_id):
        category = CategoryModel.query.get(category_id)
        if category:
            data = request.json
            name = data.get('name')
            image_url = data.get('image_url')
            description = data.get('description')

            # Validate required fields
            if not all([name, image_url, description]):
                return {'error': 'All fields are required'}, 400

            # Update category attributes
            category.name = name
            category.image_url = image_url
            category.description = description

            # Commit changes to the database
            db.session.commit()

            return {'message': 'Category updated successfully'}, 200
        else:
            return {'error': 'Category not found'}, 404

    def delete(self, category_id):
        category = CategoryModel.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return {'message': 'Category deleted successfully'}, 200
        else:
            return {'error': 'Category not found'}, 404
