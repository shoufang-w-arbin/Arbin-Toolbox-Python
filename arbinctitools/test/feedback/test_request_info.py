import unittest
import os

import ArbinCTI.Core as ArbinCTI # type: ignore
from System import ( # type: ignore
    String,
    Array,
    UInt32,
)
from System.Collections.Generic import ( # type: ignore
    SortedDictionary,
    List, 
)

from arbinctitools.src.feedback.request_info import (
    GetStartDataFeedback,
    GetChannelDataFeedback,
    GetResumeDataFeedback,
    GetMappingAuxFeedback,
    GetSerialNumberFeedback, 
    GetSoftwareVersionFeedback,
    GetChannelDataSimpleModeFeedback,
    GetChannelsDataMinimalistModeFeedback,
    GetStringLimitLengthFeedback,
)

UNITTEST_VIEW_DICT = os.getenv("UNITTEST_VIEW_DICT", False)

class TestFeedbackClasses(unittest.TestCase):

    def test_GetSerailNumberFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandGetSerialNumberFeed()
        cs_instance.SerialNum   = 12345.6789
        cs_instance.Result      = ArbinCTI.ArbinCommandGetSerialNumberFeed.ASSIGN_TOKEN.CTI_GET_SERIAL_SUCCESS

        feedback_instance = GetSerialNumberFeedback(cs_instance)

        self.assertEqual(feedback_instance.serial_number, 12345.6789)
        self.assertEqual(feedback_instance.result, GetSerialNumberFeedback.EAssignToken.CTI_GET_SERIAL_SUCCESS)

        if UNITTEST_VIEW_DICT:
            print("GetSerailNumberFeedback:", feedback_instance.to_dict())

    def test_GetMITSVersionFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandGetServerSoftwareVersionNumberFeed()
        cs_instance.ServerVersionNumber = "1.2.3.4"

        feedback_instance = GetSoftwareVersionFeedback(cs_instance)

        self.assertEqual(feedback_instance.version, "1.2.3.4")

        if UNITTEST_VIEW_DICT:
            print("GetMITSVersionFeedback:", feedback_instance.to_dict())
            
    def test_GetStartDataFeedback_instantiation(self):
        str_list_instance = List[String]()
        str_list_instance.Add("Test1")
        str_list_instance.Add("Step2")

        assignment_info_instance = ArbinCTI.ArbinCommandGetStartDataFeed.StartDatalInfo()
        assignment_info_instance.Channel = 1
        assignment_info_instance.channelCode = ArbinCTI.ArbinCommandGetStartDataFeed.EGetDataResult.SUCCESS
        assignment_info_instance.Schedule = "TestSchedule"
        assignment_info_instance.fMV_UD1 = 1.1
        assignment_info_instance.fMV_UD2 = 2.2
        assignment_info_instance.fMV_UD3 = 3.3
        assignment_info_instance.fMV_UD4 = 4.4
        assignment_info_instance.fMV_UD5 = 5.5
        assignment_info_instance.fMV_UD6 = 6.6
        assignment_info_instance.fMV_UD7 = 7.7
        assignment_info_instance.fMV_UD8 = 8.8
        assignment_info_instance.fMV_UD9 = 9.9
        assignment_info_instance.fMV_UD10 = 10.1
        assignment_info_instance.fMV_UD11 = 11.11
        assignment_info_instance.fMV_UD12 = 12.12
        assignment_info_instance.fMV_UD13 = 13.13
        assignment_info_instance.fMV_UD14 = 14.14
        assignment_info_instance.fMV_UD15 = 15.15
        assignment_info_instance.fMV_UD16 = 16.16
        assignment_info_instance.TestNames = str_list_instance
        assignment_info_instance.Steps = str_list_instance

        cs_instance = ArbinCTI.ArbinCommandGetStartDataFeed()
        cs_instance.m_Channels = List[ArbinCTI.ArbinCommandGetStartDataFeed.StartDatalInfo]()
        cs_instance.m_Channels.Add(assignment_info_instance)

        feedback_instance = GetStartDataFeedback(cs_instance)

        self.assertEqual(len(feedback_instance.channel_data), 1)
        channel = feedback_instance.channel_data[0]
        self.assertEqual(channel.channel, 1)
        self.assertEqual(channel.channel_code, GetStartDataFeedback.EResult.SUCCESS)
        self.assertEqual(channel.schedule, "TestSchedule")
        self.assertAlmostEqual(channel.fMV_UD1, 1.1, places=6)
        self.assertAlmostEqual(channel.fMV_UD2, 2.2, places=6)
        self.assertAlmostEqual(channel.fMV_UD3, 3.3, places=6)
        self.assertAlmostEqual(channel.fMV_UD4, 4.4, places=6)
        self.assertAlmostEqual(channel.fMV_UD5, 5.5, places=6)
        self.assertAlmostEqual(channel.fMV_UD6, 6.6, places=6)
        self.assertAlmostEqual(channel.fMV_UD7, 7.7, places=6)
        self.assertAlmostEqual(channel.fMV_UD8, 8.8, places=6)
        self.assertAlmostEqual(channel.fMV_UD9, 9.9, places=6)
        self.assertAlmostEqual(channel.fMV_UD10, 10.1, places=6)
        self.assertAlmostEqual(channel.fMV_UD11, 11.11, places=6)
        self.assertAlmostEqual(channel.fMV_UD12, 12.12, places=6)
        self.assertAlmostEqual(channel.fMV_UD13, 13.13, places=6)
        self.assertAlmostEqual(channel.fMV_UD14, 14.14, places=6)
        self.assertAlmostEqual(channel.fMV_UD15, 15.15, places=6)
        self.assertAlmostEqual(channel.fMV_UD16, 16.16, places=6)
        self.assertEqual(channel.test_names, ["Test1", "Step2"])
        self.assertEqual(channel.step_names, ["Test1", "Step2"])
        
        if UNITTEST_VIEW_DICT:
            print("GetStartDataFeedback:", feedback_instance.to_dict())

    def test_GetChannelDataFeedback_instantiation(self):
        can_list_instance = List[ArbinCTI.ArbinCommandGetChannelDataFeed.CANInfo]()
        can_info_instance = ArbinCTI.ArbinCommandGetChannelDataFeed.CANInfo()
        can_info_instance.nIndex = 123
        can_list_instance.Add(can_info_instance)

        smb_list_instance = List[ArbinCTI.ArbinCommandGetChannelDataFeed.SMBInfo]()
        smb_info_instance = ArbinCTI.ArbinCommandGetChannelDataFeed.SMBInfo()
        smb_info_instance.nIndex = 456
        smb_list_instance.Add(smb_info_instance)

        aux_type_num = int(ArbinCTI.ArbinCommandGetChannelDataFeed.ChannelInfo.AUX_TYPE.MAX_NUM)
        aux_array_instance = Array.CreateInstance(
            List[ArbinCTI.ArbinCommandGetChannelDataFeed.AuxData], 
            aux_type_num
        )
        for i in range(aux_type_num):
            aux_array_instance[i] = List[ArbinCTI.ArbinCommandGetChannelDataFeed.AuxData]()
        aux_data_instance = ArbinCTI.ArbinCommandGetChannelDataFeed.AuxData()
        aux_data_instance.Value = 1.23
        aux_data_instance.dtValue = 45.6
        aux_array_instance[0].Add(aux_data_instance)

        eq_list_instance = List[ArbinCTI.Common.CTISPTTEQData]()
        eq_data_instance = ArbinCTI.Common.CTISPTTEQData()
        eq_data_instance.ParentTrayGlobalIndex = 34
        eq_list_instance.Add(eq_data_instance)

        cell_list_instance = List[ArbinCTI.Common.CTISPTTCellData]()
        cell_data_instance = ArbinCTI.Common.CTISPTTCellData()
        cell_data_instance.ParentTrayGlobalIndex = 56
        cell_list_instance.Add(cell_data_instance)

        channel_info_instance = ArbinCTI.ArbinCommandGetChannelDataFeed.ChannelInfo()
        channel_info_instance.Channel = 1
        channel_info_instance.Status = ArbinCTI.ArbinCommandGetChannelDataFeed.ChannelStatus.External_Charge
        channel_info_instance.CommFailure = False
        channel_info_instance.Schedule = "TestSchedule"
        channel_info_instance.CANCfg = "CANConfig"
        channel_info_instance.SMBCfg = "SMBConfig"
        channel_info_instance.Chart = "TestChart"
        channel_info_instance.Testname = "TestName"
        channel_info_instance.ExitCondition = "ExitCondition"
        channel_info_instance.StepAndCycle = "StepCycle"
        channel_info_instance.StepIndex = 2
        channel_info_instance.CycleIndex = 3
        channel_info_instance.Barcode = "123456789"
        channel_info_instance.MasterChannel = 0
        channel_info_instance.TestTime = 123.45
        channel_info_instance.StepTime = 12.34
        channel_info_instance.Voltage = 3.7
        channel_info_instance.Current = 1.5
        channel_info_instance.Power = 5.55
        channel_info_instance.TestObject = "Battery"
        channel_info_instance.NominalCapacity = 2500.0
        channel_info_instance.Imax = 2.0
        channel_info_instance.Vmax = 4.2
        channel_info_instance.Vmin = 3.0
        channel_info_instance.NominalVoltage = 3.7
        channel_info_instance.NominalCapacitance = 0.0
        channel_info_instance.NominalIR = 0.01
        channel_info_instance.SpecificCapacity = 1.0
        channel_info_instance.IsAutoCalculate = True
        channel_info_instance.Mass = 50.0
        channel_info_instance.ChargeCapacity = 1000.0
        channel_info_instance.DischargeCapacity = 800.0
        channel_info_instance.ChargeEnergy = 50.0
        channel_info_instance.DishargeEnergy = 40.0
        channel_info_instance.InternalResistance = 0.005
        channel_info_instance.dvdt = 0.1
        channel_info_instance.dvdq = 0.05
        channel_info_instance.dqdv = 0.02
        channel_info_instance.ACR = 0.001
        channel_info_instance.ACI = 0.002
        channel_info_instance.ACIPhase = 0.5
        channel_info_instance.CAN       = can_list_instance
        channel_info_instance.SMB       = smb_list_instance
        channel_info_instance.Auxs      = aux_array_instance
        channel_info_instance.EQDatas   = eq_list_instance
        channel_info_instance.CellDatas = cell_list_instance

        cs_instance = ArbinCTI.ArbinCommandGetChannelDataFeed()
        cs_instance.m_Channels = List[ArbinCTI.ArbinCommandGetChannelDataFeed.ChannelInfo]()
        cs_instance.m_Channels.Add(channel_info_instance)

        feedback_instance = GetChannelDataFeedback(cs_instance)

        self.assertEqual(len(feedback_instance.channel_data), 1)
        channel_data = feedback_instance.channel_data[0]
        self.assertEqual(channel_data.channel_index, 1)
        self.assertEqual(channel_data.status, GetChannelDataFeedback.EChannelStatus.External_Charge)
        self.assertFalse(channel_data.comm_failure)
        self.assertEqual(channel_data.schedule, "TestSchedule")
        self.assertEqual(channel_data.can_cfg, "CANConfig")
        self.assertEqual(channel_data.smb_cfg, "SMBConfig")
        self.assertEqual(channel_data.chart, "TestChart")
        self.assertEqual(channel_data.test_name, "TestName")
        self.assertEqual(channel_data.exit_condition, "ExitCondition")
        self.assertEqual(channel_data.step_and_cycle, "StepCycle")
        self.assertEqual(channel_data.step_index, 2)
        self.assertEqual(channel_data.cycle_index, 3)
        self.assertEqual(channel_data.barcode, "123456789")
        self.assertEqual(channel_data.master_channel, 0)
        self.assertAlmostEqual(channel_data.test_time, 123.45, places=6)
        self.assertAlmostEqual(channel_data.step_time, 12.34, places=6)
        self.assertAlmostEqual(channel_data.voltage, 3.7, places=6)
        self.assertAlmostEqual(channel_data.current, 1.5, places=6)
        self.assertAlmostEqual(channel_data.power, 5.55, places=6)
        self.assertEqual(channel_data.test_object, "Battery")
        self.assertAlmostEqual(channel_data.nominal_capacity, 2500.0, places=6)
        self.assertAlmostEqual(channel_data.imax, 2.0, places=6)
        self.assertAlmostEqual(channel_data.vmax, 4.2, places=6)
        self.assertAlmostEqual(channel_data.vmin, 3.0, places=6)
        self.assertAlmostEqual(channel_data.nominal_voltage, 3.7, places=6)
        self.assertAlmostEqual(channel_data.nominal_capacitance, 0.0, places=6)
        self.assertAlmostEqual(channel_data.nominal_ir, 0.01, places=6)
        self.assertAlmostEqual(channel_data.specific_capacity, 1.0, places=6)
        self.assertTrue(channel_data.is_auto_calculate)
        self.assertAlmostEqual(channel_data.mass, 50.0, places=6)
        self.assertAlmostEqual(channel_data.charge_capacity, 1000.0, places=6)
        self.assertAlmostEqual(channel_data.discharge_capacity, 800.0, places=6)
        self.assertAlmostEqual(channel_data.charge_energy, 50.0, places=6)
        self.assertAlmostEqual(channel_data.discharge_energy, 40.0, places=6)
        self.assertAlmostEqual(channel_data.internal_resistance, 0.005, places=6)
        self.assertAlmostEqual(channel_data.dvdt, 0.1, places=6)
        self.assertAlmostEqual(channel_data.dvdq, 0.05, places=6)
        self.assertAlmostEqual(channel_data.dqdv, 0.02, places=6)
        self.assertAlmostEqual(channel_data.acr, 0.001, places=6)
        self.assertAlmostEqual(channel_data.aci, 0.002, places=6)
        self.assertAlmostEqual(channel_data.aci_phase, 0.5, places=6)
        self.assertEqual(len(channel_data.can), 1)
        self.assertEqual(channel_data.can[0].idx, 123)
        
        self.assertEqual(len(channel_data.smb), 1)
        self.assertEqual(channel_data.smb[0].idx, 456)

        self.assertEqual(len(channel_data.auxs), 12)
        self.assertEqual(len(channel_data.auxs[0]), 1)
        self.assertAlmostEqual(channel_data.auxs[0][0].value, 1.23, places=5)
        self.assertAlmostEqual(channel_data.auxs[0][0].value_dt, 45.6, places=5)

        self.assertEqual(len(channel_data.eq_data), 1)
        self.assertEqual(channel_data.eq_data[0].parent_tray_global_index, 34)

        self.assertEqual(len(channel_data.cell_data), 1)
        self.assertEqual(channel_data.cell_data[0].parent_tray_global_index, 56)

        if UNITTEST_VIEW_DICT:
            print("GetChannelDataFeedback:", feedback_instance.to_dict())

    def test_EChannelType_to_cs(self):
        self.assertEqual(GetChannelDataFeedback.EGetChannelType.ALLCHANNEL.to_cs(), ArbinCTI.ArbinCommandGetChannelDataFeed.GET_CHANNEL_TYPE.ALLCHANNEL)
        self.assertEqual(GetChannelDataFeedback.EGetChannelType.RUNNING.to_cs(), ArbinCTI.ArbinCommandGetChannelDataFeed.GET_CHANNEL_TYPE.RUNNING)
        self.assertEqual(GetChannelDataFeedback.EGetChannelType.UNSAFE.to_cs(), ArbinCTI.ArbinCommandGetChannelDataFeed.GET_CHANNEL_TYPE.UNSAFE)

    def test_GetMappingAuxFeedback_instantiation(self):
        aux_channel_info_instance = ArbinCTI.Common.GetMappingAux.AuxChannelInfo()
        aux_channel_info_instance.AuxChannelType = ArbinCTI.EAuxChannelType.Voltage
        aux_channel_info_instance.AuxCount = 5

        mapping_info_instance = ArbinCTI.Common.GetMappingAux.MappingInfo()
        mapping_info_instance.ChannelIndex = 1
        mapping_info_instance.AuxChannelInfos = List[ArbinCTI.Common.GetMappingAux.AuxChannelInfo]()
        mapping_info_instance.AuxChannelInfos.Add(aux_channel_info_instance)

        feedback_instance = ArbinCTI.ArbinCommandGetMappingAuxFeed()
        feedback_instance.TaskID = 123
        feedback_instance.MappingInfos = List[ArbinCTI.Common.GetMappingAux.MappingInfo]()
        feedback_instance.MappingInfos.Add(mapping_info_instance)

        feedback = GetMappingAuxFeedback(feedback_instance)

        self.assertEqual(feedback.task_id, 123)
        self.assertEqual(len(feedback.mapping_info), 1)
        mapping_info = feedback.mapping_info[0]
        self.assertEqual(mapping_info.channel_index, 1)
        self.assertEqual(len(mapping_info.aux_channel_info), 1)
        aux_channel_info = mapping_info.aux_channel_info[0]
        self.assertEqual(aux_channel_info.aux_channel_type, GetMappingAuxFeedback.EAuxChannelType.Voltage)
        self.assertEqual(aux_channel_info.aux_count, 5)

        if UNITTEST_VIEW_DICT:
            print("GetMappingAuxFeedback:", feedback.to_dict())

    def test_GetResumeDataFeedback_instantiation(self):
        resume_data_instance = ArbinCTI.ArbinCommandGetResumeDataFeed.ResumeDatalInfo.RESUME_DATA()
        resume_data_instance.TestID = 1
        resume_data_instance.Cycle = 2
        resume_data_instance.StepIndex = 3
        resume_data_instance.TestTime = 123.45
        resume_data_instance.StepTime = 12.34
        resume_data_instance.CCapacity = 100.0
        resume_data_instance.DCapacity = 80.0
        resume_data_instance.CEnergy = 50.0
        resume_data_instance.DEnergy = 40.0
        resume_data_instance.TC_Time1 = 1.1
        resume_data_instance.TC_CCapacity1 = 10.0
        resume_data_instance.TC_DCapacity1 = 15.0
        resume_data_instance.TC_CEnergy1 = 5.0
        resume_data_instance.TC_DEnergy1 = 7.0
        resume_data_instance.TC_Counter1 = 1
        resume_data_instance.MVUD1 = 1.1

        assignment_info_instance = ArbinCTI.ArbinCommandGetResumeDataFeed.ResumeDatalInfo()
        assignment_info_instance.Channel = 1
        assignment_info_instance.channelCode = ArbinCTI.ArbinCommandGetResumeDataFeed.EGetDataResult.SUCCESS
        assignment_info_instance.ResumeData = resume_data_instance
        assignment_info_instance.TestName = "TestName"
        assignment_info_instance.Schedule = "TestSchedule"
        assignment_info_instance.Createor = "Creator"
        assignment_info_instance.Comment = "Comment"
        assignment_info_instance.StartTime = "StartTime"
        assignment_info_instance.Steps = List[String]()
        assignment_info_instance.Steps.Add("Step1")
        assignment_info_instance.Steps.Add("Step2")

        cs_instance = ArbinCTI.ArbinCommandGetResumeDataFeed()
        cs_instance.m_Channels = List[ArbinCTI.ArbinCommandGetResumeDataFeed.ResumeDatalInfo]()
        cs_instance.m_Channels.Add(assignment_info_instance)

        feedback_instance = GetResumeDataFeedback(cs_instance)

        self.assertEqual(len(feedback_instance.channel_data), 1)
        channel = feedback_instance.channel_data[0]
        self.assertEqual(channel.channel_index, 1)
        self.assertEqual(channel.channel_code, GetResumeDataFeedback.EResult.SUCCESS)
        self.assertEqual(channel.test_name, "TestName")
        self.assertEqual(channel.schedule, "TestSchedule")
        self.assertEqual(channel.creator, "Creator")
        self.assertEqual(channel.comment, "Comment")
        self.assertEqual(channel.start_time, "StartTime")
        self.assertEqual(channel.step_names, ["Step1", "Step2"])

        resume_data = channel.resume_data
        self.assertEqual(resume_data.test_id, 1)
        self.assertEqual(resume_data.cycle, 2)
        self.assertEqual(resume_data.step_index, 3)
        self.assertAlmostEqual(resume_data.test_time, 123.45, places=6)
        self.assertAlmostEqual(resume_data.step_time, 12.34, places=6)
        self.assertAlmostEqual(resume_data.c_capacity, 100.0, places=6)
        self.assertAlmostEqual(resume_data.d_capacity, 80.0, places=6)
        self.assertAlmostEqual(resume_data.c_energy, 50.0, places=6)
        self.assertAlmostEqual(resume_data.d_energy, 40.0, places=6)
        self.assertAlmostEqual(resume_data.tc_time1, 1.1, places=6)
        self.assertAlmostEqual(resume_data.tc_c_capacity1, 10.0, places=6)
        self.assertAlmostEqual(resume_data.tc_d_capacity1, 15.0, places=6)
        self.assertAlmostEqual(resume_data.tc_c_energy1, 5.0, places=6)
        self.assertAlmostEqual(resume_data.tc_d_energy1, 7.0, places=6)
        self.assertAlmostEqual(resume_data.tc_counter1, 1, places=6)
        self.assertAlmostEqual(resume_data.mvud1, 1.1, places=6)

        if UNITTEST_VIEW_DICT:
            print("GetResumeDataFeedback:", feedback_instance.to_dict())

    def test_GetChannelDataSimpleModeFeedback_instantiation(self):
        aux_array_instance = Array.CreateInstance(
            List[ArbinCTI.ArbinCommandGetChannelDataFeed.AuxData], 
            12
        )
        for i in range(12):
            aux_array_instance[i] = List[ArbinCTI.ArbinCommandGetChannelDataFeed.AuxData]()
        aux_data_instance = ArbinCTI.ArbinCommandGetChannelDataFeed.AuxData()
        aux_data_instance.Value = 1.23
        aux_data_instance.dtValue = 45.6
        aux_array_instance[0].Add(aux_data_instance)

        channel_info_instance = ArbinCTI.ArbinCommandGetChannelDataSimpleModeFeed.ChannelInfo()
        channel_info_instance.Channel = 1
        channel_info_instance.Status = ArbinCTI.ArbinCommandGetChannelDataFeed.ChannelStatus.External_Charge
        channel_info_instance.CommFailure = False
        channel_info_instance.MasterChannel = 0
        channel_info_instance.TestTime = 123.45
        channel_info_instance.StepTime = 12.34
        channel_info_instance.Voltage = 3.7
        channel_info_instance.Current = 1.5
        channel_info_instance.Auxs = aux_array_instance

        cs_instance = ArbinCTI.ArbinCommandGetChannelDataSimpleModeFeed()
        cs_instance.m_Channels = List[ArbinCTI.ArbinCommandGetChannelDataSimpleModeFeed.ChannelInfo]()
        cs_instance.m_Channels.Add(channel_info_instance)

        feedback_instance = GetChannelDataSimpleModeFeedback(cs_instance)

        self.assertEqual(len(feedback_instance.channel_data), 1)
        channel_data = feedback_instance.channel_data[0]
        self.assertEqual(channel_data.channel_index, 1)
        self.assertEqual(channel_data.status, GetChannelDataFeedback.EChannelStatus.External_Charge)
        self.assertFalse(channel_data.comm_failure)
        self.assertEqual(channel_data.master_channel, 0)
        self.assertAlmostEqual(channel_data.test_time, 123.45, places=6)
        self.assertAlmostEqual(channel_data.step_time, 12.34, places=6)
        self.assertAlmostEqual(channel_data.voltage, 3.7, places=6)
        self.assertAlmostEqual(channel_data.current, 1.5, places=6)
        self.assertEqual(len(channel_data.auxs), 12)
        self.assertEqual(len(channel_data.auxs[0]), 1)
        self.assertAlmostEqual(channel_data.auxs[0][0].value, 1.23, places=5)
        self.assertAlmostEqual(channel_data.auxs[0][0].value_dt, 45.6, places=5)

        if UNITTEST_VIEW_DICT:
            print("GetChannelDataSimpleModeFeedback:", feedback_instance.to_dict())

    def test_GetStringLimitLengthFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandGetStringLimitLengthFeed()
        cs_instance.StringLimitDatas = SortedDictionary[ArbinCTI.ArbinCommandGetStringLimitLengthFeed.ECTIStringLimitLengthType, UInt32]()
        cs_instance.StringLimitDatas.Add(ArbinCTI.ArbinCommandGetStringLimitLengthFeed.ECTIStringLimitLengthType.TestName, 50)

        feedback_instance = GetStringLimitLengthFeedback(cs_instance)

        self.assertEqual(len(feedback_instance.string_limit_data), 1)
        string_limit_data = feedback_instance.string_limit_data
        self.assertEqual(list(string_limit_data.keys())[0], GetStringLimitLengthFeedback.ECTIStringLimitLengthType.TestName)
        self.assertEqual(list(string_limit_data.values())[0], 50)

        if UNITTEST_VIEW_DICT:
            print("GetStringLimitLengthFeedback:", feedback_instance.to_dict())

    def test_GetChannelsDataMinimalistModeFeedback_instantiation(self):
        channel_info_instance = ArbinCTI.ArbinCommandGetChannelDataMinimalistModeFeed.ChannelInfo()
        channel_info_instance.Channel = 1
        channel_info_instance.Voltage = 3.7
        channel_info_instance.Current = 1.5

        cs_instance = ArbinCTI.ArbinCommandGetChannelDataMinimalistModeFeed()
        cs_instance.m_Channels = List[ArbinCTI.ArbinCommandGetChannelDataMinimalistModeFeed.ChannelInfo]()
        cs_instance.m_Channels.Add(channel_info_instance)

        feedback_instance = GetChannelsDataMinimalistModeFeedback(cs_instance)

        self.assertEqual(len(feedback_instance.channel_data), 1)
        channel_data = feedback_instance.channel_data[0]
        self.assertEqual(channel_data.channel_index, 1)
        self.assertAlmostEqual(channel_data.voltage, 3.7, places=6)
        self.assertAlmostEqual(channel_data.current, 1.5, places=6)

        if UNITTEST_VIEW_DICT:
            print("GetChannelsDataMinimalistModeFeedback:", feedback_instance.to_dict())