import unittest
from unittest.mock import MagicMock
from arbinclienttools.src.enumeration import EEngagementResult
from arbinclienttools.src.feedback.formation_management import (
    GetEngagementStatusFeedback,
    EngageTrayFeedback
)

class TestFormationManagementFeedback(unittest.TestCase):

    def test_sptt_engagement_meta_value_initialization(self):
        # Create a mock object for SPTTEngagementMetaValue
        mock_meta_value = MagicMock()
        mock_meta_value.Value = 1.23
        mock_meta_value.AliasName = 'TestAlias'
        mock_meta_value.Result = 'Success'

        meta_value = GetEngagementStatusFeedback.SPTTEngagementMetaValue(mock_meta_value)

        self.assertEqual(meta_value.value, 1.23)
        self.assertEqual(meta_value.alias_name, 'TestAlias')
        self.assertEqual(meta_value.result, 'Success')

    def test_sptt_engagement_status_initialization(self):
        # Create a mock object for SPTTEngagementStatus
        mock_status = MagicMock()
        mock_status.GlobalID = 101
        mock_status.IsEngagementDown = True
        mock_status.IsEngagementUp = False
        mock_status.IsTrayInserted = True
        mock_status.Result = 'Success'
        mock_status.EngagementResult = 0  # EEngagementResult.Success
        mock_status.EngagementMetaValues = [MagicMock(Value=1.0, AliasName='Meta1', Result='OK')]

        status = GetEngagementStatusFeedback.SPTTEngagementStatus(mock_status)

        self.assertEqual(status.global_id, 101)
        self.assertTrue(status.is_engagement_down)
        self.assertFalse(status.is_engagement_up)
        self.assertTrue(status.is_tray_inserted)
        self.assertEqual(status.result, 'Success')
        self.assertEqual(status.engagement_result, EEngagementResult.Success)
        self.assertEqual(len(status.engagement_meta_values), 1)
        self.assertEqual(status.engagement_meta_values[0].value, 1.0)
        self.assertEqual(status.engagement_meta_values[0].alias_name, 'Meta1')
        self.assertEqual(status.engagement_meta_values[0].result, 'OK')

    def test_get_engagement_status_feedback_initialization(self):
        # Create a mock object for GetEngagementStatusFeedback
        mock_feedback = MagicMock()
        mock_feedback.SN = '12345'
        mock_feedback.EngagementStatus = MagicMock()

        feedback = GetEngagementStatusFeedback(mock_feedback)

        self.assertEqual(feedback.sn, '12345')

    def test_invalid_get_engagement_status_feedback_type(self):
        # Test for invalid type of feedback object
        with self.assertRaises(ValueError):
            invalid_mock = MagicMock()
            invalid_mock.SN = 'InvalidSN'
            GetEngagementStatusFeedback(invalid_mock)

    def test_sptt_engage_tray_initialization(self):
        # Create a mock object for SPTTEngageTray
        mock_tray = MagicMock()
        mock_tray.GlobalID = 202
        mock_tray.Engage = True
        mock_tray.Result = 'Engaged'
        mock_tray.EngagementResult = 1  # EEngagementResult.Failed

        engage_tray = EngageTrayFeedback.SPTTEngageTray(mock_tray)

        self.assertEqual(engage_tray.global_id, 202)
        self.assertTrue(engage_tray.engage)
        self.assertEqual(engage_tray.result, 'Engaged')
        self.assertEqual(engage_tray.engagement_result, EEngagementResult.Failed)

    def test_engage_tray_feedback_initialization(self):
        # Create a mock object for EngageTrayFeedback
        mock_feedback = MagicMock()
        mock_feedback.SN = '67890'
        mock_feedback.EngageTrays = [MagicMock(GlobalID=202, Engage=True, Result='Engaged', EngagementResult=1)]

        feedback = EngageTrayFeedback(mock_feedback)

        self.assertEqual(feedback.sn, '67890')
        self.assertEqual(len(feedback.engage_trays), 1)
        self.assertEqual(feedback.engage_trays[0].global_id, 202)
        self.assertTrue(feedback.engage_trays[0].engage)
        self.assertEqual(feedback.engage_trays[0].result, 'Engaged')
        self.assertEqual(feedback.engage_trays[0].engagement_result, EEngagementResult.Failed)

    def test_invalid_engage_tray_feedback_type(self):
        # Test for invalid type of feedback object
        with self.assertRaises(ValueError):
            invalid_mock = MagicMock()
            invalid_mock.SN = 'InvalidSN'
            EngageTrayFeedback(invalid_mock)

if __name__ == "__main__":
    unittest.main()
