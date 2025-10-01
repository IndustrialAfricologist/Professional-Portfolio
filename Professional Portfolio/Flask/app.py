import os
import logging
from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Optional
from sqlalchemy.exc import SQLAlchemyError

# Configuration class for Flask application setting
class Config:
    """Configuration settings for the Flask application."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')  # Use environment variable for database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications to save resources
    SECRET_KEY = os.urandom(24)  # Generates a random 24-byte key for session management

# Initialize the app and database
app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from the Config class
db = SQLAlchemy(app)  # Initialize the SQLAlchemy database instance
api = Api(app)  # Initialize the Flask-Restful API

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Project model for the database
class Project(db.Model):
    """Model representing a project in the database."""
    project_id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the project
    name = db.Column(db.String(100), nullable=False)  # Name of the project
    description = db.Column(db.String(200), nullable=True)  # Description of the project
    status = db.Column(db.String(50), nullable=False)  # Current status of the project
    deadline = db.Column(db.Date, nullable=True)  # Deadline for the project

    def __repr__(self):
        return f'<Project {self.name}>'  # String representation of the project

# Define the form for creating and editing projects
class ProjectForm(FlaskForm):
    """Form for creating and editing projects."""
    name = StringField('Project Name', validators=[DataRequired()])  # Project name field
    description = TextAreaField('Description', validators=[Optional()])  # Project description field
    status = SelectField('Status', choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], validators=[DataRequired()])  # Project status field
    deadline = DateField('Deadline', format='%Y-%m-%d', validators=[Optional()])  # Project deadline field
    submit = SubmitField('Submit')  # Submit button

def delete_project_by_id(project_id):
    """Delete a project by its ID."""
    project = Project.query.get_or_404(project_id)  # Retrieve the project or return a 404 error
    db.session.delete(project)  # Delete the project from the session
    db.session.commit()  # Commit the session to save changes

@app.route('/project/delete/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    """Handle project deletion via web interface."""
    try:
        delete_project_by_id(project_id)  # Attempt to delete the project
        flash('Project deleted successfully!', 'success')
        return redirect(url_for('dashboard'))  # Redirect to the dashboard after deletion
    except SQLAlchemyError as e:  # Catch specific SQLAlchemy errors
        logging.error("Error deleting project %d: %s", project_id, e)  # Log the error
        flash('Error deleting project', 'danger')
        return jsonify({'message': 'Error deleting project'}), 500  # Return an error response

# Resource for handling a list of projects
class ProjectListResource(Resource):
    """Resource for handling a list of projects."""
    def get(self):
        """Retrieve all projects."""
        projects = Project.query.all()  # Retrieve all projects from the database
        # Return a list of project details
        return [{'id': project.project_id, 'name': project.name, 'description': project.description, 'status': project.status, 'deadline': project.deadline} for project in projects]

    def post(self):
        """Create a new project."""
        data = request.get_json()  # Get JSON data from the request
        if not data or 'name' not in data or 'status' not in data:
            return {'message': 'Invalid input'}, 400  # Validate input data
        
        new_project = Project(
            name=data['name'],
            description=data.get('description'),
            status=data['status'],
            deadline=data.get('deadline')
        )
        db.session.add(new_project)  # Add the new project to the session
        db.session.commit()  # Commit the session to save the new project
        return {'id': new_project.project_id}, 201  # Return the ID of the newly created project with a 201 status code

# Resource for handling a specific project by ID
class ProjectResource(Resource):
    """Resource for handling a specific project by its ID."""
    def get(self, project_id):
        """Retrieve a specific project by ID."""
        project = Project.query.get_or_404(project_id)  # Retrieve the project by ID or return a 404 error if not found
        return {'id': project.project_id, 'name': project.name, 'description': project.description, 'status': project.status, 'deadline': project.deadline}

    def put(self, project_id):
        """Update a specific project by ID."""
        project = Project.query.get_or_404(project_id)  # Retrieve the project by ID or return a 404 error if not found
        data = request.get_json()  # Get JSON data from the request
        if not data or 'name' not in data or 'status' not in data:
            return {'message': 'Invalid input'}, 400  # Validate input data
        
        # Update project attributes with new data
        project.name = data['name']
        project.description = data.get('description')
        project.status = data['status']
        project.deadline = data.get('deadline')
        db.session.commit()  # Commit the session to save changes
        return {'message': 'Project updated successfully'}  # Return a success message

    def delete(self, project_id):
        """Delete a specific project by ID."""
        try:
            delete_project_by_id(project_id)  # Attempt to delete the project
            return {'message': 'Project deleted successfully'}  # Return success message
        except SQLAlchemyError as e:  # Catch specific SQLAlchemy errors
            logging.error("Database error: %s", e)  # Log the error
            return {'message': 'Error deleting project'}, 500  # Return an error response

# Register API routes
api.add_resource(ProjectListResource, '/api/projects')  # Route for listing and creating projects
api.add_resource(ProjectResource, '/api/projects/<int:project_id>')  # Route for retrieving, updating, and deleting a specific project

# Home route to render the dashboard
@app.route('/')
def dashboard():
    """Render the project dashboard."""
    projects = Project.query.all()  # Query all projects from the database
    return render_template('dashboard.html', projects=projects)  # Render the dashboard template with projects

# Route to handle project creation and editing
@app.route('/project/new', methods=['GET', 'POST'])
@app.route('/project/edit/<int:project_id>', methods=['GET', 'POST'])
def create_or_edit_project(project_id=None):
    """Handle project creation or editing via web interface."""
    form = ProjectForm()  # Instantiate the project form

    if project_id:  # If editing an existing project
        project = Project.query.get_or_404(project_id)
        if request.method == 'GET':
            form.name.data = project.name
            form.description.data = project.description
            form.status.data = project.status
            form.deadline.data = project.deadline

    if form.validate_on_submit():  # Check if the form is submitted and valid
        if project_id:  # Update existing project
            project.name = form.name.data
            project.description = form.description.data
            project.status = form.status.data
            project.deadline = form.deadline.data
            flash('Project updated successfully!', 'success')
        else:  # Create new project
            project = Project(
                name=form.name.data,
                description=form.description.data,
                status=form.status.data,
                deadline=form.deadline.data
            )
            db.session.add(project)  # Add the project to the session
            flash('Project created successfully!', 'success')

        db.session.commit()  # Commit the session to save the project
        return redirect(url_for('dashboard'))  # Redirect to the dashboard after creation or update
    return render_template('project_form.html', form=form)  # Render the project form template

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()  # Create all database tables defined by the models

if __name__ == '__main__':
    app.run(debug=False)  # Run the application in debug mode; set to False for production