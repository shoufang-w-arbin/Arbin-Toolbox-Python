import unittest

from System import ( # type: ignore
    Byte,
    Boolean,
    Int32,
    UInt32,
    Single,
    String,
    Array
)
from System.Collections.Generic import List # type: ignore

from ctitoolbox.src.data_type.cs_data_type import CSTypeConverter

class TestCSTypeConverter(unittest.TestCase):

    def test_to_cs_byte_array(self):
        # Test with bytes object
        python_bytes = b'hello'
        cs_array = CSTypeConverter.to_cs_byte_array(python_bytes)
        self.assertIsInstance(cs_array, Array[Byte])
        self.assertEqual(len(cs_array), len(python_bytes))
        for i, b in enumerate(python_bytes):
            self.assertEqual(cs_array[i], b)

        # Test with bytearray
        python_bytearray = bytearray([1, 2, 3, 4, 5])
        cs_array = CSTypeConverter.to_cs_byte_array(python_bytearray)
        self.assertIsInstance(cs_array, Array[Byte])
        self.assertEqual(len(cs_array), len(python_bytearray))
        for i, b in enumerate(python_bytearray):
            self.assertEqual(cs_array[i], b)

        # Test with empty bytes
        empty_bytes = b''
        cs_array = CSTypeConverter.to_cs_byte_array(empty_bytes)
        self.assertIsInstance(cs_array, Array[Byte])
        self.assertEqual(len(cs_array), 0)

        # Test with invalid input
        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_byte_array("not a bytes object")

        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_byte_array(123)

        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_byte_array([1, 2, 3])  # list, not bytes or bytearray

    def test_to_cs_int32(self):
        self.assertIsInstance(CSTypeConverter.to_cs_int(5), Int32)
        self.assertEqual(CSTypeConverter.to_cs_int(5), Int32(5))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_int("5")

    def test_to_cs_uint32(self):
        self.assertIsInstance(CSTypeConverter.to_cs_uint(5), UInt32)
        self.assertEqual(CSTypeConverter.to_cs_uint(5), UInt32(5))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_uint(-5)
        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_uint("5")

    def test_to_cs_float(self):
        self.assertIsInstance(CSTypeConverter.to_cs_float(5.5), Single)
        self.assertEqual(CSTypeConverter.to_cs_float(5.5), Single(5.5))
        self.assertIsInstance(CSTypeConverter.to_cs_float(5), Single)
        self.assertEqual(CSTypeConverter.to_cs_float(5), Single(5))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_float("5.5")

    def test_to_cs_bool(self):
        self.assertIsInstance(CSTypeConverter.to_cs_bool(True), Boolean)
        self.assertEqual(CSTypeConverter.to_cs_bool(True), Boolean(True))
        self.assertEqual(CSTypeConverter.to_cs_bool(False), Boolean(False))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_bool(1)

    def test_to_cs_string(self):
        self.assertIsInstance(CSTypeConverter.to_cs_string("test"), String)
        self.assertEqual(CSTypeConverter.to_cs_string("test"), String("test"))
        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_string(5)

    def test_to_cs_list(self):
        # Test with integers
        int_list = CSTypeConverter.to_cs_list(CSTypeConverter.ItemType.INT, [1, 2, 3])
        self.assertIsInstance(int_list, List[Int32])
        self.assertEqual(len(int_list), 3)
        self.assertEqual(int_list[0], 1)

        # Test with floats
        float_list = CSTypeConverter.to_cs_list(CSTypeConverter.ItemType.FLOAT, [1.1, 2.2, 3.3])
        self.assertIsInstance(float_list, List[Single])
        self.assertEqual(len(float_list), 3)
        self.assertAlmostEqual(float(float_list[0]), 1.1, places=6)

        # Test with booleans
        bool_list = CSTypeConverter.to_cs_list(CSTypeConverter.ItemType.BOOL, [True, False, True])
        self.assertIsInstance(bool_list, List[Boolean])
        self.assertEqual(len(bool_list), 3)
        self.assertEqual(bool_list[0], True)

        # Test with strings
        string_list = CSTypeConverter.to_cs_list(CSTypeConverter.ItemType.STRING, ["a", "b", "c"])
        self.assertIsInstance(string_list, List[String])
        self.assertEqual(len(string_list), 3)
        self.assertEqual(string_list[0], "a")
        
        # Test with unsupported type
        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_list(CSTypeConverter.ItemType.FLOAT, [1, "2", 3])

        # Test with mixed types
        with self.assertRaises(ValueError):
            CSTypeConverter.to_cs_list(CSTypeConverter.ItemType.INT, [1, "2", 3])
            CSTypeConverter.to_cs_list(CSTypeConverter.ItemType.INT, [1, "2", 3])