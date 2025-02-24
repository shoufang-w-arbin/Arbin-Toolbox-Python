import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.base import (
    DictReprBase,
    SafeIntEnumBase
)

"""
Common objects for ArbinClient
- CANMonitorInfo
- SMBMonitorInfo
- AuxData
- SPTTEQMonitorData
- SPTTCellMonitorData
- SubChannelInfo
- ShowUDSMessageValue
- SimulationInfo
- AuxMapping
- CANBMSFile
- SMBFile
"""

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
    class ESPTTCellStatus(SafeIntEnumBase):
        None = 0
        UnUse = 1
        Idle = 2
        Charging = 3
        Discharging = 4
        CurrentUnsafe = 5
        VoltageUnsafe = 6

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
        self.cell_status                 = self.ESPTTCellStatus(int(obj.CellStatus))
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

