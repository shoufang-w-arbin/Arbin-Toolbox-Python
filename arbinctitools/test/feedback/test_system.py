import os
import unittest

import ArbinCTI.Core as ArbinCTI # type: ignore

from arbinctitools.src.feedback.system import (
    LoginFeedback,
    LogicConnectFeedback,
    SendMsgToCTIFeedback,
    UnknownCommandFeedback,
    StartAutomaticCalibrationFeedback,
)

UNITTEST_VIEW_DICT = os.getenv("UNITTEST_VIEW_DICT", False)

class TestFeedbackClasses(unittest.TestCase):

    def test_LoginFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandLoginFeed()
        cs_instance.Result      = ArbinCTI.ArbinCommandLoginFeed.LOGIN_RESULT.CTI_LOGIN_SUCCESS
        cs_instance.UserType    = 0
        cs_instance.SN          = "12345"
        cs_instance.Note        = "Note"
        cs_instance.NickName    = "NickName"
        cs_instance.Location    = "Location"
        cs_instance.EmergencyContactNameAndPhoneNumber = "John Doe, +123456789"
        cs_instance.OtherComments = "Other description"
        cs_instance.Email       = "example@example.com"
        cs_instance.ITAC        = 1
        cs_instance.CALL        = "+987654321"
        cs_instance.IsAllowToControl = 1
        cs_instance.ChannelNum  = 16
        cs_instance.Version     = ArbinCTI.ArbinCommandLoginFeed.CTI_VERSION.CTI_PRO7
        cs_instance.ServerInfo  = "Server Info"

        feedback_instance = LoginFeedback(cs_instance)
        self.assertEqual(feedback_instance.result, LoginFeedback.ELoginResult.CTI_LOGIN_SUCCESS)
        self.assertEqual(feedback_instance.user_type, 0)
        self.assertEqual(feedback_instance.serial_number, "12345")
        self.assertEqual(feedback_instance.note, "Note")
        self.assertEqual(feedback_instance.nickname, "NickName")
        self.assertEqual(feedback_instance.location, "Location")
        self.assertEqual(feedback_instance.emergency_contact, "John Doe, +123456789")
        self.assertEqual(feedback_instance.other_comments, "Other description")
        self.assertEqual(feedback_instance.email, "example@example.com")
        self.assertEqual(feedback_instance.itac, 1)
        self.assertEqual(feedback_instance.call, "+987654321")
        self.assertEqual(feedback_instance.is_allow_to_control, 1)
        self.assertEqual(feedback_instance.channel_count, 16)
        self.assertEqual(feedback_instance.version, LoginFeedback.ECTIVersion.CTI_PRO7)
        self.assertEqual(feedback_instance.server_info, "Server Info")

        if UNITTEST_VIEW_DICT:
            print("LoginFeedback:", feedback_instance.to_dict())

    def test_LogicConnectFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandLogicConnectFeed()
        cs_instance.dwSetKickOut = 1
        cs_instance.dwConnectResult = 0

        feedback_instance = LogicConnectFeedback(cs_instance)

        self.assertEqual(feedback_instance.dwSetKickOut, 1)
        self.assertEqual(feedback_instance.dwConnectResult, 0)

        if UNITTEST_VIEW_DICT:
            print("LogicConnectFeedback:", feedback_instance.to_dict())

    def test_StartAutomaticCalibrationFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandStartAutomaticCalibrationFeed()
        cs_instance.Result = ArbinCTI.ArbinCommandStartAutomaticCalibrationFeed.AUTOCALI_START_RESULT.CTI_AUTOCALI_START_SUCCESS

        feedback_instance = StartAutomaticCalibrationFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, StartAutomaticCalibrationFeedback.EResult.CTI_AUTOCALI_START_SUCCESS)

        if UNITTEST_VIEW_DICT:
            print("StartAutomaticCalibrationFeedback:", feedback_instance.to_dict())

    def test_SendMsgToCTIFeedBack_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandSendMsgToCTIFeed()
        cs_instance.Result = ArbinCTI.ArbinCommandSendMsgToCTIFeed.SEND_MSG_TO_CTI_RESULT.SEND_MSG_TO_CTI_SUCCESS

        feedback_instance = SendMsgToCTIFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, SendMsgToCTIFeedback.EResult.CTI_SEND_MSG_SUCCESS)

        if UNITTEST_VIEW_DICT:
            print("SendMsgToCTIFeedBack:", feedback_instance.to_dict())

    def test_UnknownCommandFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandUnknownCommandFeed()
        cs_instance.UnknownCMD = 999
        cs_instance.UnknownCMDExtend = 888

        feedback_instance = UnknownCommandFeedback(cs_instance)

        self.assertEqual(feedback_instance.unknown_commnad, 999)
        self.assertEqual(feedback_instance.unknown_commnad_extend, 888)

        if UNITTEST_VIEW_DICT:
            print("UnknownCommandFeedback:", feedback_instance.to_dict())
