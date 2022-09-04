from ma import ma 
from models.user import UserModel

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        user = UserModel
        load_instance = True