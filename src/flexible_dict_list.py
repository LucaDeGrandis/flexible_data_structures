from collections import defaultdict
from .flexible_data_structure import FlexibleDataStructure

def flexible_dict_list():
    return defaultdict(lambda: defaultdict(FlexibleDataStructure))
