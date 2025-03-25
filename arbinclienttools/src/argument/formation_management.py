__doc__ = """
[Formation Management Arguments]
- GetEngagementStatusArgs
- EngageTrayArgs

[Subsidary Classes]
- SPTTEngageTray
"""

from dataclasses import (
    dataclass, 
    field,
)

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.cs_conv import CSConv
from arbinclienttools.src.enumeration import (
    EEngagementResult,
)

@dataclass
class SPTTEngageTray:
    """
    Wrapper class of of 'Arbin.Library.DataModel.FormationManagement.SPTTEngageTray'
    """
    global_id:         int               = -1
    engage:            bool              = True
    result:            str               = ""
    engagement_result: EEngagementResult = EEngagementResult.Success

    def to_cs(self) -> ArbinDataModel.FormationManagement.SPTTEngageTray:
        cs_instance = ArbinDataModel.FormationManagement.SPTTEngageTray()
        cs_instance.GlobalID = CSConv.to_int(self.global_id)
        cs_instance.Engage   = CSConv.to_bool(self.engage)
        cs_instance.Result   = CSConv.to_string(self.result)
        cs_instance.EngagementResult = ArbinDataModel.EEngagementResult(self.engagement_result.value)
        return cs_instance
    
@dataclass
class GetEngagementStatusArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.FormationManagement.GetEngagementStatusArgs'
    """
    sn:             str  = ""
    engagement_id:  list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.FormationManagement.GetEngagementStatusArgs:
        cs_instance = ArbinDataModel.FormationManagement.GetEngagementStatusArgs()
        cs_instance.EngagementIDs = CSConv.to_list(self.engagement_id, CSConv.EDataType.INT)
        cs_instance.SN            = CSConv.to_string(self.sn)
        return cs_instance

@dataclass
class EngageTrayArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.FormationManagement.EngageTrayArgs'
    """
    sn:          str  = ""
    engage_tray: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.FormationManagement.EngageTrayArgs:
        if not all([isinstance(info, SPTTEngageTray) for info in self.engage_tray]):
            raise TypeError("'engage_tray' must be a list of 'arbinclienttools.SPTTEngageTray'")
        
        cs_instance = ArbinDataModel.FormationManagement.EngageTrayArgs()
        cs_instance.EngageTrays = CSConv.to_list(self.engage_tray)
        cs_instance.SN          = CSConv.to_string(self.sn)
        return cs_instance
    