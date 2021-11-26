import os


class Connection(object):

    @classmethod
    def has_host(self):
        return os.environ.get('MODE', 'LOCAL') == 'LOCAL'

    @classmethod
    def get_host_local(self):
        return 'http://localhost:{0}'.format(os.environ.get('DYNAMODB_PORT'))
