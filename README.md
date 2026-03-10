# eCommerce Admin Panel

A full-stack admin panel for an eCommerce system with **FastAPI** (Python) backend and **vanilla HTML/CSS/JavaScript** frontend.

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Vanilla JS, Fetch API)
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy

## Project Structure

```
ecommerce/
├── app/
│   ├── main.py              # FastAPI app, CORS, static mount
│   ├── database.py          # SQLAlchemy engine, session, get_db
│   ├── models/
│   │   ├── category.py
│   │   ├── subcategory.py
│   │   └── product.py
│   ├── schemas/
│   │   ├── category.py
│   │   ├── subcategory.py
│   │   └── product.py
│   └── routers/
│       ├── dashboard.py     # Dashboard stats API
│       ├── category.py
│       ├── subcategory.py
│       └── product.py
├── frontend/
│   ├── index.html           # Redirects to dashboard
│   ├── dashboard.html
│   ├── categories.html
│   ├── subcategories.html
│   ├── products.html
│   ├── css/
│   │   └── admin.css
│   └── js/
│       ├── api.js
│       ├── categories.js
│       ├── subcategories.js
│       └── products.js
├── requirements.txt
└── README.md
```

## Database Schema

- **Category:** `id`, `title`, `status`, `created_at`
- **SubCategory:** `id`, `category_id`, `name`, `status`, `created_at`
- **Product:** `id`, `title`, `sku`, `category_id`, `subcategory_id`, `size`, `color`, `price`, `status`, `created_at`

SQLite database file: `./ecommerce.db` (created automatically in the project root when you first run the app).

## How to Run

### 1. Create a virtual environment (recommended)

```bash
cd c:\Users\91998\OneDrive\Desktop\ecommerce
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Open the admin panel

- **Admin UI:** [http://localhost:8000/static/dashboard.html](http://localhost:8000/static/dashboard.html) or [http://localhost:8000/admin](http://localhost:8000/admin)
- **API docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Root:** [http://localhost:8000/](http://localhost:8000/)

## Using PostgreSQL

Set the `DATABASE_URL` environment variable before running:

```bash
set DATABASE_URL=postgresql://user:password@localhost:5432/ecommerce
uvicorn app.main:app --reload --port 8000
```

Install the driver: `pip install psycopg2-binary`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/dashboard/stats` | Dashboard counts (categories, subcategories, products, active products) |
| GET/POST | `/api/categories/` | List / Create category |
| GET/PUT/DELETE | `/api/categories/{id}` | Get / Update / Delete category |
| GET/POST | `/api/subcategories/` | List / Create subcategory |
| GET/PUT/DELETE | `/api/subcategories/{id}` | Get / Update / Delete subcategory |
| GET/POST | `/api/products/` | List / Create product |
| GET/PUT/DELETE | `/api/products/{id}` | Get / Update / Delete product |

## Features

- **Dashboard:** Total Categories, Subcategories, Products, Active Products
- **Categories:** CRUD, Activate/Deactivate
- **SubCategories:** CRUD, linked to Category, Activate/Deactivate
- **Products:** CRUD, linked to Category and SubCategory, Size, Color, SKU, Price, Activate/Deactivate
- **UI:** Sidebar navigation, tables with actions, modal forms, responsive layout
