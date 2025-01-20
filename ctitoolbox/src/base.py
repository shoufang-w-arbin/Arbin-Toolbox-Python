import copy
import json
from enum import IntEnum, Enum

class DictReprBase:
    def to_dict(self):
        data = copy.deepcopy(self.__dict__)
        for key, value in data.items():
            if isinstance(value, (IntEnum, Enum)):
                data[key] = value.name
            elif hasattr(value, 'to_dict'):
                data[key] = value.to_dict()
            elif isinstance(value, list) and all(hasattr(item, 'to_dict') for item in value):
                data[key] = [item.to_dict() for item in value]
        return data

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2)
    
class SafeEnum(IntEnum):
    @classmethod
    def _missing_(cls, value):
        return cls._create_pseudo_member_(value)
    
    @classmethod
    def _create_pseudo_member_(cls, value):
        pseudo_member = int.__new__(cls, value)
        pseudo_member._name_ = f'UNKNOWN_{value}'
        pseudo_member._value_ = value
        return pseudo_member