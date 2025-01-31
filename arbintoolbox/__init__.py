import os
import clr

current_dir = os.path.dirname(os.path.abspath(__file__))

clr.AddReference("System")
clr.AddReference(os.path.join(current_dir, "bin", "ArbinCTI"))

from arbintoolbox.src.cs_conv import CSConv
from arbintoolbox.src.arbincti.argument.argument import (
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
from arbintoolbox.src.arbincti.feedback.channel_control import (
    StartChannelFeedback,
    StopChannelFeedback,
    ResumeChannelFeedback,
    JumpChannelFeedback,
    ContinueChannelFeedback,
    StartChannelAdvancedFeedback,
)
from arbintoolbox.src.arbincti.feedback.request_info import (
    GetChannelDataFeedback,
    GetResumeDataFeedback,
    GetStartDataFeedback,
    GetMappingAuxFeedback,
)
from arbintoolbox.src.arbincti.feedback.file_management import (
    UploadFileFeedback,
    DownloadFileFeedback,
    BrowseDirectoryFeedback,
    CheckFileExistFeedback,
    NewFolderFeedback,
    DeleteFileFeedback,
    NewOrDeleteFeedback
)
from arbintoolbox.src.arbincti.feedback.schedule_operation import (
    AssignScheduleFeedback,
    AssignFileFeedback,
    SetMetaVariableFeedback,
    SetMetaVariableTimeSensitiveFeedback,
    GetMetaVariableFeedback,
    ModifyScheduleFeedback,
    AssignBarcodeInfoFeedback,
    GetBarcodeInfoFeedback,
    GetMachineTypeFeedback,
    GetTrayStatusFeedback,
    EngageTrayFeedback
)
from arbintoolbox.src.arbincti.feedback.system import (
    GetSerialNumberFeedback,
    GetSoftwareVersionFeedback,
    LoginFeedback,
    SendMsgToCTIFeedback,
    UnknownCommandFeedback,
    StartAutomaticCalibrationFeedback
)