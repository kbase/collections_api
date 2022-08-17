import json
import os


class Collections():
    def __init__(self):
        bd = os.path.dirname(__file__)
        self.mock_data = os.path.join(bd, "../../mock_data")
        fp = os.path.join(self.mock_data, "gtdb.json")
        self.gtdb = json.load(open(fp))

    def list_collections(self):
        return [self.gtdb]
    
    def get_collection(self, collection):
        return self.gtdb 
