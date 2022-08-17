# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from .collections import Collections
#END_HEADER


class collections_api:
    '''
    Module Name:
    collections_api

    Module Description:
    A KBase module: collections_api
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/kbase/collections_api"
    GIT_COMMIT_HASH = "9d3d7db9a480ed41524ccc8e1092cc8110985c0a"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        self.collections = Collections()
        #END_CONSTRUCTOR
        pass


    def list_collections(self, ctx):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :returns: instance of unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN list_collections
        output = self.collections.list_collections()
        #END list_collections

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method list_collections return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]

    def get_collection(self, ctx, collection):
        """
        :param collection: instance of String
        :returns: instance of mapping from String to unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN get_collection
        output = self.collections.get_collection(collection)
        #END get_collection

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method get_collection return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
