import unittest
import os

import ArbinCTI.Core as ArbinCTI # type: ignore

from arbinctitools.src.argument.argument import (
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
    SafetyScope, 
    AuxChannelRequirementBase,
    AuxChannelRequirement,
    AuxSafetyRequirement,
    ScheduleModifyInfo,
    ModifyScheduleArgs
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
        time_sensitive_set_mv = TimeSensitiveSetMV(mvud=TimeSensitiveSetMV.EMVUD.MVUD1, value=10.5)

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

    def test_meta_variable_info_ex_initialization(self):
        """Test initialization of MetaVariableInfoEx with keyword arguments"""
        meta_var_info_ex = MetaVariableInfoEx(
            channel_index=1,
            mv_meta_code=100,
            mv_data_type=10.5,
            data_type=TE_DATA_TYPE.MP_DATA_TYPE_AuxdTdt,
        )

        self.assertEqual(meta_var_info_ex.channel_index, 1)
        self.assertEqual(meta_var_info_ex.mv_meta_code, 100)
        self.assertEqual(meta_var_info_ex.mv_data_type, 10.5)
        self.assertEqual(meta_var_info_ex.data_type, TE_DATA_TYPE.MP_DATA_TYPE_AuxdTdt)
        self.assertEqual(meta_var_info_ex.error, b'\x00')

        cs_instance = meta_var_info_ex.to_cs()

        self.assertEqual(cs_instance.m_ChannelIndexInGlobal, 1)
        self.assertEqual(cs_instance.m_MV_MetaCode, 100)
        self.assertEqual(cs_instance.m_fMV_Value, 10.5)
        self.assertEqual(cs_instance.DataType, ArbinCTI.TE_DATA_TYPE.MP_DATA_TYPE_AuxdTdt)
        self.assertEqual(cs_instance.Error, 0)

    def test_meta_variable_info_ex_initialization_from_cs(self):
        """Test initialization of MetaVariableInfoEx with C# object"""
        cs_instance = ArbinCTI.MetaVariableInfoEx()
        cs_instance.m_ChannelIndexInGlobal = 1
        cs_instance.m_MV_MetaCode = 100
        cs_instance.m_fMV_Value = 10.5
        cs_instance.DataType = ArbinCTI.TE_DATA_TYPE.MP_DATA_TYPE_AuxdTdt
        cs_instance.Error = b'\x01'

        meta_var_info_ex = MetaVariableInfoEx(cs_instance)

        self.assertEqual(meta_var_info_ex.channel_index, 1)
        self.assertEqual(meta_var_info_ex.mv_meta_code, 100)
        self.assertEqual(meta_var_info_ex.mv_data_type, 10.5)
        self.assertEqual(meta_var_info_ex.data_type, TE_DATA_TYPE.MP_DATA_TYPE_AuxdTdt)
        self.assertEqual(meta_var_info_ex.error, 1)

        if UNITTEST_VIEW_DICT:
            print("MetaVariableInfoEx:", meta_var_info_ex.to_dict())

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

    def test_safety_scope_to_cs(self):
        """Test conversion of SafetyScope to C# object"""
        safety_scope = SafetyScope(low=1.0, high=2.0)

        cs_instance = safety_scope.to_cs()

        self.assertEqual(cs_instance.Low, 1.0)
        self.assertEqual(cs_instance.High, 2.0)

    def test_aux_channel_requirement_base_to_cs(self):
        """Test conversion of AuxChannelRequirementBase to C# object"""
        aux_channel_req_base = AuxChannelRequirementBase(enable=True, aux_count=5)

        cs_instance = aux_channel_req_base.to_cs()

        self.assertEqual(cs_instance.Enable, True)
        self.assertEqual(cs_instance.AuxCount, 5)

    def test_aux_channel_requirement_to_cs(self):
        """Test conversion of AuxChannelRequirement to C# object"""
        safety_scope = SafetyScope(low=1.0, high=2.0)
        aux_channel_req = AuxChannelRequirement(enable=True, aux_count=5, safety_scope=safety_scope)

        cs_instance = aux_channel_req.to_cs()

        self.assertEqual(cs_instance.Enable, True)
        self.assertEqual(cs_instance.AuxCount, 5)
        self.assertEqual(cs_instance.SafetyScope.Low, 1.0)
        self.assertEqual(cs_instance.SafetyScope.High, 2.0)

    def test_aux_safety_requirement_to_cs(self):
        """Test conversion of AuxSafetyRequirement to C# object"""
        temp_scope = SafetyScope(low=1.0, high=2.0)
        current_scope = SafetyScope(low=3.0, high=4.0)
        voltage_scope = SafetyScope(low=5.0, high=6.0)
        aux_safety_req = AuxSafetyRequirement(enable=True, aux_count=5, temperature_safety_scope=temp_scope, current_safety_scope=current_scope, voltage_safety_scope=voltage_scope)

        cs_instance = aux_safety_req.to_cs()

        self.assertEqual(cs_instance.Enable, True)
        self.assertEqual(cs_instance.AuxCount, 5)
        self.assertEqual(cs_instance.TemperatureSafetyScope.Low, 1.0)
        self.assertEqual(cs_instance.TemperatureSafetyScope.High, 2.0)
        self.assertEqual(cs_instance.CurrentSafetyScope.Low, 3.0)
        self.assertEqual(cs_instance.CurrentSafetyScope.High, 4.0)
        self.assertEqual(cs_instance.VoltageSafetyScope.Low, 5.0)
        self.assertEqual(cs_instance.VoltageSafetyScope.High, 6.0)

    def test_schedule_modify_info_to_cs(self):
        """Test conversion of ScheduleModifyInfo to C# object"""
        aux_do_req = AuxChannelRequirementBase(enable=True, aux_count=5)
        aux_ao_req = AuxChannelRequirementBase(enable=False, aux_count=3)
        aux_voltage_req = AuxChannelRequirement(enable=True, aux_count=2, safety_scope=SafetyScope(low=1.0, high=2.0))
        aux_safety_req = AuxSafetyRequirement(enable=True, aux_count=1, temperature_safety_scope=SafetyScope(low=3.0, high=4.0))

        schedule_modify_info = ScheduleModifyInfo(
            schedule_name="TestSchedule",
            aux_do_requirement=aux_do_req,
            aux_ao_requirement=aux_ao_req,
            aux_voltage_requirement=aux_voltage_req,
            aux_safety_requirement=aux_safety_req
        )

        cs_instance = schedule_modify_info.to_cs()

        self.assertEqual(cs_instance.ScheduleName, "TestSchedule")
        self.assertEqual(cs_instance.AuxDORequirement.Enable, True)
        self.assertEqual(cs_instance.AuxDORequirement.AuxCount, 5)
        self.assertEqual(cs_instance.AuxAORequirement.Enable, False)
        self.assertEqual(cs_instance.AuxAORequirement.AuxCount, 3)
        self.assertEqual(cs_instance.AuxVoltageRequirement.Enable, True)
        self.assertEqual(cs_instance.AuxVoltageRequirement.AuxCount, 2)
        self.assertEqual(cs_instance.AuxVoltageRequirement.SafetyScope.Low, 1.0)
        self.assertEqual(cs_instance.AuxVoltageRequirement.SafetyScope.High, 2.0)
        self.assertEqual(cs_instance.AuxSafelyRequirement.Enable, True)
        self.assertEqual(cs_instance.AuxSafelyRequirement.AuxCount, 1)
        self.assertEqual(cs_instance.AuxSafelyRequirement.TemperatureSafetyScope.Low, 3.0)
        self.assertEqual(cs_instance.AuxSafelyRequirement.TemperatureSafetyScope.High, 4.0)

    def test_modify_schedule_args_to_cs(self):
        """Test conversion of ModifyScheduleArgs to C# object"""
        aux_do_req = AuxChannelRequirementBase(enable=True, aux_count=5)
        aux_ao_req = AuxChannelRequirementBase(enable=False, aux_count=3)
        aux_voltage_req = AuxChannelRequirement(enable=True, aux_count=2, safety_scope=SafetyScope(low=1.0, high=2.0))
        aux_safety_req = AuxSafetyRequirement(enable=True, aux_count=1, temperature_safety_scope=SafetyScope(low=3.0, high=4.0))

        schedule_modify_info = ScheduleModifyInfo(
            schedule_name="TestSchedule",
            aux_do_requirement=aux_do_req,
            aux_ao_requirement=aux_ao_req,
            aux_voltage_requirement=aux_voltage_req,
            aux_safety_requirement=aux_safety_req
        )

        modify_schedule_args = ModifyScheduleArgs(
            task_id=789,
            schedule_modify_info=[schedule_modify_info]
        )

        cs_instance = modify_schedule_args.to_cs()

        self.assertEqual(cs_instance.TaskID, 789)
        self.assertEqual(len(cs_instance.ScheduleModifyInfo), 1)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].ScheduleName, "TestSchedule")
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxDORequirement.Enable, True)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxDORequirement.AuxCount, 5)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxAORequirement.Enable, False)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxAORequirement.AuxCount, 3)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxVoltageRequirement.Enable, True)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxVoltageRequirement.AuxCount, 2)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxVoltageRequirement.SafetyScope.Low, 1.0)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxVoltageRequirement.SafetyScope.High, 2.0)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxSafelyRequirement.Enable, True)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxSafelyRequirement.AuxCount, 1)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxSafelyRequirement.TemperatureSafetyScope.Low, 3.0)
        self.assertEqual(cs_instance.ScheduleModifyInfo[0].AuxSafelyRequirement.TemperatureSafetyScope.High, 4.0)