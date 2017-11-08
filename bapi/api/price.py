from flask import request
from flask_restplus.resource import Resource
from flask_restplus import fields
from bapi.api.core import api
from bapi.core.storage import storage
from beancount.core.number import D
from beancount.core import amount, data

ns = api.namespace('price', description='Prices')

price_model = api.model('Price', {
    'date': fields.Date(required=True, description='Date of the price'),
    'quoteCurrency': fields.String(required=True, description='Currency to be priced'),
    'baseCurrency': fields.String(required=True, description='Base currency the price is in'),
    'price': fields.Arbitrary(required=True, description='Price')
})

prices_update_model = api.model('PriceUpdate', {
    'filename': fields.String(required=True, description='Filename of the price file'),
    'prices' : fields.List(fields.Nested(price_model)),
})

@ns.route('/')
class Price(Resource):

    @api.expect(prices_update_model, validate=True)
    def post(self):
        prices = []
        requestData = request.json
        
        for requestPrice in requestData['prices']:
            prices.append(data.Price(
                None,
                requestPrice['date'],
                requestPrice['quoteCurrency'],
                amount.Amount(D(str(requestPrice['price'])), requestPrice['baseCurrency'])))

        storage.setPrices(prices, requestData['filename'])
        
        return 'ok'
