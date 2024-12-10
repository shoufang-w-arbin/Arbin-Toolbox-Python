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
    class ItemType(Enum):
        BYTE    = Byte
        BOOL    = Boolean
        INT     = Int32
        USHORT  = UInt16
        UINT    = UInt32
        FLOAT   = Single
        DOUBLE  = Double
        STRING  = String

    @staticmethod
    def to_cs_byte(value):
        """Convert a Python integer to a .NET 'byte'."""
        if isinstance(value, bytes) and len(value) == 1:
            return Byte(value)
        raise ValueError("Value must be an byte")

    @staticmethod
    def to_cs_bool(value):
        """Convert a Python boolean to a .NET 'bool'."""
        if isinstance(value, bool):
            return Boolean(value)
        raise ValueError("Value must be a boolean")

    @staticmethod
    def to_cs_int(value):
        """Convert a Python integer to a .NET 'int'."""
        if isinstance(value, int):
            return Int32(value)
        raise ValueError("Value must be an integer")

    @staticmethod
    def to_cs_ushort(value):
        """Convert a Python integer to a .NET 'ushort'."""
        if isinstance(value, int) and value >= 0:
            return UInt16(value)
        raise ValueError("Value must be a non-negative integer for usigned short integer")
    
    @staticmethod
    def to_cs_uint(value):
        """Convert a Python integer to a .NET 'uint'."""
        if isinstance(value, int) and value >= 0:
            return UInt32(value)
        raise ValueError("Value must be a non-negative integer for unsigned integer")

    @staticmethod
    def to_cs_float(value):
        """Convert a Python float to a .NET 'float'."""
        if isinstance(value, (float, int)):
            return Single(value)
        raise ValueError("Value must be a float or an integer")
        
    @staticmethod
    def to_cs_double(value):
        """Convert a Python float to a .NET 'double'."""
        if isinstance(value, (float, int)):
            return Double(value)
        raise ValueError("Value must be a float or an integer")

    @staticmethod
    def to_cs_string(value):
        """Convert a Python string to a .NET 'string'."""
        if isinstance(value, str):
            return String(value)
        raise ValueError("Value must be a string")
    
    @staticmethod
    def to_cs_byte_array(value):
        """Convert a Python integer to a .NET 'byte[]'."""
        if isinstance(value, (bytes, bytearray)):
            return Array[Byte](value)
        raise ValueError("Value must be a bytes object or bytearray.")
    
    @staticmethod
    def to_cs_list(item_type: ItemType, list_object: list):
        """Create a .NET List of given data type from Python arguments. Supported data types: byte, bool, int, ushort, uint, float, double, string."""
        if not isinstance(item_type, CSTypeConverter.ItemType):
            raise ValueError(f"Unsupported data type: {item_type}")
        
        conversion_map = {
            CSTypeConverter.ItemType.BYTE:   CSTypeConverter.to_cs_byte,
            CSTypeConverter.ItemType.BOOL:   CSTypeConverter.to_cs_bool,
            CSTypeConverter.ItemType.INT:    CSTypeConverter.to_cs_int,
            CSTypeConverter.ItemType.USHORT: CSTypeConverter.to_cs_ushort,
            CSTypeConverter.ItemType.UINT:   CSTypeConverter.to_cs_uint,
            CSTypeConverter.ItemType.FLOAT:  CSTypeConverter.to_cs_float,
            CSTypeConverter.ItemType.DOUBLE: CSTypeConverter.to_cs_double,
            CSTypeConverter.ItemType.STRING: CSTypeConverter.to_cs_string,
        }

        list_instance = List[item_type.value]()
        for obj in list_object:
            try:
                list_instance.Add(conversion_map[item_type](obj))
            except Exception as e:
                raise ValueError(f"Error converting item {obj}, object type {type(obj)}, to {item_type.name}.")

        return list_instance