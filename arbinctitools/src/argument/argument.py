from dataclasses import dataclass, field

import ArbinCTI.Core as ArbinCTI                # type: ignore
from System.Collections.Generic import List     # type: ignore

from common.src.cs_conv import CSConv

from common.src.base import (
    DictReprBase,
    SafeIntEnumBase
)

"""
CTI DATA TYPE WRAPPERS
Classes:
- TE_DATA_TYPE
- StartResumeEx
- MetaVariableInfo
- MetaVariableInfoEx
- CMetavariableDataCodeApply
- TimeSensitiveSetMV:           TimeSensitiveSetMV, TimeSensitiveSetMVArgs
- StartChannelAdvanced:         TestObjectSetting, StartChannelInfo, StartChannelAdvancedArgs
- ModifySchedule:               SafetyScope, AuxChannelRequirementBase, AuxChannelRequirement, AuxSafetyRequirement, ScheduleModifyInfo, ModifyScheduleArgs
"""
class TE_DATA_TYPE(SafeIntEnumBase):
    MP_DATA_TYPE_MetaValue = 1
    MP_DATA_TYPE_AuxTemperature = 10
    MP_DATA_TYPE_AuxdTdt = 11
    MP_DATA_TYPE_AuxVoltage = 12
    MP_DATA_TYPE_AuxdVdt = 13
    MP_DATA_TYPE_AuxPressure = 14
    MP_DATA_TYPE_AuxdPdt = 15
    MP_DATA_TYPE_AuxPh = 16
    MP_DATA_TYPE_AuxdPhVdt = 17
    MP_DATA_TYPE_AuxFlowRate = 18
    MP_DATA_TYPE_AuxdFRdt = 19
    MP_DATA_TYPE_AuxConcentration = 20
    MP_DATA_TYPE_AuxdConcentrationdt = 21
    MP_DATA_TYPE_AuxDI = 22
    MP_DATA_TYPE_AuxDO = 23
    MP_DATA_TYPE_CANBMS = 24
    MP_DATA_TYPE_AuxExternalCharge = 25
    MP_DATA_TYPE_AuxHumidity = 26
    MP_DATA_TYPE_AuxdHumdt = 27
    MP_DATA_TYPE_SMBBMS = 28
    MP_DATA_TYPE_AuxAO = 30
    MP_DATA_TYPE_EQ = 31
    MP_DATA_TYPE_CELL = 32

@dataclass
class StartResumeEx:
    """
    Python wrapper of 'ArbinCTI.Core.StartResumeEx'
    """
    channelIndex          : int    = 0
    TestID                : int    = 0
    TestNames             : str    = ""
    Schedules             : str    = ""
    nSelectSteps          : int    = 0
    Cycle                 : int    = 0
    TestTime              : float  = 0.0
    StepTime              : float  = 0.0
    CCapacity             : float  = 0.0
    DCapacity             : float  = 0.0
    CEnergy               : float  = 0.0
    DEnergy               : float  = 0.0
    TC_Time1              : float  = 0.0
    TC_Time2              : float  = 0.0
    TC_Time3              : float  = 0.0
    TC_Time4              : float  = 0.0
    TC_CCapacity1         : float  = 0.0
    TC_CCapacity2         : float  = 0.0
    TC_DCapacity1         : float  = 0.0
    TC_DCapacity2         : float  = 0.0
    TC_CEnergy1           : float  = 0.0
    TC_CEnergy2           : float  = 0.0
    TC_DEnergy1           : float  = 0.0
    TC_DEnergy2           : float  = 0.0
    MV_Counter1           : float  = 0.0
    MV_Counter2           : float  = 0.0
    MV_Counter3           : float  = 0.0
    MV_Counter4           : float  = 0.0
    MV_Counter5           : float  = 0.0
    MV_Counter6           : float  = 0.0
    MV_Counter7           : float  = 0.0
    MV_Counter8           : float  = 0.0
    ChargeCapacityTime    : float  = 0.0
    DischargeCapacityTime : float  = 0.0
    MVUD1                 : float  = 0.0
    MVUD2                 : float  = 0.0
    MVUD3                 : float  = 0.0
    MVUD4                 : float  = 0.0
    MVUD5                 : float  = 0.0
    MVUD6                 : float  = 0.0
    MVUD7                 : float  = 0.0
    MVUD8                 : float  = 0.0
    MVUD9                 : float  = 0.0
    MVUD10                : float  = 0.0
    MVUD11                : float  = 0.0
    MVUD12                : float  = 0.0
    MVUD13                : float  = 0.0
    MVUD14                : float  = 0.0
    MVUD15                : float  = 0.0
    MVUD16                : float  = 0.0

    def to_cs(self) -> ArbinCTI.StartResumeEx:    
        instance = ArbinCTI.StartResumeEx()     
        self._set_basic_fields(instance)
        self._set_tc_fields(instance)
        self._set_mv_fields(instance)
        return instance

    def _set_basic_fields(self, instance):
        instance.channelIndex        = CSConv.to_uint(self.channelIndex)
        instance.TestID              = CSConv.to_int(self.TestID)
        instance.TestNames           = CSConv.to_string(self.TestNames)
        instance.Schedules           = CSConv.to_string(self.Schedules)
        instance.nSelectSteps        = CSConv.to_uint(self.nSelectSteps)
        instance.Cycle               = CSConv.to_uint(self.Cycle)
        instance.TestTime            = CSConv.to_double(self.TestTime)
        instance.StepTime            = CSConv.to_double(self.StepTime)
        instance.CCapacity           = CSConv.to_double(self.CCapacity)
        instance.DCapacity           = CSConv.to_double(self.DCapacity)
        instance.CEnergy             = CSConv.to_double(self.CEnergy)
        instance.DEnergy             = CSConv.to_double(self.DEnergy)
        instance.ChargeCapacityTime  = CSConv.to_double(self.ChargeCapacityTime)
        instance.DischargeCapacityTime = CSConv.to_double(self.DischargeCapacityTime)

    def _set_tc_fields(self, instance):
        instance.TC_Time1            = CSConv.to_double(self.TC_Time1)
        instance.TC_Time2            = CSConv.to_double(self.TC_Time2)
        instance.TC_Time3            = CSConv.to_double(self.TC_Time3)
        instance.TC_Time4            = CSConv.to_double(self.TC_Time4)
        instance.TC_CCapacity1       = CSConv.to_double(self.TC_CCapacity1)
        instance.TC_CCapacity2       = CSConv.to_double(self.TC_CCapacity2)
        instance.TC_DCapacity1       = CSConv.to_double(self.TC_DCapacity1)
        instance.TC_DCapacity2       = CSConv.to_double(self.TC_DCapacity2)
        instance.TC_CEnergy1         = CSConv.to_double(self.TC_CEnergy1)
        instance.TC_CEnergy2         = CSConv.to_double(self.TC_CEnergy2)
        instance.TC_DEnergy1         = CSConv.to_double(self.TC_DEnergy1)
        instance.TC_DEnergy2         = CSConv.to_double(self.TC_DEnergy2)

    def _set_mv_fields(self, instance):
        instance.MV_Counter1         = CSConv.to_float(self.MV_Counter1)
        instance.MV_Counter2         = CSConv.to_float(self.MV_Counter2)
        instance.MV_Counter3         = CSConv.to_float(self.MV_Counter3)
        instance.MV_Counter4         = CSConv.to_float(self.MV_Counter4)
        instance.MV_Counter5         = CSConv.to_float(self.MV_Counter5)
        instance.MV_Counter6         = CSConv.to_float(self.MV_Counter6)
        instance.MV_Counter7         = CSConv.to_float(self.MV_Counter7)
        instance.MV_Counter8         = CSConv.to_float(self.MV_Counter8)
        instance.MVUD1               = CSConv.to_float(self.MVUD1)
        instance.MVUD2               = CSConv.to_float(self.MVUD2)
        instance.MVUD3               = CSConv.to_float(self.MVUD3)
        instance.MVUD4               = CSConv.to_float(self.MVUD4)
        instance.MVUD5               = CSConv.to_float(self.MVUD5)
        instance.MVUD6               = CSConv.to_float(self.MVUD6)
        instance.MVUD7               = CSConv.to_float(self.MVUD7)
        instance.MVUD8               = CSConv.to_float(self.MVUD8)
        instance.MVUD9               = CSConv.to_float(self.MVUD9)
        instance.MVUD10              = CSConv.to_float(self.MVUD10)
        instance.MVUD11              = CSConv.to_float(self.MVUD11)
        instance.MVUD12              = CSConv.to_float(self.MVUD12)
        instance.MVUD13              = CSConv.to_float(self.MVUD13)
        instance.MVUD14              = CSConv.to_float(self.MVUD14)
        instance.MVUD15              = CSConv.to_float(self.MVUD15)
        instance.MVUD16              = CSConv.to_float(self.MVUD16)

@dataclass
class MetaVariableInfo:
    """
    Python wrapper of 'ArbinCTI.Core.ArbinCommandGetMetaVariablesFeed.MetaVariableInfo'
    Attributes:
        m_Channel:      IV channel global index
        m_MV_MetaCode:  AUX virtual index
        m_MV_DataType:  TE_DATA_TYPE
    """
    channel_index : int          = 0
    mv_meta_code  : int          = 52
    mv_data_type  : TE_DATA_TYPE = 1

    def to_cs(self) -> ArbinCTI.ArbinCommandGetMetaVariablesFeed.MetaVariableInfo:           
        instance               = ArbinCTI.ArbinCommandGetMetaVariablesFeed.MetaVariableInfo()
        instance.m_Channel     = CSConv.to_ushort(self.channel_index)
        instance.m_MV_MetaCode = CSConv.to_ushort(self.mv_meta_code)
        instance.m_MV_DataType = ArbinCTI.TE_DATA_TYPE(self.mv_data_type.value)
        return instance

class MetaVariableInfoEx(DictReprBase):
    """
    Python wrapper of 'ArbinCTI.Core.MetaVariableInfoEx'.
    Initialize with a C# MetaVariableInfoEx object or keyword arguments (channel_index, mv_meta_code, mv_data_type, data_type).
    """
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], ArbinCTI.MetaVariableInfoEx):
            self.channel_index = int(args[0].m_ChannelIndexInGlobal)
            self.mv_meta_code  = int(args[0].m_MV_MetaCode)
            self.mv_data_type  = float(args[0].m_fMV_Value)
            self.data_type     = TE_DATA_TYPE(int(args[0].DataType))
            self.error         = args[0].Error

        else:
            self.channel_index = kwargs.get("channel_index", 0)
            self.mv_meta_code  = kwargs.get("mv_meta_code", 52)
            self.mv_data_type  = kwargs.get("mv_data_type", 0.0)
            self.data_type     = kwargs.get("data_type", TE_DATA_TYPE.MP_DATA_TYPE_MetaValue)
            self.error         = b"\x00"

            if not isinstance(self.channel_index, int):
                raise TypeError("channel_index must be an int")
            if not isinstance(self.mv_meta_code, int):
                raise TypeError("mv_meta_code must be an int")
            if not isinstance(self.mv_data_type, float):
                raise TypeError("mv_data_type must be a float")
            if not isinstance(self.data_type, TE_DATA_TYPE):
                raise TypeError("data_type must be an instance of TE_DATA_TYPE")

    def to_cs(self) -> ArbinCTI.MetaVariableInfoEx:                 
        instance = ArbinCTI.MetaVariableInfoEx()
        instance.m_ChannelIndexInGlobal = CSConv.to_ushort(self.channel_index)
        instance.m_MV_MetaCode          = CSConv.to_ushort(self.mv_meta_code)
        instance.m_fMV_Value            = CSConv.to_float(self.mv_data_type)
        instance.DataType               = ArbinCTI.TE_DATA_TYPE(self.data_type.value)
        instance.Error                  = CSConv.to_byte(self.error)
        return instance

class TimeSensitiveSetMV(DictReprBase):
    """
    Python wrapper of 'ArbinCTI.Core.TimeSensitiveSetMV'. 
    Initialize with C# TimeSensitiveSetMV object or keyword arguments (mvud, value).
    """
    class EMVUD(SafeIntEnumBase):
        MVUD1 = 52
        MVUD2 = 53
        MVUD3 = 54
        MVUD4 = 55
        MVUD5 = 105
        MVUD6 = 106
        MVUD7 = 107
        MVUD8 = 108
        MVUD9 = 109
        MVUD10 = 110
        MVUD11 = 111
        MVUD12 = 112
        MVUD13 = 113
        MVUD14 = 114
        MVUD15 = 115

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], ArbinCTI.TimeSensitiveSetMV):                                                         
            self.mvud  = TimeSensitiveSetMV.EMVUD(int(args[0].MVUD))
            self.value = float(args[0].Value)
        else:
            self.mvud  = kwargs.get("mvud", TimeSensitiveSetMV.EMVUD.MVUD1)
            self.value = kwargs.get("value", 0.0)
            if not isinstance(self.mvud, TimeSensitiveSetMV.EMVUD):
                raise TypeError("mvud must be an instance of TimeSensitiveSetMV.EMVUD")
            if not isinstance(self.value, (float, int)):
                raise TypeError("value must be a float or int")


    def to_cs(self) -> ArbinCTI.TimeSensitiveSetMV:                          
        instance        = ArbinCTI.TimeSensitiveSetMV()                    
        instance.MVUD   = ArbinCTI.TimeSensitiveSetMV.EMVUD(self.mvud.value) 
        instance.Value  = CSConv.to_float(self.value)
        return instance
    
@dataclass
class TimeSensitiveSetMVArgs:
    """
    Python wrapper of 'ArbinCTI.Core.TimeSensitiveSetMVArgs'

    Attributes:
        timeout : float
        channels: list[TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel]
    """
    timeout : float = 1.0
    channels: list  = field(default_factory=list)

    @dataclass
    class TimeSensitiveSetMVChannel:
        """
        Python wrapper of 'ArbinCTI.Core.TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel'

        Attributes:
            global_index : global index of IV channel
            mv_list      : list of TimeSensitiveSetMVArgs.TimesensitiveSetMV objects
            log          : log data to database if set.
        
        Raises:
            ValueError: If invalid number or types of arguments
        """
        global_index : int
        mv_list      : list = field(default_factory=list)
        log          : bool = True

        def to_cs(self) -> ArbinCTI.TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel: 
            if not all(isinstance(obj, TimeSensitiveSetMV) for obj in self.mv_list):
                raise ValueError("All items in 'mv_list' must be of type TimeSensitiveSetMV")

            instance = ArbinCTI.TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel( 
                CSConv.to_int(self.global_index),
                CSConv.to_list(self.mv_list),
                CSConv.to_bool(self.log)
            )     
            return instance
        
    def to_cs(self) -> ArbinCTI.TimeSensitiveSetMVArgs:
        if not all(isinstance(obj, TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel) for obj in self.channels):
            raise ValueError("All items in 'channels' must be of type TimeSensitiveSetMVChannel")
        
        instance         = ArbinCTI.TimeSensitiveSetMVArgs()
        instance.Timeout = CSConv.to_float(self.timeout)
        try:
            [instance.Channels.Add(obj.to_cs()) for obj in self.channels]
        except Exception as e:
            raise ValueError(f"Error converting TimeSensitiveSetMVChannel: {str(e)}")
        return instance    

class CMetavariableDataCodeApply:
    """
    Python wrapper of 'ArbinCTI.Core.CMetavariableDataCodeApply'
    """
    class EReadWriteMode(SafeIntEnumBase):
        Read = 0
        WriteAndRead = 1

    def __init__(self, global_index: int, mv_value_type: TE_DATA_TYPE = TE_DATA_TYPE.MP_DATA_TYPE_MetaValue, mv_meta_code: int = (0x10000)-1, mode: EReadWriteMode = EReadWriteMode.Read):
        self.global_index  = global_index
        self.mv_value_type = mv_value_type
        self.mv_meta_code  = mv_meta_code
        self.mode          = mode

    def to_cs(self) -> ArbinCTI.CMetavariableDataCodeApply:  
        instance = ArbinCTI.CMetavariableDataCodeApply()            
        instance.m_GlobalIndex  = CSConv.to_ushort(self.global_index)
        instance.m_MV_ValueType = ArbinCTI.TE_DATA_TYPE(self.mv_value_type.value) 
        instance.m_MV_MetaCode  = CSConv.to_ushort(self.mv_meta_code)
        instance.ReadWriteMode  = ArbinCTI.EReadWriteMode(self.mode.value)      
        return instance

@dataclass
class TestObjectSetting:
    """Python wrapper of 'ArbinCTI.Core.Common.Start.TestObjectSetting'"""
    mass                     : float = 0.0
    specific_capacity        : float = 0.0
    nominal_capacity         : float = 0.0
    nominal_ir               : float = 0.0
    nominal_voltage          : float = 0.0
    nominal_capacitor        : float = 0.0
    max_current_charge       : float = 0.0
    min_voltage_charge       : float = 0.0
    max_voltage_charge       : float = 0.0
    is_auto_calc_n_capacity  : bool  = False

    def to_cs(self) -> ArbinCTI.Common.Start.TestObjectSetting:
        instance = ArbinCTI.Common.Start.TestObjectSetting()
        instance.Mass                    = CSConv.to_float(self.mass)
        instance.SpecificCapacity        = CSConv.to_double(self.specific_capacity)
        instance.NorminalCapacity        = CSConv.to_double(self.nominal_capacity)
        instance.NorminalIR              = CSConv.to_double(self.nominal_ir)
        instance.NorminalVoltage         = CSConv.to_double(self.nominal_voltage)
        instance.NorminalCapacitor       = CSConv.to_double(self.nominal_capacitor)
        instance.MaxCurrentCharge        = CSConv.to_double(self.max_current_charge)
        instance.MinVoltageCharge        = CSConv.to_double(self.min_voltage_charge)
        instance.MaxVoltageCharge        = CSConv.to_double(self.max_voltage_charge)
        instance.IsAutoCalcNCapacity     = CSConv.to_bool(self.is_auto_calc_n_capacity)
        return instance
    
@dataclass
class StartChannelInfo:
    """Python wrapper of 'ArbinCTI.Core.Common.Start.StartChannelInfo'"""
    channel_index : int               = -1
    test_name     : str               = ""
    schedule_name : str               = ""
    barcode       : str               = ""
    test_object   : TestObjectSetting = field(default_factory=TestObjectSetting)

    def to_cs(self) -> ArbinCTI.Common.Start.StartChannelInfo:
        if not isinstance(self.test_object, TestObjectSetting):
            raise TypeError("'test_object' must be of type TestObjectSetting")
        
        instance = ArbinCTI.Common.Start.StartChannelInfo()
        instance.ChannelIndex = CSConv.to_int(self.channel_index)
        instance.TestName     = CSConv.to_string(self.test_name)
        instance.ScheduleName = CSConv.to_string(self.schedule_name)
        instance.Barcode      = CSConv.to_string(self.barcode)
        instance.TestObject   = self.test_object.to_cs()
        return instance
    
@dataclass
class StartChannelAdvancedArgs:
    """Python wrapper of 'ArbinCTI.Core.Common.Start.StartChannelAdvancedArgs'"""
    task_id  : int  = 0
    channels : list = field(default_factory=list)

    def to_cs(self) -> ArbinCTI.Common.Start.StartChannelAdvancedArgs:
        if not all(isinstance(obj, StartChannelInfo) for obj in self.channels):
            raise ValueError("All items in 'channels' must be of type StartChannelInfo")
        
        instance = ArbinCTI.Common.Start.StartChannelAdvancedArgs()
        instance.TaskID   = CSConv.to_long(self.task_id)
        instance.Channels = CSConv.to_list(self.channels)
        return instance
    
@dataclass
class GetMappingAuxArgs:
    task_id : int = 0

    def to_cs(self) -> ArbinCTI.Common.GetMappingAux.GetMappingAuxArgs:
        instance = ArbinCTI.Common.GetMappingAux.GetMappingAuxArgs()
        instance.TaskID = CSConv.to_long(self.task_id)
        return instance

@dataclass
class SafetyScope:
    low  : float = 0
    high : float = 0

    def to_cs(self) -> ArbinCTI.Common.ModifySchedule.SafetyScope:
        instance = ArbinCTI.Common.ModifySchedule.SafetyScope()
        instance.Low  = CSConv.to_double(self.low)
        instance.High = CSConv.to_double(self.high)
        return instance

@dataclass
class AuxChannelRequirementBase:
    enable    : bool = False
    aux_count : int  = 0
    
    def to_cs(self) -> ArbinCTI.Common.ModifySchedule.AuxChannelRequirementBase:
        instance = ArbinCTI.Common.ModifySchedule.AuxChannelRequirementBase()
        instance.Enable    = CSConv.to_bool(self.enable)
        instance.AuxCount  = CSConv.to_uint(self.aux_count)
        return instance

@dataclass
class AuxChannelRequirement(AuxChannelRequirementBase):
    safety_scope : SafetyScope = field(default_factory=SafetyScope)

    def to_cs(self) -> ArbinCTI.Common.ModifySchedule.AuxChannelRequirement:
        instance = ArbinCTI.Common.ModifySchedule.AuxChannelRequirement()
        instance.Enable      = CSConv.to_bool(self.enable)
        instance.AuxCount    = CSConv.to_uint(self.aux_count)
        instance.SafetyScope = self.safety_scope.to_cs()
        return instance

@dataclass
class AuxSafetyRequirement(AuxChannelRequirementBase):
    temperature_safety_scope : SafetyScope = field(default_factory=SafetyScope)
    current_safety_scope     : SafetyScope = field(default_factory=SafetyScope)
    voltage_safety_scope     : SafetyScope = field(default_factory=SafetyScope)

    def to_cs(self) -> ArbinCTI.Common.ModifySchedule.AuxSafelyRequirement:
        instance = ArbinCTI.Common.ModifySchedule.AuxSafelyRequirement()
        instance.Enable                  = CSConv.to_bool(self.enable)
        instance.AuxCount                = CSConv.to_uint(self.aux_count)
        instance.TemperatureSafetyScope  = self.temperature_safety_scope.to_cs()
        instance.CurrentSafetyScope      = self.current_safety_scope.to_cs()
        instance.VoltageSafetyScope      = self.voltage_safety_scope.to_cs()
        return instance

@dataclass
class ScheduleModifyInfo:
    schedule_name                    : str                       = ""
    aux_do_requirement               : AuxChannelRequirementBase = field(default_factory=AuxChannelRequirementBase)
    aux_ao_requirement               : AuxChannelRequirementBase = field(default_factory=AuxChannelRequirementBase)
    canbms_requirement               : AuxChannelRequirementBase = field(default_factory=AuxChannelRequirementBase)
    smb_requirement                  : AuxChannelRequirementBase = field(default_factory=AuxChannelRequirementBase)
    aux_voltage_requirement          : AuxChannelRequirement     = field(default_factory=AuxChannelRequirement)
    aux_temperature_requirement      : AuxChannelRequirement     = field(default_factory=AuxChannelRequirement)
    aux_pressure_requirement         : AuxChannelRequirement     = field(default_factory=AuxChannelRequirement)
    aux_di_requirement               : AuxChannelRequirement     = field(default_factory=AuxChannelRequirement)
    aux_external_charge_requirement  : AuxChannelRequirement     = field(default_factory=AuxChannelRequirement)
    aux_humidity_requirement         : AuxChannelRequirement     = field(default_factory=AuxChannelRequirement)
    aux_safety_requirement           : AuxSafetyRequirement      = field(default_factory=AuxSafetyRequirement)

    def to_cs(self) -> ArbinCTI.Common.ModifySchedule.ScheduleModifyInfo:
        instance = ArbinCTI.Common.ModifySchedule.ScheduleModifyInfo()
        instance.ScheduleName                   = CSConv.to_string(self.schedule_name)
        instance.AuxDORequirement               = self.aux_do_requirement.to_cs()
        instance.AuxAORequirement               = self.aux_ao_requirement.to_cs()
        instance.CANBMSRequirement              = self.canbms_requirement.to_cs()
        instance.SMBRequirement                 = self.smb_requirement.to_cs()
        instance.AuxVoltageRequirement          = self.aux_voltage_requirement.to_cs()
        instance.AuxTemperatureRequirement      = self.aux_temperature_requirement.to_cs()
        instance.AuxPressureRequirement         = self.aux_pressure_requirement.to_cs()
        instance.AuxDIRequirement               = self.aux_di_requirement.to_cs()
        instance.AuxExternalChargeRequirement   = self.aux_external_charge_requirement.to_cs()
        instance.AuxHumidityRequirement         = self.aux_humidity_requirement.to_cs()
        instance.AuxSafelyRequirement           = self.aux_safety_requirement.to_cs()
        return instance

@dataclass
class ModifyScheduleArgs:
    task_id: int = 0
    schedule_modify_info: list = field(default_factory=list)

    def to_cs(self) -> ArbinCTI.Common.ModifySchedule.ModifyScheduleArgs:
        if not all(isinstance(obj, ScheduleModifyInfo) for obj in self.schedule_modify_info):
            raise ValueError("All items in 'schedule_modify_info' must be of type ScheduleModifyInfo")
        
        instance = ArbinCTI.Common.ModifySchedule.ModifyScheduleArgs()
        instance.TaskID = CSConv.to_long(self.task_id)
        instance.ScheduleModifyInfo = CSConv.to_list(self.schedule_modify_info)
        return instance