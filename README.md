# 🛍️ Product Review System

A **RESTful API** for managing products and reviews, built using **Django** and **Django REST Framework** with role-based JWT authentication.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## ✨ Features

- 🔑 JWT-based authentication system
- 👤 Admin vs Regular user roles
- 📦 Admins can manage (CRUD) products
- 📝 Regular users can review products
- 📊 Aggregated product ratings
- 🔍 Search, filter, and ordering for products
- 🧪 Fully testable with Postman

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/hariprasadmanoj3/product-review-system.git
cd product-review-system

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (optional for admin login)
python manage.py createsuperuser

# 6. Load sample data
python manage.py load_sample_data

# 7. Start development server
python manage.py runserver
