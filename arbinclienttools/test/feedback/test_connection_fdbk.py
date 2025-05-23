import unittest
from unittest.mock import MagicMock
from arbinclienttools.src.feedback.connection import LoginFeedback
from arbinclienttools.src.enumeration import ELoginResult

class TestLoginFeedback(unittest.TestCase):

    def test_user_info_initialization(self):
        # Create a mock object for UserInfo
        mock_user_info = MagicMock()
        mock_user_info.UserRole = 'Admin'
        mock_user_info.UserPermission = 'Full'
        mock_user_info.UserName = 'test_user'
        mock_user_info.UserImageBase64 = 'image_base64_string'
        mock_user_info.Comments = 'Test user'
        mock_user_info.EmailAddress = 'test@domain.com'
        mock_user_info.TelephoneNumber = '1234567890'
        mock_user_info.ChannelNumber = {'channel_1': 1, 'channel_2': 2}

        user_info = LoginFeedback.UserInfo(mock_user_info)

        self.assertEqual(user_info.user_role, 'Admin')
        self.assertEqual(user_info.user_permission, 'Full')
        self.assertEqual(user_info.user_name, 'test_user')
        self.assertEqual(user_info.user_image_base64, 'image_base64_string')
        self.assertEqual(user_info.comments, 'Test user')
        self.assertEqual(user_info.email_address, 'test@domain.com')
        self.assertEqual(user_info.telephone_number, '1234567890')
        self.assertEqual(user_info.channel_number, {'channel_1': 1, 'channel_2': 2})

    def test_sys_cfg_global_initialization(self):
        # Create a mock object for SysCfgGlobal
        mock_sys_cfg_global = MagicMock()
        mock_sys_cfg_global.Customer = 'CustomerA'
        mock_sys_cfg_global.Company = 'CompanyX'
        mock_sys_cfg_global.CustomerNote = 'Test customer note'
        mock_sys_cfg_global.DataLogSpeed = 100
        mock_sys_cfg_global.UPSEnabled = True
        mock_sys_cfg_global.UPSUsePositiveSignal = False
        mock_sys_cfg_global.UPSShutdownComputer = True
        mock_sys_cfg_global.UpsAutoResumeTest = False
        mock_sys_cfg_global.UpsThresholdMin = 10
        mock_sys_cfg_global.CurrentRangeCount = 5
        mock_sys_cfg_global.VoltageRangeCount = 10

        sys_cfg_global = LoginFeedback.SystemConfigFile.SysCfgGlobal(mock_sys_cfg_global)

        self.assertEqual(sys_cfg_global.customer, 'CustomerA')
        self.assertEqual(sys_cfg_global.company, 'CompanyX')
        self.assertEqual(sys_cfg_global.customer_note, 'Test customer note')
        self.assertEqual(sys_cfg_global.data_log_speed, 100)
        self.assertTrue(sys_cfg_global.ups_enabled)
        self.assertFalse(sys_cfg_global.ups_use_positive_signal)
        self.assertTrue(sys_cfg_global.ups_shutdown_computer)
        self.assertFalse(sys_cfg_global.ups_auto_resume_test)
        self.assertEqual(sys_cfg_global.ups_threshold_min, 10)
        self.assertEqual(sys_cfg_global.current_range_count, 5)
        self.assertEqual(sys_cfg_global.voltage_range_count, 10)

    def test_login_feedback_initialization(self):
        # Create a mock object for LoginFeedback
        mock_login_fdbk = MagicMock()
        mock_login_fdbk.LoginResult = 0  # ELoginResult.Success
        mock_login_fdbk.Result = 'Login successful'
        
        # Create mock for ServerInfo and UserInfo
        mock_server_info = MagicMock()
        mock_server_info.UserInfo = MagicMock()
        mock_server_info.ServerVersionNumber = '1.0.0'
        mock_server_info.SystemConfig = None
        
        mock_login_fdbk.ServerInformation = mock_server_info
        
        login_feedback = LoginFeedback(mock_login_fdbk)
        
        self.assertEqual(login_feedback.login_reusult, ELoginResult.Success)
        self.assertEqual(login_feedback.result, 'Login successful')
        self.assertIsNotNone(login_feedback.server_information)
        self.assertEqual(login_feedback.server_information.server_version_number, '1.0.0')
        self.assertIsNone(login_feedback.server_information.system_config)

    def test_invalid_login_feedback_type(self):
        # Test case where the type of obj passed to LoginFeedback is not as expected
        with self.assertRaises(ValueError):
            invalid_mock = MagicMock()
            invalid_mock.LoginResult = 'Invalid Type'
            LoginFeedback(invalid_mock)


if __name__ == "__main__":
    unittest.main()
