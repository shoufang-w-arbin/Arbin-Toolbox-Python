import unittest
from System import Int32, String, Double
import System.Collections.Generic as Generic
from System.Collections.Generic import List as CsList
from unittest.mock import MagicMock
import Arbin.Library.DataModel as ArbinDataModel # type: ignore
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
        mock_obj = ArbinDataModel.RequestInformation.GetStartDataFDBK()
        mock_obj.SN = "9876"

        resume_info = ArbinDataModel.RequestInformation.ResumeDataInfo()
        resume_info.Createor = "Admin"
        resume_info.Comment = "Start of test"
        resume_info.StartTime = "2025-05-30 08:00:00"
        resume_info.StepLabels.Add("Init")
        resume_info.StepLabels.Add("Main")
        resume_info.Result = "Started"
        resume_info.GetDataResult = ArbinDataModel.EGetDataResult.Success

        mock_obj.StartDatas.Add(resume_info)

        feedback = GetStartDataFeedback(mock_obj)

        self.assertEqual(feedback.sn, 9876)
        self.assertEqual(len(feedback.start_data), 1)

        data = feedback.start_data[0]
        self.assertEqual(data.creator, "Admin")
        self.assertEqual(data.comment, "Start of test")
        self.assertEqual(data.start_time, "2025-05-30 08:00:00")
        self.assertEqual(data.step_labels, ["Init", "Main"])
        self.assertEqual(data.step_count, 2)
        self.assertEqual(data.result, "Started")
        self.assertEqual(data.get_data_result.value, ArbinDataModel.EGetDataResult.Success.value__)


    def test_get_resume_data_feedback_initialization(self):
        # Create the .NET feedback object
        mock_obj = ArbinDataModel.RequestInformation.GetResumeDataFDBK()
        mock_obj.SN = "4321"

        resume_info = ArbinDataModel.RequestInformation.ResumeDataInfo()
        resume_info.Createor = "Tester"
        resume_info.Comment = "Resume from failure"
        resume_info.StartTime = "2025-05-30 10:00:00"
        resume_info.StepLabels.Add("Charge")
        resume_info.StepLabels.Add("Discharge")
        resume_info.Result = "Success"
        resume_info.GetDataResult = ArbinDataModel.EGetDataResult.Success

        mock_obj.ResumeDatalInfos.Add(resume_info)

        feedback = GetResumeDataFeedback(mock_obj)

        self.assertEqual(feedback.sn, 4321)
        self.assertEqual(len(feedback.resume_data_info), 1)

        data = feedback.resume_data_info[0]
        self.assertEqual(data.creator, "Tester")
        self.assertEqual(data.comment, "Resume from failure")
        self.assertEqual(data.start_time, "2025-05-30 10:00:00")
        self.assertEqual(data.result, "Success")
        self.assertEqual(data.get_data_result.value, ArbinDataModel.EGetDataResult.Success.value__)


    def test_get_monitor_data_feedback_initialization(self):
        mock_obj = ArbinDataModel.RequestInformation.GetMonitorDataFDBK()
        mock_obj.MonitorDatas = [MagicMock()] 
        mock_obj.Result = "Success"
        mock_obj.GetMonitorDataResult = ArbinDataModel.EGetMonitorDataResult.Success
        mock_obj.SN = "789"

        feedback = GetMonitorDataFeedback(mock_obj)

        self.assertEqual(len(feedback.channel_monitor_data), 1)
        self.assertEqual(feedback.result, "Success")
        self.assertEqual(feedback.get_monitor_data_result, EGetMonitorDataResult(0))
        self.assertEqual(feedback.sn, 789)

    def test_get_barcode_info_feedback_initialization(self):
        mock_obj = ArbinDataModel.RequestInformation.GetBarcodeInfoFDBK()
        mock_obj.SN = "1234"

        barcode_info = ArbinDataModel.Common.BarcodeInfo()
        barcode_info.BarcodeType = ArbinDataModel.EBarcodeType.Cell       
        barcode_info.GlobalID = 0
        barcode_info.Barcode = "ABC123"
        barcode_info.Info = "Sample Info"
        barcode_info.Result = "Success"
        barcode_info.BarcodeResult = ArbinDataModel.EBarcodeResult.Success

        mock_obj.BarcodeInfos.Add(barcode_info)

        feedback = GetBarcodeInfoFeedback(mock_obj)

        self.assertEqual(feedback.sn, 1234)
        self.assertEqual(len(feedback.barcode_info), 1)

        barcode = feedback.barcode_info[0]
        self.assertEqual(barcode.barcode_type.value, ArbinDataModel.EBarcodeType.Cell.value__)
        self.assertEqual(barcode.global_id, 0)
        self.assertEqual(barcode.barcode, "ABC123")
        self.assertEqual(barcode.info, "Sample Info")
        self.assertEqual(barcode.result, "Success")
        self.assertEqual(barcode.barcode_result.value, ArbinDataModel.EBarcodeResult.Success.value__)

    def test_subscribe_monitor_data_feedback_initialization(self):
        channel_monitor_data = ArbinDataModel.ChannelMonitorData()

        mock_obj = ArbinDataModel.RequestInformation.SubscribeMonitorDataFDBK()
        mock_obj.ID = "ID123"
        mock_obj.TaskID = 200
        mock_obj.ChannelMonitorDatas.Add(channel_monitor_data)

        feedback = SubscribeMonitorDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.channel_monitor_data), 1)

    def test_subscribe_channel_data_feedback_initialization(self):
        mock_obj = ArbinDataModel.RequestInformation.SubscribeChannelDataFDBK()
        mock_obj.ID = "ID789"
        mock_obj.TaskID = 456

        channel_data = ArbinDataModel.ChannelData()
        channel_data.SN = "SN123"
        channel_data.ChannelID = 5
        channel_data.Barcode = "BC456"
        channel_data.TestName = "Test"
        channel_data.TestID = 1001
        channel_data.DateTime = 1717078900
        channel_data.DataPoint = 42
        channel_data.Status = "Running"
        channel_data.TestTime = 12.5
        channel_data.StepTime = 3.2
        channel_data.StepID = 1
        channel_data.SubStepID = 0
        channel_data.CycleID = 7
        channel_data.Voltage = 3.7
        channel_data.Current = 1.2

        mock_obj.ChannelDatas.Add(channel_data)

        feedback = SubscribeChannelDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID789")
        self.assertEqual(feedback.task_id, 456)
        self.assertEqual(len(feedback.channel_data), 1)

        cd = feedback.channel_data[0]
        self.assertEqual(cd.sn, "SN123")
        self.assertEqual(cd.channel_id, 5)
        self.assertEqual(cd.barcode, "BC456")
        self.assertEqual(cd.test_name, "Test")
        self.assertEqual(cd.test_id, 1001)
        self.assertEqual(cd.date_time, 1717078900)
        self.assertEqual(cd.data_point, 42)
        self.assertEqual(cd.status, "Running")
        self.assertAlmostEqual(cd.test_time, 12.5)
        self.assertAlmostEqual(cd.step_time, 3.2)
        self.assertEqual(cd.step_id, 1)
        self.assertEqual(cd.sub_step_id, 0)
        self.assertEqual(cd.cycle_id, 7)
        self.assertAlmostEqual(cd.voltage, 3.7)
        self.assertAlmostEqual(cd.current, 1.2)


    def test_subscribe_test_info_data_feedback_initialization(self):
        test_info = ArbinDataModel.TestInfoData()
        test_info.SN = "SN001"
        test_info.ChannelID = 1
        test_info.Barcode = "BC001"
        test_info.TestName = "TestName"
        test_info.TestID = 123
        test_info.StartFileTime = 123456789
        test_info.StartDateTime = "2025-05-30T10:00:00"
        test_info.Creator = "Tester"
        test_info.Comment = "Test comment"
        test_info.ScheduleName = "ScheduleX"
        test_info.TestObjectName = "ObjectX"

        feedback_obj = ArbinDataModel.RequestInformation.SubscribeTestInfoDataFDBK()
        feedback_obj.ID = "ID123"
        feedback_obj.TaskID = 200
        feedback_obj.ChannelTestInfos.Add(test_info)

        feedback = SubscribeTestInfoDataFeedback(feedback_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.channel_test_info), 1)
        self.assertEqual(feedback.channel_test_info[0].sn, "SN001")


    def test_subscribe_event_data_feedback_initialization(self):
        channel_events = ArbinDataModel.ChannelEventData()

        mock_obj = ArbinDataModel.RequestInformation.SubscribeEventDataFDBK()
        mock_obj.ID = "ID123"
        mock_obj.TaskID = 200
        mock_obj.ChannelEvents.Add(channel_events)

        feedback = SubscribeEventDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.channel_event), 1)

    def test_subscribe_diagnostic_event_data_feedback_initialization(self):
        channel_diag_data = ArbinDataModel.ChannelDiagnosticEventData()
        channel_diag_data.channel_id = 1
        channel_diag_data.sn = "1234"
        channel_diag_data.diagnostic_envet_msg = "msg"

        mock_obj = ArbinDataModel.RequestInformation.SubscribeDiagnosticEventDataFDBK()
        mock_obj.ID = "ID123"
        mock_obj.TaskID = 200
        mock_obj.ChannelDiagnosticEvents.Add(channel_diag_data)

        feedback = SubscribeDiagnosticEventDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.channel_diagnostic_event), 1)

    def test_subscribe_sptt_eq_cell_data_feedback_initialization(self):
        mock_obj = ArbinDataModel.RequestInformation.SubscribeSPTTEQCellDataFDBK()
        mock_obj.ID = "ID123"
        mock_obj.TaskID = 200

        eq_data = ArbinDataModel.SPTTLogData()
        eq_data.Barcode = "12345"
        eq_data.TestID = 1
        eq_data.ChannelID = 10
        eq_data.EQVirtualID = 100
        eq_data.EQGlobalID = 101
        eq_data.CellVirtualID = 200
        eq_data.CellGlobalID = 201
        eq_data.TrayID = 5
        eq_data.Status = "Running"
        eq_data.PositionX = 1
        eq_data.PositionY = 2
        eq_data.DateTime = 1234567890
        eq_data.DataPoint = 123
        eq_data.TestTime = 12.5
        eq_data.StepTime = 5.0
        eq_data.CycleID = 2
        eq_data.StepID = 1
        eq_data.SubStepID = 0
        eq_data.Current = 0.5
        eq_data.Voltage = 3.7
        eq_data.Temperature = 25.0
        eq_data.ChargeCapacity = 1.2
        eq_data.DischargeCapacity = 1.1
        eq_data.ChargeEnergy = 4.5
        eq_data.DischargeEnergy = 4.3
        eq_data.DataFlags = 0

        mock_obj.EQDatas.Add(eq_data)
        mock_obj.CellDatas.Add(eq_data)

        feedback = SubscribeSPTTEQCellDataFeedback(mock_obj)

        self.assertEqual(feedback.id_, "ID123")
        self.assertEqual(feedback.task_id, 200)
        self.assertEqual(len(feedback.eq_data), 1)
        self.assertEqual(len(feedback.cell_dasta), 1)
        self.assertEqual(feedback.eq_data[0].barcode, "12345")
          


if __name__ == "__main__":
    unittest.main()
