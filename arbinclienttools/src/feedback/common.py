__doc__ = """
[Common Objects]
- CANMonitorInfo
- SMBMonitorInfo
- AuxData
- SPTTEQMonitorData
- SPTTCellMonitorData
- SubChannelInfo
- ShowUDSMessageValue
- SimulationInfo
- AuxMapping
- CANBMSFile (not implemented yet)
- SMBFile (not implemented yet)
- ChannelMonitorData
- BarcodeInfo
- AIMetaVariableInfo
"""

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.cs_conv import CSConv
from common.src.base import (
    DictReprBase,
    SafeIntEnumBase
)
from arbinclienttools.src.enumeration import (
    ESPTTCellStatus,
    EGetDataResult,
    EBarcodeResult,
    EBarcodeType,
    EMetaVariableType,
    EMetavariableResult,
    EMetaDataType,
    EMetavariableCode,
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

class ResumeDataInfo(DictReprBase):
    """
    Wrapper class of of 'Arbin.Library.DataModel.RequestInformation.ResumeDataInfo'
    """
    def __init__(self, obj):
        self.creator         = str(obj.Creator)
        self.comment         = str(obj.Comment)
        self.start_time      = str(obj.StartTime)
        self.step_labels     = list(obj.StepLabels)
        self.step_count      = int(obj.StepCount)
        self.result          = str(obj.Result)
        self.get_data_result = EGetDataResult(int(obj.GetDataResult))

class BarcodeInfo(DictReprBase):
    def __init__(self, obj):
        self.barcode_type   = EBarcodeType(int(obj.BarcodeType))
        self.global_id      = int(obj.GlobalID)
        self.barcode        = str(obj.Barcode)
        self.info           = str(obj.Info)
        self.result         = str(obj.Result)
        self.barcode_result = EBarcodeResult(int(obj.BarcodeResult))

class AIMetaVariableInfo(DictReprBase):
    def __init__(self, obj):
        self.global_id                   = int(obj.GlobalID)
        self.meta_variable_type          = EMetaVariableType(int(obj.MetaVariableType))
        self.value                       = float(obj.Value)
        self.result                      = str(obj.Result)
        self.metavariable_result         = EMetavariableResult(int(obj.MetavariableResult))
        self.index_                      = int(obj.Index)
        self.meta_data_type              = EMetaDataType(int(obj.MetaDataType))
        self.meta_code                   = EMetavariableCode(int(obj.MetaCode))
        self.meta_variable_type_string   = str(obj.MetaVariableTypeString)

        