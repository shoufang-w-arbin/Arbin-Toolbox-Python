__doc__ = """
[Test Management Arguments]
- UpLoadFileArgs
- BrowseFileListArgs
- ModifyScheduleArgs
- AssignFileArgs
- UpdateMetaVariablesArgs
- AssignBarcodeInfoArgs
- TimeSensitiveSetMVArgs

[Subsidary Classes]
- SafetyScope
- AuxChannelRequirementBase
- AuxChannelRequirement
- AuxSafetyRequirement
- ScheduleModifyInfo
"""

from dataclasses import (
    dataclass,
    field,
)

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from arbinclienttools.src.common.cs_conv import CSConv
from arbinclienttools.src.enumeration import (
    EAIFileType,
    ETimeSensitiveMVUD,
)
from arbinclienttools.src.argument.common import (
    AIMetaVariableInfo,
    BarcodeInfo,
)

@dataclass
class SafetyScope:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.SafetyScope'. 
    """
    low  : float = 0
    high : float = 0

    def to_cs(self) -> ArbinDataModel.TestManagement.SafetyScope:
        cs_instance = ArbinDataModel.TestManagement.SafetyScope()
        cs_instance.Low  = CSConv.to_double(self.low)
        cs_instance.High = CSConv.to_double(self.high)
        return cs_instance

@dataclass
class AuxChannelRequirementBase:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.AuxChannelRequirementBase'. 
    """
    enable    : bool = False
    aux_count : int  = 0
    
    def to_cs(self) -> ArbinDataModel.TestManagement.AuxChannelRequirementBase:
        cs_instance = ArbinDataModel.TestManagement.AuxChannelRequirementBase()
        cs_instance.Enable    = CSConv.to_bool(self.enable)
        cs_instance.AuxCount  = CSConv.to_uint(self.aux_count)
        return cs_instance

@dataclass
class AuxChannelRequirement(AuxChannelRequirementBase):
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.AuxChannelRequirement'. 
    """
    safety_scope : SafetyScope = field(default_factory=SafetyScope)

    def to_cs(self) -> ArbinDataModel.TestManagement.AuxChannelRequirement:
        cs_instance = ArbinDataModel.TestManagement.AuxChannelRequirement()
        cs_instance.Enable      = CSConv.to_bool(self.enable)
        cs_instance.AuxCount    = CSConv.to_uint(self.aux_count)
        cs_instance.SafetyScope = self.safety_scope.to_cs()
        return cs_instance

@dataclass
class AuxSafetyRequirement(AuxChannelRequirementBase):
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.AuxSafetyRequirement'. 
    """
    temperature_safety_scope : SafetyScope = field(default_factory=SafetyScope)
    current_safety_scope     : SafetyScope = field(default_factory=SafetyScope)
    voltage_safety_scope     : SafetyScope = field(default_factory=SafetyScope)

    def to_cs(self) -> ArbinDataModel.TestManagement.AuxSafelyRequirement:
        cs_instance =ArbinDataModel.TestManagement.AuxSafelyRequirement()
        cs_instance.Enable                  = CSConv.to_bool(self.enable)
        cs_instance.AuxCount                = CSConv.to_uint(self.aux_count)
        cs_instance.TemperatureSafetyScope  = self.temperature_safety_scope.to_cs()
        cs_instance.CurrentSafetyScope      = self.current_safety_scope.to_cs()
        cs_instance.VoltageSafetyScope      = self.voltage_safety_scope.to_cs()
        return cs_instance

@dataclass
class ScheduleModifyInfo:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.ScheduleModifyInfo'. 
    """
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

    def to_cs(self) -> ArbinDataModel.TestManagement.ScheduleModifyInfo:
        cs_instance = ArbinDataModel.TestManagement.ScheduleModifyInfo()
        cs_instance.ScheduleName                   = CSConv.to_string(self.schedule_name)
        cs_instance.AuxDORequirement               = self.aux_do_requirement.to_cs()
        cs_instance.AuxAORequirement               = self.aux_ao_requirement.to_cs()
        cs_instance.CANBMSRequirement              = self.canbms_requirement.to_cs()
        cs_instance.SMBRequirement                 = self.smb_requirement.to_cs()
        cs_instance.AuxVoltageRequirement          = self.aux_voltage_requirement.to_cs()
        cs_instance.AuxTemperatureRequirement      = self.aux_temperature_requirement.to_cs()
        cs_instance.AuxPressureRequirement         = self.aux_pressure_requirement.to_cs()
        cs_instance.AuxDIRequirement               = self.aux_di_requirement.to_cs()
        cs_instance.AuxExternalChargeRequirement   = self.aux_external_charge_requirement.to_cs()
        cs_instance.AuxHumidityRequirement         = self.aux_humidity_requirement.to_cs()
        cs_instance.AuxSafelyRequirement           = self.aux_safety_requirement.to_cs()
        return cs_instance

@dataclass
class UploadFileArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.UpLoadFileArgs'. 
    """
    remote_relative_file_name: str      = ""
    local_full_file_name:      str      = ""
    is_overwrite:              bool     = True
    callback_func:             callable = lambda x: None

    def to_cs(self) -> ArbinDataModel.TestManagement.UploadFileArgs:
        if not callable(self.callback_func):
            raise TypeError("'callback_func' must be callable")
        if self.callback_func.__code__.co_argcount != 1:
            raise ValueError("'callback_func' must accept one argument, which will be an instance of 'Arbin.Library.DataModel.TestManagement.UploadFileResult'")
        
        cs_instance = ArbinDataModel.TestManagement.UploadFileArgs()
        cs_instance.RemoteRelativeFileName = CSConv.to_string(self.remote_relative_file_name)
        cs_instance.LocalFullFileName      = CSConv.to_string(self.local_full_file_name)
        cs_instance.IsOverride             = CSConv.to_bool(self.is_overwrite)
        cs_instance.OnUploadFileResult     = ArbinDataModel.TestManagement.UploadFileResultEventHandler(self.callback_func)
        return cs_instance

@dataclass
class BrowseFileListArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.BrowseFileListArgs'. 
    """
    sn:         str         = ""
    file_type:  EAIFileType = EAIFileType.Schedule

    def to_cs(self) -> ArbinDataModel.TestManagement.BrowseFileListArgs:
        cs_instance = ArbinDataModel.TestManagement.BrowseFileListArgs()
        cs_instance.SN       = CSConv.to_string(self.sn)
        cs_instance.FileType = ArbinDataModel.EAIFileType(self.file_type.value)
        return cs_instance
    
@dataclass
class ModifyScheduleArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.ModifyScheduleArgs'. 
    """
    schedule_modify_info: list      = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.TestManagement.ModifyScheduleArgs:
        if not all([isinstance(info, ScheduleModifyInfo) for info in self.schedule_modify_info]):
            raise TypeError("'schedule_modify_info' must be a list of 'arbinclienttools.ScheduleModifyInfo'")
        
        cs_instance = ArbinDataModel.TestManagement.ModifyScheduleArgs()
        cs_instance.ScheduleModifyInfos = CSConv.to_list(self.schedule_modify_info)
        return cs_instance

@dataclass
class AssignFileArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.AssignFileArgs'
    """
    sn:         str          = ""
    channel_id: list         = field(default_factory=list)
    file_name:  str          = ""
    file_type:  EAIFileType  = EAIFileType.None_

    def to_cs(self) -> ArbinDataModel.TestManagement.AssignFileArgs:
        cs_instance = ArbinDataModel.TestManagement.AssignFileArgs()
        cs_instance.ChannelIDs  = CSConv.to_list(self.channel_id, CSConv.EDataType.INT)
        cs_instance.FileName    = CSConv.to_string(self.file_name)
        cs_instance.FileType    = ArbinDataModel.EAIFileType(self.file_type.value)
        cs_instance.SN          = CSConv.to_string(self.sn)
        return cs_instance
    
@dataclass
class UpdateMetaVariablesArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.UpdateMetaVariablesArgs'
    """
    sn:                 int  = 0
    meta_variable_info: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.TestManagement.UpdateMetaVariablesArgs:
        if not all([isinstance(info, AIMetaVariableInfo) for info in self.meta_variable_info]):
            raise TypeError("'meta_variable_info' must be a list of 'AIMetaVariableInfo'")
        
        cs_instance = ArbinDataModel.TestManagement.UpdateMetaVariablesArgs()
        cs_instance.MetaVariableInfos = CSConv.to_list(self.meta_variable_info)
        cs_instance.SN = CSConv.to_int(self.sn)
        return cs_instance

@dataclass
class AssignBarcodeInfoArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.AssignBarcodeInfoArgs'
    """
    sn:           str  = field(default="")
    barcode_info: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.TestManagement.AssignBarcodeInfoArgs:
        if not all([isinstance(info, BarcodeInfo) for info in self.barcode_info]):
            raise TypeError("'barcode_info' must be a list of 'arbinclienttools.BarcodeInfo'")
        
        cs_instance = ArbinDataModel.TestManagement.AssignBarcodeInfoArgs()
        cs_instance.SN           = CSConv.to_string(self.sn)
        cs_instance.BarcodeInfos = CSConv.to_list(self.barcode_info)
        return cs_instance
    
@dataclass
class TimeSensitiveSetMV:
    """
    Wrapper class of 'Arbin.Libray.DataModel.TestManagement.TimeSensitiveSetMV'.
    """
    mvud: ETimeSensitiveMVUD = ETimeSensitiveMVUD.MVUD1
    value: float = 0.0

    def to_cs(self) -> ArbinDataModel.TestManagement.TimeSensitiveSetMV:                          
        instance        = ArbinDataModel.TestManagement.TimeSensitiveSetMV()                    
        instance.MVUD   = ArbinDataModel.ETimeSensitiveMVUD(self.mvud.value) 
        instance.Value  = CSConv.to_float(self.value)
        return instance
    
@dataclass
class TimeSensitiveSetMVChannel:
    """
    Wrapper class of 'Arbin.Library.DataModel.TestManagement.TimeSensitiveSetMVChannel'
    """
    channel_id   : int
    mv_list      : list = field(default_factory=list)
    log          : bool = True

    def to_cs(self) -> ArbinDataModel.TestManagement.TimeSensitiveSetMVChannel: 
        if not all(isinstance(obj, TimeSensitiveSetMV) for obj in self.mv_list):
            raise ValueError("All items in 'mv_list' must be of type `arbinclienttools.TimeSensitiveSetMV")

        instance = ArbinDataModel.TestManagement.TimeSensitiveSetMVChannel()
        instance.ChannelID = CSConv.to_int(self.channel_id)
        instance.SetMVList = CSConv.to_list(self.mv_list)
        instance.IsDoLog   = CSConv.to_bool(self.log)
        return instance

@dataclass
class TimeSensitiveSetMVArgs:
    """
    Wrapper class of 'Arbin.Library.DataModel.TestManagement.TimeSensitiveSetMVArgs'
    """
    timeout     : float = 1.0
    channel_list: list  = field(default_factory=list)
    sn          : str   = ""

    def to_cs(self) -> ArbinDataModel.TestManagement.TimeSensitiveSetMVArgs:
        if not all(isinstance(x, TimeSensitiveSetMVChannel) for x in self.channels):
            raise ValueError("All items in 'channels' must be of type arbinclienttools.TimeSensitiveSetMVChannel")
        instance           = ArbinDataModel.TestManagement.TimeSensitiveSetMVArgs()
        instance.Timeout   = CSConv.to_float(self.timeout)
        instance.SN        = CSConv.to_string(self.sn)
        instance.SetMVList = CSConv.to_list(self.channel_list)
        return instance    