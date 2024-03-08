from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash,generate_password_hash



db = SQLAlchemy()

class CustomerModel(db.Model):
    """Model representing a customer."""
    __tablename__ = "customers"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)  
    age = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(30), server_default='User')
    gender = db.Column(db.String(10), nullable=False)
    national_id = db.Column(db.String(20), nullable=False, unique=True)  # Unique National ID Number
    nationality = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # Store hashed passwords
    created_at = db.Column(db.TIMESTAMP(), default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP(), onupdate=db.func.now())
    bookings = db.relationship('BookingModel', backref='customer', lazy=True)
    
    @classmethod
    def get_by_id(cls, customer_id):
        """Get a customer by ID."""
        return cls.query.get(customer_id)

    def set_password(self, password):
        """Set the password for the customer."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored password."""
        return check_password_hash(self.password_hash, password)

    def to_json(self):
     """Convert the customer object to a JSON-serializable dictionary."""
     return {
        'id': self.id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'email': self.email,
        'phone': self.phone,
        'location': self.location,
        'age': self.age,
        'role': self.role,
        'gender': self.gender,
        'national_id': self.national_id,
        'nationality': self.nationality,
        'image_url': self.image_url,
        'created_at': self.created_at.isoformat() if self.created_at else None,
        'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        'bookings': [booking.to_json() for booking in self.bookings]
    }





class CarModel(db.Model):
    """Model representing a car."""
    __tablename__ = "cars"
    
    car_id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(20), nullable=False)
    licence_plate = db.Column(db.String(20), unique=True, nullable=False)
    rental_rate = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    availability_status = db.Column(db.String, default=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)  # Corrected foreign key   
    bookings = db.relationship('BookingModel', backref='car', lazy=True)
    
    def to_json(self):
        return {
            'car_id': self.car_id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'color': self.color,
            'licence_plate': self.licence_plate,
            'rental_rate': self.rental_rate,
            'image_url': self.image_url,
            'availability_status': self.availability_status,
            'category_id': self.category_id
        }
    
class BookingModel(db.Model):
    """Model representing a booking."""
    __tablename__ = "bookings"
    
    booking_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey("cars.car_id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    start_date = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False)
    total_price = db.Column(db.Float, nullable=False)  
    status = db.Column(db.String(20), nullable=False)  # Add booking status
    
    
    def to_json(self):
        return {
            'booking_id': self.booking_id,
            'car_id': self.car_id,
            'customer_id': self.customer_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'total_price': self.total_price,
            'status': self.status
        }

class LocationModel(db.Model):
    """Model representing a location."""
    __tablename__ = "locations"
    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(100), nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    contact_email = db.Column(db.String(120), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    
    def to_json(self):
        """Convert the location object to a JSON-serializable dictionary."""
        return {
            'location_id': self.location_id,
            'location_name': self.location_name,
            'contact_person': self.contact_person,
            'contact_number': self.contact_number,
            'contact_email': self.contact_email,
            'image_url': self.image_url
        }

class ReviewModel(db.Model):
    """Model representing a review."""
    __tablename__ = "reviews"
    review_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    car_id = db.Column(db.Integer, db.ForeignKey("cars.car_id"))
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(1000), nullable=False)
    
    def to_json(self):
        return {
            'review_id': self.review_id,
            'customer_id': self.customer_id,
            'car_id': self.car_id,
            'rating': self.rating,
            'comment': self.comment
        }

class PaymentModel(db.Model):
    """Model representing a payment."""
    __tablename__ = "payments"
    payment_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey("cars.car_id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.booking_id"))
    payment_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.TIMESTAMP(), default=db.func.now())

    booking = db.relationship('BookingModel', backref='payments', lazy=True)
    
class CategoryModel(db.Model):
     """Model representing a category of car."""
     __tablename__ = 'categories'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(30), nullable=False, unique=True)
     image_url = db.Column(db.String(255), nullable=False) 
     description = db.Column(db.String(255), nullable=False) 
     cars = db.relationship('CarModel', backref='category', lazy=True)
     
     def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_url': self.image_url,
            'description': self.description
        }
