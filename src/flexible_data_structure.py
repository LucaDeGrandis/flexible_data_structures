from collections import defaultdict

class FlexibleDataStructure:
    def __init__(self):
        self.data = defaultdict(FlexibleDataStructure)

    def append(self, item):
        if isinstance(self.data, dict) and not self.data:
            self.data = []
        self.data.append(item)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        if isinstance(self.data, list):
            raise ValueError("Cannot use dictionary operations on a list")
        self.data[key] = value
