from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import Post, Category
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    categories = Category.query.all()
    return render_template('index.html', posts=posts, categories=categories)

@main.route('/post/<int:post_id>', methods=['GET', 'PUT'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'GET':
        return jsonify(post.to_dict())
    
    elif request.method == 'PUT':
        try:
            post.title = request.form['title']
            post.content = request.form['content']
            post.category_id = request.form['category_id']
            db.session.commit()
            return jsonify({'success': True})
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'error': str(e)})

@main.route('/create', methods=['POST'])
def create():
    try:
        title = request.form['title']
        content = request.form['content']
        category_id = request.form['category_id']
        
        post = Post(
            title=title,
            content=content,
            category_id=category_id
        )
        
        db.session.add(post)
        db.session.commit()
        
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)})

@main.route('/post/<int:post_id>/delete', methods=['DELETE'])
def delete_post(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)})

@main.route('/categories')
def categories():
    categories = Category.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in categories])

@main.route('/category', methods=['POST'])
def create_category():
    try:
        name = request.form['name']
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}) 