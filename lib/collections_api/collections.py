import json
import os


class Collections:
    def __init__(self):
        bd = os.path.dirname(__file__)
        self.mock_data = os.path.join(bd, "../../mock_data")
        fp = os.path.join(self.mock_data, "collections.json")
        self.collections = json.load(open(fp))

    def list_collections(self):
        return self.collections

    def get_collection(self, collection_id):
        try:
            collection = next((c for c in self.collections if c["id"] == collection_id))
        except StopIteration as e:
            raise ValueError(f'No collection exists with ID "{collection_id}"') from e
        return collection
