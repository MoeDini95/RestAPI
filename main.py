from flask import Flask
from flask_restful import Api, Resource


app = Flask (__name__)
api = Api(app)


# First resource as a 'get' request
class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}


# Registering this api request as a resource 
api.add_resource(HelloWorld, "/helloworld")

# This will start the server and start the application server 
# it will also run debug mode 
if __name__ == "__main__":
    app.run(debug=True)

