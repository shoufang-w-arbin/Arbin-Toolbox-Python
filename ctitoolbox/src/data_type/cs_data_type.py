from enum import Enum

from System import ( # type: ignore
    Byte,
    Boolean,
    Int32,
    UInt16,
    UInt32,
    Single,
    Double,
    String,
    Array
)
from System.Collections.Generic import List # type: ignore

"""""""""""""""""""""""""""
BASIC DATA TYPES
Supported data types: 
- byte
- byte[]
- bool
- int
- ushort
- uint
- float
- double
- string
- list of basic data types
"""""""""""""""""""""""""""
class CSTypeConverter:
    class EDataType(Enum):
        BYTE    = Byte
        BOOL    = Boolean
        INT     = Int32
        USHORT  = UInt16
        UINT    = UInt32
        FLOAT   = Single
        DOUBLE  = Double
        STRING  = String

    @staticmethod
    def to_byte(value):
        """Convert a single python 'byte' to a csharp 'byte'. Use to_cs_byte_array for multiple bytes."""
        if not (isinstance(value, bytes) and len(value) == 1):
            raise ValueError("Value must be a byte")
        return Byte(value)

    @staticmethod
    def to_bool(value):
        """Convert a python 'bool' to a csharp 'bool'."""
        if not isinstance(value, bool):
            raise ValueError("Value must be a boolean")
        return Boolean(value)

    @staticmethod
    def to_int(value):
        """Convert a python 'int' to a csharp 'int'."""
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        return Int32(value)

    @staticmethod
    def to_ushort(value):
        """Convert a python 'int' to a csharp 'ushort'."""
        if not (isinstance(value, int) and value >= 0):
            raise ValueError("Value must be a non-negative integer for unsigned short integer")
        return UInt16(value)
    
    @staticmethod
    def to_uint(value):
        """Convert a python 'int' to a csharp 'uint'."""
        if not (isinstance(value, int) and value >= 0):
            raise ValueError("Value must be a non-negative integer for unsigned integer")
        return UInt32(value)

    @staticmethod
    def to_float(value):
        """Convert a python float to a csharp 'float'."""
        if not isinstance(value, (float, int)):
            raise ValueError("Value must be a float or an integer")
        return Single(value)
        
    @staticmethod
    def to_double(value):
        """Convert a python float to a csharp 'double'."""
        if not isinstance(value, (float, int)):
            raise ValueError("Value must be a float or an integer")
        return Double(value)

    @staticmethod
    def to_string(value):
        """Convert a python 'str' to a csharp 'string'."""
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        return String(value)
    
    @staticmethod
    def to_byte_array(value):
        """Convert a python 'bytearray' to a csharp 'byte[]'."""
        if not isinstance(value, (bytes, bytearray)):
            raise ValueError("Value must be a bytes object or bytearray.")
        return Array[Byte](value)
    
    @staticmethod
    def to_list(object_list: list, *args):
        """
        Convert a python list to a csharp List.\n
        If an EDataType is provided, the list is converted to a csharp List of that type.
        If not, the objects in the list are presumed to have a 'to_cs' method.
        """
        # EDataType is provided
        if len(args) == 1:
            if not isinstance(args[0], CSTypeConverter.EDataType):
                raise ValueError(f"Unsupported data type: {args[0]}. Must be EItemType.")
            
            item_type = args[0]
            _conversion_map = {
                CSTypeConverter.EDataType.BYTE:   CSTypeConverter.to_byte,
                CSTypeConverter.EDataType.BOOL:   CSTypeConverter.to_bool,
                CSTypeConverter.EDataType.INT:    CSTypeConverter.to_int,
                CSTypeConverter.EDataType.USHORT: CSTypeConverter.to_ushort,
                CSTypeConverter.EDataType.UINT:   CSTypeConverter.to_uint,
                CSTypeConverter.EDataType.FLOAT:  CSTypeConverter.to_float,
                CSTypeConverter.EDataType.DOUBLE: CSTypeConverter.to_double,
                CSTypeConverter.EDataType.STRING: CSTypeConverter.to_string,
            }

            for i in range(len(object_list)):
                obj = object_list[i]
                try:
                    object_list[i] = _conversion_map[item_type](obj)
                except Exception as e:
                    raise ValueError(f"Error converting item {obj}, object type {type(obj)}, to {item_type.name}.")
                
            return CSTypeConverter._to_cs_list(object_list, item_type)
        
        # No EDataType provided
        elif len(args) == 0:
            if not all(isinstance(obj, type(object_list[0])) and hasattr(obj, 'to_cs') for obj in object_list):
                raise ValueError("All objects in the list must be of the same type and have a 'to_cs' method.")
            
            object_list = [obj.to_cs() for obj in object_list]

            return CSTypeConverter._to_cs_list(object_list, object_list[0].GetType())
        
        else:
            raise ValueError("Invalid arguments passed to to_cs_list")
        
    @staticmethod
    def _to_cs_list(object_list, item_type):
        """Convert a python list of csharp objects to a csharp List of given data type."""
        list_instance = List[item_type]()
        for obj in object_list:
            list_instance.Add(obj)
        return list_instance