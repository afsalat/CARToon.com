# CARToon_com 🎨🛒

An e-commerce platform built with Django, providing seamless user management, a shopping cart system, and easy product browsing. CARToon_com is designed to offer a smooth, efficient shopping experience for users.

## 🚀 Features
- **User Authentication**: Secure signup, login, and logout.
- **Shopping Cart**: Easily add, view, and manage products in the cart.
- **Product Display**: View detailed information for each product.
- **Responsive Interface**: User-friendly templates for all devices.

## 🛠️ Technologies
- **Backend**: Django, Django ORM
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default, can be switched to PostgreSQL/MySQL)
- **Authentication & Security**: Django’s built-in user authentication, CSRF protection

## 📥 Installation

### Prerequisites
- Python 3.7 or higher
- Django 4.2 or higher

### Setup
1. **Clone this repository**:
    ```bash
    git clone https://github.com/your-username/CARToon_com.git
    cd CARToon_com
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access)**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Visit the application**:
   Open your browser at `http://127.0.0.1:8000`.

## 🧭 Usage Guide

### User Authentication
- **Sign Up**: Register a new account.
- **Login**: Access your account.
- **Logout**: Securely log out.

### Shopping Cart
- **Add Products**: Easily add items to the cart from the product page.
- **View Cart**: See all items in your cart.
- **Update Cart**: Increase/decrease quantities or remove items as needed.

## 🔗 Key Endpoints

| URL                         | Method | Description                     |
|-----------------------------|--------|---------------------------------|
| `/accounts/login/`          | GET/POST | User login page                |
| `/accounts/logout/`         | GET    | Logs out the user               |
| `/add-to-cart/<id>/`        | POST   | Adds a product to the cart      |
| `/view-cart/`               | GET    | View cart items                 |
| `/update-cart/<action>/<id>/` | POST | Modify quantity or remove item |

## 🛠 Troubleshooting

### Common Issues
- **TemplateDoesNotExist**: Verify the template files exist in the correct directories.
- **Invalid Form**: Ensure all fields are completed and CSRF tokens are included.
- **Static Files Issue**: Run `python manage.py collectstatic` if static files are not displaying in production.

### Enable Logging
Add the following to `settings.py` to log errors:

```python
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },