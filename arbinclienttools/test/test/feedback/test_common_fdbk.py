import unittest
from unittest.mock import MagicMock
from arbinclienttools.src.feedback.common import CSConv
from arbinclienttools.src.enumeration import ESPTTCellStatus, EGetDataResult

class TestCANMonitorInfo(unittest.TestCase):
    def test_init(self):
        # Mock data simulating ArbinDataModel
        mock_obj = MagicMock()
        mock_obj.AliasName = "CAN_Alias"
        mock_obj.MetaName = "CAN_Meta"
        mock_obj.DataType = 1
        mock_obj.Value = "10.5"
        mock_obj.IsOffline = False
        
        can_monitor = CANMonitorInfo(mock_obj)

        self.assertEqual(can_monitor.alias_name, "CAN_Alias")
        self.assertEqual(can_monitor.meta_name, "CAN_Meta")
        self.assertEqual(can_monitor.data_type, 1)
        self.assertEqual(can_monitor.value, "10.5")
        self.assertFalse(can_monitor.is_offline)

class TestSMBMonitorInfo(unittest.TestCase):
    def test_init(self):
        mock_obj = MagicMock()
        mock_obj.AliasName = "SMB_Alias"
        mock_obj.MetaName = "SMB_Meta"
        mock_obj.DataType = 2
        mock_obj.Value = "5.0"
        mock_obj.IsOffline = True
        
        smb_monitor = SMBMonitorInfo(mock_obj)

        self.assertEqual(smb_monitor.alias_name, "SMB_Alias")
        self.assertEqual(smb_monitor.meta_name, "SMB_Meta")
        self.assertEqual(smb_monitor.data_type, 2)
        self.assertEqual(smb_monitor.value, "5.0")
        self.assertTrue(smb_monitor.is_offline)

class TestAuxData(unittest.TestCase):
    def test_init(self):
        mock_obj = MagicMock()
        mock_obj.AuxType = "Temperature"
        mock_obj.AliasName = "Temp_Alias"
        mock_obj.AuxChGlobalID = 100
        mock_obj.AuxChVirtualID = 200
        mock_obj.Value = 30.5
        mock_obj.dxdt = 0.02
        
        aux_data = AuxData(mock_obj)

        self.assertEqual(aux_data.aux_type, "Temperature")
        self.assertEqual(aux_data.alias_name, "Temp_Alias")
        self.assertEqual(aux_data.aux_ch_global_id, 100)
        self.assertEqual(aux_data.aux_ch_virtual_id, 200)
        self.assertEqual(aux_data.value, 30.5)
        self.assertEqual(aux_data.dxdt, 0.02)

class TestSPTTEQMonitorData(unittest.TestCase):
    def test_init(self):
        mock_obj = MagicMock()
        mock_obj.ParentEngagementGlobalID = 1
        mock_obj.EQGlobalID = 100
        mock_obj.EQVirtualIDInIV = 10
        mock_obj.Voltage = 3.7
        mock_obj.Current = 2.0
        mock_obj.Power = 7.4
        mock_obj.ChargeCapacity = 1.0
        mock_obj.DischargeCapacity = 1.5
        mock_obj.ChargeEnergy = 3.0
        mock_obj.DischargeEnergy = 3.5
        mock_obj.InternalResistance = 0.01
        mock_obj.AuxiliaryTemperature = 25.5
        mock_obj.Status = "Active"
        mock_obj.Barcode = "123ABC"
        mock_obj.Info = "Test Data"
        
        eq_data = SPTTEQMonitorData(mock_obj)

        self.assertEqual(eq_data.parent_engagement_global_id, 1)
        self.assertEqual(eq_data.eq_global_id, 100)
        self.assertEqual(eq_data.eq_virtual_id_in_iv, 10)
        self.assertEqual(eq_data.voltage, 3.7)
        self.assertEqual(eq_data.current, 2.0)
        self.assertEqual(eq_data.power, 7.4)
        self.assertEqual(eq_data.charge_capacity, 1.0)
        self.assertEqual(eq_data.discharge_capacity, 1.5)
        self.assertEqual(eq_data.charge_energy, 3.0)
        self.assertEqual(eq_data.discharge_energy, 3.5)
        self.assertEqual(eq_data.internal_resistance, 0.01)
        self.assertEqual(eq_data.auxiliary_temperature, 25.5)
        self.assertEqual(eq_data.status, "Active")
        self.assertEqual(eq_data.barcode, "123ABC")
        self.assertEqual(eq_data.info, "Test Data")

class TestSPTTCellMonitorData(unittest.TestCase):
    def test_init(self):
        mock_obj = MagicMock()
        mock_obj.ParentEngagementGlobalID = 1
        mock_obj.ParentEQGlobalID = 200
        mock_obj.CellGlobalID = 300
        mock_obj.CellVirtualIDInIV = 400
        mock_obj.PositionX = 10
        mock_obj.PositionY = 20
        mock_obj.Voltage = 3.7
        mock_obj.Current = 1.5
        mock_obj.Power = 5.55
        mock_obj.ChargeCapacity = 1.0
        mock_obj.DischargeCapacity = 1.1
        mock_obj.ChargeEnergy = 3.5
        mock_obj.DischargeEnergy = 3.6
        mock_obj.InternalResistance = 0.02
        mock_obj.AuxiliaryTemperature = 27.0
        mock_obj.Status = "Charging"
        mock_obj.CellStatus = 1  # ESPTTCellStatus enum
        mock_obj.Barcode = "CELL123"
        mock_obj.Info = "Cell Data"
        
        cell_data = SPTTCellMonitorData(mock_obj)

        self.assertEqual(cell_data.parent_engagement_global_id, 1)
        self.assertEqual(cell_data.parent_eq_global_id, 200)
        self.assertEqual(cell_data.cell_global_id, 300)
        self.assertEqual(cell_data.cell_virtual_id_in_iv, 400)
        self.assertEqual(cell_data.position_x, 10)
        self.assertEqual(cell_data.position_y, 20)
        self.assertEqual(cell_data.voltage, 3.7)
        self.assertEqual(cell_data.current, 1.5)
        self.assertEqual(cell_data.power, 5.55)
        self.assertEqual(cell_data.charge_capacity, 1.0)
        self.assertEqual(cell_data.discharge_capacity, 1.1)
        self.assertEqual(cell_data.charge_energy, 3.5)
        self.assertEqual(cell_data.discharge_energy, 3.6)
        self.assertEqual(cell_data.internal_resistance, 0.02)
        self.assertEqual(cell_data.auxiliary_temperature, 27.0)
        self.assertEqual(cell_data.status, "Charging")
        self.assertEqual(cell_data.cell_status, ESPTTCellStatus(int(mock_obj.CellStatus)))
        self.assertEqual(cell_data.barcode, "CELL123")
        self.assertEqual(cell_data.info, "Cell Data")

class TestResumeDataInfo(unittest.TestCase):
    def test_init(self):
        mock_obj = MagicMock()
        mock_obj.Creator = "John Doe"
        mock_obj.Comment = "Test Comment"
        mock_obj.StartTime = "2025-04-28T00:00:00"
        mock_obj.StepLabels = ["Step 1", "Step 2"]
        mock_obj.StepCount = 2
        mock_obj.Result = "Success"
        mock_obj.GetDataResult = 0  # EGetDataResult enum
        
        resume_data = ResumeDataInfo(mock_obj)

        self.assertEqual(resume_data.creator, "John Doe")
        self.assertEqual(resume_data.comment, "Test Comment")
        self.assertEqual(resume_data.start_time, "2025-04-28T00:00:00")
        self.assertEqual(resume_data.step_labels, ["Step 1", "Step 2"])
        self.assertEqual(resume_data.step_count, 2)
        self.assertEqual(resume_data.result, "Success")
        self.assertEqual(resume_data.get_data_result, EGetDataResult(int(mock_obj.GetDataResult)))

if __name__ == '__main__':
    unittest.main()
