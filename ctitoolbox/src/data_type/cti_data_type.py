from dataclasses import dataclass, field

import ArbinCTI.Core as ArbinCTI                # type: ignore
from System.Collections.Generic import List     # type: ignore

from ctitoolbox.src.data_type.cs_data_type import CSConv

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
        instance.Error    = CSConv.to_byte(self.error)
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
            try:
                self._convert_time_sensitive_mvs()
            except Exception as e:
                raise ValueError(f"Error converting TimeSensitiveSetMVChannel: {str(e)}")

            instance = ArbinCTI.TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel( 
                CSConv.to_int(self.global_index),
                self.mv_list,
                CSConv.to_bool(self.log)
            )     
            return instance
        
        def _convert_time_sensitive_mvs(self):
            list_instance = List[ArbinCTI.TimeSensitiveSetMV]()
            try:
                [list_instance.Add(obj.to_cs()) for obj in self.mv_list]
            except Exception as e:
                raise ValueError(f"Error converting TimeSensitiveSetMV: {str(e)}")
            finally:
                self.mv_list = list_instance
        
    def to_cs(self) -> ArbinCTI.TimeSensitiveSetMVArgs:
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
