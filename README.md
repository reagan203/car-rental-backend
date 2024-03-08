# Car Rentals Backend

This is a backend system for managing car rentals, implemented in Python. It includes models for customers, bookings, categories, cars, and locations, and uses SQLite as the database.

## Setup

1. **Clone the Repository**: 
    ```
    git clone <repository-url>
    ```
2. **Install Dependencies**:
    ```
    pip install -r requirements.txt
    ```
3. **Database Setup**:
    - The SQLite database file is already included (`database.db`). You can find it in the `data` directory.
    - If you need to make changes to the database schema, you can use any SQLite client to modify the `database.db` file directly.

## Models

### Customers
- The `Customers` model represents the customers who rent cars.
- Fields:
  - `id`: Primary key
  - `name`: Name of the customer
  - `email`: Email address of the customer
  - `phone`: Phone number of the customer
  - `address`: Address of the customer

### Bookings
- The `Bookings` model represents the bookings made by customers.
- Fields:
  - `id`: Primary key
  - `customer_id`: Foreign key referencing the `Customers` table
  - `car_id`: Foreign key referencing the `Cars` table
  - `start_date`: Start date of the booking
  - `end_date`: End date of the booking

### Categories
- The `Categories` model represents the categories of cars available for rental.
- Fields:
  - `id`: Primary key
  - `name`: Name of the category
  - `description`: Description of the category

### Cars
- The `Cars` model represents individual cars available for rental.
- Fields:
  - `id`: Primary key
  - `category_id`: Foreign key referencing the `Categories` table
  - `model`: Model of the car
  - `brand`: Brand of the car
  - `year`: Year of the car
  - `color`: Color of the car
  - `license_plate`: License plate number of the car
  - `availability`: Availability status of the car (e.g., available, rented)

### Locations
- The `Locations` model represents the locations where cars are available for rental.
- Fields:
  - `id`: Primary key
  - `name`: Name of the location
  - `address`: Address of the location
  - `city`: City of the location
  - `state`: State of the location
  - `country`: Country of the location

## Usage

- This backend provides APIs for managing customers, bookings, categories, cars, and locations.
- You can explore and test the APIs using tools like Postman or any HTTP client library in Python.
- Refer to the API documentation for detailed information on available endpoints and their usage.

## API Documentation

- Detailed API documentation can be found in the `API.md` file.

## Contributors

- [Your Name](https://github.com/yourusername)

## License

This project is licensed under the [MIT License](LICENSE).
