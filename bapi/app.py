#!/usr/bin/env python3
import click
from flask import Flask
from bapi.api.core import api
from bapi.api.query import ns as query_ns
from bapi.api.repo import ns as repo_ns
from bapi.api.price import ns as price_ns
from bapi.api.transaction import ns as transaction_ns
from bapi.core.storage import storage
from bapi import __version__

@click.command()
@click.option('-p', '--port', type=int, default=1234,
              help='The port to listen on. (default: 1234)')
@click.option('-H', '--host', type=str, default='localhost',
              help='The host to listen on. (default: localhost)')
@click.option('-d', '--debug', is_flag=True,
              help='Turn on debugging.')
@click.option('--repo/--no-repo', default=False)
@click.argument('basedir',
                type=click.Path(exists=True, resolve_path=True))
@click.argument('filename',
                type=click.Path(exists=False, resolve_path=False))
@click.version_option(version=__version__, prog_name='bapi')
def main(basedir, filename, port, host, debug, repo):
    storage.load(basedir, filename)
    
    app = Flask(__name__)

    api.add_namespace(query_ns)
    if repo:
        api.add_namespace(repo_ns)
        api.add_namespace(price_ns)
        api.add_namespace(transaction_ns)

    api.init_app(app)

    app.run(host=host, port=port, debug=debug, threaded=True)

if __name__ == '__main__':
    main()
