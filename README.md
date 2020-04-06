# Media Repository System

This project is a media repository platform for partnered domain experts. Partnered domain experts can prepare and upload videos through dedicated admin dashboard. Interested viewers can subscribe to the platform and can access content uploaded by domain experts.

## Technologies stack
- **Language:** Python
- **Framework:** Django 
- **Database:** SQLite

## Project Structure

```
[root]
|_website/          - contains website related configs and environment settings/scripts
|___ __init__.py
|___settings.py
|___urls.py
|___asgi.py
|___wsgi.py
|
|_media_repo/       - main server application for media repository
|___ __init__.py
|___admin.py
|___apps.py
|___models.py
|___migrations/
|______ __init__.py
|______ ...
|___tests.py
|
|_media_repo_demo/  - demo application for media repository
|___ __init__.py
|___admin.py
|___apps.py
|___views.py
|___templates/      - HTML templates for views
|______pages/             - main pages to be embedded in base layout
|______partials/          - partial components
|______base_layout.html   - basic page layout
|
|_media/            - protected storage for media loaded by domain expert
|_static/           - static file storage
|_manage.py
|_db.sqlite3        - database file
```

## Prerequisite installations
- Python & Django

## How to run

Execute following command in project's root directory to run locally

```shell
python manage.py runserver
```

Now to login to admin interface visit http://localhost:8000/admin
