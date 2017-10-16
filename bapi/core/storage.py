from beancount import loader
from beancount.query import query
from bapi.core.exception import BapiException
from beancount.parser import printer

class Storage:
    def load(self, fileName):
        self.fileName = fileName
        self.entries, errors, self.options = loader.load_file(fileName)
        if errors:
            printer.print_errors(errors)
            raise BapiException('Failed to load file ' + fileName + '.')

    def runQuery(self, queryString):
        return query.run_query(self.entries, self.options, queryString)

storage = Storage()
