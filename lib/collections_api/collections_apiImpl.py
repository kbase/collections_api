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
    GIT_URL = "git@github.com:kbase/collections_api.git"
    GIT_COMMIT_HASH = "59b518809b3dc2c1bfe5861aaa5c8351f169df34"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        self.collections = Collections()
        #END_CONSTRUCTOR
        pass


    def list_collections(self, ctx):
        """
        :returns: instance of type "ListCollectionsResults" -> list of type
           "collection" -> unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN list_collections
        output = self.collections.list_collections()
        #END list_collections

        # At some point might do deeper type checking...
        if not isinstance(output, list):
            raise ValueError('Method list_collections return value ' +
                             'output is not type list as required.')
        # return the results
        return [output]

    def get_collection(self, ctx, params):
        """
        :param params: instance of type "GetCollectionParams" -> structure:
           parameter "collection_id" of String
        :returns: instance of type "GetCollectionResults" -> type
           "collection" -> unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN get_collection
        output = self.collections.get_collection(params.collection_id)
        #END get_collection

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method get_collection return value ' +
                             'output is not type object as required.')
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
