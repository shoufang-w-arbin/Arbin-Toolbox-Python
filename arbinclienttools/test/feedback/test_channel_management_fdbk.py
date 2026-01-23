import unittest
import os
import Arbin.Library.DataModel as ArbinDataModel # type: ignore
from arbinclienttools.src.feedback.channel_management import (
    StartChannelFeedback,
    StopChannelFeedback,
    ResumeChannelFeedback,
    JumpStepFeedback,
    ContinueChannelFeedback,
)

UNITTEST_VIEW_DICT = os.getenv("UNITTEST_VIEW_DICT", False)

class TestChannelControlFeedback(unittest.TestCase):

    def test_start_channel_feedback_success(self):
        fdbk = ArbinDataModel.ChannelManagement.StartChannelFDBK()
        fdbk.SuccessfulChannelIDs.Add(1)
        fdbk.SN = "123456"

        # Create and add a failed result
        fail_result = ArbinDataModel.ChannelManagement.StartChannelResult()
        fail_result.ChannelID = 102
        fail_result.Result = "Error"
        fail_result.StartResult = ArbinDataModel.EStartChannelResult.Success
        fail_result.Message = "Failed to start channel"
        fdbk.FailedResults.Add(fail_result)

        # Act
        feedback = StartChannelFeedback(fdbk)

        # Assert
        self.assertEqual(feedback.successful_channel_id, [1])
        self.assertEqual(feedback.sn, 123456)
        self.assertEqual(len(feedback.failed_result), 1)
        self.assertEqual(feedback.failed_result[0].channel_id, 102)
        self.assertEqual(feedback.failed_result[0].result, "Error")
        self.assertEqual(feedback.failed_result[0].start_result.value, ArbinDataModel.EStartChannelResult.Success.value__)
        self.assertEqual(feedback.failed_result[0].message, "Failed to start channel")

    def test_StopChannelFeedback_instantiation(self):
        cs_instance = ArbinDataModel.ChannelManagement.StopChannelFDBK()
        cs_instance.Result = "ChannelNotConnectError"
        cs_instance.StopResult = ArbinDataModel.EStopChannelResult.ChannelNotConnectError
        cs_instance.SN = "123456"
        
        feedback_instance = StopChannelFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, "ChannelNotConnectError")
        self.assertEqual(feedback_instance.stop_channel_result.value, ArbinDataModel.EStopChannelResult.ChannelNotConnectError.value__)
        self.assertEqual(feedback_instance.sn, 123456)

    def test_ResumeChannelFeedback_instantiation(self):
        cs_instance = ArbinDataModel.ChannelManagement.ResumeChannelFDBK()
        cs_instance.SN = "12345"

        fail_result = ArbinDataModel.ChannelManagement.ResumeChannelResult()
        fail_result.ResumeResult = ArbinDataModel.EResumeChannelResult.Success
        cs_instance.FailedResults.Add(fail_result)
        
        feedback_instance = ResumeChannelFeedback(cs_instance)
        
        self.assertEqual(feedback_instance.failed_result[0].resume_result.value, ArbinDataModel.EResumeChannelResult.Success.value__)
        self.assertEqual(feedback_instance.sn, 12345)
        

    def test_JumpChannelFeedback_instantiation(self):
        cs_instance = ArbinDataModel.ChannelManagement.JumpStepFDBK()
        cs_instance.ChannelID = 1
        cs_instance.Result = "Success"
        cs_instance.JumpStepResult = ArbinDataModel.EJumpStepResult.Success
        cs_instance.SN = "12345"

        
        feedback_instance = JumpStepFeedback(cs_instance)
        
        self.assertEqual(feedback_instance.jump_step_result.value, ArbinDataModel.EJumpStepResult.Success.value__)
        self.assertEqual(feedback_instance.result, "Success")
        self.assertEqual(feedback_instance.sn, 12345)
        self.assertEqual(feedback_instance.channel_id, 1)
        
        if UNITTEST_VIEW_DICT:
            print("JumpChannelFeedback:", feedback_instance.to_dict())

    def test_ContinueChannelFeedback_instantiation(self):
        cs_instance = ArbinDataModel.ChannelManagement.ContinueChannelFDBK()
        cs_instance.SuccessfulChannelIDs.Add(10)
        cs_instance.SN = "7890"

        # Populate a failed result
        fail_result = ArbinDataModel.ChannelManagement.ContinueChannelResult()
        fail_result.ChannelID = 0
        fail_result.Result = "SomeError"
        fail_result.ContinueResult = ArbinDataModel.EContinueChannelResult.Success
        fail_result.Message = "Channel resumed with warning"
        cs_instance.FailedResults.Add(fail_result)

        feedback_instance = ContinueChannelFeedback(cs_instance)

        self.assertEqual(feedback_instance.successful_channel_id, [10])
        self.assertEqual(feedback_instance.sn, 7890)
        self.assertEqual(len(feedback_instance.failed_result), 1)
        self.assertEqual(feedback_instance.failed_result[0].channel_id, 0)
        self.assertEqual(feedback_instance.failed_result[0].result, "SomeError")
        self.assertEqual(feedback_instance.failed_result[0].continue_result.value, ArbinDataModel.EContinueChannelResult.Success.value__)
        self.assertEqual(feedback_instance.failed_result[0].message, "Channel resumed with warning")

if __name__ == "__main__":
    unittest.main()
