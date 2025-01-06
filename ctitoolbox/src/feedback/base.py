import copy
import json
from enum import IntEnum, Enum

class FeedbackBase:
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