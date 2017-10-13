from beancount import loader
from beancount.query import query

class Storage:
    def load(self, fileName):
        self.fileName = fileName
        self.entries, self.errors, self.options = loader.load_file(fileName)

    def runQuery(self, queryString):
        return query.run_query(self.entries, self.options, queryString)

storage = Storage()
