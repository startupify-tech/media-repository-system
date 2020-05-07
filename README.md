# Media Repository System

This project is a media repository platform for partnered domain experts. Partnered domain experts can prepare and upload videos through dedicated admin dashboard. Interested viewers can subscribe to the platform and can access content uploaded by domain experts.

## Technologies stack
- **Language:** Python-v3
- **Framework:** Django-v3 & Django REST
- **Database:** SQLite-v3

## Project Structure

```
[src]
|_website/      - contains website related configs and environment settings/scripts
|___ __init__.py
|___settings.py
|___urls.py
|___asgi.py
|___wsgi.py
|
|_core/         - main server application for media repository
|___ __init__.py
|___admin.py
|___apps.py
|___models.py
|___migrations/
|______ __init__.py
|______ ...
|___tests.py
|
|_demo/         - demo application for media repository (Note:For now refer to core app. Will use demo later)
|___ __init__.py
|___admin.py
|___apps.py
|___views.py
|___templates/      - HTML templates for views (Note: refer to template directory in src/)
|______pages/             - main pages to be embedded in base layout
|______partials/          - partial components
|______base_layout.html   - basic page layout
|
|_templates/    - stores templates used for views
|___home.html   - homepage layout
|___base.html   - Basic page layout to be extended by all templates
|
|_media/        - protected storage for media loaded by domain expert (created automatically on upload)
|_static/       - static file storage
|_manage.py
|_db.sqlite3    - database file
```

## Prerequisite installations
- Python & Django
- Rest framework (pip install djangorestframework)

## How to run

Execute following command in project's root directory to run locally

```shell
py -m venv env
pip install -r requirements.txt
.\env\Scripts\activate
python manage.py runserver
```

Now to login to admin interface visit http://localhost:8000/admin
- username : admin
- password : a1111111

## Coding Practice Followed

**Variable and Type Declarations**

- Used following case style for naming any variable:
  - PascalCase <- for class, interface and other type definitions,
  - snake_case <- for naming class attributes, methods, objects and vars, and
  - UPPERCASE <- for const and enums
- Use meaningful names for naming any variable.
- Any variable, constant or type name should not exceed 32 chars.

**Code formatting**

- Maintain a uniformity while coding.
- Used 4 spaces format for indentation. Always format code using PyCharm's format document option before committing the code.
- Review, cleanup and remove redundant code or imports before pushing changes to repository.

**Code Comments**

- Try to add comments wherever possible to enhance readability of your code.
- If you are using complex logic is complex anywhere referred from any online resource, add reference to it in comments.
- Leave any word of care or note in cases where you want to warn other developers about use of any logic, or comment out any existing logic.

**Git Practices**

- Never push any modifications directly on `master` or any other production branch.
- There are 3 kind of branch types. Use following prefix while creating any branch:
  - Feature branch - `feature/`
  - Hotfix branch - `hotfix/`
  - Release branch - `release/`
- Create a pull request and a reviewer when you are done with the development work and ready for code review.
- While committing your code, use proper and concise messages.
- Never check in secrets, passwords or protected URLs with code. Use env or other config file for saving confidential settings and don't push them on Git repositories.

## *References*

- [Getting started with Django](https://docs.djangoproject.com/en/3.0/intro/)
- [Build an API with Django](https://www.youtube.com/playlist?list=PLLRM7ROnmA9HzbIXYN6D3wOZ0wUrqNs_d)
- [Managing files](https://docs.djangoproject.com/en/3.0/topics/files/)
- [Writing a custom storage system](https://docs.djangoproject.com/en/3.0/howto/custom-file-storage/)
