import System
from System.Collections.Generic import List as CsList
import unittest
from arbinclienttools.src.argument.formation_management import (
    SPTTEngageTray,
    GetEngagementStatusArgs,
    EngageTrayArgs
)
from arbinclienttools.src.enumeration import EEngagementResult

class TestFormationManagementArgs(unittest.TestCase):

    def test_sptt_engage_tray_to_cs(self):
        tray = SPTTEngageTray(
            global_id=1001,
            engage=False,
            result="Completed",
            engagement_result=EEngagementResult.Error
        )
        cs = tray.to_cs()

        self.assertEqual(cs.GlobalID, 1001)
        self.assertFalse(cs.Engage)
        self.assertEqual(cs.Result, "Completed")
        self.assertEqual(cs.EngagementResult.value, EEngagementResult.Error)

    def test_get_engagement_status_args_to_cs(self):
        args = GetEngagementStatusArgs(
            sn="SN12345",
            engagement_id=[1, 2, 3]
        )
        cs = args.to_cs()

        self.assertEqual(cs.SN, "SN12345")
        self.assertIsInstance(cs.EngagementIDs, CsList[System.Int32])

    def test_engage_tray_args_to_cs_success(self):
        tray1 = SPTTEngageTray(global_id=1001)
        tray2 = SPTTEngageTray(global_id=1002)

        args = EngageTrayArgs(
            sn="SN54321",
            engage_tray=[tray1, tray2]
        )
        cs = args.to_cs()

        self.assertEqual(cs.SN, "SN54321")
        self.assertEqual(len(cs.EngageTrays), 2)
        self.assertEqual(cs.EngageTrays[0].GlobalID, 1001)
        self.assertEqual(cs.EngageTrays[1].GlobalID, 1002)

    def test_engage_tray_args_invalid_type_raises(self):
        args = EngageTrayArgs(
            sn="InvalidTest",
            engage_tray=["not_a_tray"]
        )
        with self.assertRaises(TypeError):
            args.to_cs()

if __name__ == '__main__':
    unittest.main()
