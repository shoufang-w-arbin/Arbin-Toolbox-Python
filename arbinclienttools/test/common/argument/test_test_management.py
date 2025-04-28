import unittest
from arbinclienttools.src.argument.test_management_arguments import *

class TestSafetyScope(unittest.TestCase):
    def test_to_cs(self):
        instance = SafetyScope(low=1.0, high=5.0)
        cs = instance.to_cs()
        self.assertEqual(cs.Low, 1.0)
        self.assertEqual(cs.High, 5.0)

class TestAuxChannelRequirementBase(unittest.TestCase):
    def test_to_cs(self):
        instance = AuxChannelRequirementBase(enable=True, aux_count=4)
        cs = instance.to_cs()
        self.assertTrue(cs.Enable)
        self.assertEqual(cs.AuxCount, 4)

class TestAuxChannelRequirement(unittest.TestCase):
    def test_to_cs(self):
        instance = AuxChannelRequirement(enable=True, aux_count=2, safety_scope=SafetyScope(low=0.5, high=1.5))
        cs = instance.to_cs()
        self.assertTrue(cs.Enable)
        self.assertEqual(cs.AuxCount, 2)
        self.assertEqual(cs.SafetyScope.Low, 0.5)
        self.assertEqual(cs.SafetyScope.High, 1.5)

class TestAuxSafetyRequirement(unittest.TestCase):
    def test_to_cs(self):
        instance = AuxSafetyRequirement(
            enable=True,
            aux_count=3,
            temperature_safety_scope=SafetyScope(10, 40),
            current_safety_scope=SafetyScope(0.1, 1.2),
            voltage_safety_scope=SafetyScope(2.5, 4.0),
        )
        cs = instance.to_cs()
        self.assertTrue(cs.Enable)
        self.assertEqual(cs.AuxCount, 3)
        self.assertEqual(cs.TemperatureSafetyScope.Low, 10)
        self.assertEqual(cs.CurrentSafetyScope.Low, 0.1)
        self.assertEqual(cs.VoltageSafetyScope.High, 4.0)

class TestScheduleModifyInfo(unittest.TestCase):
    def test_to_cs(self):
        instance = ScheduleModifyInfo(schedule_name="Test")
        cs = instance.to_cs()
        self.assertEqual(cs.ScheduleName, "Test")

class TestUploadFileArgs(unittest.TestCase):
    def test_to_cs(self):
        instance = UploadFileArgs(
            remote_relative_file_name="remote.txt",
            local_full_file_name="local.txt",
            is_overwrite=True,
            callback_func=lambda x: None,
        )
        cs = instance.to_cs()
        self.assertEqual(cs.RemoteRelativeFileName, "remote.txt")
        self.assertEqual(cs.LocalFullFileName, "local.txt")
        self.assertTrue(cs.IsOverride)

    def test_callback_validation(self):
        with self.assertRaises(TypeError):
            UploadFileArgs(callback_func=123).to_cs()

class TestBrowseFileListArgs(unittest.TestCase):
    def test_to_cs(self):
        instance = BrowseFileListArgs(sn="SN123")
        cs = instance.to_cs()
        self.assertEqual(cs.SN, "SN123")

class TestModifyScheduleArgs(unittest.TestCase):
    def test_to_cs(self):
        instance = ModifyScheduleArgs(schedule_modify_info=[ScheduleModifyInfo()])
        cs = instance.to_cs()
        self.assertEqual(len(cs.ScheduleModifyInfos), 1)

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            ModifyScheduleArgs(schedule_modify_info=["not a ScheduleModifyInfo"]).to_cs()

class TestAssignFileArgs(unittest.TestCase):
    def test_to_cs(self):
        instance = AssignFileArgs(sn="SN001", channel_id=[1, 2], file_name="file.sched")
        cs = instance.to_cs()
        self.assertEqual(cs.SN, "SN001")
        self.assertEqual(cs.FileName, "file.sched")

class TestUpdateMetaVariablesArgs(unittest.TestCase):
    def test_type_validation(self):
        with self.assertRaises(TypeError):
            UpdateMetaVariablesArgs(meta_variable_info=["wrong type"]).to_cs()

class TestAssignBarcodeInfoArgs(unittest.TestCase):
    def test_type_validation(self):
        with self.assertRaises(TypeError):
            AssignBarcodeInfoArgs(barcode_info=["wrong type"]).to_cs()

class TestTimeSensitiveSetMV(unittest.TestCase):
    def test_to_cs(self):
        instance = TimeSensitiveSetMV(mvud=ETimeSensitiveMVUD.MVUD2, value=42.0)
        cs = instance.to_cs()
        self.assertEqual(cs.Value, 42.0)

class TestTimeSensitiveSetMVChannel(unittest.TestCase):
    def test_to_cs(self):
        instance = TimeSensitiveSetMVChannel(
            channel_id=5,
            mv_list=[TimeSensitiveSetMV(mvud=ETimeSensitiveMVUD.MVUD1, value=1.0)],
            log=False
        )
        cs = instance.to_cs()
        self.assertEqual(cs.ChannelID, 5)
        self.assertFalse(cs.IsDoLog)

    def test_mv_list_validation(self):
        with self.assertRaises(ValueError):
            TimeSensitiveSetMVChannel(channel_id=1, mv_list=["wrong"]).to_cs()

class TestTimeSensitiveSetMVArgs(unittest.TestCase):
    def test_to_cs(self):
        instance = TimeSensitiveSetMVArgs(
            timeout=2.0,
            channel_list=[
                TimeSensitiveSetMVChannel(channel_id=1, mv_list=[TimeSensitiveSetMV()])
            ],
            sn="SN123"
        )
        cs = instance.to_cs()
        self.assertEqual(cs.SN, "SN123")

    def test_channels_validation(self):
        bad_instance = TimeSensitiveSetMVArgs(channel_list=["not a TimeSensitiveSetMVChannel"])
        with self.assertRaises(ValueError):
            bad_instance.to_cs()

if __name__ == "__main__":
    unittest.main()
