#!/usr/bin/env python3
from flask import Flask
from bapi.api.core import api
from bapi.api.query import ns as query_ns
from bapi.core import config

app = Flask(__name__)

api.add_namespace(query_ns)
api.init_app(app)

def main():
    app.run(port=1234, debug=True, threaded=True)

if __name__ == '__main__':
    config.filename = 'dummy.beancount'
    main()
