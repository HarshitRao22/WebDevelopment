from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = 'contacts_secret_key_2024'

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from JSON file"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    """Save contacts to JSON file"""
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=2)

def get_next_id():
    """Get the next available contact ID"""
    contacts = load_contacts()
    if not contacts:
        return 1
    return max(contact['id'] for contact in contacts) + 1

def is_valid_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    """Validate phone number format"""
    phone = re.sub(r'[\s\-\(\)]', '', phone)
    return len(phone) >= 10 and phone.isdigit()

@app.route('/')
def index():
    """Display all contacts"""
    contacts = load_contacts()
    # Sort by name
    contacts.sort(key=lambda x: x['name'].lower())
    
    # Get statistics
    total_contacts = len(contacts)
    
    return render_template('index.html', contacts=contacts, total_contacts=total_contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    """Add a new contact"""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        address = request.form.get('address', '').strip()
        notes = request.form.get('notes', '').strip()
        
        # Validation
        if not name:
            flash('Name is required!', 'error')
            return redirect(url_for('add_contact'))
        
        if email and not is_valid_email(email):
            flash('Invalid email format!', 'error')
            return redirect(url_for('add_contact'))
        
        if phone and not is_valid_phone(phone):
            flash('Invalid phone number format!', 'error')
            return redirect(url_for('add_contact'))
        
        contacts = load_contacts()
        
        # Check for duplicate name
        if any(c['name'].lower() == name.lower() for c in contacts):
            flash('Contact with this name already exists!', 'warning')
            return redirect(url_for('add_contact'))
        
        new_contact = {
            'id': get_next_id(),
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'notes': notes,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        contacts.append(new_contact)
        save_contacts(contacts)
        
        flash(f'Contact "{name}" added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    """Edit a contact"""
    contacts = load_contacts()
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    
    if not contact:
        flash('Contact not found!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        address = request.form.get('address', '').strip()
        notes = request.form.get('notes', '').strip()
        
        # Validation
        if not name:
            flash('Name is required!', 'error')
            return redirect(url_for('edit_contact', contact_id=contact_id))
        
        if email and not is_valid_email(email):
            flash('Invalid email format!', 'error')
            return redirect(url_for('edit_contact', contact_id=contact_id))
        
        if phone and not is_valid_phone(phone):
            flash('Invalid phone number format!', 'error')
            return redirect(url_for('edit_contact', contact_id=contact_id))
        
        # Check for duplicate name (excluding current contact)
        if any(c['name'].lower() == name.lower() and c['id'] != contact_id for c in contacts):
            flash('Another contact with this name already exists!', 'warning')
            return redirect(url_for('edit_contact', contact_id=contact_id))
        
        contact['name'] = name
        contact['email'] = email
        contact['phone'] = phone
        contact['address'] = address
        contact['notes'] = notes
        contact['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        save_contacts(contacts)
        
        flash(f'Contact "{name}" updated successfully!', 'success')
        return redirect(url_for('view_contact', contact_id=contact_id))
    
    return render_template('edit.html', contact=contact)

@app.route('/view/<int:contact_id>')
def view_contact(contact_id):
    """View a single contact"""
    contacts = load_contacts()
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    
    if not contact:
        flash('Contact not found!', 'error')
        return redirect(url_for('index'))
    
    return render_template('view.html', contact=contact)

@app.route('/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    """Delete a contact"""
    contacts = load_contacts()
    contact_name = next((c['name'] for c in contacts if c['id'] == contact_id), None)
    
    contacts = [c for c in contacts if c['id'] != contact_id]
    save_contacts(contacts)
    
    flash(f'Contact "{contact_name}" deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/search')
def search():
    """Search contacts"""
    query = request.args.get('q', '').strip().lower()
    contacts = load_contacts()
    
    if query:
        results = [c for c in contacts if 
                  query in c['name'].lower() or 
                  query in c['email'].lower() or 
                  query in c['phone'].lower()]
        results.sort(key=lambda x: x['name'].lower())
    else:
        results = []
    
    return render_template('search.html', results=results, query=query)

@app.route('/export')
def export_contacts():
    """Export contacts as JSON"""
    contacts = load_contacts()
    return jsonify(contacts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
