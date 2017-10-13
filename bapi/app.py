#!/usr/bin/env python3
import click
from flask import Flask
from bapi.api.core import api
from bapi.api.query import ns as query_ns
from bapi.core.storage import storage
from bapi import __version__

@click.command()
@click.argument('filename',
                type=click.Path(exists=True, resolve_path=True))
@click.version_option(version=__version__, prog_name='bapi')
def main(filename):
    storage.load(filename)
    
    app = Flask(__name__)

    api.add_namespace(query_ns)
    api.init_app(app)

    app.run(port=1234, debug=True, threaded=True)

if __name__ == '__main__':
    main()
