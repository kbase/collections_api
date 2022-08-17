/*
A KBase module: collections_api
*/

module collections_api {
    
    typedef UnspecifiedObject collection;

    typedef list<collection> ListCollectionsResults;

    funcdef list_collections() returns (ListCollectionsResults output) authentication required;

    typedef structure {
        string collection_id;
    } GetCollectionParams;

    typedef collection GetCollectionResults;

    funcdef get_collection(GetCollectionParams params) returns (GetCollectionResults output) authentication required;
};
