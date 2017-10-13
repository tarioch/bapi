from flask_restplus.resource import Resource
from flask_restplus import fields
from bapi.api.core import api
from bapi.core.storage import storage

ns = api.namespace('query', description='Operations related to bean-query')

class ValueField(fields.Raw):
    def format(self, value):
        result = {}
        for name, column in value._asdict().items():
            result[name] = str(column)

        return result

query_result = api.model('Query result', {
    'rows' : fields.List(ValueField()),
})

@ns.route('/')
class Query(Resource):
    @api.marshal_with(query_result)
    def get(self):
        _, rows = storage.runQuery('select position, currency')
        
        return {'rows': rows}

