# Client Project Tracker: Flask + SQLite REST Dashboard for Freelancers

## Project Overview
The **Client Project Tracker** is a web application built with Flask that helps freelancers manage their client projects efficiently. It allows users to perform CRUD (Create, Read, Update, Delete) operations on project data, ensuring that all projects are organized and easily accessible. The application utilizes Flask-RESTful for API functionality and SQLite for data storage.

## Code Overview
The code is structured around several key components:

1. **`app.py`**: This is the main application file that initializes the Flask app, sets up the database, and defines routes for the web interface and API endpoints.

2. **`Project` Model**: This SQLAlchemy model represents a project with fields for ID, name, description, status, and deadline. It handles the database interactions for project data.

3. **`ProjectForm`**: A Flask-WTF form that facilitates the creation and editing of projects. It includes fields for project name, description, status, and deadline, with server-side validation.

4. **API Resources**: The application defines resources for handling project data:
   - **`ProjectListResource`**: Manages the list of projects, allowing users to retrieve all projects or add a new one.
   - **`ProjectResource`**: Handles operations for individual projects, including retrieval, updating, and deletion.

5. **Templates**: The application includes HTML templates for rendering the dashboard and project forms, utilizing Bootstrap for styling.

## Output
The application provides a dashboard displaying all client projects, with options to add, edit, or delete projects. Users can also interact with the API to manage project data programmatically.

## Required Libraries
To run this project, you need to install the following libraries:
- `Flask`
- `Flask-RESTful`
- `Flask-WTF`
- `Flask-SQLAlchemy`
- `SQLite` (included with Python standard library)

You can install the required libraries using pip:
```bash
pip install Flask Flask-RESTful Flask-WTF Flask-SQLAlchemy
```

## Usage
To run the application, execute the following command in your terminal:
```bash
python app.py
```
Visit `http://127.0.0.1:5000/` in your web browser to access the dashboard. You can also use the API endpoints to manage projects programmatically.
```