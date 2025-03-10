__doc__ = """
ArbinMQ Arguments
- CANMonitorInfo
- SMBMonitorInfo
- AuxData
- SPTTEQMonitorData
- SPTTCellMonitorData
- SubChannelInfo
- ShowUDSMessageValue
- SimulationInfo
- AuxMapping
- CANBMSFile (Not implemented)
- SMBFile (Not implemented)
- SubscribeMonitorDataFeedback
- SubscribeChannelDataFeedback
- SubscribeTestInfoDataFeedback
- SubscribeEventDataFeedback
- SubscribeDiagnosticEventDataFeedback
- SubscribeSPTTEQCELLDataFeedback
"""

import Arin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.base import (
    DictReprBase,
    SafeIntEnumBase
)
from arbinclienttools.src.common.enumeration import (
    ESPTTCellStatus
)

class CANMonitorInfo(DictReprBase):
    def __init__(self, obj):
        self.alias_name = str(obj.AliasName)
        self.meta_name  = str(obj.MetaName)
        self.data_type  = int(obj.DataType)
        self.value      = str(obj.Value)
        self.is_offline = bool(obj.IsOffline)

class SMBMonitorInfo(DictReprBase):
    def __init__(self, obj):
        self.alias_name = str(obj.AliasName)
        self.meta_name  = str(obj.MetaName)
        self.data_type  = int(obj.DataType)
        self.value      = str(obj.Value)
        self.is_offline = bool(obj.IsOffline)

class AuxData(DictReprBase):
    def __init__(self, obj):
        self.aux_type          = str(obj.AuxType)
        self.alias_name        = str(obj.AliasName)
        self.aux_ch_global_id  = int(obj.AuxChGlobalID)
        self.aux_ch_virtual_id = int(obj.AuxChVirtualID)
        self.value             = float(obj.Value)
        self.dxdt              = float(obj.dxdt)

class SPTTEQMonitorData(DictReprBase):
    def __init__(self, obj):
        self.parent_engagement_global_id = int(obj.ParentEngagementGlobalID)
        self.eq_global_id                = int(obj.EQGlobalID)
        self.eq_virtual_id_in_iv         = int(obj.EQVirtualIDInIV)
        self.voltage                     = float(obj.Voltage)
        self.current                     = float(obj.Current)
        self.power                       = float(obj.Power)
        self.charge_capacity             = float(obj.ChargeCapacity)
        self.discharge_capacity          = float(obj.DischargeCapacity)
        self.charge_energy               = float(obj.ChargeEnergy)
        self.discharge_energy            = float(obj.DischargeEnergy)
        self.internal_resistance         = float(obj.InternalResistance)
        self.auxiliary_temperature       = float(obj.AuxiliaryTemperature)
        self.status                      = str(obj.Status)
        self.barcode                     = str(obj.Barcode)
        self.info                        = str(obj.Info)

class SPTTCellMonitorData(DictReprBase):
    def __init__(self, obj):
        self.parent_engagement_global_id = int(obj.ParentEngagementGlobalID)
        self.parent_eq_global_id         = int(obj.ParentEQGlobalID)
        self.cell_global_id              = int(obj.CellGlobalID)
        self.cell_virtual_id_in_iv       = int(obj.CellVirtualIDInIV)
        self.position_x                  = int(obj.PositionX)
        self.position_y                  = int(obj.PositionY)
        self.voltage                     = float(obj.Voltage)
        self.current                     = float(obj.Current)
        self.power                       = float(obj.Power)
        self.charge_capacity             = float(obj.ChargeCapacity)
        self.discharge_capacity          = float(obj.DischargeCapacity)
        self.charge_energy               = float(obj.ChargeEnergy)
        self.discharge_energy            = float(obj.DischargeEnergy)
        self.internal_resistance         = float(obj.InternalResistance)
        self.auxiliary_temperature       = float(obj.AuxiliaryTemperature)
        self.status                      = str(obj.Status)
        self.cell_status                 = ESPTTCellStatus(int(obj.CellStatus))
        self.barcode                     = str(obj.Barcode)
        self.info                        = str(obj.Info)

class SubChannelInfo(DictReprBase):
    def __init__(self, obj):
        self.sub_channel_id     = int(obj.SubChannelID)
        self.current            = float(obj.Current)
        self.voltage            = float(obj.Voltage)
        self.b_ref_voltage      = float(obj.BRefVoltage)
        self.delta_voltage      = float(obj.DeltaVoltage)
        self.charge_capacity    = float(obj.ChargeCapacity)
        self.discharge_capacity = float(obj.DischargeCapacity)
        self.charge_energy      = float(obj.ChargeEnergy)
        self.discharge_energy   = float(obj.DischargeEnergy)

class ShowUDSMessageValue(DictReprBase):
    class UDSSignalValue(DictReprBase):
        class UDSSignalStatus(SafeIntEnumBase):
            Successes = 0
            NoRead = 1
            FailRead = 2
            NotExist = 3

        def __init__(self, obj):
            self.name              = str(obj.Name)
            self.Value             = str(obj.Value)
            self.uds_signal_status = self.UDSSignalStatus(int(obj.UDSSignalStatus)) 

    def __init__(self, obj):
        self.name     = str(obj.Name)
        self.request  = [self.UDSSignalValue(v) for v in obj.Request]
        self.response = [self.UDSSignalValue(v) for v in obj.Response]

class SimulationInfo(DictReprBase):
    def __init__(self, obj):
        self.simulation_name = str(obj.SimulationName)
        self.ex_info         = str(obj.ExInfos)

class AuxMapping(DictReprBase):
    def __init__(self, obj):
        self.aux_type = str(obj.AuxType)
        self.aux_ch_global_id  = int(obj.AuxChGlobalID)
        self.aux_ch_virtual_id = int(obj.AuxChVirtualID)
        self.alias_name        = str(obj.AliasName)
        self.unit              = str(obj.Unit)
    
class CANBMSFile(DictReprBase):
    def __init__(self):
        raise NotImplementedError
    
class SMBFile(DictReprBase):
    def __init__(self):
        raise NotImplementedError

class SubscribeMonitorDataFeedback(DictReprBase):
    class ChannelMonitorData(DictReprBase):
        def __init__(self, data: ArbinDataModel.ChannelMonitorData):
            self.sn                              = str(data.SN)
            self.channel_id                      = int(data.ChannelID)
            self.status                          = str(data.Status)
            self.communication_failure           = bool(data.CommunicationFailure)
            self.schedule_name                   = str(data.ScheduleName)
            self.test_object_name                = str(data.TestObjectName)
            self.can_bms_name                    = str(data.CANBMSName)
            self.smb_name                        = str(data.SMBName)
            self.chart_name                      = str(data.ChartName)
            self.test_name                       = str(data.TestName)
            self.exit_condition                  = str(data.ExitCondition)
            self.step_and_cycle                  = str(data.StepAndCycle)
            self.step_id                         = int(data.StepID)
            self.sub_step_id                     = int(data.SubStepID)
            self.cycle_id                        = int(data.CycleID)
            self.barcode                         = str(data.Barcode)
            self.master_channel_id               = int(data.MasterChannelID)
            self.test_time                       = float(data.TestTime)
            self.step_time                       = float(data.StepTime)
            self.date_time                       = int(data.DateTime)
            self.voltage                         = float(data.Voltage)
            self.current                         = float(data.Current)
            self.power                           = float(data.Power)
            self.nominal_capacity_of_test_object = float(data.NominalCapacityOfTestObject)
            self.current_max_of_test_object      = float(data.CurrentMaxOfTestObject)
            self.voltage_max_of_test_object      = float(data.VoltageMaxOfTestObject)
            self.voltage_min_of_test_object      = float(data.VoltageMinOfTestObject)
            self.nominal_voltage_of_test_object  = float(data.NominalVoltageOfTestObject)
            self.nominal_capacitance_of_test_object = float(data.NominalCapacitanceOfTestObject)
            self.nominal_ir_of_test_object       = float(data.NominalIROfTestObject)
            self.specific_capacity_of_test_object = float(data.SpecificCapacityOfTestObject)
            self.is_auto_calculate_of_test_object = bool(data.IsAutoCalculateOfTestObject)
            self.mass_of_test_object             = float(data.MassOfTestObject)
            self.charge_capacity                 = float(data.ChargeCapacity)
            self.discharge_capacity              = float(data.DischargeCapacity)
            self.charge_energy                   = float(data.ChargeEnergy)
            self.discharge_energy                = float(data.DischargeEnergy)
            self.internal_resistance             = float(data.InternalResistance)
            self.dv_dt                           = float(data.dVdt)
            self.dq_dv                           = float(data.dQdV)
            self.dv_dq                           = float(data.dVdQ)
            self.acr                             = float(data.ACR)
            self.aci                             = float(data.ACI)
            self.aci_phase                       = float(data.ACIPhase)
            self.mvuds                           = list(data.MVUDs)
            self.cans                            = [CANMonitorInfo(d) for d in data.CANs]
            self.smbs                            = [SMBMonitorInfo(d) for d in data.SMBs]
            self.auxs                            = [AuxData(d) for d in data.Auxs]
            self.eq_datas                        = [SPTTEQMonitorData(d) for d in data.EQDatas]
            self.cell_datas                      = [SPTTCellMonitorData(d) for d in data.CellDatas]
            self.sub_channels                    = [SubChannelInfo(d) for d in data.SubChannels]
            self.uds_datas                       = [ShowUDSMessageValue(d) for d in data.UDSDatas]
            self.dnlc                            = float(data.DNLC)
            self.dnc                             = float(data.DNC)
        
    def __init__(self, feedback: ArbinDataModel.SubscribeMonitorDataFDBK):
        if not isinstance(feedback, ArbinDataModel.SubscribeMonitorDataFDBK):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeMonitorDataFDBK', got '{type(feedback)}'")
        self.id_                  = str(feedback.ID)
        self.task_id              = int(feedback.TaskID)
        self.channel_monitor_data = [self.ChannelMonitorData(data) for data in feedback.ChannelMonitorDatas]

class SubscribeChannelDataFeedback(DictReprBase):
    class ChannelData:
        def __init__(self, data: ArbinDataModel.ChannelData):
            self.sn                 = str(data.SN)
            self.channel_id         = int(data.ChannelID)
            self.barcode            = str(data.Barcode)
            self.test_name          = str(data.TestName)
            self.test_id            = int(data.TestID)
            self.date_time          = int(data.DateTime)
            self.data_point         = int(data.DataPoint)
            self.status             = str(data.Status)
            self.test_time          = float(data.TestTime)
            self.step_time          = float(data.StepTime)
            self.step_id            = int(data.StepID)
            self.sub_step_id        = int(data.SubStepID)
            self.cycle_id           = int(data.CycleID)
            self.voltage            = float(data.Voltage)
            self.current            = float(data.Current)
            self.power              = float(data.Power)
            self.charge_capacity    = float(data.ChargeCapacity)
            self.discharge_capacity = float(data.DischargeCapacity)
            self.charge_energy      = float(data.ChargeEnergy)
            self.discharge_energy   = float(data.DischargeEnergy)
            self.internal_resistance= float(data.InternalResistance)
            self.dv_dt              = float(data.dVdt)
            self.dq_dv              = float(data.dQdV)
            self.dv_dq              = float(data.dVdQ)
            self.data_flags         = int(data.DataFlags)
            self.limit_id           = float(data.LimitID)
            self.mvuds              = list(data.MVUDs)
            self.tc_counters        = list(data.TCCounters)
            self.cans               = [CANMonitorInfo(d) for d in data.CANs]
            self.smbs               = [SMBMonitorInfo(d) for d in data.SMBs]
            self.auxs               = [AuxData(d) for d in data.Auxs]
            self.dnlc               = float(data.DNLC)
            self.dnc                = float(data.DNC)

    def __init__(self, feedback: ArbinDataModel.SubscribeChannelDataFDBK):
        if not isinstance(feedback, ArbinDataModel.SubscribeChannelDataFDBK):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeChannelDataFDBK', got '{type(feedback)}'")
        self.id_ = str(feedback.ID)
        self.task_id = int(feedback.TaskID)
        self.channel_data = [self.ChannelData(data) for data in feedback.ChannelDatas]

class SubscribeTestInfoDataFeedback(DictReprBase):
    class TestInfoData:
        class TestInfoSPTTEngagement(DictReprBase):
            def __init__(self, obj):
                self.engagement_id = int(obj.EngagementID)
                self.barcode       = str(obj.Barcode)

        class TestInfoSPTTEQ(DictReprBase):
            def __init__(self, obj):
                self.parent_engagement_id = int(obj.ParentEngagementID)
                self.eq_virtual_id_iv     = int(obj.EQVirtualIDInIV)
                self.eq_global_id         = int(obj.EQGlobalID)

        class TestInfoSPTTCell(DictReprBase):
            def __init__(self, obj):
                self.parent_engagement_id   = int(obj.ParentEngagementID)
                self.parent_eq_global_id    = int(obj.ParentEQGlobalID)
                self.cell_virtual_id_in_iv  = int(obj.CellVirtualIDInIV)
                self.cell_global_id         = int(obj.CellGlobalID)
                self.position_x             = int(obj.PositionX)
                self.position_y             = int(obj.PositionY)
                self.barcode                = str(obj.Barcode)

        def __init__(self, data: ArbinDataModel.TestInfoData):
            self.sn                      = str(data.SN)
            self.channel_id              = int(data.ChannelID)
            self.barcode                 = str(data.Barcode)
            self.test_name               = str(data.TestName)
            self.test_id                 = int(data.TestID)
            self.start_file_time         = int(data.StartFileTime)
            self.start_date_time         = str(data.StartDateTime)
            self.creator                 = str(data.Creator)
            self.comment                 = str(data.Comment)
            self.schedule_name           = str(data.ScheduleName)
            self.test_object_name        = str(data.TestObjectName)
            self.can_bms_name            = str(data.CANBMSName)
            self.can_bms_file_content    = data.CANBMSFileContent # ignored for now
            self.smb_name                = str(data.SMBName)
            self.smb_file_content        = data.SMBFileContent    # ignored for now
            self.capacity                = float(data.Capacity)
            self.specific_capacity       = float(data.SpecificCapacity)
            self.specific_mass           = float(data.SpecificMass)
            self.software_version        = str(data.SoftwareVersion)
            self.firmware_version        = str(data.FirmwareVersion)
            self.simulation_file_names   = [SimulationInfo(d) for d in data.SimulationFileNames]
            self.mappings                = [AuxMapping(d) for d in data.Mappings]
            self.engagements             = [self.TestInfoSPTTEngagement(d) for d in data.Engagements]
            self.eq_datas                = [self.TestInfoSPTTEQ(d) for d in data.EQDatas]
            self.cell_datas              = [self.TestInfoSPTTCell(d) for d in data.CellDatas]

    def __init__(self, feedback: ArbinDataModel.SubscribeTestInfoDataFDBK):
        if not isinstance(feedback, ArbinDataModel.SubscribeTestInfoDataFDBK):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeTestInfoDataFDBK', got '{type(feedback)}'")
        self.id_ = str(feedback.ID)
        self.task_id = int(feedback.TaskID)
        self.channel_test_info = [self.TestInfoData(data) for data in feedback.ChannelTestInfos]

class SubscribeEventDataFeedback(DictReprBase):
    class ChannelEvents(DictReprBase):
        def __init__(self, obj):
            self._id         = str(obj.SN)
            self.channel_id  = int(obj.ChannelID)
            self.test_id     = int(obj.TestID)
            self.date_time   = int(obj.DateTime)
            self.event_type  = int(obj.EventType)
            self.event_desc  = str(obj.EventDesc)
            self.test_time   = float(obj.TestTime)
            self.step_time   = float(obj.StepTime)
            self.cycle_id    = int(obj.CycleID)
            self.step_id     = int(obj.StepID)
            self.sub_step_id = int(obj.SubStepID)
            self.limit_id    = int(obj.LimitID)
            self.tc_counter1 = int(obj.TCCounter1)
            self.tc_counter2 = int(obj.TCCounter2)
            self.tc_counter3 = int(obj.TCCounter3)
            self.tc_counter4 = int(obj.TCCounter4)
            self.tc_counter5 = int(obj.TCCounter5)
            self.tc_counter6 = int(obj.TCCounter6)
            self.tc_counter7 = int(obj.TCCounter7)
            self.tc_counter8 = int(obj.TCCounter8)
            self.tc_timer1   = float(obj.TCTimer1)
            self.tc_timer2   = float(obj.TCTimer2)
            self.tc_timer3   = float(obj.TCTimer3)
            self.tc_timer4   = float(obj.TCTimer4)
    def __init__(self, feedback: ArbinDataModel.SubscribeEventDataFDBK):
        if not isinstance(feedback, ArbinDataModel.SubscribeEventDataFDBK):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeEventDataFDBK', got '{type(feedback)}'")
        self.id_ = str(feedback.ID)
        self.task_id = int(feedback.TaskID)
        self.channel_event = [self.ChannelEvents(data) for data in feedback.ChannelEvents]

class SubscribeDiagnosticEventDataFeedback(DictReprBase):
    class ChannelDiagnosticEventData(DictReprBase):
        def __init__(self, obj):
            self.sn                   = str(obj.SN)
            self.channel_id           = int(obj.ChannelID)
            self.diagnostic_envet_msg = str(obj.DiagnosticEventMsg)

    def __init__(self, feedback: ArbinDataModel.SubscribeDiagnosticEventDataFDBK):
        if not isinstance(feedback, ArbinDataModel.SubscribeDiagnosticEventDataFDBK):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeDiagnosticEventDataFDBK', got '{type(feedback)}'")
        self.id_                      = str(feedback.ID)
        self.task_id                  = int(feedback.TaskID)
        self.channel_diagnostic_event = [self.ChannelDiagnosticEventData(data) for data in feedback.ChannelDiagnosticEvents]

class SubscribeSPTTEQCELLDataFeedback(DictReprBase):
    class SPTTLogData(DictReprBase):
        def __init__(self, obj):
            self.barcode            = str(obj.Barcode)
            self.test_id            = int(obj.TestID)
            self.channel_id         = int(obj.ChannelID)
            self.eq_virtual_id      = int(obj.EQVirtualID)
            self.eq_global_id       = int(obj.EQGlobalID)
            self.cell_virtual_id    = int(obj.CellVirtualID)
            self.cell_global_id     = int(obj.CellGlobalID)
            self.tray_id            = int(obj.TrayID)
            self.status             = str(obj.Status)
            self.position_x         = int(obj.PositionX)
            self.position_y         = int(obj.PositionY)
            self.date_time          = int(obj.DateTime)
            self.data_point         = int(obj.DataPoint)
            self.test_time          = float(obj.TestTime)
            self.step_time          = float(obj.StepTime)
            self.cycle_id           = int(obj.CycleID)
            self.step_id            = int(obj.StepID)
            self.sub_step_id        = int(obj.SubStepID)
            self.current            = float(obj.Current)
            self.voltage            = float(obj.Voltage)
            self.temperature        = float(obj.Temperature)
            self.charge_capacity    = float(obj.ChargeCapacity)
            self.discharge_capacity = float(obj.DischargeCapacity)
            self.charge_energy      = float(obj.ChargeEnergy)
            self.discharge_energy   = float(obj.DischargeEnergy)
            self.data_flags         = int(obj.DataFlags)

    def __init__(self, feedback: ArbinDataModel.SubscribeSPTTEQCELLDataFeedback):
        if not isinstance(feedback, ArbinDataModel.SubscribeSPTTEQCELLDataFeedback):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeSPTTEQCELLDataFeedback', got '{type(feedback)}'")
        self.id_        = str(feedback.ID)
        self.task_id    = int(feedback.TaskID)
        self.eq_data    = [self.SPTTLogData(data) for data in feedback.EQDatas]
        self.cell_dasta = [self.SPTTLogData(data) for data in feedback.CellDatas]









