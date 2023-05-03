# django_project

# Artist API

## Required Technologies
- Python
- django

## Getting Startd
- Make sure you have python installed.
### 1. Package installation
- django -> ``` pip install django ```

### 2 Starting the app
- The app will use port 8000 so stop if there is any program using this port.
- $``` python manage.py runserver ```
- $``` python manage.py runserver <port_mum> ```

### 3 Endpoints
- admin route - ```http://127.0.0.1:8000/admin``` use admin- admin as credentials or you can create your own superuser.

    - GET ```http://127.0.0.1:8000/api/works``` -> returns all works.
    - GET ``` http://127.0.0.1:8000/api/works?artist=[Artist Name]``` -> Integrate Search with Artist name.
    - GET ``` http://127.0.0.1:8000/api/works?work_type=Youtube``` -> Integrate Filtering with Work Type.
    - POST ``` http://127.0.0.1:8000/api/register``` -> creates a new user.


