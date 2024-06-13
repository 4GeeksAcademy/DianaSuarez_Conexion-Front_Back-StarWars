from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),unique=False, nullable=False)
    birth_year = db.Column(db.String(250), unique=False, nullable=False)
    eye_color = db.Column(db.String(250), unique=False, nullable=False)
    hair_color = db.Column(db.String(250), unique=False, nullable=False)
    favorites_people = db.relationship("FavoritePeople", backref="peoples", lazy=True )
    url_img1 = db.Column(db.String(300), nullable=True)

    def __repr__(self):
            return '<People %r>' % self.name

    def serialize(self):
            return {
                "id": self.id,
                "name": self.name,
                "birth_year": self.birth_year, 
                "eye_color": self.eye_color,
                "hair_color":self.hair_color,
                "url_img1" : self.url_img1
            }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    favorite= db.relationship("Favorite", backref="user", lazy=True)
    def __repr__(self):
            return '<User %r>' % self.name

    def serialize(self):
            return {
                "id": self.id,
                "name": self.name,
                "email": self.email,
            }
    
# class Favorite(db.Model):
#     __tablename__ = 'favorite'
#     id = db.Column(db.Integer, primary_key=True)
#     usuario_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     name = db.Column(db.String(250), unique=False, nullable=False)
    
#     def __repr__(self):
#             return '<Favorite %r>' % self.id

#     def serialize(self):
#             return {
#                 "id": self.id,
#                 "name": self.name,
#                 "usuario_id": self.usuario_id
#             }
    
# class FavoritePeople(db.Model):
#     __tablename__ = 'favoritepeople'
#     id = db.Column(db.Integer, primary_key=True)
#     usuario_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     people_id = db.Column(db.Integer, db.ForeignKey("people.id"))
    
#     def __repr__(self):
#             return '<FavoritePeople %r>' % self.id

#     def serialize(self):
#             result = FavoritePeople.query.filter_by(id=self.people_name).first()
#             return {
#                 "id": self.id,
#                 "people_name": result.serialize()["name"],
#                 "user_id": self.user_id
#             }

