__doc__ = """
[Formation Management Feedback]
- GetEngagementStatusFeedback
- EngageTrayFeedback
"""
import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from arbinclienttools.src.common.base import (
    DictReprBase,
)
from arbinclienttools.src.enumeration import (
    EEngagementResult
)

class GetEngagementStatusFeedback(DictReprBase):
    class SPTTEngagementMetaValue(DictReprBase):
        def __init__(self, obj):
            self.value      = float(obj.Value)
            self.alias_name = str(obj.AliasName)
            self.result     = str(obj.Result)

    class SPTTEngagementStatus(DictReprBase):
        def __init__(self, obj):
            self.global_id              = int(obj.GlobalID)
            self.is_engagement_down     = bool(obj.IsEngagementDown)
            self.is_engagement_up       = bool(obj.IsEngagementUp)
            self.is_tray_inserted       = bool(obj.IsTrayInserted)
            self.result                 = str(obj.Result)
            self.engagement_result      = EEngagementResult(int(obj.EngagementResult))
            self.engagement_meta_values = [GetEngagementStatusFeedback.SPTTEngagementMetaValue(x) for x in obj.EngagementMetaValues]

    def __init__(self, feedback):
        if not isinstance(feedback, ArbinDataModel.FormationManagement.GetEngagementStatusFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.FormationManagement.GetEngagementStatusFDBK")
        self.sn = str(feedback.SN)


class EngageTrayFeedback(DictReprBase):
    class SPTTEngageTray(DictReprBase):
        def __init__(self, obj):
            self.global_id          = int(obj.GlobalID)
            self.engage             = bool(obj.Engage)
            self.result             = str(obj.Result)
            self.engagement_result  = EEngagementResult(int(obj.EngagementResult))
       
    def __init__(self, feedback):
        if not isinstance(feedback, ArbinDataModel.FormationManagement.EngageTrayFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.FormationManagement.EngageTrayFDBK")
        self.sn           = str(feedback.SN)
        self.engage_trays = [self.SPTTEngageTray(x) for x in feedback.EngageTrays]
