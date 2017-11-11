from flask import request
from flask_restplus.resource import Resource
from flask_restplus import fields
from bapi.api.core import api
from bapi.core.storage import storage
from beancount.core.number import D
from beancount.core import amount, data

ns = api.namespace('transaction', description='Transactions')

posting_model = api.model('Posting', {
    'account': fields.String(required=True, description='Account of the posting'),
    'amount': fields.Arbitrary(description='Amount'),
    'currency': fields.String(description='Currency'),
    'cost': fields.Arbitrary(description='Cost'),
    'costCurrency': fields.String(description='Cost Currency'),
})

trx_add_model = api.model('TransactionAdd', {
    'filename': fields.String(required=True, description='Filename of the file'),
    'date': fields.Date(required=True, description='Date of the transaction'),
    'flag': fields.String(enum=['*', '!'], default='*', description='Flag for the transaction'),
    'payee': fields.String('Payee of the transaction'),
    'naration': fields.String('Naration of the transaction'),
    'postings' : fields.List(fields.Nested(posting_model)),
})

@ns.route('/')
class Transaction(Resource):

    @api.expect(trx_add_model, validate=True)
    def put(self):
        requestData = request.json
        
        postings = []
        for reqPost in requestData['postings']:
            if 'cost' in reqPost and 'costCurrency' in reqPost:
                cost = data.CostSpec(
                    D(str(reqPost['cost'])), 
                    None,
                    reqPost['costCurrency'],
                    None,
                    None,
                    None
                )
            else:
                cost = None

            if 'amount' in reqPost and 'currency' in reqPost:
                amt = amount.Amount(D(str(reqPost['amount'])), reqPost['currency'])
            else:
                amt = None

            postings.append(data.Posting(
                reqPost['account'],
                amt,
                cost,
                None,
                None,
                None
            ))
        print(requestData)
        storage.addTransaction(data.Transaction(
            None,
            requestData['date'],
            requestData.get('flag', '*'),
            requestData.get('payee', None),
            requestData.get('naration', None),
            None,
            None,
            postings
        ), requestData['filename'])
        
        return 'ok'
