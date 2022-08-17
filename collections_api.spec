/*
A KBase module: collections_api
*/

module collections_api {

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef list_collections() returns (UnspecifiedObject output) authentication required;

    funcdef get_collection(string collection) returns (mapping<string,UnspecifiedObject> output) authentication required;
};
