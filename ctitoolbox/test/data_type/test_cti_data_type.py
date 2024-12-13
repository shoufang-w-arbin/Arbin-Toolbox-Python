import unittest
import os

import ArbinCTI.Core as ArbinCTI # type: ignore

from ctitoolbox.src.data_type.cti_data_type import (
    TE_DATA_TYPE, 
    EMVUD,
    EReadWriteMode,
    StartResumeEx,
    MetaVariableInfo,
    MetaVariableInfoEx,
    TimeSensitiveSetMV,
    TimeSensitiveSetMVArgs,
    CMetavariableDataCodeApply
)

UNITTEST_VIEW_DICT = os.getenv("UNITTEST_VIEW_DICT", False)

class TestArbinCTIClasses(unittest.TestCase):

    def setUp(self):
        # Any setup logic needed before each test
        pass

    def test_start_resume_ex_to_cs(self):
        """Test conversion of StartResumeEx to C# object"""
        start_resume_ex = StartResumeEx(
            channelIndex=1,
            TestID=123,
            TestNames="Test1",
            Schedules="Schedule1",
            nSelectSteps=2,
            Cycle=10,
            TestTime=100.0,
            StepTime=50.0,
            CCapacity=200.0,
            DCapacity=100.0,
            CEnergy=300.0,
            DEnergy=150.0,
            ChargeCapacityTime=500.0,
            DischargeCapacityTime=300.0
        )

        cs_instance = start_resume_ex.to_cs()

        self.assertEqual(cs_instance.channelIndex, 1)
        self.assertEqual(cs_instance.TestID, 123)
        self.assertEqual(cs_instance.TestNames, "Test1")
        self.assertEqual(cs_instance.Schedules, "Schedule1")
        self.assertEqual(cs_instance.nSelectSteps, 2)
        self.assertEqual(cs_instance.Cycle, 10)
        self.assertEqual(cs_instance.TestTime, 100.0)
        self.assertEqual(cs_instance.StepTime, 50.0)
        self.assertEqual(cs_instance.CCapacity, 200.0)
        self.assertEqual(cs_instance.DCapacity, 100.0)
        self.assertEqual(cs_instance.CEnergy, 300.0)
        self.assertEqual(cs_instance.DEnergy, 150.0)
        self.assertEqual(cs_instance.ChargeCapacityTime, 500.0)
        self.assertEqual(cs_instance.DischargeCapacityTime, 300.0)

    def test_meta_variable_info_to_cs(self):
        """Test conversion of MetaVariableInfo to C# object"""
        meta_var_info = MetaVariableInfo(
            channel_index = 1,
            mv_meta_code  = 100,
            mv_data_type  = TE_DATA_TYPE.MP_DATA_TYPE_AuxTemperature
        )

        cs_instance = meta_var_info.to_cs()

        self.assertEqual(cs_instance.m_Channel, 1)
        self.assertEqual(cs_instance.m_MV_MetaCode, 100)
        self.assertEqual(cs_instance.m_MV_DataType, ArbinCTI.TE_DATA_TYPE.MP_DATA_TYPE_AuxTemperature)

    def test_c_metavariable_data_code_apply_to_cs(self):
        """Test conversion of CMetavariableDataCodeApply to C# object"""
        c_meta_var_apply = CMetavariableDataCodeApply(
            global_index=2,
            mv_value_type=TE_DATA_TYPE.MP_DATA_TYPE_AuxVoltage,
            mv_meta_code=5000,
            mode=EReadWriteMode.Read
        )

        cs_instance = c_meta_var_apply.to_cs()

        self.assertEqual(cs_instance.m_GlobalIndex, 2)
        self.assertEqual(cs_instance.m_MV_ValueType, ArbinCTI.TE_DATA_TYPE.MP_DATA_TYPE_AuxVoltage)
        self.assertEqual(cs_instance.m_MV_MetaCode, 5000)
        self.assertEqual(cs_instance.ReadWriteMode, ArbinCTI.EReadWriteMode.Read)

    def test_time_sensitive_set_mv_to_cs(self):
        """Test conversion of TimeSensitiveSetMV to C# object"""
        time_sensitive_set_mv = TimeSensitiveSetMV(EMVUD.MVUD1, 10.5)

        cs_instance = time_sensitive_set_mv.to_cs()

        self.assertEqual(cs_instance.MVUD, ArbinCTI.TimeSensitiveSetMV.EMVUD.MVUD1)
        self.assertEqual(cs_instance.Value, 10.5)

    def test_time_sensitive_set_mv_from_cs(self):
        """Test conversion of TimeSensitiveSetMV to C# object"""
        cs_instance = ArbinCTI.TimeSensitiveSetMV()
        cs_instance.MVUD = ArbinCTI.TimeSensitiveSetMV.EMVUD.MVUD1
        cs_instance.Value = 10.5

        time_sensitive_set_mv = TimeSensitiveSetMV(cs_instance)

        self.assertEqual(time_sensitive_set_mv.mvud, EMVUD.MVUD1)
        self.assertEqual(time_sensitive_set_mv.value, 10.5)

        if UNITTEST_VIEW_DICT:
            print("TimeSensitiveSetMV:", time_sensitive_set_mv.to_dict())

    def test_time_sensitive_set_mv_args_to_cs(self):
        """Test conversion of TimeSensitiveSetMVArgs to C# object"""
        time_sensitive_set_mv = TimeSensitiveSetMV(EMVUD.MVUD1, 20.0)
        time_sensitive_set_mv_channel = TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel(
            global_index=1,
            time_sensitive_mvs=[time_sensitive_set_mv],
            log=False
        )

        time_sensitive_set_mv_args = TimeSensitiveSetMVArgs(
            timeout=10.0,
            channels=[time_sensitive_set_mv_channel]
        )

        cs_instance = time_sensitive_set_mv_args.to_cs()

        self.assertEqual(cs_instance.Timeout, 10.0)
        self.assertEqual(len(cs_instance.Channels), 1)
        self.assertEqual(cs_instance.Channels[0].GlobalIndex, 1)
        self.assertEqual(cs_instance.Channels[0].TimeSensitiveSetMVCount, 1)
        self.assertEqual(cs_instance.Channels[0].IsDoLog, False)

    def test_meta_variable_info_ex_to_cs(self):
        """Test conversion of MetaVariableInfoEx to C# object"""
        meta_var_info_ex = MetaVariableInfoEx(
            data_type=TE_DATA_TYPE.MP_DATA_TYPE_AuxdTdt,
            error=b'\x01'
        )

        cs_instance = meta_var_info_ex.to_cs()

        self.assertEqual(cs_instance.DataType, ArbinCTI.TE_DATA_TYPE.MP_DATA_TYPE_AuxdTdt)
        self.assertEqual(cs_instance.Error, 1)