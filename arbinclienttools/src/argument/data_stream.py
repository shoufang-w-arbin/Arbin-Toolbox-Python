__doc__ = """
ArbinMQ Arguments
- SubscribeMonitorDataArgs
- SubscribeChannelDataArgs
- SubscribeTestInfoDataArgs
- SubscribeEventDataArgs
- SubscribeDiagnosticEventDataArgs
- SubscribeSPTTEQCELLDataArgs
"""

from dataclasses import dataclass

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

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

