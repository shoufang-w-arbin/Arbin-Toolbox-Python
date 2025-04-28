import unittest
import os
from unittest.mock import MagicMock
from arbinctitools.src.feedback.channel_control import (
    StartChannelFeedback,
    StopChannelFeedback,
    ResumeChannelFeedback,
    JumpChannelFeedback,
    ContinueChannelFeedback,
    StartChannelAdvancedFeedback,
)

UNITTEST_VIEW_DICT = os.getenv("UNITTEST_VIEW_DICT", False)

class TestChannelControlFeedback(unittest.TestCase):

    def test_StartChannelFeedback_instantiation(self):
        cs_instance = MagicMock()
        cs_instance.Result = 0x17  # CTI_START_POWER_PROTECTED
        
        feedback_instance = StartChannelFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, StartChannelFeedback.EStartToken.CTI_START_POWER_PROTECTED)

        if UNITTEST_VIEW_DICT:
            print("StartChannelFeedback:", feedback_instance.to_dict())

    def test_StopChannelFeedback_instantiation(self):
        cs_instance = MagicMock()
        cs_instance.Result = 0x13  # STOP_CHANNEL_NOT_CONNECT
        
        feedback_instance = StopChannelFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, StopChannelFeedback.EStopToken.STOP_CHANNEL_NOT_CONNECT)

        if UNITTEST_VIEW_DICT:
            print("StopChannelFeedback:", feedback_instance.to_dict())

    def test_ResumeChannelFeedback_instantiation(self):
        cs_instance = MagicMock()
        cs_instance.Result = 0x12  # RESUME_CHANNEL_RUNNING
        
        feedback_instance = ResumeChannelFeedback(cs_instance)
        
        self.assertEqual(feedback_instance.result, ResumeChannelFeedback.EResumeToken.RESUME_CHANNEL_RUNNING)
        
        if UNITTEST_VIEW_DICT:
            print("ResumeChannelFeedback:", feedback_instance.to_dict())

    def test_JumpChannelFeedback_instantiation(self):
        cs_instance = MagicMock()
        cs_instance.Result = 0x14  # CTI_JUMP_SCHEDULE_VALID
        cs_instance.errorChannel = 5
        
        feedback_instance = JumpChannelFeedback(cs_instance)
        
        self.assertEqual(feedback_instance.result, JumpChannelFeedback.EJumpToken.CTI_JUMP_SCHEDULE_VALID)
        self.assertEqual(feedback_instance.error_channel, 5)
        
        if UNITTEST_VIEW_DICT:
            print("JumpChannelFeedback:", feedback_instance.to_dict())

    def test_ContinueChannelFeedback_instantiation(self):
        cs_instance = MagicMock()
        cs_instance.Result = 0x14  # CTI_CONTINUE_CHANNEL_CALIBRATING
        
        feedback_instance = ContinueChannelFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, ContinueChannelFeedback.EContinueToken.CTI_CONTINUE_CHANNEL_CALIBRATING)
        
        if UNITTEST_VIEW_DICT:
            print("ContinueChannelFeedback:", feedback_instance.to_dict())

    def test_StartChannelAdvancedFeedback_instantiation(self):
        result_instance = MagicMock()
        result_instance.ChannelIndex = 1
        result_instance.StartResult = 0x0  # CTI_START_SUCCESS
        result_instance.Message = "Success"

        success_list_instance = [1]

        failed_results_instance = [result_instance]

        cs_instance = MagicMock()
        cs_instance.TaskID = 123
        cs_instance.SuccessfulChannelIDs = success_list_instance
        cs_instance.FailedResults = failed_results_instance
        feedback_instance = StartChannelAdvancedFeedback(cs_instance)

        self.assertEqual(feedback_instance.task_id, 123)
        self.assertEqual(feedback_instance.successful_channel_id, [1])
        self.assertEqual(len(feedback_instance.failed_result), 1)
        self.assertEqual(feedback_instance.failed_result[0].channel_index, 1)
        self.assertEqual(feedback_instance.failed_result[0].result, StartChannelFeedback.EStartToken.CTI_START_SUCCESS)
        self.assertEqual(feedback_instance.failed_result[0].message, "Success")
        self.assertFalse(feedback_instance.is_success)

        if UNITTEST_VIEW_DICT:
            print("StartChannelAdvancedFeedback:", feedback_instance.to_dict())

if __name__ == "__main__":
    unittest.main()
