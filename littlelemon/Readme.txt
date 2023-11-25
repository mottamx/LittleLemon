### API Paths

1. **admin/**
   - *Description:* Django default Admin interface.
   - *Usage:* Access the Django Admin interface for administrative tasks.

2. **restaurant/**
   - *Description:* Root of the application.
   - *Usage:* Navigate to the root of the restaurant application.

3. **restaurant/booking/tables/**
   - *Description:* Routes to interact with the Booking model in the database.
   - *Usage:*
     - `GET`: Retrieve a list of bookings.
     - `POST`: Add a new booking to the database.
   - *Authentication:*
     - `GET`: Requires a valid token or Superuser authentication.
     - `POST`: Requires Superuser authentication.

4. **auth/users/**
   - *Description:* Djoser view for managing users (primarily for Superuser).
   - *Usage:* Add, modify, or retrieve user information.
   - *Authentication:* Requires Superuser authentication.

5. **restaurant/menu/**
   - *Description:* Routes for interacting with the Menu model.
   - *Usage:*
     - `GET`: Retrieve a list of menu items.
   - *Authentication:*
     - Requires a valid token or Superuser authentication.

6. **restaurant/menu/<int:pk>**
   - *Description:* View a single element of the Menu model.
   - *Usage:* Retrieve details of a specific menu item.
   - *Authentication:*
     - Requires a valid token or Superuser authentication.

7. **restaurant/api-token-auth/**
   - *Description:* Endpoint for obtaining an authentication token.
   - *Usage:* Make a `POST` request with valid `username` and `password` to obtain a token.
   - *Authentication:* Requires valid user credentials.

8. **restaurant/users/**
   - *Description:* Djoser view for managing users (primarily for Superuser).
   - *Usage:* Add, modify, or retrieve user information.
   - *Authentication:* Requires Superuser authentication.

**MySQL credentials:**
root
flabagaster3D* (temporary for testing)