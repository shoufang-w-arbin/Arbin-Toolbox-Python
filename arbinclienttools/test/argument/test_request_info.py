import unittest
import System
from System.Collections.Generic import List as CsList

from arbinclienttools.src.argument.request_info import (
    GetMonitorDataArgs,
    GetResumeDataArgs,
    GetStartDataArgs,
    GetMetaVariablesArgs,
    GetBarcodeInfoArgs,
    GetMappingAuxArgs,
    SubscribeMonitorDataArgs,
    SubscribeChannelDataArgs,
    SubscribeTestInfoDataArgs,
    SubscribeEventDataArgs,
    SubscribeDiagnosticEventDataArgs,
    SubscribeSPTTEQCellDataArgs,
)
from arbinclienttools.src.argument.common import AIMetaVariableInfo, GetBarcodeInfo
from arbinclienttools.src.enumeration import EFilterMonitorChannelType

class TestRequestInformationArgs(unittest.TestCase):

    def test_get_monitor_data_args_to_cs(self):
        args = GetMonitorDataArgs(
            sn="MonitorSN",
            need_type=1000,
            channel_id=5,
            filter_monitor_channel_type=EFilterMonitorChannelType.Running
        )
        cs = args.to_cs()

        self.assertEqual(cs.sn, "MonitorSN")
        self.assertIsInstance(cs.need_type, System.Int32)
        self.assertIsInstance(cs.channel_id, System.Int32)
        self.assertEqual(cs.filter_monitor_channel_type.value, EFilterMonitorChannelType.Running)

    def test_get_resume_data_args_to_cs(self):
        args = GetResumeDataArgs(sn="ResumeSN", channel_id=[1, 2, 3])
        cs = args.to_cs()

        self.assertEqual(cs.sn, "ResumeSN")
        self.assertIsInstance(cs.channel_id, CsList[System.Int32])

    def test_get_start_data_args_to_cs(self):
        args = GetStartDataArgs(sn="StartSN", channel_id=[4, 5])
        cs = args.to_cs()

        self.assertEqual(cs.sn, "StartSN")
        self.assertIsInstance(cs.channel_id, CsList[System.Int32])

    def test_get_meta_variables_args_to_cs(self):
        mv1 = AIMetaVariableInfo(global_id=1)
        mv2 = AIMetaVariableInfo(global_id=2)

        args = GetMetaVariablesArgs(sn=12345, meta_variable_type=[mv1, mv2])
        cs = args.to_cs()

        self.assertEqual(cs.SN, 12345)
        self.assertEqual(len(cs.MetaVariableTypes), 2)

    def test_get_meta_variables_args_invalid_type(self):
        args = GetMetaVariablesArgs(sn=12345, meta_variable_type=["invalid"])

        with self.assertRaises(TypeError):
            args.to_cs()

    def test_get_barcode_info_args_to_cs(self):
        bc1 = GetBarcodeInfo(barcode_type=1, global_id=1)
        bc2 = GetBarcodeInfo(barcode_type=2, global_id=2)

        args = GetBarcodeInfoArgs(sn="BarcodeSN", barcode_info=[bc1, bc2])
        with self.assertRaises(TypeError):
            args.to_cs()

    def test_get_barcode_info_args_invalid_type(self):
        args = GetBarcodeInfoArgs(sn="InvalidSN", barcode_info=["wrong_type"])

        with self.assertRaises(TypeError):
            args.to_cs()

    def test_get_mapping_aux_args_to_cs(self):
        args = GetMappingAuxArgs()
        cs = args.to_cs()

        self.assertIsNotNone(cs)

    def test_subscribe_monitor_data_args_to_cs(self):
        args = SubscribeMonitorDataArgs()
        cs = args.to_cs()

        self.assertIsNotNone(cs)

    def test_subscribe_channel_data_args_to_cs(self):
        args = SubscribeChannelDataArgs()
        cs = args.to_cs()

        self.assertIsNotNone(cs)

    def test_subscribe_test_info_data_args_to_cs(self):
        args = SubscribeTestInfoDataArgs()
        cs = args.to_cs()

        self.assertIsNotNone(cs)

    def test_subscribe_event_data_args_to_cs(self):
        args = SubscribeEventDataArgs()
        cs = args.to_cs()

        self.assertIsNotNone(cs)

    def test_subscribe_diagnostic_event_data_args_to_cs(self):
        args = SubscribeDiagnosticEventDataArgs()
        cs = args.to_cs()

        self.assertIsNotNone(cs)

    def test_subscribe_sptt_eq_cell_data_args_to_cs(self):
        args = SubscribeSPTTEQCellDataArgs()
        cs = args.to_cs()

        self.assertIsNotNone(cs)

if __name__ == "__main__":
    unittest.main()
