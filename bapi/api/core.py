from flask_restplus.api import Api
from bapi import __version__
from bapi.core.exception import BapiException

api = Api(version=__version__, title='Beancount REST API',
          description='A REST API for Beancount')

@api.errorhandler(BapiException)
def handle_exception(error):
    return {'message': str(error)}, 400
