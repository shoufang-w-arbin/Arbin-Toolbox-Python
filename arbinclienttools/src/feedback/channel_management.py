__doc__ = """
[Channel Management Feedback]
- StartChannelFeedback
- StopChannelFeedback
- JumpStepFeedback
- ResumeChannelFeedback
- ContinueChannelFeedback
"""

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.base import (
    DictReprBase,
)

from arbinclienttools.src.enumeration import (
    EStartChannelResult,
    EStopChannelResult,
    EJumpStepResult,
    EResumeChannelResult,
    EContinueChannelResult,
)

class StartChannelFeedback(DictReprBase):
    class StartChannelResult(DictReprBase):
        def __init__(self, obj):
            self.channel_id   = int(obj.ChannelID)
            self.result       = str(obj.Result)
            self.start_result = EStartChannelResult(int(obj.StartResult))
            self.message      = str(obj.Message)

    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.ChannelManagement.StartChannelFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.ChannelManagement.StartChannelFDBK")
        self.successful_channel_id  = list(obj.SuccessfulChannelIDs)
        self.failed_result          = [self.StartChannelResult(res) for res in obj.FailedResults]
        self.is_success             = bool(obj.IsSuccess)
        self.sn                     = int(obj.SN)

class StopChannelFeedback(DictReprBase):
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.ChannelManagement.StopChannelFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.ChannelManagement.StopChannelFDBK")
    
        self.channel_id          = int(obj.ChannelID)
        self.result              = str(obj.Result)
        self.stop_channel_result = EStopChannelResult(int(obj.StopResult))
        self.sn                  = int(obj.SN)     

class JumpStepFeedback(DictReprBase):
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.ChannelManagement.JumpStepFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.ChannelManagement.JumpStepFDBK")
        
        self.channel_id     = int(obj.ChannelID)
        self.result         = str(obj.Result)
        self.jump_step_result = EJumpStepResult(int(obj.JumpStepResult))
        self.sn             = int(obj.SN)

class ResumeChannelFeedback(DictReprBase):
    class ResumeChannelResult(DictReprBase):
        def __init__(self, obj):
            self.channel_id    = int(obj.ChannelID)
            self.result        = str(obj.Result)
            self.resume_result = EResumeChannelResult(int(obj.ResumeResult))
            self.message       = str(obj.Message)

    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.ChannelManagement.ResumeChannelFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.ChannelManagement.ResumeChannelFDBK")
        
        self.successful_channel_id  = list(obj.SuccessfulChannelIDs)
        self.failed_result          = [self.ResumeChannelResult(x) for x in obj.FailedResults]
        self.is_success             = bool(obj.IsSuccess)
        self.sn                     = int(obj.SN)

class ContinueChannelFeedback(DictReprBase):
    class ContinueChannelResult(DictReprBase):
        def __init__(self, obj):
            self.channel_id    = int(obj.ChannelID)
            self.result        = str(obj.Result)
            self.resume_result = EContinueChannelResult(int(obj.ResumeResult))
            self.message       = str(obj.Message)

    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.ChannelManagement.ContinueChannelFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.ChannelManagement.ContinueChannelFDBK")
        
        self.successful_channel_id  = list(obj.SuccessfulChannelIDs)
        self.failed_result          = [self.ContinueChannelResult(x) for x in obj.FailedResults]
        self.is_success             = bool(obj.IsSuccess)
        self.sn                     = int(obj.SN)