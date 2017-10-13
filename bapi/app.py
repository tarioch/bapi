#!/usr/bin/env python3
from flask import Flask
from bapi.api.core import api
from bapi.api.query import ns as query_ns
from bapi.core.storage import storage

def main():
    storage.load('dummy.beancount')
    
    app = Flask(__name__)

    api.add_namespace(query_ns)
    api.init_app(app)

    app.run(port=1234, debug=True, threaded=True)

if __name__ == '__main__':
    main()
