import unittest
import os

from System import Int32 # type: ignore
from System.Collections.Generic import ( # type: ignore
    SortedDictionary,
    List
)
import ArbinCTI.Core as ArbinCTI # type: ignore

from arbintoolbox.src.arbincti.argument.argument import (
    TE_DATA_TYPE,
    TimeSensitiveSetMV
)
from arbintoolbox.src.arbincti.feedback.schedule_operation import (
    AssignScheduleFeedback,
    AssignFileFeedback,
    SetMetaVariableFeedback,
    SetMetaVariableTimeSensitiveFeedback,
    GetMetaVariableFeedback,
    UpdateParameterFeedback,
    ModifyScheduleFeedback,
    AssignBarcodeInfoFeedback,
    GetBarcodeInfoFeedback,
    GetMachineTypeFeedback,
    GetTrayStatusFeedback,
    EngageTrayFeedback,
)

UNITTEST_VIEW_DICT = os.getenv("UNITTEST_VIEW_DICT", False)

class TestFeedbackClasses(unittest.TestCase):

    def test_AssignScheduleFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandAssignScheduleFeed()
        cs_instance.Result = ArbinCTI.ArbinCommandAssignScheduleFeed.ASSIGN_TOKEN.CTI_ASSIGN_SUCCESS

        feedback_instance = AssignScheduleFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, AssignScheduleFeedback.EAssignToken.CTI_ASSIGN_SUCCESS)

        if UNITTEST_VIEW_DICT:
            print("AssignScheduleFeedback:", feedback_instance.to_dict())

    def test_AssignFileFeedback_instantiation(self):
        cs_instance                     = ArbinCTI.ArbinCommandAssignFileFeed()
        cs_instance.Result              = ArbinCTI.ArbinCommandAssignFileFeed.ASSIGN_TOKEN.CTI_ASSIGN_INDEX
        cs_instance.ChanListResultPairs = SortedDictionary[ArbinCTI.ArbinCommandAssignFileFeed.ASSIGN_TOKEN, List[Int32]]()


        list_instance1, list_instance2 = List[Int32](), List[Int32]()
        for i in range(1, 4):
            list_instance1.Add(i)
            list_instance2.Add(i + 3)

        cs_instance.ChanListResultPairs.Add(ArbinCTI.ArbinCommandAssignFileFeed.ASSIGN_TOKEN.CTI_ASSIGN_SUCCESS, list_instance1)
        cs_instance.ChanListResultPairs.Add(ArbinCTI.ArbinCommandAssignFileFeed.ASSIGN_TOKEN.CTI_ASSIGN_ERROR, list_instance2)
        cs_instance.Reason = "Reason"

        feedback_instance = AssignFileFeedback(cs_instance)
        self.assertEqual(feedback_instance.result, AssignFileFeedback.EAssignToken.CTI_ASSIGN_INDEX)
        self.assertEqual(feedback_instance.reason, "Reason")
        self.assertEqual(feedback_instance.channel_list_result[AssignFileFeedback.EAssignToken.CTI_ASSIGN_SUCCESS], list(list_instance1))
        self.assertEqual(feedback_instance.channel_list_result[AssignFileFeedback.EAssignToken.CTI_ASSIGN_ERROR], list(list_instance2))

        if UNITTEST_VIEW_DICT:
            print("AssignFileFeedback:", feedback_instance.to_dict())

    def test_SetMetaVariableFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandSetMetaVariableFeed()
        cs_instance.Result = ArbinCTI.ArbinCommandSetMetaVariableFeed.SET_MV_RESULT.CTI_SET_MV_CHANNEL_NOT_STARTED

        feedback_instance = SetMetaVariableFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, SetMetaVariableFeedback.EResult.CTI_SET_MV_CHANNEL_NOT_STARTED)

        if UNITTEST_VIEW_DICT:
            print("SetMetaVariableFeedback:", feedback_instance.to_dict())

    def test_SetMetaVariableTimeSensitiveFeedback_instantiation(self):
        mv_instance = ArbinCTI.TimeSensitiveSetMV()
        mv_instance.MVUD = ArbinCTI.TimeSensitiveSetMV.EMVUD.MVUD6
        mv_instance.Value = 1.23

        mv_list_instance = List[ArbinCTI.TimeSensitiveSetMV]()
        mv_list_instance.Add(mv_instance)

        time_sensitive_set_mv_result = ArbinCTI.ArbinCommandTimeSensitiveSetMVFeed.TimeSensitiveSetMVResult()
        time_sensitive_set_mv_result.Result = ArbinCTI.ArbinCommandTimeSensitiveSetMVFeed.EResult.SUCCESS_NOTRUNNING
        time_sensitive_set_mv_result.MachineStatus = ArbinCTI.ArbinCommandTimeSensitiveSetMVFeed.EControlStatus.Idle
        time_sensitive_set_mv_result.GlobalIndex = 1
        time_sensitive_set_mv_result.StepIndex = 2
        time_sensitive_set_mv_result.SubStepIndex = 3
        time_sensitive_set_mv_result.Current = 4.5
        time_sensitive_set_mv_result.Voltage = 6.789
        time_sensitive_set_mv_result.MVs = mv_list_instance

        setmv_list_instance = List[ArbinCTI.ArbinCommandTimeSensitiveSetMVFeed.TimeSensitiveSetMVResult]()
        setmv_list_instance.Add(time_sensitive_set_mv_result)

        cs_instance = ArbinCTI.ArbinCommandTimeSensitiveSetMVFeed()
        cs_instance.Results = setmv_list_instance

        feedback_instance = SetMetaVariableTimeSensitiveFeedback(cs_instance)

        self.assertEqual(feedback_instance.results[0].result, SetMetaVariableTimeSensitiveFeedback.EResult.SUCCESS_NOTRUNNING)
        self.assertEqual(feedback_instance.results[0].machine_status, SetMetaVariableTimeSensitiveFeedback.EControlStatus.Idle)
        self.assertEqual(feedback_instance.results[0].global_index, 1)
        self.assertEqual(feedback_instance.results[0].step_index, 2)
        self.assertEqual(feedback_instance.results[0].sub_step_index, 3)
        self.assertAlmostEqual(feedback_instance.results[0].current, 4.5)
        self.assertAlmostEqual(feedback_instance.results[0].voltage, 6.789)

        self.assertEqual(feedback_instance.results[0].mvs[0].mvud, TimeSensitiveSetMV.EMVUD.MVUD6)
        self.assertAlmostEqual(feedback_instance.results[0].mvs[0].value, 1.23)

        if UNITTEST_VIEW_DICT:
            print("SetMetaVariableTimeSensitiveFeedback:", feedback_instance.to_dict())

    def test_GetMetaVariableFeedback_instantiation(self):
        mv_info_instance = ArbinCTI.ArbinCommandGetMetaVariablesFeed.MetaVariableInfo()
        mv_info_instance.m_Channel = 1
        mv_info_instance.m_MV_Error = ArbinCTI.ArbinCommandGetMetaVariablesFeed.GET_MV_RESULT.CTI_GET_MV_DATATYPE_NOTSUPPORT
        mv_info_instance.m_MV_DataType = ArbinCTI.TE_DATA_TYPE.MP_DATA_TYPE_AuxFlowRate
        mv_info_instance.m_MV_MetaCode = 2
        mv_info_instance.m_Value = 3.45

        mv_info_list_instance = List[ArbinCTI.ArbinCommandGetMetaVariablesFeed.MetaVariableInfo]()
        mv_info_list_instance.Add(mv_info_instance)

        cs_instance = ArbinCTI.ArbinCommandGetMetaVariablesFeed()
        cs_instance.MetaVariableInfos = mv_info_list_instance

        feedback_instance = GetMetaVariableFeedback(cs_instance)

        self.assertIsInstance(feedback_instance.meta_variable_info, list)
        self.assertEqual(feedback_instance.meta_variable_info[0].channel_index, 1)
        self.assertEqual(feedback_instance.meta_variable_info[0].mv_error, GetMetaVariableFeedback.EResult.CTI_GET_MV_DATATYPE_NOTSUPPORT)
        self.assertEqual(feedback_instance.meta_variable_info[0].mv_data_type, TE_DATA_TYPE.MP_DATA_TYPE_AuxFlowRate)
        self.assertEqual(feedback_instance.meta_variable_info[0].mv_meta_code, 2)
        self.assertAlmostEqual(feedback_instance.meta_variable_info[0].value, 3.45)

        if UNITTEST_VIEW_DICT:
            print("GetMetaVariableFeedback:", feedback_instance.to_dict())


    def test_AssignFileFeedback_EFileKind_to_cs(self):
        for kind in AssignFileFeedback.EFileKind:
            with self.subTest(kind=kind):
                cs_kind = kind.to_cs()
                self.assertEqual(cs_kind, ArbinCTI.ArbinCommandAssignFileFeed.EFileKind(kind.value))

    def test_UpdateParameterFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandUpdateParameterFeed()
        cs_instance.Result = ArbinCTI.ArbinCommandUpdateParameterFeed.UPDATE_TOKEN.CTI_UPDATE_SUCCESS
        cs_instance.Reason = "Update successful"
        cs_instance.ResultChanListPairs = SortedDictionary[ArbinCTI.ArbinCommandUpdateParameterFeed.UPDATE_TOKEN, List[Int32]]()

        list_instance1, list_instance2 = List[Int32](), List[Int32]()
        for i in range(1, 4):
            list_instance1.Add(i)
            list_instance2.Add(i + 3)

        cs_instance.ResultChanListPairs.Add(ArbinCTI.ArbinCommandUpdateParameterFeed.UPDATE_TOKEN.CTI_UPDATE_SUCCESS, list_instance1)
        cs_instance.ResultChanListPairs.Add(ArbinCTI.ArbinCommandUpdateParameterFeed.UPDATE_TOKEN.CTI_UPDATE_ERROR, list_instance2)

        feedback_instance = UpdateParameterFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, UpdateParameterFeedback.EUpdateToken.CTI_UPDATE_SUCCESS)
        self.assertEqual(feedback_instance.reason, "Update successful")
        self.assertEqual(feedback_instance.chan_list_pairs[UpdateParameterFeedback.EUpdateToken.CTI_UPDATE_SUCCESS], list(list_instance1))
        self.assertEqual(feedback_instance.chan_list_pairs[UpdateParameterFeedback.EUpdateToken.CTI_UPDATE_ERROR], list(list_instance2))

        if UNITTEST_VIEW_DICT:
            print("UpdateParameterFeedback:", feedback_instance.to_dict())

    def test_ModifyScheduleFeedback_instantiation(self):
        modify_schedule_result = ArbinCTI.Common.ModifySchedule.ModifyScheduleResult()
        modify_schedule_result.ScheduleName = "TestSchedule"
        modify_schedule_result.Result = ArbinCTI.Common.Enumeration.MODIFY_SCHEDULE_TOKEN.CTI_MODIFY_SUCCESS
        modify_schedule_result.Message = "Modification successful"

        modify_schedule_result_list = List[ArbinCTI.Common.ModifySchedule.ModifyScheduleResult]()
        modify_schedule_result_list.Add(modify_schedule_result)

        cs_instance = ArbinCTI.ArbinCommandModifyScheduleFeed()
        cs_instance.TaskID = 123
        cs_instance.ScheduleModifyInfos = modify_schedule_result_list

        feedback_instance = ModifyScheduleFeedback(cs_instance)

        self.assertEqual(feedback_instance.task_id, 123)
        self.assertEqual(feedback_instance.schedule_modify_info[0].schedule_name, "TestSchedule")
        self.assertEqual(feedback_instance.schedule_modify_info[0].result, ModifyScheduleFeedback.EModifyScheduleToken.CTI_MODIFY_SUCCESS)
        self.assertEqual(feedback_instance.schedule_modify_info[0].message, "Modification successful")

        if UNITTEST_VIEW_DICT:
            print("ModifyScheduleFeedback:", feedback_instance.to_dict())

    def test_AssignBarcodeInfoFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandAssignBarcodeInfoFeed()
        cs_instance.ChannelType = ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.EChannelType.IV

        barcode_info_instance = ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.ChannelBarcodeInfo()
        barcode_info_instance.ChannelType = ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.EChannelType.IV
        barcode_info_instance.GlobalIndex = 1
        barcode_info_instance.Barcode = "123456"
        barcode_info_instance.Info = "Info"
        barcode_info_instance.Error = ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.ASSIGN_BARCODE_RESULT.CTI_ASSIGN_BARCODE_SUCCESS

        barcode_info_list_instance = List[ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.ChannelBarcodeInfo]()
        barcode_info_list_instance.Add(barcode_info_instance)

        cs_instance.BarcodeInfos = barcode_info_list_instance

        feedback_instance = AssignBarcodeInfoFeedback(cs_instance)

        self.assertEqual(feedback_instance.channel_type, AssignBarcodeInfoFeedback.EChannelType.IV)
        self.assertEqual(feedback_instance.barcode_info[0].channel_type, AssignBarcodeInfoFeedback.EChannelType.IV)
        self.assertEqual(feedback_instance.barcode_info[0].global_index, 1)
        self.assertEqual(feedback_instance.barcode_info[0].barcode, "123456")
        self.assertEqual(feedback_instance.barcode_info[0].info, "Info")
        self.assertEqual(feedback_instance.barcode_info[0].error, AssignBarcodeInfoFeedback.EAssignBarcodeResult.CTI_ASSIGN_BARCODE_SUCCESS)

        if UNITTEST_VIEW_DICT:
            print("AssignBarcodeInfoFeedback:", feedback_instance.to_dict())

    def test_AssignBarcodeInfoFeedback_ChannelBarcodeInfo_instantiation(self):
        channel_type = AssignBarcodeInfoFeedback.EChannelType.IV
        global_index = 1
        barcode = "123456"
        info = "Info"

        channel_barcode_info_instance = AssignBarcodeInfoFeedback.ChannelBarcodeInfo(channel_type, global_index, barcode, info)

        self.assertEqual(channel_barcode_info_instance.channel_type, channel_type)
        self.assertEqual(channel_barcode_info_instance.global_index, global_index)
        self.assertEqual(channel_barcode_info_instance.barcode, barcode)
        self.assertEqual(channel_barcode_info_instance.info, info)

        cs_instance = channel_barcode_info_instance.to_cs()
        self.assertEqual(cs_instance.ChannelType, ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.EChannelType.IV)
        self.assertEqual(cs_instance.GlobalIndex, global_index)
        self.assertEqual(cs_instance.Barcode, barcode)
        self.assertEqual(cs_instance.Info, info)

    def test_AssignBarcodeInfoFeedback_ChannelBarcodeInfo_instantiation_from_cs(self):
        cs_instance = ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.ChannelBarcodeInfo()
        cs_instance.ChannelType = ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.EChannelType.IV
        cs_instance.GlobalIndex = 1
        cs_instance.Barcode = "123456"
        cs_instance.Info = "Info"
        cs_instance.Error = ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.ASSIGN_BARCODE_RESULT.CTI_ASSIGN_BARCODE_SUCCESS

        channel_barcode_info_instance = AssignBarcodeInfoFeedback.ChannelBarcodeInfo(cs_instance)

        self.assertEqual(channel_barcode_info_instance.channel_type, AssignBarcodeInfoFeedback.EChannelType.IV)
        self.assertEqual(channel_barcode_info_instance.global_index, 1)
        self.assertEqual(channel_barcode_info_instance.barcode, "123456")
        self.assertEqual(channel_barcode_info_instance.info, "Info")
        self.assertEqual(channel_barcode_info_instance.error, AssignBarcodeInfoFeedback.EAssignBarcodeResult.CTI_ASSIGN_BARCODE_SUCCESS)

    def test_GetBarcodeInfoFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandGetBarcodeInfoFeed()
        cs_instance.ChannelType = ArbinCTI.ArbinCommandGetBarcodeInfoFeed.EChannelType.IV

        barcode_info_instance = ArbinCTI.ArbinCommandGetBarcodeInfoFeed.ChannelBarcodeInfo()
        barcode_info_instance.ChannelType = ArbinCTI.ArbinCommandGetBarcodeInfoFeed.EChannelType.IV
        barcode_info_instance.GlobalIndex = 1
        barcode_info_instance.Barcode = "123456"
        barcode_info_instance.Info = "Info"
        barcode_info_instance.Error = ArbinCTI.ArbinCommandGetBarcodeInfoFeed.GET_BARCODE_RESULT.CTI_GET_BARCODE_SUCCESS

        barcode_info_list_instance = List[ArbinCTI.ArbinCommandGetBarcodeInfoFeed.ChannelBarcodeInfo]()
        barcode_info_list_instance.Add(barcode_info_instance)

        cs_instance.BarcodeInfos = barcode_info_list_instance

        feedback_instance = GetBarcodeInfoFeedback(cs_instance)

        self.assertEqual(feedback_instance.channel_type, GetBarcodeInfoFeedback.EChannelType.IV)
        self.assertEqual(feedback_instance.barcode_info[0].channel_type, GetBarcodeInfoFeedback.EChannelType.IV)
        self.assertEqual(feedback_instance.barcode_info[0].global_index, 1)
        self.assertEqual(feedback_instance.barcode_info[0].barcode, "123456")
        self.assertEqual(feedback_instance.barcode_info[0].info, "Info")
        self.assertEqual(feedback_instance.barcode_info[0].error, GetBarcodeInfoFeedback.EGetBarcodeResult.CTI_GET_BARCODE_SUCCESS)

        if UNITTEST_VIEW_DICT:
            print("GetBarcodeInfoFeedback:", feedback_instance.to_dict())

    def test_GetBarcodeInfoFeedback_ChannelBarcodeInfo_instantiation_from_cs(self):
        cs_instance = ArbinCTI.ArbinCommandGetBarcodeInfoFeed.ChannelBarcodeInfo()
        cs_instance.ChannelType = ArbinCTI.ArbinCommandGetBarcodeInfoFeed.EChannelType.IV
        cs_instance.GlobalIndex = 1
        cs_instance.Barcode = "123456"
        cs_instance.Info = "Info"
        cs_instance.Error = ArbinCTI.ArbinCommandGetBarcodeInfoFeed.GET_BARCODE_RESULT.CTI_GET_BARCODE_SUCCESS

        channel_barcode_info_instance = GetBarcodeInfoFeedback.ChannelBarcodeInfo(cs_instance)

        self.assertEqual(channel_barcode_info_instance.channel_type, GetBarcodeInfoFeedback.EChannelType.IV)
        self.assertEqual(channel_barcode_info_instance.global_index, 1)
        self.assertEqual(channel_barcode_info_instance.barcode, "123456")
        self.assertEqual(channel_barcode_info_instance.info, "Info")
        self.assertEqual(channel_barcode_info_instance.error, GetBarcodeInfoFeedback.EGetBarcodeResult.CTI_GET_BARCODE_SUCCESS)