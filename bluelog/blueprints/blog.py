from flask import Blueprint

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/about')
def about():
    return 'This is the blog page.'