from os import path
from beancount import loader
from beancount.query import query
from bapi.core.exception import BapiException
from beancount.parser import printer
from beancount.query.query_compile import CompilationError
from beancount.query.query_parser import ParseError

class Storage:
    def load(self, basedir, fileName):
        self.basedir = basedir
        self.fileName = fileName
        self.reload()
    
    def basedir(self):
        return self.basedir
    
    def reload(self):
        self.entries, errors, self.options = loader.load_file(path.join(self.basedir, self.fileName))
        if errors:
            printer.print_errors(errors)
            raise BapiException('Failed to load file ' + self.fileName + '.')

    def runQuery(self, queryString):
        try:
            return query.run_query(self.entries, self.options, queryString)
        except (CompilationError, ParseError) as exc :
            raise BapiException('Query failed: ' + str(exc)) from exc
    
    def setPrices(self, prices, fileName):
        with open(path.join(self.basedir, fileName), 'w') as output:
            printer.print_entries(prices, file=output)
    
    def addTransaction(self, transaction, fileName):
        with open(path.join(self.basedir, fileName), 'a') as output:
            printer.print_entry(transaction, file=output)
        

storage = Storage()
