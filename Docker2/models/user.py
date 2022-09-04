from db import db

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Intenger, primary_key='True')
    name = db.Column(db.String, nullable='False', unique='True')
    email = db.Column(db.String, nullable='False', unique='True')

    def __init__(self, name, email ):
         self.name = name
         self.email = email

    def __repr__(self, ):
        return f'UserModel(name = {self.name}, email = {self.email})'

    def json (self, ):
        return {
            'name': self.name,
            'email': self.email
        }


    @classmethod
    def find_by_name(cls, name) -> "UserModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id) -> "UserModel":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls) -> "UserModel":
        return cls.query.all()

    def save_to_db(self,) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self,) -> None:
        db.session.delete(self)
        db.session.commit()

