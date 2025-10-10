"""
Flask Application Example - Basic Web Development

This module demonstrates a basic Flask web application.

To run:
    pip install flask
    python app.py

Then visit http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# In-memory storage for demo purposes
tasks = []


@app.route('/')
def index():
    """Home page."""
    return render_template('index.html', tasks=tasks)


@app.route('/about')
def about():
    """About page."""
    info = {
        'name': 'Flask Basics App',
        'version': '1.0',
        'author': 'Python Lessons'
    }
    return render_template('about.html', info=info)


@app.route('/greet/<name>')
def greet(name):
    """Dynamic route with parameter."""
    return f"<h1>Hello, {name}!</h1>"


@app.route('/add-task', methods=['GET', 'POST'])
def add_task():
    """Handle task form submission."""
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append({'id': len(tasks) + 1, 'text': task, 'done': False})
            return redirect(url_for('index'))
    return render_template('form.html')


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """API endpoint returning JSON."""
    return jsonify(tasks)


@app.route('/api/tasks', methods=['POST'])
def create_task():
    """API endpoint for creating a task."""
    data = request.get_json()
    task = {
        'id': len(tasks) + 1,
        'text': data.get('text', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify(task), 201


@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    """Toggle task completion status."""
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            break
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Delete a task."""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return "<h1>404 - Page Not Found</h1><p>The page you're looking for doesn't exist.</p>", 404


@app.errorhandler(500)
def internal_error(e):
    """Custom 500 error page."""
    return "<h1>500 - Internal Server Error</h1><p>Something went wrong on our end.</p>", 500


if __name__ == '__main__':
    print("=" * 50)
    print("FLASK APPLICATION STARTING")
    print("=" * 50)
    print("\nAvailable routes:")
    print("  - http://localhost:5000/")
    print("  - http://localhost:5000/about")
    print("  - http://localhost:5000/greet/<name>")
    print("  - http://localhost:5000/add-task")
    print("\nAPI endpoints:")
    print("  - GET  http://localhost:5000/api/tasks")
    print("  - POST http://localhost:5000/api/tasks")
    print("\n" + "=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
