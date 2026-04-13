# Web Development Tasks

A comprehensive collection of web development projects showcasing HTML, CSS, JavaScript, and Flask skills.

## Tasks

### Static Web Pages
- **Task-1**: 📝 Portfolio Website - Personal portfolio showcase
- **Task-2**: 📱 Responsive Layout Project - Mobile-friendly responsive design
- **Task-3**: ✨ Interactive Features - Dynamic web interactions

### Flask Web Applications
- **Task-4**: 📚 Blog Application - Create, Read, Update, Delete blog posts with timestamps
- **Task-5**: 📇 Contact Management System - Store and manage contacts with search functionality

## Live Demo Links

### Static Websites (GitHub Pages)
View live demos online:
- [Task-1 Portfolio](https://harshitrao22.github.io/WebDevelopment/Task-1/)
- [Task-2 Responsive Layout](https://harshitrao22.github.io/WebDevelopment/Task-2/)
- [Task-3 Interactive Features](https://harshitrao22.github.io/WebDevelopment/Task-3/)

### Flask Applications (Local Only)
Flask apps must be run locally using the instructions below.

## Project Structure

```
WebDevelopment/
├── Task-1/                 # Portfolio HTML
│   └── index.html
├── Task-2/                 # Responsive Layout HTML
│   └── index.html
├── Task-3/                 # Interactive Features HTML
│   └── index.html
├── Task-4/                 # Flask Blog Application
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── create.html
│   │   ├── edit.html
│   │   └── view.html
│   └── static/
│       └── style.css
├── Task-5/                 # Flask Contact Manager
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── add.html
│   │   ├── edit.html
│   │   ├── view.html
│   │   └── search.html
│   └── static/
│       └── style.css
└── README.md
```

## How to View Static Websites

### Option 1: View Online on GitHub Pages
Simply click the live demo links above!

### Option 2: View Locally
1. Clone the repository: `git clone https://github.com/HarshitRao22/WebDevelopment.git`
2. Navigate to the project folder
3. Open `Task-1/index.html`, `Task-2/index.html`, or `Task-3/index.html` in your browser

## How to Run Flask Applications

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Task-4: Blog Application

1. **Clone the repository**
   ```bash
   git clone https://github.com/HarshitRao22/WebDevelopment.git
   cd WebDevelopment/Task-4
   ```

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   - Navigate to `http://localhost:5000`
   - Start creating and managing blog posts!

### Task-5: Contact Management System

1. **Clone the repository**
   ```bash
   git clone https://github.com/HarshitRao22/WebDevelopment.git
   cd WebDevelopment/Task-5
   ```

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   - Navigate to `http://localhost:5001`
   - Start managing your contacts!

## Technologies Used

### Static Websites
- HTML5
- CSS3
- JavaScript (ES6+)
- Responsive Design

### Flask Applications
- Python 3.8+
- Flask 3.0.0
- Jinja2 Templating
- JSON Data Storage
- HTML5 & CSS3
- Responsive Design

## Features

### Task-4: Blog Application
✅ Create blog posts  
✅ Read all posts or individual posts  
✅ Edit existing posts  
✅ Delete posts  
✅ Timestamps for creation and updates  
✅ Beautiful responsive UI  

### Task-5: Contact Manager
✅ Add new contacts  
✅ View all contacts  
✅ Search contacts by name, email, or phone  
✅ Edit contact information  
✅ Delete contacts  
✅ Direct call/email links  
✅ Contact validation  
✅ Beautiful responsive UI  

## Troubleshooting

### Port Already in Use
If you see "Port already in use" error:
- Task-4 runs on port 5000
- Task-5 runs on port 5001

You can change the port in `app.py` by modifying:
```python
app.run(debug=True, host='0.0.0.0', port=YOUR_PORT)
```

### Module Not Found Error
Make sure you've installed requirements:
```bash
pip install -r requirements.txt
```

### Permission Denied (Mac/Linux)
If you get permission issues, try:
```bash
python3 app.py
```

## Future Enhancements

- User authentication system
- Database integration (SQLAlchemy + SQLite/PostgreSQL)
- Email notifications
- Export functionality (CSV, PDF)
- Advanced search filters
- User-friendly dashboard
- Mobile app version
- Cloud deployment

## Author

**Harshit Rao**  
GitHub: [@HarshitRao22](https://github.com/HarshitRao22)

## License

This project is open source and available for educational purposes.

## Getting Help

For detailed instructions on each application, refer to:
- [Task-4 Blog README](./Task-4/README.md)
- [Task-5 Contact Manager README](./Task-5/README.md)
