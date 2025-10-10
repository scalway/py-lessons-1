# Lesson 6: Flask Basics

## Learning Objectives

- Understand web development basics with Flask
- Learn to create routes and handle requests
- Master templates and static files
- Understand form handling
- Learn about request/response cycle

## Topics Covered

### 1. Getting Started
- Installing Flask
- Creating a basic app
- Running the development server

### 2. Routes and Views
- URL routing
- Dynamic routes
- HTTP methods (GET, POST)

### 3. Templates
- Using Jinja2 templates
- Template inheritance
- Passing data to templates

### 4. Forms and Data
- Handling form submissions
- Request data access
- JSON responses

### 5. Static Files
- Serving CSS, JavaScript, images
- Static file organization

## Examples

Install Flask first:
```bash
pip install flask
```

Run the example application:
```bash
python app.py
```

Then visit http://localhost:5000 in your browser.

## Key Concepts

- Flask is a micro web framework
- Routes map URLs to Python functions
- Templates separate logic from presentation
- Use blueprints for larger applications
- Always validate user input

## Project Structure

```
06_flask_basics/
├── app.py              # Main application
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   └── form.html
└── static/             # CSS, JS, images
    └── style.css
```
