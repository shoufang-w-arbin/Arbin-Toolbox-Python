import os
import unittest

import ArbinCTI.Core as ArbinCTI # type: ignore

from ctitoolbox.src.feedback.system import (
    GetSerailNumberFeedback, 
    GetMITSVersionFeedback,
    LoginFeedback
)

UNITTEST_VIEW_DICT = os.getenv("UNITTEST_VIEW_DICT", False)

class TestFeedbackClasses(unittest.TestCase):

    def test_GetSerailNumberFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandGetSerialNumberFeed()
        cs_instance.SerialNum   = 12345.6789
        cs_instance.Result      = ArbinCTI.ArbinCommandGetSerialNumberFeed.ASSIGN_TOKEN.CTI_GET_SERIAL_SUCCESS

        feedback_instance = GetSerailNumberFeedback(cs_instance)

        self.assertEqual(feedback_instance.serial_number, 12345.6789)
        self.assertEqual(feedback_instance.result, GetSerailNumberFeedback.EAssignToken.CTI_GET_SERIAL_SUCCESS)

        if UNITTEST_VIEW_DICT:
            print("GetSerailNumberFeedback:", feedback_instance.to_dict())

    def test_GetMITSVersionFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandGetServerSoftwareVersionNumberFeed()
        cs_instance.ServerVersionNumber = "1.2.3.4"

        feedback_instance = GetMITSVersionFeedback(cs_instance)

        self.assertEqual(feedback_instance.version, "1.2.3.4")

        if UNITTEST_VIEW_DICT:
            print("GetMITSVersionFeedback:", feedback_instance.to_dict())

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
        