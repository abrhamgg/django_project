# django_project

# Artist API

## Required Technologies
- Python
- django

## Getting Startd

### 1. Package installation
- django -> ``` pip install django ```

### 2. Setting up the enviroment.

### 3. Starting the app
- The app will use port 8000 so stop if there is any program using this port.
- $``` python manage.py runserver```

### 4. Endpoints
- Product routes
    - GET ```/products``` -> returns all products.
    - GET ``` /products/:id``` -> returns a product by id.
    - GET ``` /products/category/:category``` -> returns products with specific category.
    - POST ``` /products``` -> creates a new product. Token is required
    - GET ``` /popular_products``` -> returns 5 products with maximum number of orders.

### 5. Running Tests.
- $ ``` npm test or npm run test```

