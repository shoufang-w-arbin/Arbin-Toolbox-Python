import unittest
import os

from System import Int32 # type: ignore
from System.Collections.Generic import ( # type: ignore
    SortedDictionary,
    List
)
import ArbinCTI.Core as ArbinCTI # type: ignore

from ctitoolbox.src.data_type.cti_data_type import (
    TE_DATA_TYPE,
    TimeSensitiveSetMV
)
from ctitoolbox.src.feedback.schedule_operation import (
    AssignScheduleFeedback,
    AssignFileFeedback,
    SetMetaVariableFeedback,
    SetMetaVariableTimeSensitiveFeedback,
    GetMetaVariableFeedback
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
