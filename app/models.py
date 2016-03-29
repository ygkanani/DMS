from app import db
from flask.ext.login import LoginManager, UserMixin

keys = db.Table('keys',
    db.Column('tag_id', db.Integer, db.ForeignKey('key.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('document.id'))
)

class Document(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(128), index=True)
	type = db.Column(db.String(5))
	size = db.Column(db.Integer)
	downloads = db.Column(db.Integer)
	path = db.Column(db.String(256), unique=True)
	upload_on = db.Column(db.DateTime)
	tags = db.relationship('Key', secondary=keys, backref=db.backref('documents', lazy='dynamic'))
	
def __repr__(self):
    return '<Document %r>' % (self.title)
        
class Key(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	key = db.Column(db.String(10), unique=True)
	
def __repr__(self):
    return "<Key %r')>" % (self.key)
        
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
	