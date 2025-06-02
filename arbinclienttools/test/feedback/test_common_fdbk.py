import unittest
from System import Int32, String
from unittest.mock import MagicMock
from arbinclienttools.src.feedback.common import *
from arbinclienttools.src.enumeration import ESPTTCellStatus, EGetDataResult

class TestCANMonitorInfo(unittest.TestCase):
    def test_can_monitor_info_instantiation(self):
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
    def test_smb_monitor_info_instantiation(self):
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
    def test_aux_data_instantiation(self):
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
    def test_sptt_eq_monitor_data_instantiation(self):
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
    def test_sptt_cell_monitor_data_instantiation(self):
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

class TestSubChannelInfo(unittest.TestCase):
    def test_sub_channel_info_instantiation(self):
        mock_obj = MagicMock()
        mock_obj.SubChannelID = 10
        mock_obj.Current = 1.23
        mock_obj.Voltage = 4.56
        mock_obj.BRefVoltage = 3.21
        mock_obj.DeltaVoltage = 0.12
        mock_obj.ChargeCapacity = 100.5
        mock_obj.DischargeCapacity = 80.3
        mock_obj.ChargeEnergy = 75.0
        mock_obj.DischargeEnergy = 65.0

        sub_channel = SubChannelInfo(mock_obj)

        self.assertEqual(sub_channel.sub_channel_id, 10)
        self.assertAlmostEqual(sub_channel.current, 1.23)
        self.assertAlmostEqual(sub_channel.voltage, 4.56)
        self.assertAlmostEqual(sub_channel.b_ref_voltage, 3.21)
        self.assertAlmostEqual(sub_channel.delta_voltage, 0.12)
        self.assertAlmostEqual(sub_channel.charge_capacity, 100.5)
        self.assertAlmostEqual(sub_channel.discharge_capacity, 80.3)
        self.assertAlmostEqual(sub_channel.charge_energy, 75.0)
        self.assertAlmostEqual(sub_channel.discharge_energy, 65.0)

class TestShowUDSMessageValue(unittest.TestCase):
    def test_show_uds_message_value_instantiation(self):
        def make_signal(name, value, status):
            mock = MagicMock()
            mock.Name = name
            mock.Value = value
            mock.UDSSignalStatus = status
            return mock

        mock_obj = MagicMock()
        mock_obj.Name = "TestUDS"
        mock_obj.Request = [make_signal("Req1", "Val1", 0), make_signal("Req2", "Val2", 1)]
        mock_obj.Response = [make_signal("Res1", "Val3", 2), make_signal("Res2", "Val4", 3)]

        uds = ShowUDSMessageValue(mock_obj)

        self.assertEqual(uds.name, "TestUDS")
        self.assertEqual(len(uds.request), 2)
        self.assertEqual(uds.request[0].name, "Req1")
        self.assertEqual(uds.request[0].uds_signal_status.value, 0)
        self.assertEqual(uds.response[1].name, "Res2")
        self.assertEqual(uds.response[1].uds_signal_status.value, 3)

class TestSimulationInfo(unittest.TestCase):
    def test_simulation_info_instantiation(self):
        mock_obj = MagicMock()
        mock_obj.SimulationName = "SimTest"
        mock_obj.ExInfos = "Extra info here"
        
        sim_info = SimulationInfo(mock_obj)
        
        self.assertEqual(sim_info.simulation_name, "SimTest")
        self.assertEqual(sim_info.ex_info, "Extra info here")

class TestAuxMapping(unittest.TestCase):
    def test_aux_mapping_instantiation(self):
        mock_obj = MagicMock()
        mock_obj.AuxType = "TypeA"
        mock_obj.AuxChGlobalID = 101
        mock_obj.AuxChVirtualID = 202
        mock_obj.AliasName = "Alias1"
        mock_obj.Unit = "mV"
        
        aux = AuxMapping(mock_obj)
        self.assertEqual(aux.aux_type, "TypeA")
        self.assertEqual(aux.aux_ch_global_id, 101)
        self.assertEqual(aux.aux_ch_virtual_id, 202)
        self.assertEqual(aux.alias_name, "Alias1")
        self.assertEqual(aux.unit, "mV")

class TestChannelMonitorData(unittest.TestCase):
    def test_channel_monitor_data_instantiation(self):
        mock_data = MagicMock()
        mock_data.SN = "SN123"
        mock_data.ChannelID = 1
        mock_data.Status = "Active"
        mock_data.CommunicationFailure = False
        mock_data.ScheduleName = "Sched1"
        mock_data.TestObjectName = "TestObj"
        mock_data.CANBMSName = "CANBMS1"
        mock_data.SMBName = "SMB1"
        mock_data.ChartName = "Chart1"
        mock_data.TestName = "Test1"
        mock_data.ExitCondition = "Exit1"
        mock_data.StepAndCycle = "Step1Cycle1"
        mock_data.StepID = 2
        mock_data.SubStepID = 3
        mock_data.CycleID = 4
        mock_data.Barcode = "BC123"
        mock_data.MasterChannelID = 5
        mock_data.TestTime = 10.5
        mock_data.StepTime = 5.5
        mock_data.DateTime = 1620000000
        mock_data.Voltage = 3.7
        mock_data.Current = 1.5
        mock_data.Power = 5.5
        mock_data.NominalCapacityOfTestObject = 100.0
        mock_data.CurrentMaxOfTestObject = 2.0
        mock_data.VoltageMaxOfTestObject = 4.2
        mock_data.VoltageMinOfTestObject = 3.0
        mock_data.NominalVoltageOfTestObject = 3.6
        mock_data.NominalCapacitanceOfTestObject = 2000.0
        mock_data.NominalIROfTestObject = 0.01
        mock_data.SpecificCapacityOfTestObject = 120.0
        mock_data.IsAutoCalculateOfTestObject = True
        mock_data.MassOfTestObject = 50.0
        mock_data.ChargeCapacity = 90.0
        mock_data.DischargeCapacity = 80.0
        mock_data.ChargeEnergy = 70.0
        mock_data.DischargeEnergy = 60.0
        mock_data.InternalResistance = 0.005
        mock_data.dVdt = 0.002
        mock_data.dQdV = 0.003
        mock_data.dVdQ = 0.004
        mock_data.ACR = 0.1
        mock_data.ACI = 0.2
        mock_data.ACIPhase = 0.3
        mock_data.MVUDs = []
        mock_data.CANs = []
        mock_data.SMBs = []
        mock_data.Auxs = []
        mock_data.EQDatas = []
        mock_data.CellDatas = []
        mock_data.SubChannels = []
        mock_data.UDSDatas = []
        mock_data.DNLC = 0.01
        mock_data.DNC = 0.02

        ch_data = ChannelMonitorData(mock_data)

        self.assertEqual(ch_data.sn, "SN123")
        self.assertEqual(ch_data.channel_id, 1)
        self.assertEqual(ch_data.status, "Active")
        self.assertFalse(ch_data.communication_failure)
        self.assertEqual(ch_data.schedule_name, "Sched1")
        self.assertEqual(ch_data.test_object_name, "TestObj")
        self.assertEqual(ch_data.can_bms_name, "CANBMS1")
        self.assertEqual(ch_data.smb_name, "SMB1")
        self.assertEqual(ch_data.chart_name, "Chart1")
        self.assertEqual(ch_data.test_name, "Test1")
        self.assertEqual(ch_data.exit_condition, "Exit1")
        self.assertEqual(ch_data.step_and_cycle, "Step1Cycle1")
        self.assertEqual(ch_data.step_id, 2)
        self.assertEqual(ch_data.sub_step_id, 3)
        self.assertEqual(ch_data.cycle_id, 4)
        self.assertEqual(ch_data.barcode, "BC123")
        self.assertEqual(ch_data.master_channel_id, 5)
        self.assertAlmostEqual(ch_data.test_time, 10.5)
        self.assertAlmostEqual(ch_data.step_time, 5.5)
        self.assertEqual(ch_data.date_time, 1620000000)
        self.assertAlmostEqual(ch_data.voltage, 3.7)
        self.assertAlmostEqual(ch_data.current, 1.5)
        self.assertAlmostEqual(ch_data.power, 5.5)
        self.assertAlmostEqual(ch_data.nominal_capacity_of_test_object, 100.0)
        self.assertAlmostEqual(ch_data.current_max_of_test_object, 2.0)
        self.assertAlmostEqual(ch_data.voltage_max_of_test_object, 4.2)
        self.assertAlmostEqual(ch_data.voltage_min_of_test_object, 3.0)
        self.assertAlmostEqual(ch_data.nominal_voltage_of_test_object, 3.6)
        self.assertAlmostEqual(ch_data.nominal_capacitance_of_test_object, 2000.0)
        self.assertAlmostEqual(ch_data.nominal_ir_of_test_object, 0.01)
        self.assertAlmostEqual(ch_data.specific_capacity_of_test_object, 120.0)
        self.assertTrue(ch_data.is_auto_calculate_of_test_object)
        self.assertAlmostEqual(ch_data.mass_of_test_object, 50.0)
        self.assertAlmostEqual(ch_data.charge_capacity, 90.0)
        self.assertAlmostEqual(ch_data.discharge_capacity, 80.0)
        self.assertAlmostEqual(ch_data.charge_energy, 70.0)
        self.assertAlmostEqual(ch_data.discharge_energy, 60.0)
        self.assertAlmostEqual(ch_data.internal_resistance, 0.005)
        self.assertAlmostEqual(ch_data.dv_dt, 0.002)
        self.assertAlmostEqual(ch_data.dq_dv, 0.003)
        self.assertAlmostEqual(ch_data.dv_dq, 0.004)
        self.assertAlmostEqual(ch_data.acr, 0.1)
        self.assertAlmostEqual(ch_data.aci, 0.2)
        self.assertAlmostEqual(ch_data.aci_phase, 0.3)
        self.assertEqual(ch_data.mvuds, [])
        self.assertEqual(ch_data.cans, [])
        self.assertEqual(ch_data.smbs, [])
        self.assertEqual(ch_data.auxs, [])
        self.assertEqual(ch_data.eq_datas, [])
        self.assertEqual(ch_data.cell_datas, [])
        self.assertEqual(ch_data.sub_channels, [])
        self.assertEqual(ch_data.uds_datas, [])
        self.assertAlmostEqual(ch_data.dnlc, 0.01)
        self.assertAlmostEqual(ch_data.dnc, 0.02)

class TestResumeDataInfo(unittest.TestCase):
    def test_resume_data_info_instantiation(self):
        mock_obj = MagicMock()
        mock_obj.Createor = "John Doe"
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

class BarcodeInfo(DictReprBase):
    def test_barcode_info_initialization(self):
        # Create and configure the actual .NET BarcodeInfo object
        obj = ArbinDataModel.RequestInformation.BarcodeInfo()
        obj.BarcodeType = ArbinDataModel.EBarcodeType.IV
        obj.GlobalID = Int32(123)
        obj.Barcode = String("TEST123")
        obj.Info = String("Some sample info")
        obj.Result = String("OK")
        obj.BarcodeResult = Int32(1)  # EBarcodeResult.Success

        # Wrap into the BarcodeInfo class
        info = BarcodeInfo(obj)

        # Assert values
        self.assertEqual(info.barcode_type, EBarcodeType.IV)
        self.assertEqual(info.global_id, 123)
        self.assertEqual(info.barcode, "TEST123")
        self.assertEqual(info.info, "Some sample info")
        self.assertEqual(info.result, "OK")
        self.assertEqual(info.barcode_result, EBarcodeResult.Success)

class AIMetaVariableInfo(DictReprBase):
    def test_ai_meta_variable_info_instantiation(self):
        obj = ArbinDataModel.RequestInformation.ArbinAIMetaVariableInfo()
        obj.GlobalID = 1
        obj.MetaVariableType = int(EMetaVariableType.Current)
        obj.Value = 3.14
        obj.Result = "Pass"
        obj.MetavariableResult = int(EMetavariableResult.Success)
        obj.Index = 0
        obj.MetaDataType = int(EMetaDataType.Float)
        obj.MetaCode = int(EMetavariableCode.ChargeCapacity)
        obj.MetaVariableTypeString = "Current"

        info = AIMetaVariableInfo(obj)

        self.assertEqual(info.global_id, 1)
        self.assertEqual(info.meta_variable_type, EMetaVariableType.Current)
        self.assertEqual(info.value, 3.14)
        self.assertEqual(info.result, "Pass")
        self.assertEqual(info.metavariable_result, EMetavariableResult.Success)
        self.assertEqual(info.index_, 0)
        self.assertEqual(info.meta_data_type, EMetaDataType.Float)
        self.assertEqual(info.meta_code, EMetavariableCode.ChargeCapacity)
        self.assertEqual(info.meta_variable_type_string, "Current")

if __name__ == '__main__':
    unittest.main()
