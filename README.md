ProjectManager
=====

ProjectManager is a simple Django app to manage projects.

Quick start
-----------

1. Add "project" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'project',
    ]

2. Include the project URLconf in your project urls.py like this::

    path('projects/', include('project.urls')),

3. Run `python manage.py migrate` to create the project models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a project (you'll need the Admin app enabled).