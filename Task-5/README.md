# Contact Management System

A Flask-based contact management application where users can store, organize, and manage their contacts efficiently.

## Features

✅ **Create** - Add new contacts with detailed information  
✅ **Read** - View all contacts or individual contact details  
✅ **Update** - Edit existing contact information  
✅ **Delete** - Remove contacts from your database  
🔍 **Search** - Find contacts by name, email, or phone number  
📊 **Statistics** - See total contact count  
📞 **Call & Email Links** - Direct links to call or email contacts  
📱 **Responsive Design** - Works on all devices  
💾 **JSON Storage** - Simple file-based data storage  

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
Navigate to `http://localhost:5001`

## Project Structure

```
Task-5/
├── app.py                 # Main Flask application
├── contacts.json         # Contacts storage (auto-created)
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── templates/           # HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # All contacts
│   ├── add.html        # Add contact form
│   ├── edit.html       # Edit contact form
│   ├── view.html       # View single contact
│   └── search.html     # Search results
└── static/             # Static files
    └── style.css       # Styling
```

## Usage

### Add a Contact
1. Click **"+ Add Contact"** in the navigation
2. Fill in contact details (name is required)
3. Email and phone are validated for format
4. Click **"✅ Add Contact"**

### View All Contacts
- Go to **"All Contacts"** or home page
- See all contacts in a grid layout
- Contacts are sorted alphabetically

### Search Contacts
1. Click **"🔍 Search"** in the navigation
2. Enter search term (name, email, or phone)
3. View matching results
4. Search from home page using the search box

### View Contact Details
1. Click **"👁️ View"** on any contact card
2. See full contact information
3. See creation and update timestamps
4. Access call/email links

### Edit a Contact
1. Click **"✏️ Edit"** on any contact card
2. Update desired information
3. Click **"✏️ Update Contact"**

### Delete a Contact
1. Click **"🗑️ Delete"** on any contact card
2. Confirm deletion
3. Contact is permanently removed

## Data Storage

Contacts are stored in `contacts.json` file in JSON format:

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1234567890",
    "address": "123 Main St, City, State",
    "notes": "Important client",
    "created_at": "2024-04-05 10:30:00",
    "updated_at": "2024-04-05 10:30:00"
  }
]
```

## Validation

- **Name**: Required, must be unique, max 100 characters
- **Email**: Optional, must be valid email format
- **Phone**: Optional, must have at least 10 digits
- **Address**: Optional, free text
- **Notes**: Optional, free text

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3 with responsive design
- **Storage**: JSON (file-based storage)
- **Styling**: Custom CSS with modern design

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | View all contacts |
| `/add` | GET, POST | Add new contact |
| `/edit/<id>` | GET, POST | Edit contact |
| `/view/<id>` | GET | View contact details |
| `/delete/<id>` | POST | Delete contact |
| `/search` | GET | Search contacts |
| `/export` | GET | Export contacts as JSON |

## Future Enhancements

- Database integration (SQLAlchemy + SQLite/PostgreSQL)
- User authentication & accounts
- Contact groups/categories
- Duplicate contact detection
- Contact photo/avatar support
- Export to CSV/VCF format
- Backup & restore functionality
- Contact sharing
- Birthday reminders

## Tips

- Use the search feature for quick access to frequently used contacts
- Add notes to remember important details about contacts
- Contacts are automatically sorted alphabetically
- Email and phone links make it easy to reach out instantly

## Author

Created as a web development learning project.
