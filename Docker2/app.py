from flask import jsonify
from db import ma 
from db import db
from controllers.user import User

from resources.user import User, UserList, user_ns
from marshmallow import ValidationError

from server.instance import server

api = server.api
app = server.app

@app.before_first_request
def createTables ():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


api.add_resource(User, '/user/<int:id>')
api.add_resource(UserList, '/user')



if __name__ == '__main__':
    db.init_app()
    ma.init_app()
    server.run()