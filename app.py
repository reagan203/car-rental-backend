from flask import Flask 
from flask_migrate import Migrate
from flask_restful import Api
from flask_bcrypt import Bcrypt
from models import db 
from flask_jwt_extended import JWTManager
from flask_cors import CORS
#resouces.routes
from Resources.profile import CustomerProfile
from Resources.login import Login
from Resources.signup import Signup
from Resources.customers import Customers
from Resources.reviews import Reviews
from Resources.cars import Cars
from Resources.locations import Locations
from Resources.bookings import Bookings
from Resources.category import Category,CategoryList



app = Flask(__name__)

CORS(app)


# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] =('sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)

# Initialize bcrypt
bcrypt = Bcrypt(app)

# Configure JWT
app.config['JWT_SECRET_KEY'] = ( 'super-secret')
jwt = JWTManager(app)

# Create API instance
api = Api(app)




api.add_resource(CustomerProfile, '/profile', '/profile/<int:user_id>')
api.add_resource(Login, '/login')
api.add_resource(Signup, '/signup')
api.add_resource(Customers, '/customers')
api.add_resource(Reviews, '/reviews')
api.add_resource(Cars, '/cars', '/cars/<int:car_id>')
api.add_resource(Locations, '/locations', '/locations/<int:location_id>')
api.add_resource(Bookings, '/bookings', '/bookings/<int:booking_id>')
api.add_resource(Category, '/categories/<int:category_id>')
api.add_resource(CategoryList, '/categorylist')



if __name__ == '__main__':
    app.run(debug=True, port=5000)