import copy

import ArbinCTI.Core as ArbinCTI # type: ignore

from common.src.base import (
    DictReprBase,
    SafeIntEnumBase
)

"""""""""""""""""""""""""""
Channel Control
- StartChannelFeedback
- StopChannelFeedback
- ResumeChannelFeedback
- JumpChannelFeedback
- ContinueChannelFeedback
- GetChannelDataFeedback
- GetResumeDataFeedback
- GetStartDataFeedback
- StartChannelAdvancedFeedback
"""""""""""""""""""""""""""
class StartChannelFeedback(DictReprBase):
    class EStartToken(SafeIntEnumBase):
        CTI_START_SUCCESS = 0
        CTI_START_INDEX = 0x10
        CTI_START_ERROR = 0x11
        CTI_START_CHANNEL_RUNNING = 0x12
        CTI_START_CHANNEL_NOT_CONNECT = 0x13
        CTI_START_SCHEDULE_VALID = 0x14
        CTI_START_NO_SCHEDULE_ASSIGNED = 0x15
        CTI_START_SCHEDULE_VERSION = 0x16
        CTI_START_POWER_PROTECTED = 0x17
        CTI_START_RESULTS_FILE_SIZE_LIMIT = 0x18
        CTI_START_STEP_NUMBER = 0x19
        CTI_START_NO_CAN_CONFIGURATON_ASSIGNED = 0x1A
        CTI_START_AUX_CHANNEL_MAP = 0x1B
        CTI_START_BUILD_AUX_COUNT = 0x1C
        CTI_START_POWER_CLAMP_CHECK = 0x1D
        CTI_START_AI = 0x1E
        CTI_START_SAFOR_GROUPCHAN = 0x1F
        CTI_START_BT6000RUNNINGGROUP = 0x20
        CTI_START_CHANNEL_DOWNLOADING_SCHEDULE = 0x21
        CTI_START_DATABASE_QUERY_TEST_NAME_ERROR = 0x22
        CTI_START_TEXTNAME_EXITS = 0x23
        CTI_START_GO_STEP = 0x24
        CTI_START_INVALID_PARALLEL = 0x25
        CTI_START_SAFETY = 0x26
        CTI_START_SECHEDULE_NAME_DIFFERENT = 0x27
        CTI_START_BATTERYSIMULATION_NOT_PARALLEL = 0x28
        CTI_START_CSV_WAIT_TIME = 0x29
        CTI_START_CHANNEL_SUSPENT = 0x2A
        CTI_START_TESTNAME_TOO_LONG = 0x2B

    def __init__(self, feedback: ArbinCTI.ArbinCommandStartChannelFeed): 
        if not isinstance(feedback, ArbinCTI.ArbinCommandStartChannelFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandStartChannelFeed', got '{type(feedback)}'")
        self.result = StartChannelFeedback.EStartToken(int(feedback.Result))

class StopChannelFeedback(DictReprBase):
    class EStopToken(SafeIntEnumBase):
        SUCCESS = 0
        STOP_INDEX = 0x10
        STOP_ERROR = 0x11
        STOP_NOT_RUNNING = 0x12
        STOP_CHANNEL_NOT_CONNECT = 0x13

    def __init__(self, feedback: ArbinCTI.ArbinCommandStopChannelFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandStopChannelFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandStopChannelFeed', got '{type(feedback)}'")
        self.result = StopChannelFeedback.EStopToken(int(feedback.Result))

class ResumeChannelFeedback(DictReprBase):
    class EResumeToken(SafeIntEnumBase):
        RESUME_SUCCESS = 0
        RESUME_INDEX = 0x10
        RESUME_ERROR = 0x11
        RESUME_CHANNEL_RUNNING = 0x12
        RESUME_CHANNEL_NOT_CONNECT = 0x13
        RESUME_SCHEDULE_VALID = 0x14
        RESUME_NO_SCHEDULE_ASSIGNED = 0x15
        RESUME_SCHEDULE_VERSION = 0x16
        RESUME_POWER_PROTECTED = 0x17
        RESUME_RESULTS_FILE_SIZE_LIMIT = 0x18
        RESUME_STEP_NUMBER = 0x19
        RESUME_NO_CAN_CONFIGURATON_ASSIGNED = 0x1A
        RESUME_AUX_CHANNEL_MAP = 0x1B
        RESUME_BUILD_AUX_COUNT = 0x1C
        RESUME_POWER_CLAMP_CHECK = 0x1D
        RESUME_AI = 0x1E
        RESUME_SAFOR_GROUPCHAN = 0x1F
        RESUME_BT6000RUNNINGGROUP = 0x20
        RESUME_CHANNEL_DOWNLOADING_SCHEDULE = 0x21
        RESUME_DATABASE_QUERY_TEST_NAME_ERROR = 0x22
        RESUME_NO_TEST_NAME = 0x23
        RESUME_LOAD_RESUME = 0x24
        RESUME_MAX_MULTIPLE_RESULT = 0x25
        CTI_RESUME_SAFETY = 0x26
        CTI_RESUME_BATTERYSIMULATION_NOT_PARALLEL = 0x27
        CTI_RESUME_CHANNEL_SUSPENT = 0x28

    def __init__(self, feedback: ArbinCTI.ArbinCommandResumeChannelFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandResumeChannelFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandResumeChannelFeed', got '{type(feedback)}'")
        self.result = ResumeChannelFeedback.EResumeToken(int(feedback.Result))

class JumpChannelFeedback(DictReprBase):
    class EJumpToken(SafeIntEnumBase):
        CTI_JUMP_SUCCESS = 0
        CTI_JUMP_INDEX = 0x10
        CTI_JUMP_ERROR = 0x11
        CTI_JUMP_CHANNEL_RUNNING = 0x12
        CTI_JUMP_CHANNEL_NOT_CONNECT = 0x13
        CTI_JUMP_SCHEDULE_VALID = 0x14
        CTI_JUMP_NO_SCHEDULE_ASSIGNED = 0x15
        CTI_JUMP_SCHEDULE_VERSION = 0x16
        CTI_JUMP_POWER_PROTECTED = 0x17
        CTI_JUMP_RESULTS_FILE_SIZE_LIMIT = 0x18
        CTI_JUMP_STEP_NUMBER = 0x19
        CTI_JUMP_NO_CAN_CONFIGURATON_ASSIGNED = 0x1A
        CTI_JUMP_AUX_CHANNEL_MAP = 0x1B
        CTI_JUMP_BUILD_AUX_COUNT = 0x1C
        CTI_JUMP_POWER_CLAMP_CHECK = 0x1D
        CTI_JUMP_AI = 0x1E
        CTI_JUMP_SAFOR_GROUPCHAN = 0x1F
        CTI_JUMP_BT6000RUNNINGGROUP = 0x20
        CTI_JUMP_CHANNEL_DOWNLOADING_SCHEDULE = 0x21
        CTI_JUMP_DATABASE_QUERY_TEST_NAME_ERROR = 0x22
        CTI_JUMP_TEXTNAME_EXITS = 0x23
        CTI_JUMP_GO_STEP = 0x24
        CTI_JUMP_INVALID_PARALLEL = 0x25
        CTI_JUMP_SAFETY = 0x26
        CTI_JUMP_SECHEDULE_NAME_DIFFERENT = 0x27
        CTI_JUMP_BATTERYSIMULATION_NOT_PARALLEL = 0x28
        CTI_JUMP_CHANNEL_SUSPENT = 0x29,
        CTI_JUMP_ACIM_TESTING = 0x2A

    def __init__(self, feedback: ArbinCTI.ArbinCommandJumpChannelFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandJumpChannelFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandJumpChannelFeed', got '{type(feedback)}'")
        self.result        = JumpChannelFeedback.EJumpToken(int(feedback.Result))
        self.error_channel = int(feedback.errorChannel)

class ContinueChannelFeedback(DictReprBase):
    class EContinueToken(SafeIntEnumBase):
        CTI_CONTINUE_SUCCESS = 0
        CTI_CONTINUE_ERROR = 0x11
        CTI_CONTINUE_CHANNEL_RUNNING = 0x12
        CTI_CONTINUE_CHANNEL_NOT_CONNECT = 0x13
        CTI_CONTINUE_CHANNEL_CALIBRATING = 0x14
        CTI_CONTINUE_NOT_PAUSE_NORMAL = 0x15
        CTI_CONTINUE_CHANNEL_UNSAFE = 0x16
    
    def __init__(self, feedback: ArbinCTI.ArbinCommandContinueChannelFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandContinueChannelFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandContinueChannelFeed', got '{type(feedback)}'")
        self.result = ContinueChannelFeedback.EContinueToken(int(feedback.Result))

class StartChannelAdvancedFeedback(DictReprBase):
    class StartChannelResult(DictReprBase):
        def __init__(self, result: ArbinCTI.ArbinCommandStartChannelAdvancedFeed.StartChannelResult):
            self.channel_index = int(result.ChannelIndex)
            self.result        = StartChannelFeedback.EStartToken(int(result.StartResult))
            self.message       = str(result.Message)
        

    def __init__(self, feedback: ArbinCTI.ArbinCommandStartChannelAdvancedFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandStartChannelAdvancedFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandStartChannelAdvancedFeed', got '{type(feedback)}'")
        self.task_id                = int(feedback.TaskID)
        self.successful_channel_id  = list(feedback.SuccessfulChannelIDs)
        self.failed_result          = [StartChannelAdvancedFeedback.StartChannelResult(result) for result in feedback.FailedResults]
        self.is_success             = len(self.failed_result) == 0
