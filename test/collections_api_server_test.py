# -*- coding: utf-8 -*-
import os
import time
import unittest
from configparser import ConfigParser

from collections_api.collections_apiImpl import collections_api
from collections_api.collections_apiServer import MethodContext
from collections_api.authclient import KBaseAuth as _KBaseAuth

from installed_clients.WorkspaceClient import Workspace


class collections_apiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = os.environ.get('KB_AUTH_TOKEN', None)
        config_file = os.environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('collections_api'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'collections_api',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.serviceImpl = collections_api(cls.cfg)
        cls.scratch = cls.cfg['scratch']

    @classmethod
    def tearDownClass(cls):
        pass

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_list_collections(self):
        ret = self.serviceImpl.list_collections(self.ctx)
    
    def test_get_collection(self):
        ret = self.serviceImpl.get_collection(self.ctx, {'collection_id':"gtdb"})
        collection = ret[0]
        assert collection.get('id') == 'gtdb'
    
    def test_get_collection_bad_id(self):
        with self.assertRaises(ValueError) as context:
            self.serviceImpl.get_collection(self.ctx, {'collection_id':"bad_id"})
        assert 'No collection exists with id "bad_id"' in str(context.exception)
