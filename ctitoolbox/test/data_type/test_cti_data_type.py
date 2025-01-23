import unittest
import os

import ArbinCTI.Core as ArbinCTI # type: ignore

from ctitoolbox.src.data_type.cti_data_type import (
    TE_DATA_TYPE, 
    StartResumeEx,
    MetaVariableInfo,
    MetaVariableInfoEx,
    TimeSensitiveSetMV,
    TimeSensitiveSetMVArgs,
    CMetavariableDataCodeApply,
    TestObjectSetting,
    StartChannelInfo,
    StartChannelAdvancedArgs,
    GetMappingAuxArgs,
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
            mode=CMetavariableDataCodeApply.EReadWriteMode.Read
        )

        cs_instance = c_meta_var_apply.to_cs()

        self.assertEqual(cs_instance.m_GlobalIndex, 2)
        self.assertEqual(cs_instance.m_MV_ValueType, ArbinCTI.TE_DATA_TYPE.MP_DATA_TYPE_AuxVoltage)
        self.assertEqual(cs_instance.m_MV_MetaCode, 5000)
        self.assertEqual(cs_instance.ReadWriteMode, ArbinCTI.EReadWriteMode.Read)

    def test_time_sensitive_set_mv_to_cs(self):
        """Test conversion of TimeSensitiveSetMV to C# object"""
        time_sensitive_set_mv = TimeSensitiveSetMV(TimeSensitiveSetMV.EMVUD.MVUD1, 10.5)

        cs_instance = time_sensitive_set_mv.to_cs()

        self.assertEqual(cs_instance.MVUD, ArbinCTI.TimeSensitiveSetMV.EMVUD.MVUD1)
        self.assertEqual(cs_instance.Value, 10.5)

    def test_time_sensitive_set_mv_from_cs(self):
        """Test conversion of TimeSensitiveSetMV to C# object"""
        cs_instance = ArbinCTI.TimeSensitiveSetMV()
        cs_instance.MVUD = ArbinCTI.TimeSensitiveSetMV.EMVUD.MVUD1
        cs_instance.Value = 10.5

        time_sensitive_set_mv = TimeSensitiveSetMV(cs_instance)

        self.assertEqual(time_sensitive_set_mv.mvud, TimeSensitiveSetMV.EMVUD.MVUD1)
        self.assertEqual(time_sensitive_set_mv.value, 10.5)

        if UNITTEST_VIEW_DICT:
            print("TimeSensitiveSetMV:", time_sensitive_set_mv.to_dict())

    def test_time_sensitive_set_mv_args_to_cs(self):
        """Test conversion of TimeSensitiveSetMVArgs to C# object"""
        time_sensitive_set_mv = TimeSensitiveSetMV(TimeSensitiveSetMV.EMVUD.MVUD1, 20.0)
        time_sensitive_set_mv_channel = TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel(
            global_index=1,
            mv_list=[time_sensitive_set_mv],
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

    def test_test_object_setting_to_cs(self):
        """Test conversion of TestObjectSetting to C# object"""
        test_object_setting = TestObjectSetting(
            mass=1.0,
            specific_capacity=2.0,
            nominal_capacity=3.0,
            nominal_ir=4.0,
            nominal_voltage=5.0,
            nominal_capacitor=6.0,
            max_current_charge=7.0,
            min_voltage_charge=8.0,
            max_voltage_charge=9.0,
            is_auto_calc_n_capacity=True
        )

        cs_instance = test_object_setting.to_cs()

        self.assertEqual(cs_instance.Mass, 1.0)
        self.assertEqual(cs_instance.SpecificCapacity, 2.0)
        self.assertEqual(cs_instance.NorminalCapacity, 3.0)
        self.assertEqual(cs_instance.NorminalIR, 4.0)
        self.assertEqual(cs_instance.NorminalVoltage, 5.0)
        self.assertEqual(cs_instance.NorminalCapacitor, 6.0)
        self.assertEqual(cs_instance.MaxCurrentCharge, 7.0)
        self.assertEqual(cs_instance.MinVoltageCharge, 8.0)
        self.assertEqual(cs_instance.MaxVoltageCharge, 9.0)
        self.assertEqual(cs_instance.IsAutoCalcNCapacity, True)

    def test_start_channel_info_to_cs(self):
        """Test conversion of StartChannelInfo to C# object"""
        test_object_setting = TestObjectSetting(
            mass=1.0,
            specific_capacity=2.0,
            nominal_capacity=3.0,
            nominal_ir=4.0,
            nominal_voltage=5.0,
            nominal_capacitor=6.0,
            max_current_charge=7.0,
            min_voltage_charge=8.0,
            max_voltage_charge=9.0,
            is_auto_calc_n_capacity=True
        )

        start_channel_info = StartChannelInfo(
            channel_index=1,
            test_name="TestName",
            schedule_name="ScheduleName",
            barcode="Barcode",
            test_object=test_object_setting
        )

        cs_instance = start_channel_info.to_cs()

        self.assertEqual(cs_instance.ChannelIndex, 1)
        self.assertEqual(cs_instance.TestName, "TestName")
        self.assertEqual(cs_instance.ScheduleName, "ScheduleName")
        self.assertEqual(cs_instance.Barcode, "Barcode")
        self.assertEqual(cs_instance.TestObject.Mass, 1.0)
        self.assertEqual(cs_instance.TestObject.SpecificCapacity, 2.0)
        self.assertEqual(cs_instance.TestObject.NorminalCapacity, 3.0)
        self.assertEqual(cs_instance.TestObject.NorminalIR, 4.0)
        self.assertEqual(cs_instance.TestObject.NorminalVoltage, 5.0)
        self.assertEqual(cs_instance.TestObject.NorminalCapacitor, 6.0)
        self.assertEqual(cs_instance.TestObject.MaxCurrentCharge, 7.0)
        self.assertEqual(cs_instance.TestObject.MinVoltageCharge, 8.0)
        self.assertEqual(cs_instance.TestObject.MaxVoltageCharge, 9.0)
        self.assertEqual(cs_instance.TestObject.IsAutoCalcNCapacity, True)

    def test_start_channel_advanced_args_to_cs(self):
        """Test conversion of StartChannelAdvancedArgs to C# object"""
        test_object_setting = TestObjectSetting(
            mass=1.0,
            specific_capacity=2.0,
            nominal_capacity=3.0,
            nominal_ir=4.0,
            nominal_voltage=5.0,
            nominal_capacitor=6.0,
            max_current_charge=7.0,
            min_voltage_charge=8.0,
            max_voltage_charge=9.0,
            is_auto_calc_n_capacity=True
        )

        start_channel_info = StartChannelInfo(
            channel_index=1,
            test_name="TestName",
            schedule_name="ScheduleName",
            barcode="Barcode",
            test_object=test_object_setting
        )

        start_channel_advanced_args = StartChannelAdvancedArgs(
            task_id=123,
            channels=[start_channel_info]
        )

        cs_instance = start_channel_advanced_args.to_cs()

        self.assertEqual(cs_instance.TaskID, 123)
        self.assertEqual(len(cs_instance.Channels), 1)
        self.assertEqual(cs_instance.Channels[0].ChannelIndex, 1)
        self.assertEqual(cs_instance.Channels[0].TestName, "TestName")
        self.assertEqual(cs_instance.Channels[0].ScheduleName, "ScheduleName")
        self.assertEqual(cs_instance.Channels[0].Barcode, "Barcode")
        self.assertEqual(cs_instance.Channels[0].TestObject.Mass, 1.0)
        self.assertEqual(cs_instance.Channels[0].TestObject.SpecificCapacity, 2.0)
        self.assertEqual(cs_instance.Channels[0].TestObject.NorminalCapacity, 3.0)
        self.assertEqual(cs_instance.Channels[0].TestObject.NorminalIR, 4.0)
        self.assertEqual(cs_instance.Channels[0].TestObject.NorminalVoltage, 5.0)
        self.assertEqual(cs_instance.Channels[0].TestObject.NorminalCapacitor, 6.0)
        self.assertEqual(cs_instance.Channels[0].TestObject.MaxCurrentCharge, 7.0)
        self.assertEqual(cs_instance.Channels[0].TestObject.MinVoltageCharge, 8.0)
        self.assertEqual(cs_instance.Channels[0].TestObject.MaxVoltageCharge, 9.0)
        self.assertEqual(cs_instance.Channels[0].TestObject.IsAutoCalcNCapacity, True)
 
    def test_get_mapping_aux_args_to_cs(self):
        """Test conversion of GetMappingAuxArgs to C# object"""
        get_mapping_aux_args = GetMappingAuxArgs(task_id=456)

        cs_instance = get_mapping_aux_args.to_cs()

        self.assertEqual(cs_instance.TaskID, 456)