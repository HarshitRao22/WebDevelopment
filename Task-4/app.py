from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

POSTS_FILE = 'posts.json'

def load_posts():
    """Load posts from JSON file"""
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_posts(posts):
    """Save posts to JSON file"""
    with open(POSTS_FILE, 'w') as f:
        json.dump(posts, f, indent=2)

def get_next_id():
    """Get the next available post ID"""
    posts = load_posts()
    if not posts:
        return 1
    return max(post['id'] for post in posts) + 1

@app.route('/')
def index():
    """Display all blog posts"""
    posts = load_posts()
    posts.sort(key=lambda x: x['created_at'], reverse=True)
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    """Create a new blog post"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Title and content are required!', 'error')
            return redirect(url_for('create'))
        
        posts = load_posts()
        new_post = {
            'id': get_next_id(),
            'title': title,
            'content': content,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        posts.append(new_post)
        save_posts(posts)
        
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    """Edit a blog post"""
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    
    if not post:
        flash('Post not found!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Title and content are required!', 'error')
            return redirect(url_for('edit', post_id=post_id))
        
        post['title'] = title
        post['content'] = content
        post['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_posts(posts)
        
        flash('Blog post updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit.html', post=post)

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    """Delete a blog post"""
    posts = load_posts()
    posts = [p for p in posts if p['id'] != post_id]
    save_posts(posts)
    
    flash('Blog post deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/view/<int:post_id>')
def view(post_id):
    """View a single blog post"""
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    
    if not post:
        flash('Post not found!', 'error')
        return redirect(url_for('index'))
    
    return render_template('view.html', post=post)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
