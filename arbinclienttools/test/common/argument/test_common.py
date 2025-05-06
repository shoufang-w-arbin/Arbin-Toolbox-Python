import unittest

from common import AIMetaVariableInfo, BarcodeInfo, GetBarcodeInfo
from arbinclienttools.src.enumeration import EMetaVariableType, EBarcodeType, EBarcodeResult

class TestCommonArgs(unittest.TestCase):

    def test_ai_metavariable_info_to_cs(self):
        data = AIMetaVariableInfo(
            global_id=123,
            meta_variable_type=EMetaVariableType.MetaCode_MV_UD2,
            index_=1,
            value=99.5
        )
        cs = data.to_cs()

        self.assertEqual(cs.GlobalID, 123)
        self.assertEqual(cs.MetaVariableType, EMetaVariableType.MetaCode_MV_UD2.to_cs())
        self.assertEqual(cs.Index, 1)
        self.assertEqual(cs.Value, 99.5)

    def test_barcode_info_to_cs(self):
        data = BarcodeInfo(
            barcode_type=EBarcodeType.SN,
            barcode="ABC12345",
            global_id=456,
            info="Test Barcode",
            result=EBarcodeResult.Failed.name,
            barcode_result=EBarcodeResult.Failed
        )
        cs = data.to_cs()

        self.assertEqual(cs.BarcodeType.value, EBarcodeType.SN.value)
        self.assertEqual(cs.Barcode, "ABC12345")
        self.assertEqual(cs.GlobalID, 456)
        self.assertEqual(cs.Info, "Test Barcode")
        self.assertEqual(cs.Result, "Failed")
        self.assertEqual(cs.BarcodeResult.value, EBarcodeResult.Failed.value)

    def test_get_barcode_info_to_cs(self):
        data = GetBarcodeInfo(
            barcode_type=EBarcodeType.IV,
            global_id=789
        )
        cs = data.to_cs()

        self.assertEqual(cs.BarcodeType.value, EBarcodeType.IV.value)
        self.assertEqual(cs.GlobalID, 789)

if __name__ == '__main__':
    unittest.main()
