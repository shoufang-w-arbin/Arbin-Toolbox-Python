__doc__ = """
Request Information
- GetMonitorDataArgs 
- GetResumeDataArgs 
- GetStartDataArgs  
"""

from dataclasses import (
    dataclass, 
    field,
)

import ArbinClient.Core as ArbinClient # type: ignore
import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.cs_conv import CSConv
from arbinclienttools.src.common.enumeration import (
    EFilterMonitorChannelType,
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