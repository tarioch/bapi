from flask import request
from flask_restplus.resource import Resource
from flask_restplus import fields, reqparse
from bapi.api.core import api
from bapi.core.storage import storage
from beancount.core import amount, number, position, inventory

ns = api.namespace('query', description='Operations related to bean-query')


query_arguments = reqparse.RequestParser()
query_arguments.add_argument('query', required=True, help='Query to execute')

class ResultRowField(fields.Raw):
    def format(self, value):
        result = {}
        for name, column in value._asdict().items():
            if isinstance(column, amount.Amount):
                val = self.formatAmount(column)
            elif isinstance(column, number.Decimal):
                val = self.formatDecimal(column)
            elif isinstance(column, position.Position):
                val = self.formatPosition(column)
            elif isinstance(column, inventory.Inventory):
                val = self.formatInventory(column)
            else:
                val = str(column)
                
            result[name] = val

        return result
    
    def formatInventory(self, val):
        res =[]
        for i in val:
            res.append(self.formatPosition(i))
            
        return res
    
    def formatPosition(self, val):
        return {
            'units': self.formatAmount(val.units),
            'cost': self.formatCost(val.cost)
        }
    
    def formatAmount(self, val):
        return {
            'amount': str(val.number),
            'currency': str(val.currency),
        }
        return str(val)
    
    def formatDecimal(self, val):
        return str(val)
    
    def formatCost(self, val):
        if val:
            return str(val)
        else:
            return None

    def schema(self):
        schema = super(ResultRowField, self).schema()
        schema['type'] = 'object'
        schema['additionalProperties'] = {'type': 'string'}

        return schema

query_result = api.model('QueryResult', {
    'rows' : fields.List(ResultRowField(description='Columns', example={'currency': 'CHF', 'amount': '122'}), required=True, description='Result rows'),
})

@ns.route('/')
class Query(Resource):

    @api.expect(query_arguments, validate=True)
    @api.marshal_with(query_result)
    def get(self):
        args = query_arguments.parse_args(request)
        query = args.get('query')
        _, rows = storage.runQuery(query)
        
        return {'rows': rows}

