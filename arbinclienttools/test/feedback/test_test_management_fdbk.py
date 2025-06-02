import unittest
import System
from System.Collections.Generic import List as CsList
from System import Int32, Double, String, DateTime
import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from arbinclienttools.src.feedback.ttest_management import (
    UploadFileResult,
    BrowseFileListFeedback,
    AssignFileFeedback,
    UpdateMetaVariableFeedback,
    GetMetaVariablesFeedback,
    AssignBarcodeInfoFeedback,
    TimeSensitiveSetMVFeedback,
)
from arbinclienttools.src.enumeration import (
    EUploadFileResult,
    EBrowseDirectoryResult,
    ECommonResult,
    EChannelStatus,
    EAssignFileResult
)


class TestTestManagementFeedback(unittest.TestCase):

    def test_upload_file_result_initialization(self):
        mock_obj = ArbinDataModel.TestManagement.UploadFileResult()
        mock_obj.Result = "Success"
        mock_obj.UploadResult = ArbinDataModel.EUploadFileResult.Success
        mock_obj.IsCancelUploadFile = False
        mock_obj.ProgressRate = 75.0

        result = UploadFileResult(mock_obj)

        self.assertEqual(result.result, "Success")
        self.assertEqual(result.upload_result, EUploadFileResult.Success)
        self.assertFalse(result.is_cancel_upload_file)
        self.assertEqual(result.progress_rate, 75.0)

    def test_browse_file_list_feedback_initialization(self):
        obj = ArbinDataModel.TestManagement.BrowseFileListFDBK()
        obj.Result = "OK"
        obj.BrowseDirectoryResult = ArbinDataModel.EBrowseDirectoryResult.Success
        obj.SN = "101"

        file_info = ArbinDataModel.TestManagement.DirFileInfo()
        file_info.Type = "File"
        file_info.DirFileName = "data.csv"
        file_info.Size = 2048
        file_info.ModifiedTime = "2025-05-01 10:00:00"

        obj.DirFileInfoList.Add(file_info)

        result = BrowseFileListFeedback(obj)

        self.assertEqual(result.result, "OK")
        self.assertEqual(result.browse_directory_result, EBrowseDirectoryResult.Success)
        self.assertEqual(len(result.dir_file_info_list), 1)
        self.assertEqual(result.dir_file_info_list[0].dir_file_name, "data.csv")
        self.assertEqual(result.sn, 101)

    def test_assign_file_feedback_initialization(self):
        mock_obj = ArbinDataModel.TestManagement.AssignFileFDBK()
        mock_obj.SuccessfulChannelIDs = CsList[System.Int32]()

        failed_result = ArbinDataModel.TestManagement.AssignFileResult()
        failed_result.ChannelID = 0
        failed_result.Result = "Success"
        failed_result.AssignFileResult = EAssignFileResult.Success
        
        mock_obj.FailedResults.Add(failed_result)
        mock_obj.SN = "5678"

        feedback = AssignFileFeedback(mock_obj)

        self.assertIsInstance(feedback.successful_channel_id, list)
        self.assertEqual(len(feedback.failed_result), 1)
        self.assertEqual(feedback.failed_result[0].channel_id, 0)
        self.assertEqual(feedback.failed_result[0].result, "Success")
        self.assertEqual(feedback.failed_result[0].assign_result, EAssignFileResult.Success)
        self.assertEqual(feedback.sn, 5678)

    def test_update_meta_variable_feedback_initialization(self):
        mock_obj = ArbinDataModel.TestManagement.UpdateMetaVariablesFDBK()
        meta_variable_info = ArbinDataModel.Common.AIMetaVariableInfo()
        meta_variable_info.GlobalID = 101
        meta_variable_info.MetaVariableType = ArbinDataModel.EMetaVariableType.MetaCode_PV_StepIndex
        meta_variable_info.Value = 0
        meta_variable_info.Result = "OK"
        meta_variable_info.MetavariableResult = ArbinDataModel.EMetavariableResult.Success
        meta_variable_info.Index = 1
        meta_variable_info.MetaDataType = ArbinDataModel.EMetaDataType.MetaVariable
        meta_variable_info.MetaCode = ArbinDataModel.EMetavariableCode.MetaCode_PV_StepIndex
        mock_obj.SN = "1213"

        mock_obj.MetaVariableInfos.Add(meta_variable_info)
        
        feedback = UpdateMetaVariableFeedback(mock_obj)

        self.assertEqual(feedback.sn, 1213)
        self.assertEqual(len(feedback.meta_variable_info), 1)
        self.assertEqual(feedback.meta_variable_info[0].global_id, 101)
        self.assertEqual(feedback.meta_variable_info[0].value, 0)
        self.assertEqual(feedback.meta_variable_info[0].result, "OK")

    def test_get_meta_variables_feedback_initialization(self):
        mock_obj = ArbinDataModel.RequestInformation.GetMetaVariablesFDBK()
        meta_variable_info = ArbinDataModel.Common.AIMetaVariableInfo()
        meta_variable_info.GlobalID = 101
        meta_variable_info.MetaVariableType = ArbinDataModel.EMetaVariableType.MetaCode_PV_StepIndex
        meta_variable_info.Value = 0
        meta_variable_info.Result = "OK"
        meta_variable_info.MetavariableResult = ArbinDataModel.EMetavariableResult.Success
        meta_variable_info.Index = 1
        meta_variable_info.MetaDataType = ArbinDataModel.EMetaDataType.MetaVariable
        meta_variable_info.MetaCode = ArbinDataModel.EMetavariableCode.MetaCode_PV_StepIndex
        mock_obj.SN = "1213"

        mock_obj.MetaVariableInfos.Add(meta_variable_info)

        feedback = GetMetaVariablesFeedback(mock_obj)

        self.assertEqual(feedback.sn, 1213)
        self.assertEqual(len(feedback.meta_variable_info), 1)
        self.assertEqual(feedback.meta_variable_info[0].global_id, 101)
        self.assertEqual(feedback.meta_variable_info[0].value, 0)
        self.assertEqual(feedback.meta_variable_info[0].result, "OK")

    def test_assign_barcode_info_feedback_initialization(self):
        obj = ArbinDataModel.TestManagement.AssignBarcodeInfoFDBK()
        barcode = ArbinDataModel.Common.BarcodeInfo()
        barcode.BarcodeType = ArbinDataModel.EBarcodeType.IV
        barcode.GlobalID = 1001
        barcode.Barcode = "ABC123"
        barcode.Info = "Test Info"
        barcode.Result = "OK"
        barcode.BarcodeResult = ArbinDataModel.EBarcodeResult.Success
        obj.BarcodeInfos.Add(barcode)
        obj.SN = "505"

        result = AssignBarcodeInfoFeedback(obj)

        self.assertEqual(len(result.barcode_info), 1)
        self.assertEqual(result.barcode_info[0].barcode, "ABC123")
        self.assertEqual(result.barcode_info[0].barcode_result.value, ArbinDataModel.EBarcodeResult.Success.value__)
        self.assertEqual(result.sn, 505)


    def test_time_sensitive_set_mv_feedback_initialization(self):
        mock_obj = ArbinDataModel.TestManagement.TimeSensitiveSetMVFDBK()
        mock_obj.SN = "1234"
        mock_obj.Timeout = 30.5

        # Create a simple fake SetMVResult object
        fake_result = type("SetMVResult", (), {})()
        fake_result.Result = 0  # assuming ECommonResult(0) is valid
        fake_result.ChannelID = 101
        fake_result.StepIndex = 5
        fake_result.SubStepIndex = 2
        fake_result.ChannelStatus = 0  # assuming EChannelStatus(0) is valid
        fake_result.SampleCurrent = 3.3
        fake_result.SampleVoltage = 4.4
        fake_result.TimestampUtc = type("Timestamp", (), {"ToString": lambda self: "2025-05-27T12:34:56Z"})()
        fake_result.MVUDValues = [1.1, 2.2, 3.3]

        # Inject the fake result into the mock object
        mock_obj.SetMetaVariableList = [fake_result]

        # Run the test
        feedback = TimeSensitiveSetMVFeedback(mock_obj)

        # Assertions
        self.assertEqual(feedback.sn, 1234)
        self.assertEqual(feedback.timeout, 30.5)
        self.assertEqual(len(feedback.set_meta_variable_list), 1)
        result = feedback.set_meta_variable_list[0]
        self.assertEqual(result.channel_id, 101)
        self.assertEqual(result.sample_current, 3.3)
        self.assertEqual(result.sample_voltage, 4.4)
        self.assertEqual(result.timestamp_utc, "2025-05-27T12:34:56Z")
        self.assertEqual(result.mvud_values, [1.1, 2.2, 3.3])


    def test_time_sensitive_set_mv_feedback_initialization(self):
        # Create a SetMVResult instance
        mv_result = ArbinDataModel.TestManagement.SetMVResult()
        mv_result.Result = ArbinDataModel.ECommonResult.Success
        mv_result.ChannelID = 7
        mv_result.StepIndex = 1
        mv_result.SubStepIndex = 2
        mv_result.ChannelStatus = ArbinDataModel.EChannelStatus.Running
        mv_result.SampleCurrent = 1.0
        mv_result.SampleVoltage = 3.0
        mv_result.TimestampUtc = DateTime.Now
        mv_result.MVUDValues = [1.0]

        # Create the main feedback object
        fdbk_obj = ArbinDataModel.TestManagement.TimeSensitiveSetMVFDBK()
        fdbk_obj.SN = "9876"
        fdbk_obj.Timeout = 30.0
        fdbk_obj.SetMetaVariableList.Add(mv_result)

        # Wrap with our Python class
        feedback = TimeSensitiveSetMVFeedback(fdbk_obj)

        # Assertions
        self.assertEqual(feedback.sn, 9876)
        self.assertEqual(feedback.timeout, 30.0)
        self.assertEqual(len(feedback.set_meta_variable_list), 1)

        result = feedback.set_meta_variable_list[0]
        self.assertEqual(result.channel_id, 7)
        self.assertEqual(result.step_index, 1)
        self.assertEqual(result.sub_step_index, 2)
        self.assertEqual(result.sample_current, 1.0)
        self.assertEqual(result.sample_voltage, 3.0)
        self.assertIsInstance(result.timestamp_utc, str)
        self.assertEqual(result.mvud_values, [1.0])


if __name__ == "__main__":
    unittest.main()
