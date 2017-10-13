from flask_restplus.resource import Resource
from flask_restplus import fields
from bapi.api.core import api
from bapi.core.storage import storage

ns = api.namespace('query', description='Operations related to bean-query')

class ResultRowField(fields.Raw):
    def format(self, value):
        result = {}
        for name, column in value._asdict().items():
            result[name] = str(column)

        return result

    def schema(self):
        schema = super(ResultRowField, self).schema()
        schema['type'] = 'object'
        schema['additionalProperties'] = {'type': 'string'}

        return schema

query_result = api.model('Query result', {
    'rows' : fields.List(ResultRowField(description='Columns', example={'currency': 'CHF', 'amount': '122'}), required=True, description='Result rows'),
})

@ns.route('/')
class Query(Resource):
    @api.marshal_with(query_result)
    def get(self):
        _, rows = storage.runQuery('select position, currency')
        
        return {'rows': rows}

