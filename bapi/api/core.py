from flask_restplus.api import Api
from bapi import __version__

api = Api(version=__version__, title='Beancount REST API',
          description='A REST API for Beancount')
