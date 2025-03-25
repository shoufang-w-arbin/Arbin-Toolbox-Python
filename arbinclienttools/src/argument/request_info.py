__doc__ = """
[Request Information Arguments]
- GetMonitorDataArgs 
- GetResumeDataArgs 
- GetStartDataArgs
- GetMetaVariableArgs
- GetBarcodeInfoArgs
- GetMappingAuxArgs (not supported yet)
- SubscribeMonitorDataArgs
- SubscribeChannelDataArgs
- SubscribeTestInfoDataArgs
- SubscribeEventDataArgs
- SubscribeDiagnosticEventDataArgs
- SubscribeSPTTEQCELLDataArgs
"""
from dataclasses import (
    dataclass, 
    field,
)

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.cs_conv import CSConv
from arbinclienttools.src.enumeration import (
    EFilterMonitorChannelType,
)
from arbinclienttools.src.argument.common import (
    AIMetaVariableInfo,
    GetBarcodeInfo,
)

@dataclass
class GetMonitorDataArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.RequestInformation.GetMonitorDataArgs'
    """
    sn:         str = ""
    need_type:  int = 7936
    channel_id: int = -1
    filter_monitor_channel_type: EFilterMonitorChannelType = EFilterMonitorChannelType.AllChanneL

    def to_cs(self) -> ArbinDataModel.RequestInformation.GetMonitorDataArgs:
        cs_instance = ArbinDataModel.RequestInformation.GetMonitorDataArgs()
        cs_instance.sn                          = CSConv.to_string(self.sn)
        cs_instance.need_type                   = CSConv.to_int(self.need_type)
        cs_instance.channel_id                  = CSConv.to_int(self.channel_id)
        cs_instance.filter_monitor_channel_type = ArbinDataModel.EFilterMonitorChannelType(self.filter_monitor_channel_type.value)
        return cs_instance
    
@dataclass
class GetResumeDataArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.RequestInformation.GetResumeDataArgs'
    """
    sn:         str  = ""
    channel_id: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.RequestInformation.GetResumeDataArgs:
        cs_instance = ArbinDataModel.RequestInformation.GetResumeDataArgs()
        cs_instance.sn         = CSConv.to_string(self.sn)
        cs_instance.channel_id = CSConv.to_list(self.channel_id, CSConv.EDataType.INT)
        return cs_instance
    
@dataclass
class GetStartDataArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.RequestInformation.GetStartDataArgs'
    """
    sn:         str  = ""
    channel_id: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.RequestInformation.GetStartDataArgs:
        cs_instance = ArbinDataModel.RequestInformation.GetStartDataArgs()
        cs_instance.sn         = CSConv.to_string(self.sn)
        cs_instance.channel_id = CSConv.to_list(self.channel_id, CSConv.EDataType.INT)
        return cs_instance

@dataclass
class GetMetaVariableArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.RequestInformation.GetMetaVariableArgs'
    """
    sn:                 int  = 0
    meta_variable_type: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.RequestInformation.GetMetaVariableArgs:
        if not all([isinstance(info, AIMetaVariableInfo) for info in self.meta_variable_type]):
            raise TypeError("'meta_variable_type' must be a list of 'arbinclienttools.EMetaVariableType'")
        
        cs_instance = ArbinDataModel.RequestInformation.GetMetaVariableArgs()
        cs_instance.SN = CSConv.to_int(self.sn)
        cs_instance.MetaVariableTypes = CSConv.to_list(self.meta_variable_type)
        return cs_instance

@dataclass
class GetBarcodeInfoArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.RequestInformation.GetBarcodeInfoArgs'
    """
    sn:             str  = ""
    barcode_info:   list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.RequestInformation.GetBarcodeInfoArgs:
        if not all([isinstance(info, GetBarcodeInfo) for info in self.barcode_info]):
            raise TypeError("'barcode_info' must be a list of 'arbinclienttools.GetBarcodeInfo'")
        
        cs_instance = ArbinDataModel.RequestInformation.GetBarcodeInfoArgs()
        cs_instance = CSConv.to_string(self.sn)
        cs_instance = CSConv.to_list(self.barcode_info)
        return cs_instance

@dataclass
class GetMappingAuxArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.RequestInformation.GetMappingAuxArgs'
    """
    def to_cs(self) -> ArbinDataModel.RequestInformation.GetMappingAuxArgs:
        return ArbinDataModel.RequestInformation.GetMappingAux()

@dataclass
class SubscribeMonitorDataArgs:
    """
    Wrapper class of 'Arbin.Library.DataModel.RequestInformation.SubscribeMonitorDataArgs'
    """
    def to_cs(self) -> ArbinDataModel.RequestInformation.SubscribeMonitorDataArgs:
        return ArbinDataModel.RequestInformation.SubscribeMonitorData()

@dataclass
class SubscribeChannelDataArgs:
    """
    Wrapper class of 'Arbin.Library.DataModel.RequestInformation.SubscribeChannelDataArgs'
    """
    def to_cs(self) -> ArbinDataModel.RequestInformation.SubscribeChannelDataArgs:
        return ArbinDataModel.RequestInformation.SubscribeChannelData()

@dataclass
class SubscribeTestInfoDataArgs:
    """
    Wrapper class of 'Arbin.Library.DataModel.RequestInformation.SubscribeTestInfoDataArgs'
    """
    def to_cs(self) -> ArbinDataModel.RequestInformation.SubscribeTestInfoDataArgs:
        return ArbinDataModel.RequestInformation.SubscribeTestInfoData()

@dataclass
class SubscribeEventDataArgs:
    """
    Wrapper class of 'Arbin.Library.DataModel.RequestInformation.SubscribeEventDataArgs'
    """
    def to_cs(self) -> ArbinDataModel.RequestInformation.SubscribeEventDataArgs:
        return ArbinDataModel.RequestInformation.SubscribeEventData()

@dataclass
class SubscribeDiagnosticEventDataArgs:
    """
    Wrapper class of 'Arbin.Library.DataModel.RequestInformation.SubscribeDiagnosticEventDataArgs'
    """
    def to_cs(self) -> ArbinDataModel.RequestInformation.SubscribeDiagnosticEventDataArgs:
        return ArbinDataModel.RequestInformation.SubscribeDiagnosticEventData()

@dataclass
class SubscribeSPTTEQCELLDataArgs:
    """
    Wrapper class of 'Arbin.Library.DataModel.RequestInformation.SubscribeSPTTEQCELLDataArgs'
    """
    def to_cs(self) -> ArbinDataModel.RequestInformation.SubscribeSPTTEQCELLDataArgs:
        return ArbinDataModel.RequestInformation.SubscribeSPTTEQCELLData()

