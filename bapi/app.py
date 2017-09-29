#!/usr/bin/env python3
from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

def main():
    app.run(host='0.0.0.0', port=1234, debug=True, threaded=True)

if __name__ == '__main__':
    main()
