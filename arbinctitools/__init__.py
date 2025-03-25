import os
import clr

current_dir = os.path.dirname(os.path.abspath(__file__))

clr.AddReference("System")
clr.AddReference(os.path.join(current_dir, "bin", "ArbinCTI"))

from common.src.cs_conv import CSConv

from arbinctitools.src.argument.argument import (
    TE_DATA_TYPE, 
    StartResumeEx,
    MetaVariableInfo,
    MetaVariableInfoEx,
    TimeSensitiveSetMV,
    TimeSensitiveSetMVArgs,
    CMetavariableDataCodeApply,
    GetMappingAuxArgs,
    TestObjectSetting, StartChannelInfo, StartChannelAdvancedArgs,
    SafetyScope, AuxChannelRequirementBase, AuxChannelRequirement, AuxSafetyRequirement, ScheduleModifyInfo, ModifyScheduleArgs
)
from arbinctitools.src.feedback.channel_control import (
    StartChannelFeedback,
    StopChannelFeedback,
    ResumeChannelFeedback,
    JumpChannelFeedback,
    ContinueChannelFeedback,
    StartChannelAdvancedFeedback,
)
from arbinctitools.src.feedback.request_info import (
    GetChannelDataFeedback,
    GetResumeDataFeedback,
    GetStartDataFeedback,
    GetMappingAuxFeedback,
    GetSerialNumberFeedback,
    GetSoftwareVersionFeedback,
    GetChannelDataSimpleModeFeedback,
    GetChannelsDataMinimalistModeFeedback,
    GetStringLimitLengthFeedback,
    GetChannelInfoExFeedback,
)
from arbinctitools.src.feedback.file_management import (
    UploadFileFeedback,
    DownloadFileFeedback,
    BrowseDirectoryFeedback,
    CheckFileExistFeedback,
    NewFolderFeedback,
    DeleteFileFeedback,
    NewOrDeleteFeedback
)
from arbinctitools.src.feedback.schedule_operation import (
    AssignScheduleFeedback,
    AssignFileFeedback,
    SetMetaVariableFeedback,
    SetMetaVariableTimeSensitiveFeedback,
    UpdateMetaVariableAdvancedExFeedback,
    GetMetaVariableFeedback,
    ModifyScheduleFeedback,
    AssignBarcodeInfoFeedback,
    GetBarcodeInfoFeedback,
    GetMachineTypeFeedback,
    GetTrayStatusFeedback,
    EngageTrayFeedback,
    UpdateParameterFeedback,
    SetIntervalTimeLogDataFeedback,
    ConvertToAnonymousOrNamedTOFeedback,
)
from arbinctitools.src.feedback.system import (
    LoginFeedback,
    SendMsgToCTIFeedback,
    UnknownCommandFeedback,
    StartAutomaticCalibrationFeedback
)