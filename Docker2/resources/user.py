from flask import request
from flask_restplus import Resource, fields

from models.user import UserModel
from schemas.user import UserSchema

from server.instance import server

user_ns = server.user_ns

ITEM_NOT_FOUND = "User not found."


user_schema = UserSchema()
user_list_schema = UserSchema(many=True)

# Model required by flask_restplus for expect
item = user_ns.model('user', {
    'name': fields.String('user name'),
    'email': fields.String('user email'),
})

class user(Resource):

    def get(self, id):
        user_data = UserModel.find_by_id(id)
        if user_data:
            return user_schema.dump(user_data)
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        user_data = UserModel.find_by_id(id)
        if user_data:
            user_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @user_ns.expect(item)
    def put(self, id):
        user_data = UserModel.find_by_id(id)
        user_json = request.get_json()

        if user_data:
            user_data.pages = user_json['name']
            user_data.title = user_json['email']
        else:
            user_data = user_schema.load(user_json)

        user_data.save_to_db()
        return user_schema.dump(user_data), 200


class userList(Resource):
    @user_ns.doc('Get all the Items')
    def get(self):
        return user_list_schema.dump(UserModel.find_all()), 200

    @user_ns.expect(item)
    @user_ns.doc('Create an Item')
    def post(self):
        user_json = request.get_json()
        user_data = user_schema.load(user_json)

        user_data.save_to_db()

        return user_schema.dump(user_data), 201