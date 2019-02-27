from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Post {self.id}>'
        
@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts= posts)
 
@app.route('/posts/new')    
def post_new():
    return render_template('new.html')

@app.route('/posts/create')    
def post_create():
    title = request.args.get('title')
    content = request.args.get('content')
    post = Post(title = title, content = content)
    db.session.add(post)
    db.session.commit()
    return render_template('create.html',post=post)
    
@app.route('/posts/<int:id>')
def post_read(id):
    post = Post.query.get(id)
    return render_template('read.html',post= post)
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8080', debug=True)
    

    
    
    
    
    
    
    
    
    
    
    