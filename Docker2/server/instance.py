from flask import Flask, Blueprint
from flask_restplus import Api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title='Flask App')
        self.app.register_blueprint = self.blueprint

        self.api.config['SQLDATABASE'] = 'sqlite:///data.db'
        self.api.config['PROPAGATES_EXCEPTIONS'] = True 
        self.api.config['SQLDATABASE_TRACK_NOTIFICATIONS'] = False


        self.book_ns = self.book_ns()
        
        def book_ns(self, ):
            return self.api.namespace(name= 'Books', description = 'operação relacionada', path='/')


        def run (self, ):
            self.app.run(
                port=5000,
                debug=True,
                host = '0.0.0.0'
            )


server = Server()