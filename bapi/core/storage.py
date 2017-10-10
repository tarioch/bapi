from beancount import loader
from beancount.query import query
from bapi.core import config

class Storage:
    def __init__(self, fileName):
        self.fileName = fileName
        self.entries, self.errors, self.options = loader.load_file(fileName)

    def runQuery(self, queryString):
        return query.run_query(self.entries, self.options, queryString)

storage = Storage('dummy.beancount')
