from dataclasses import dataclass, field

import ArbinCTI.Core as ArbinCTI                # type: ignore
from System.Collections.Generic import List     # type: ignore

from ctitoolbox.src.data_type.cs_data_type import CSTypeConverter

from ctitoolbox.src.base import (
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
- TimeSensitiveSetMV
- TimeSensitiveSetMVArgs
- CMetavariableDataCodeApply
- TestObjectSetting
- StartChannelInfo
- StartChannelAdvancedArgs
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
        instance.channelIndex        = CSTypeConverter.to_uint(self.channelIndex)
        instance.TestID              = CSTypeConverter.to_int(self.TestID)
        instance.TestNames           = CSTypeConverter.to_string(self.TestNames)
        instance.Schedules           = CSTypeConverter.to_string(self.Schedules)
        instance.nSelectSteps        = CSTypeConverter.to_uint(self.nSelectSteps)
        instance.Cycle               = CSTypeConverter.to_uint(self.Cycle)
        instance.TestTime            = CSTypeConverter.to_double(self.TestTime)
        instance.StepTime            = CSTypeConverter.to_double(self.StepTime)
        instance.CCapacity           = CSTypeConverter.to_double(self.CCapacity)
        instance.DCapacity           = CSTypeConverter.to_double(self.DCapacity)
        instance.CEnergy             = CSTypeConverter.to_double(self.CEnergy)
        instance.DEnergy             = CSTypeConverter.to_double(self.DEnergy)
        instance.ChargeCapacityTime  = CSTypeConverter.to_double(self.ChargeCapacityTime)
        instance.DischargeCapacityTime = CSTypeConverter.to_double(self.DischargeCapacityTime)

    def _set_tc_fields(self, instance):
        instance.TC_Time1            = CSTypeConverter.to_double(self.TC_Time1)
        instance.TC_Time2            = CSTypeConverter.to_double(self.TC_Time2)
        instance.TC_Time3            = CSTypeConverter.to_double(self.TC_Time3)
        instance.TC_Time4            = CSTypeConverter.to_double(self.TC_Time4)
        instance.TC_CCapacity1       = CSTypeConverter.to_double(self.TC_CCapacity1)
        instance.TC_CCapacity2       = CSTypeConverter.to_double(self.TC_CCapacity2)
        instance.TC_DCapacity1       = CSTypeConverter.to_double(self.TC_DCapacity1)
        instance.TC_DCapacity2       = CSTypeConverter.to_double(self.TC_DCapacity2)
        instance.TC_CEnergy1         = CSTypeConverter.to_double(self.TC_CEnergy1)
        instance.TC_CEnergy2         = CSTypeConverter.to_double(self.TC_CEnergy2)
        instance.TC_DEnergy1         = CSTypeConverter.to_double(self.TC_DEnergy1)
        instance.TC_DEnergy2         = CSTypeConverter.to_double(self.TC_DEnergy2)

    def _set_mv_fields(self, instance):
        instance.MV_Counter1         = CSTypeConverter.to_float(self.MV_Counter1)
        instance.MV_Counter2         = CSTypeConverter.to_float(self.MV_Counter2)
        instance.MV_Counter3         = CSTypeConverter.to_float(self.MV_Counter3)
        instance.MV_Counter4         = CSTypeConverter.to_float(self.MV_Counter4)
        instance.MV_Counter5         = CSTypeConverter.to_float(self.MV_Counter5)
        instance.MV_Counter6         = CSTypeConverter.to_float(self.MV_Counter6)
        instance.MV_Counter7         = CSTypeConverter.to_float(self.MV_Counter7)
        instance.MV_Counter8         = CSTypeConverter.to_float(self.MV_Counter8)
        instance.MVUD1               = CSTypeConverter.to_float(self.MVUD1)
        instance.MVUD2               = CSTypeConverter.to_float(self.MVUD2)
        instance.MVUD3               = CSTypeConverter.to_float(self.MVUD3)
        instance.MVUD4               = CSTypeConverter.to_float(self.MVUD4)
        instance.MVUD5               = CSTypeConverter.to_float(self.MVUD5)
        instance.MVUD6               = CSTypeConverter.to_float(self.MVUD6)
        instance.MVUD7               = CSTypeConverter.to_float(self.MVUD7)
        instance.MVUD8               = CSTypeConverter.to_float(self.MVUD8)
        instance.MVUD9               = CSTypeConverter.to_float(self.MVUD9)
        instance.MVUD10              = CSTypeConverter.to_float(self.MVUD10)
        instance.MVUD11              = CSTypeConverter.to_float(self.MVUD11)
        instance.MVUD12              = CSTypeConverter.to_float(self.MVUD12)
        instance.MVUD13              = CSTypeConverter.to_float(self.MVUD13)
        instance.MVUD14              = CSTypeConverter.to_float(self.MVUD14)
        instance.MVUD15              = CSTypeConverter.to_float(self.MVUD15)
        instance.MVUD16              = CSTypeConverter.to_float(self.MVUD16)

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
        instance.m_Channel     = CSTypeConverter.to_ushort(self.channel_index)
        instance.m_MV_MetaCode = CSTypeConverter.to_ushort(self.mv_meta_code)
        instance.m_MV_DataType = ArbinCTI.TE_DATA_TYPE(self.mv_data_type.value)
        return instance

@dataclass
class MetaVariableInfoEx:
    """
    Python wrapper of 'ArbinCTI.Core.ArbinCommandUpdateMetaVariableFeed.UpdateMV_MetaVariableInfoEX'
    """
    data_type : TE_DATA_TYPE = TE_DATA_TYPE.MP_DATA_TYPE_MetaValue
    error     : bytes        = 0

    def to_cs(self) -> ArbinCTI.MetaVariableInfoEx:                 
        instance          = ArbinCTI.MetaVariableInfoEx()                 
        instance.DataType = ArbinCTI.TE_DATA_TYPE(self.data_type.value)
        instance.Error    = CSTypeConverter.to_byte(self.error)
        return instance

class TimeSensitiveSetMV(DictReprBase):
    """
    Python wrapper of 'ArbinCTI.Core.TimeSensitiveSetMV'

    Args:
        *args: Length variable argument list that accepts either:
            - Two arguments (mvud: Enum_MvUd, value: float) to initialize a new instance
            - A single argument of type ArbinCTI.Core.TimeSensitiveSetMV to convert to Python wrapper object
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

    def __init__(self, *args):
        if len(args) == 1:                                                    
            assert(isinstance(args[0], ArbinCTI.TimeSensitiveSetMV))            
            self.mvud  = TimeSensitiveSetMV.EMVUD(int(args[0].MVUD))
            self.value = float(args[0].Value)
        elif len(args) == 2:
            assert (isinstance(args[0], TimeSensitiveSetMV.EMVUD))
            assert (isinstance(args[1], (int, float)))
            self.mvud  = args[0]
            self.value = args[1]
        else:
            raise ValueError("Invalid arguments for TimeSensitiveSetMV")

    def to_cs(self) -> ArbinCTI.TimeSensitiveSetMV:                          
        instance        = ArbinCTI.TimeSensitiveSetMV()                    
        instance.MVUD   = ArbinCTI.TimeSensitiveSetMV.EMVUD(self.mvud.value) 
        instance.Value  = CSTypeConverter.to_float(self.value)
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
                CSTypeConverter.to_int(self.global_index),
                CSTypeConverter.to_list(self.mv_list),
                CSTypeConverter.to_bool(self.log)
            )     
            return instance
        
    def to_cs(self) -> ArbinCTI.TimeSensitiveSetMVArgs:
        if not all(isinstance(obj, TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel) for obj in self.channels):
            raise ValueError("All items in 'channels' must be of type TimeSensitiveSetMVChannel")
        
        instance         = ArbinCTI.TimeSensitiveSetMVArgs()
        instance.Timeout = CSTypeConverter.to_float(self.timeout)
        instance.Channels = CSTypeConverter.to_list(self.channels)
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
        instance.m_GlobalIndex  = CSTypeConverter.to_ushort(self.global_index)
        instance.m_MV_ValueType = ArbinCTI.TE_DATA_TYPE(self.mv_value_type.value) 
        instance.m_MV_MetaCode  = CSTypeConverter.to_ushort(self.mv_meta_code)
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
        instance.Mass                    = CSTypeConverter.to_float(self.mass)
        instance.SpecificCapacity        = CSTypeConverter.to_double(self.specific_capacity)
        instance.NorminalCapacity        = CSTypeConverter.to_double(self.nominal_capacity)
        instance.NorminalIR              = CSTypeConverter.to_double(self.nominal_ir)
        instance.NorminalVoltage         = CSTypeConverter.to_double(self.nominal_voltage)
        instance.NorminalCapacitor       = CSTypeConverter.to_double(self.nominal_capacitor)
        instance.MaxCurrentCharge        = CSTypeConverter.to_double(self.max_current_charge)
        instance.MinVoltageCharge        = CSTypeConverter.to_double(self.min_voltage_charge)
        instance.MaxVoltageCharge        = CSTypeConverter.to_double(self.max_voltage_charge)
        instance.IsAutoCalcNCapacity     = CSTypeConverter.to_bool(self.is_auto_calc_n_capacity)
        return instance
    
@dataclass
class StartChannelInfo:
    """Python wrapper of 'ArbinCTI.Core.Common.Start.StartChannelInfo'"""
    channel_index : int = -1
    test_name : str = ""
    schedule_name : str = ""
    barcode : str = ""
    test_object: TestObjectSetting = None

    def to_cs(self) -> ArbinCTI.Common.Start.StartChannelInfo:
        if not isinstance(self.test_object, TestObjectSetting):
            raise TypeError("'test_object' must be of type TestObjectSetting")
        
        instance = ArbinCTI.Common.Start.StartChannelInfo()
        instance.ChannelIndex = CSTypeConverter.to_int(self.channel_index)
        instance.TestName     = CSTypeConverter.to_string(self.test_name)
        instance.ScheduleName = CSTypeConverter.to_string(self.schedule_name)
        instance.Barcode      = CSTypeConverter.to_string(self.barcode)
        instance.TestObject   = self.test_object.to_cs()
        return instance
    
@dataclass
class StartChannelAdvancedArgs:
    """Python wrapper of 'ArbinCTI.Core.Common.Start.StartChannelAdvancedArgs'"""
    task_id : int = 0
    channels : list = field(default_factory=list)

    def to_cs(self) -> ArbinCTI.Common.Start.StartChannelAdvancedArgs:
        if not all(isinstance(obj, StartChannelInfo) for obj in self.channels):
            raise ValueError("All items in 'channels' must be of type StartChannelInfo")
        
        instance = ArbinCTI.Common.Start.StartChannelAdvancedArgs()
        instance.TaskID   = CSTypeConverter.to_long(self.task_id)
        instance.Channels = CSTypeConverter.to_list(self.channels)
        return instance
    
@dataclass
class GetMappingAuxArgs:
    task_id : int = 0

    def to_cs(self) -> ArbinCTI.Common.GetMappingAux.GetMappingAuxArgs:
        instance = ArbinCTI.Common.GetMappingAux.GetMappingAuxArgs()
        instance.TaskID = CSTypeConverter.to_long(self.task_id)
        return instance