from flask import request
from flask_restplus.resource import Resource
from flask_restplus import reqparse
from bapi.api.core import api
from bapi.core.storage import storage
import git

ns = api.namespace('repo', description='Operations related to interact with repository')

commit_arguments = reqparse.RequestParser()
commit_arguments.add_argument('message', required=True, help='Commit message')

@ns.route('/update')
class RepoUpdate(Resource):

    def put(self):
        gitRepo = git.Repo(storage.basedir)
        gitRepo.git.pull('--rebase')
        storage.reload()
        
        return 'done'
    
@ns.route('/commit')
class RepoCommit(Resource):

    @api.expect(commit_arguments, validate=True)
    def post(self):
        args = commit_arguments.parse_args(request)
        message = args.get('message')
        
        gitRepo = git.Repo(storage.basedir)
        if gitRepo.is_dirty():
            gitRepo.git.commit('-a', m=message)
            gitRepo.git.push()
            return 'commited'
        else:
            return 'nothing to commit'
