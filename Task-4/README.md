# Simple Blog Application

A Flask-based blog application with Create, Read, Update, and Delete (CRUD) functionality.

## Features

✅ **Create** - Write and publish new blog posts  
✅ **Read** - View all posts or individual posts  
✅ **Update** - Edit existing blog posts  
✅ **Delete** - Remove blog posts  
📅 **Timestamps** - Track creation and update times  
🎨 **Responsive Design** - Works on all devices  

## Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

### 3. Open in Browser
Navigate to `http://localhost:5000`

## Project Structure

```
Task-4/
├── app.py                 # Main Flask application
├── posts.json            # Blog posts storage (auto-created)
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── templates/           # HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Home page
│   ├── create.html     # Create post page
│   ├── edit.html       # Edit post page
│   └── view.html       # View single post
└── static/             # Static files
    └── style.css       # Styling
```

## Usage

### Create a Post
1. Click "New Post" in the navigation
2. Enter title and content
3. Click "Publish Post"

### View a Post
1. Click "Read More" on any post card
2. View the full content

### Edit a Post
1. Click "Edit" on any post card
2. Update the title/content
3. Click "Update Post"

### Delete a Post
1. Click "Delete" on any post card
2. Confirm deletion

## Database

Posts are stored in `posts.json` file in JSON format:

```json
[
  {
    "id": 1,
    "title": "My First Post",
    "content": "This is the content...",
    "created_at": "2024-01-15 10:30:00",
    "updated_at": "2024-01-15 10:30:00"
  }
]
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3
- **Storage**: JSON (simple file-based storage)
- **Styling**: Custom CSS with responsive design

## Future Enhancements

- Database integration (SQLAlchemy + SQLite)
- User authentication
- Comments system
- Search functionality
- Tags/Categories
- Rich text editor
- Image upload support

## Author

Created as a web development learning project.
