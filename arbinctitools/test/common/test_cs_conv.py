import unittest

from System import ( # type: ignore
    Byte,
    Boolean,
    Int16,
    Int32,
    UInt16,
    UInt32,
    Single,
    Double,
    String,
    Array
)
from System.Collections.Generic import List, SortedDictionary # type: ignore

from arbinctitools.src.common.cs_conv import CSConv

class TestCSTypeConverter(unittest.TestCase):

    def test_to_byte_array(self):
        # Test with bytes object
        python_bytes = b'hello'
        cs_array = CSConv.to_byte_array(python_bytes)
        self.assertIsInstance(cs_array, Array[Byte])
        self.assertEqual(len(cs_array), len(python_bytes))
        for i, b in enumerate(python_bytes):
            self.assertEqual(cs_array[i], b)

        # Test with bytearray
        python_bytearray = bytearray([1, 2, 3, 4, 5])
        cs_array = CSConv.to_byte_array(python_bytearray)
        self.assertIsInstance(cs_array, Array[Byte])
        self.assertEqual(len(cs_array), len(python_bytearray))
        for i, b in enumerate(python_bytearray):
            self.assertEqual(cs_array[i], b)

        # Test with empty bytes
        empty_bytes = b''
        cs_array = CSConv.to_byte_array(empty_bytes)
        self.assertIsInstance(cs_array, Array[Byte])
        self.assertEqual(len(cs_array), 0)

        # Test with invalid input
        with self.assertRaises(ValueError):
            CSConv.to_byte_array("not a bytes object")

        with self.assertRaises(ValueError):
            CSConv.to_byte_array(123)

        with self.assertRaises(ValueError):
            CSConv.to_byte_array([1, 2, 3])  # list, not bytes or bytearray
    
    def test_to_short(self):
        self.assertIsInstance(CSConv.to_short(5), Int16)
        self.assertEqual(CSConv.to_short(5), Int16(5))
        with self.assertRaises(ValueError):
            CSConv.to_short("5")

    def test_to_int32(self):
        self.assertIsInstance(CSConv.to_int(5), Int32)
        self.assertEqual(CSConv.to_int(5), Int32(5))
        with self.assertRaises(ValueError):
            CSConv.to_int("5")

    def test_to_uint32(self):
        self.assertIsInstance(CSConv.to_uint(5), UInt32)
        self.assertEqual(CSConv.to_uint(5), UInt32(5))
        with self.assertRaises(ValueError):
            CSConv.to_uint(-5)
        with self.assertRaises(ValueError):
            CSConv.to_uint("5")

    def test_to_float(self):
        self.assertIsInstance(CSConv.to_float(5.5), Single)
        self.assertEqual(CSConv.to_float(5.5), Single(5.5))
        self.assertIsInstance(CSConv.to_float(5), Single)
        self.assertEqual(CSConv.to_float(5), Single(5))
        with self.assertRaises(ValueError):
            CSConv.to_float("5.5")

    def test_to_bool(self):
        self.assertIsInstance(CSConv.to_bool(True), Boolean)
        self.assertEqual(CSConv.to_bool(True), Boolean(True))
        self.assertEqual(CSConv.to_bool(False), Boolean(False))
        with self.assertRaises(ValueError):
            CSConv.to_bool(1)

    def test_to_string(self):
        self.assertIsInstance(CSConv.to_string("test"), String)
        self.assertEqual(CSConv.to_string("test"), String("test"))
        with self.assertRaises(ValueError):
            CSConv.to_string(5)

    def test_to_ushort(self):
        self.assertIsInstance(CSConv.to_ushort(5), UInt16)
        self.assertEqual(CSConv.to_ushort(5), UInt16(5))
        with self.assertRaises(ValueError):
            CSConv.to_ushort(-5)
        with self.assertRaises(ValueError):
            CSConv.to_ushort("5")

    def test_to_double(self):
        self.assertIsInstance(CSConv.to_double(5.5), Double)
        self.assertEqual(CSConv.to_double(5.5), Double(5.5))
        self.assertIsInstance(CSConv.to_double(5), Double)
        self.assertEqual(CSConv.to_double(5), Double(5))
        with self.assertRaises(ValueError):
            CSConv.to_double("5.5")

    def test_to_list_with_etype(self):
        python_list = [1, 2, 3, 4, 5]
        cs_list = CSConv.to_list(python_list, CSConv.EDataType.INT)
        self.assertIsInstance(cs_list, List[Int32])
        self.assertEqual(len(cs_list), len(python_list))
        for i, item in enumerate(python_list):
            self.assertEqual(int(cs_list[i]), item) # automatically converted to py 'int' when unzipping

        python_list = [True, False, True]
        cs_list = CSConv.to_list(python_list, CSConv.EDataType.BOOL)
        self.assertIsInstance(cs_list, List[Boolean])
        self.assertEqual(len(cs_list), len(python_list))
        for i, item in enumerate(python_list):
            self.assertEqual(cs_list[i], item) # automatically converted to py 'int' when unzipping

        with self.assertRaises(ValueError):
            CSConv.to_list(python_list, "invalid type")

    def test_to_list_without_etype(self):
        class MockObject:
            def __init__(self, value):
                self.value = value

            def to_cs(self):
                return Int32(self.value)

        python_list = [MockObject(1), MockObject(2), MockObject(3)]
        cs_list = CSConv.to_list(python_list)
        self.assertIsInstance(cs_list, List[Int32])
        self.assertEqual(len(cs_list), len(python_list))
        for i, item in enumerate(python_list):
            self.assertEqual(cs_list[i], item.value)

        with self.assertRaises(ValueError):
            CSConv.to_list([MockObject(1), "invalid object"])

    def test__to_cs_list(self):
        python_list = [Int32(1), Int32(2), Int32(3)]
        cs_list = CSConv._to_cs_list(python_list, Int32)
        self.assertIsInstance(cs_list, List[Int32])
        self.assertEqual(len(cs_list), len(python_list))
        for i, item in enumerate(python_list):
            self.assertEqual(cs_list[i], int(item))

    def test_to_cs_sorted_dict(self):
        # Test update parameter feedback
        from arbinctitools.src.feedback.schedule_operation import UpdateParameterFeedback
        python_list = [
            (UpdateParameterFeedback.EParameterDataType.NormCapacity, "value1"),
            (UpdateParameterFeedback.EParameterDataType.IMax, "value2"),
        ]
        cs_dict = CSConv.to_cs_sorted_dict(
            python_list,
            CSConv.EDataType.USHORT,
            CSConv.EDataType.STRING
        )
        self.assertIsInstance(cs_dict, SortedDictionary[UInt16, String])
        self.assertEqual(len(cs_dict), len(python_list))
        for key, value in python_list:
            self.assertEqual(cs_dict[key], String(value))

        # Test general case
        python_list = [(1, "one"), (2, "two"), (3, "three")]
        cs_dict = CSConv.to_cs_sorted_dict(python_list, CSConv.EDataType.INT, CSConv.EDataType.STRING)
        self.assertIsInstance(cs_dict, SortedDictionary[Int32, String])
        self.assertEqual(len(cs_dict), len(python_list))
        for key, value in python_list:
            self.assertEqual(cs_dict[Int32(key)], String(value))

        # Test with invalid input: not a list
        with self.assertRaises(ValueError):
            CSConv.to_cs_sorted_dict("not a list", CSConv.EDataType.INT, CSConv.EDataType.STRING)

        # Test with invalid input: list elements not tuples
        with self.assertRaises(ValueError):
            CSConv.to_cs_sorted_dict([1, 2, 3], CSConv.EDataType.INT, CSConv.EDataType.STRING)

        # Test with invalid input: tuples not of length 2
        with self.assertRaises(ValueError):
            CSConv.to_cs_sorted_dict([(1, "one", "extra")], CSConv.EDataType.INT, CSConv.EDataType.STRING)

        # Test with invalid key data type
        with self.assertRaises(ValueError):
            CSConv.to_cs_sorted_dict(python_list, "invalid type", CSConv.EDataType.STRING)

        # Test with invalid value data type
        with self.assertRaises(ValueError):
            CSConv.to_cs_sorted_dict(python_list, CSConv.EDataType.INT, "invalid type")

        # Test with invalid key-value pair conversion
        with self.assertRaises(ValueError):
            CSConv.to_cs_sorted_dict([(1, 2)], CSConv.EDataType.INT, CSConv.EDataType.STRING)