from bapi.api.core import api
from flask_restplus.resource import Resource
from beancount import loader
from beancount.query import query
from bapi.core import config
from bapi.core import storage

ns = api.namespace('query', description='Operations related to bean-query')

@ns.route('/')
class Query(Resource):
    def get(self):
        types, rows = storage.storage.runQuery('select position')
        
        res = []
        for row in rows:
            resRow = []
            res.append(resRow)
            for col in row:
                resRow.append(col.to_string())
        return res 
