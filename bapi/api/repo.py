from flask_restplus.resource import Resource
from bapi.api.core import api
from bapi.core.storage import storage
import git

ns = api.namespace('repo', description='Operations related to interact with repository')

@ns.route('/update')
class RepoUpdate(Resource):

    def put(self):
        gitRepo = git.Repo(storage.basedir)
        gitRepo.git.pull('--rebase')
        storage.reload()
        
        return 'done'
    
@ns.route('/commit/<string:message>')
class RepoCommit(Resource):

    @api.doc(params={'message': 'The commit message'})
    def post(self, message):
        gitRepo = git.Repo(storage.basedir)
        if gitRepo.is_dirty():
            gitRepo.git.commit('-a', m=message)
            gitRepo.git.push()
            return 'commited'
        else:
            return 'nothing to commit'
