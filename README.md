# django_project

# Storefront Backend

## Required Technologies
- Postgres for the database
- Node/Express for the application logic
- dotenv from npm for managing environment variables
- db-migrate from npm for migrations
- jsonwebtoken from npm for working with JWTs
- jasmine from npm for testing

## Getting Started

### 1. Package installation
- Express -> ``` npm i express ```
- dotenv -> ``` npm install dontenv```
- db-migrate ->  ```npm install -g db-migrate```  and  ```npm add db-migrate db-migrate-pg```
- jsonwebtoken -> ``` npm add jsonwebtoken```

### 2. Database Setup and Connection.
- By default postgresql will be running in port 5432 or 5433

    #### 2.3 Migration.
    - Run ```db-migrate up``` to check if the database has connected successfully.

### 3. Starting the app
- The app will use port 8000 so stop if there is any program using this port.
- $``` npm run watch```

### 4. Endpoints
- Product routes
    - GET ```/products``` -> returns all products.
    - GET ``` /products/:id``` -> returns a product by id.
    - GET ``` /products/category/:category``` -> returns products with specific category.
    - POST ``` /products``` -> creates a new product. Token is required
    - GET ``` /popular_products``` -> returns 5 products with maximum number of orders.

### 5. Running Tests.
- $ ``` npm test or npm run test```

