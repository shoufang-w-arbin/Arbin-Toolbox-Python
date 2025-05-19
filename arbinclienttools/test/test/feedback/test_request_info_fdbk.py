import unittest
from unittest.mock import MagicMock
from arbinclienttools.src.feedback.request_info import (
    GetStartDataFeedback,
    GetResumeDataFeedback,
    GetMonitorDataFeedback,
    GetBarcodeInfoFeedback,
    SubscribeMonitorDataFeedback,
    SubscribeChannelDataFeedback,
    SubscribeTestInfoDataFeedback,
    SubscribeEventDataFeedback,
    SubscribeDiagnosticEventDataFeedback,
    SubscribeSPTTEQCellDataFeedback,
)
from arbinclienttools.src.enumeration import EGetMonitorDataResult

class TestRequestInformationFeedback(unittest.TestCase):

    def test_get_start_data_feedback_initialization(self):
        # Create a mock object for ArbinDataModel.RequestInformation.GetStartDataFDBK
        mock_obj = MagicMock()
        mock_obj.StartDatas = [MagicMock()]  # Mocked ResumeDataInfo objects
        mock_obj.SN = 123

        # Initialize the class with the mock object
        feedback = GetStartDataFeedback(mock_obj)

        # Validate that the data is correctly parsed
        self.assertEqual(len(feedback.start_data), 1)
        self.assertEqual(feedback.sn, 123)

    def test_get_resume_data_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.ResumeDatalInfos = [MagicMock()]  # Mocked ResumeDataInfo objects
        mock_obj.SN = 456

        feedback = GetResumeDataFeedback(mock_obj)

        self.assertEqual(len(feedback.resume_data_info), 1)
        self.assertEqual(feedback.sn, 456)

    def test_get_monitor_data_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.MonitorDatas = [MagicMock()]  # Mocked ChannelMonitorData objects
        mock_obj.Result = "Success"
        mock_obj.GetMonitorDataResult = 1
        mock_obj.SN = 789

        feedback = GetMonitorDataFeedback(mock_obj)

        self.assertEqual(len(feedback.channel_monitor_data), 1)
        self.assertEqual(feedback.result, "Success")
        self.assertEqual(feedback.get_monitor_data_result, EGetMonitorDataResult(1))
        self.assertEqual(feedback.sn, 789)

    def test_get_barcode_info_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.BarcodeInfos = [MagicMock()]  # Mocked BarcodeInfo objects
        mock_obj.SN = 1011

        feedback = GetBarcodeInfoFeedback(mock_obj)

        self.assertEqual(len(feedback.barcode_info), 1)
        self.assertEqual(feedback.sn, 1011)

    def test_subscribe_monitor_data_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.ID = "ID123"
        mock_obj.TaskID = 200
        mock_obj.ChannelMonitorDatas = [MagicMock()]  # Mocked ChannelMonitorData objects

        feedback = SubscribeMonitorDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.channel_monitor_data), 1)

    def test_subscribe_channel_data_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.ID = "ID123"
        mock_obj.TaskID = 200
        mock_obj.ChannelDatas = [MagicMock()]  # Mocked ChannelData objects

        feedback = SubscribeChannelDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.channel_data), 1)

    def test_subscribe_test_info_data_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.ID = "ID123"
        mock_obj.TaskID = 200
        mock_obj.ChannelTestInfos = [MagicMock()]  # Mocked TestInfoData objects

        feedback = SubscribeTestInfoDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.channel_test_info), 1)

    def test_subscribe_event_data_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.ID = "ID123"
        mock_obj.TaskID = 200
        mock_obj.ChannelEvents = [MagicMock()]  # Mocked ChannelEvents objects

        feedback = SubscribeEventDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.channel_event), 1)

    def test_subscribe_diagnostic_event_data_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.ID = "ID123"
        mock_obj.TaskID = 200
        mock_obj.ChannelDiagnosticEvents = [MagicMock()]  # Mocked ChannelDiagnosticEventData objects

        feedback = SubscribeDiagnosticEventDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.channel_diagnostic_event), 1)

    def test_subscribe_sptt_eq_cell_data_feedback_initialization(self):
        mock_obj = MagicMock()
        mock_obj.ID = "ID123"
        mock_obj.TaskID = 200
        mock_obj.EQDatas = [MagicMock()]  # Mocked SPTTLogData objects
        mock_obj.CellDatas = [MagicMock()]  # Mocked SPTTLogData objects

        feedback = SubscribeSPTTEQCellDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.eq_data), 1)
        self.assertEqual(len(feedback.cell_dasta), 1)


if __name__ == "__main__":
    unittest.main()
