import copy
import json
from enum import IntEnum, Enum

class DictReprBase:
    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def to_dict(self):
        data = copy.deepcopy(self.__dict__)
        for key, value in data.items():
            if isinstance(value, (IntEnum, Enum)):
                data[key] = value.name
            elif hasattr(value, 'to_dict'):
                data[key] = value.to_dict()
            elif isinstance(value, list) and all(hasattr(item, 'to_dict') for item in value):
                data[key] = [item.to_dict() for item in value]
            elif isinstance(value, dict) and all(isinstance(key, (IntEnum, Enum)) for key in value.keys()):
                data[key] = {key.name: value for key, value in value.items()}
        return data
    
    def _unpack_cs_sorted_dict(self, cs_dict: dict, py_kv_type: tuple):
        key_type, value_type = py_kv_type
        unpacked_dict = {}
        for pair in cs_dict:
            key = key_type(int(pair.Key)) if issubclass(key_type, Enum) else key_type(pair.Key)
            unpacked_dict[key] = value_type(pair.Value)
        return unpacked_dict
    
class SafeIntEnumBase(IntEnum):
    @classmethod
    def _missing_(cls, value):
        pseudo_member = int.__new__(cls, value)
        pseudo_member._name_ = f'UNKNOWN_{value}'
        pseudo_member._value_ = value
        return pseudo_member