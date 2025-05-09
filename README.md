# Todo List
A simple system for tracking and managing all home tasks. A task page with information about all user tasks has been implemented, CRUD operations have been developed. There are buttons with logic, this means that when user clicks the button, the "mark as done" button will change -> "Cancel", and vice versa. A tag page with a list of all tags has also been developed, and it also has CRUD operations.
Built with Django.

## Features

- Create, view, update, and delete tasks
- Create, view, update, and delete tags
- Assign tags to tasks
- Display lists of tasks and tags
- Bootstrap and Crispy Forms integration
- Class-Based Views and template rendering

## Technologies

- Python 3.12  
- Django 4.2.9  
- Bootstrap 4
- Django Crispy Forms  

## Installation

1. Clone the repository:

```bash
git clone https://github.com/stager0/todo-list.git
cd todo-list
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
cp .env.example .env
```

5. Run the migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Open your browser and go to:
```bash
http://127.0.0.1:8000/
```