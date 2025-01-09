import unittest

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

from ctitoolbox.src.data_type.cs_data_type import CSTypeConverter

class TestCSTypeConverter(unittest.TestCase):

    def test_to_byte_array(self):
        # Test with bytes object
        python_bytes = b'hello'
        cs_array = CSTypeConverter.to_byte_array(python_bytes)
        self.assertIsInstance(cs_array, Array[Byte])
        self.assertEqual(len(cs_array), len(python_bytes))
        for i, b in enumerate(python_bytes):
            self.assertEqual(cs_array[i], b)

        # Test with bytearray
        python_bytearray = bytearray([1, 2, 3, 4, 5])
        cs_array = CSTypeConverter.to_byte_array(python_bytearray)
        self.assertIsInstance(cs_array, Array[Byte])
        self.assertEqual(len(cs_array), len(python_bytearray))
        for i, b in enumerate(python_bytearray):
            self.assertEqual(cs_array[i], b)

        # Test with empty bytes
        empty_bytes = b''
        cs_array = CSTypeConverter.to_byte_array(empty_bytes)
        self.assertIsInstance(cs_array, Array[Byte])
        self.assertEqual(len(cs_array), 0)

        # Test with invalid input
        with self.assertRaises(ValueError):
            CSTypeConverter.to_byte_array("not a bytes object")

        with self.assertRaises(ValueError):
            CSTypeConverter.to_byte_array(123)

        with self.assertRaises(ValueError):
            CSTypeConverter.to_byte_array([1, 2, 3])  # list, not bytes or bytearray

    def test_to_int32(self):
        self.assertIsInstance(CSTypeConverter.to_int(5), Int32)
        self.assertEqual(CSTypeConverter.to_int(5), Int32(5))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_int("5")

    def test_to_uint32(self):
        self.assertIsInstance(CSTypeConverter.to_uint(5), UInt32)
        self.assertEqual(CSTypeConverter.to_uint(5), UInt32(5))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_uint(-5)
        with self.assertRaises(ValueError):
            CSTypeConverter.to_uint("5")

    def test_to_float(self):
        self.assertIsInstance(CSTypeConverter.to_float(5.5), Single)
        self.assertEqual(CSTypeConverter.to_float(5.5), Single(5.5))
        self.assertIsInstance(CSTypeConverter.to_float(5), Single)
        self.assertEqual(CSTypeConverter.to_float(5), Single(5))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_float("5.5")

    def test_to_bool(self):
        self.assertIsInstance(CSTypeConverter.to_bool(True), Boolean)
        self.assertEqual(CSTypeConverter.to_bool(True), Boolean(True))
        self.assertEqual(CSTypeConverter.to_bool(False), Boolean(False))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_bool(1)

    def test_to_string(self):
        self.assertIsInstance(CSTypeConverter.to_string("test"), String)
        self.assertEqual(CSTypeConverter.to_string("test"), String("test"))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_string(5)

    def test_to_ushort(self):
        self.assertIsInstance(CSTypeConverter.to_ushort(5), UInt16)
        self.assertEqual(CSTypeConverter.to_ushort(5), UInt16(5))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_ushort(-5)
        with self.assertRaises(ValueError):
            CSTypeConverter.to_ushort("5")

    def test_to_double(self):
        self.assertIsInstance(CSTypeConverter.to_double(5.5), Double)
        self.assertEqual(CSTypeConverter.to_double(5.5), Double(5.5))
        self.assertIsInstance(CSTypeConverter.to_double(5), Double)
        self.assertEqual(CSTypeConverter.to_double(5), Double(5))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_double("5.5")

    def test_to_list_with_type(self):
        python_list = [1, 2, 3]
        cs_list = CSTypeConverter.to_list(python_list, CSTypeConverter.EDataType.INT)
        self.assertIsInstance(cs_list, List[Int32])
        self.assertEqual(len(cs_list), len(python_list))
        for i, item in enumerate(python_list):
            self.assertEqual(cs_list[i], Int32(item))

        with self.assertRaises(ValueError):
            CSTypeConverter.to_list(python_list, "invalid type")

        with self.assertRaises(ValueError):
            CSTypeConverter.to_list([1, "2", 3], CSTypeConverter.EDataType.INT)

    def test_to_list_without_type(self):
        class MockObject:
            def to_cs(self):
                return Int32(5)

        python_list = [MockObject(), MockObject()]
        cs_list = CSTypeConverter.to_list(python_list)
        self.assertIsInstance(cs_list, List[Int32])
        self.assertEqual(len(cs_list), len(python_list))
        for item in cs_list:
            self.assertEqual(item, Int32(5))

        with self.assertRaises(ValueError):
            CSTypeConverter.to_list([MockObject(), "invalid object"])

    def test_to_list_invalid_args(self):
        with self.assertRaises(ValueError):
            CSTypeConverter.to_list([1, 2, 3], CSTypeConverter.EDataType.INT, "extra arg")
