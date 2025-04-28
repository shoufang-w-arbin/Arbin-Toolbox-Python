import unittest
from unittest.mock import MagicMock
from arbinclienttools.src.feedback.test_management_feedback import (
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
    EAssignFileResult,
    ECommonResult,
    EChannelStatus,
)
from arbinclienttools.src.feedback.common import AIMetaVariableInfo, BarcodeInfo


class TestTestManagementFeedback(unittest.TestCase):

    def test_upload_file_result_initialization(self):
        mock_obj = MagicMock()
        mock_obj.Result = "Success"
        mock_obj.UploadResult = 1  # EUploadFileResult
        mock_obj.IsCancelUploadFile = False
        mock_obj.ProgressRate = 75.0

        result = UploadFileResult(mock_obj)

        self.assertEqual(result.result, "Success")
        self.assertEqual(result.upload_result, EUploadFileResult(1))
        self.assertFalse(result.is_cancel_upload_file)
        self.assertEqual(result.progress_rate, 75.0)

    def test_browse_file_list_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.Result = "Success"
        mock_obj.BrowseDirectoryResult = 1  # EBrowseDirectoryResult
        mock_obj.DirFileInfoList = [MagicMock()]  # Mocked DirFileInfo
        mock_obj.SN = 1234

        feedback = BrowseFileListFeedback(mock_obj)

        self.assertEqual(feedback.result, "Success")
        self.assertEqual(feedback.browse_directory_result, EBrowseDirectoryResult(1))
        self.assertEqual(len(feedback.dir_file_info_list), 1)
        self.assertEqual(feedback.sn, 1234)

    def test_assign_file_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.SuccessfulChannelIDs = [1, 2, 3]
        mock_obj.FailedResults = [MagicMock()]  # Mocked AssignFileResult
        mock_obj.IsSuccess = True
        mock_obj.SN = 5678

        feedback = AssignFileFeedback(mock_obj)

        self.assertEqual(feedback.successful_channel_id, [1, 2, 3])
        self.assertEqual(len(feedback.failed_result), 1)
        self.assertTrue(feedback.is_success)
        self.assertEqual(feedback.sn, 5678)

    def test_update_meta_variable_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.MetaVariableInfos = [MagicMock()]  # Mocked AIMetaVariableInfo
        mock_obj.SN = 91011

        feedback = UpdateMetaVariableFeedback(mock_obj)

        self.assertEqual(len(feedback.meta_variable_info), 1)
        self.assertEqual(feedback.sn, 91011)

    def test_get_meta_variables_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.MetaVariableInfos = [MagicMock()]  # Mocked AIMetaVariableInfo
        mock_obj.SN = 1213

        feedback = GetMetaVariablesFeedback(mock_obj)

        self.assertEqual(len(feedback.meta_variable_info), 1)
        self.assertEqual(feedback.sn, 1213)

    def test_assign_barcode_info_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.BarcodeInfos = [MagicMock()]  # Mocked BarcodeInfo
        mock_obj.SN = 1415

        feedback = AssignBarcodeInfoFeedback(mock_obj)

        self.assertEqual(len(feedback.barcode_info), 1)
        self.assertEqual(feedback.sn, 1415)

    def test_time_sensitive_set_mv_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.SN = 1617
        mock_obj.Timeout = 30.5
        mock_obj.SetMetaVariableList = [MagicMock()]  # Mocked SetMVResult

        feedback = TimeSensitiveSetMVFeedback(mock_obj)

        self.assertEqual(feedback.sn, 1617)
        self.assertEqual(feedback.timeout, 30.5)
        self.assertEqual(len(feedback.set_meta_variable_list), 1)

    def test_set_mv_result_initialization(self):
        mock_obj = MagicMock()
        mock_obj.Result = 1  # ECommonResult
        mock_obj.ChannelID = 18
        mock_obj.StepIndex = 2
        mock_obj.SubStepIndex = 3
        mock_obj.ChannelStatus = 1  # EChannelStatus
        mock_obj.SampleCurrent = 5.6
        mock_obj.SampleVoltage = 7.8
        mock_obj.TimestampUtc = MagicMock(ToString=MagicMock(return_value="2025-04-28T00:00:00Z"))
        mock_obj.MVUDValues = [1.2, 3.4, 5.6]

        result = TimeSensitiveSetMVFeedback.SetMVResult(mock_obj)

        self.assertEqual(result.result, ECommonResult(1))
        self.assertEqual(result.channel_id, 18)
        self.assertEqual(result.step_index, 2)
        self.assertEqual(result.sub_step_index, 3)
        self.assertEqual(result.channel_status, EChannelStatus(1))
        self.assertEqual(result.sample_current, 5.6)
        self.assertEqual(result.sample_voltage, 7.8)
        self.assertEqual(result.timestamp_utc, "2025-04-28T00:00:00Z")
        self.assertEqual(result.mvud_values, [1.2, 3.4, 5.6])


if __name__ == "__main__":
    unittest.main()
