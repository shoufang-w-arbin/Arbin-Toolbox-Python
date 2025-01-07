import os
import clr

current_dir = os.path.dirname(os.path.abspath(__file__))

clr.AddReference("System")
clr.AddReference(os.path.join(current_dir, "bin", "ArbinCTI"))

from ctitoolbox.src.data_type.cs_data_type import CSTypeConverter
from ctitoolbox.src.data_type.cti_data_type import (
    TE_DATA_TYPE, 
    StartResumeEx,
    MetaVariableInfo,
    MetaVariableInfoEx,
    TimeSensitiveSetMV,
    TimeSensitiveSetMVArgs,
    CMetavariableDataCodeApply
)
from ctitoolbox.src.feedback.channel_control import (
    StartChannelFeedback,
    StopChannelFeedback,
    ResumeChannelFeedback,
    JumpChannelFeedback,
    ContinueChannelFeedback,
    GetChannelDataFeedback,
    GetResumeDataFeedback,
    GetStartDataFeedback
)
from ctitoolbox.src.feedback.file_management import (
    UploadFileFeedback,
    DownloadFileFeedback,
    BrowseDirectoryFeedback,
    CheckFileExistFeedback,
    NewFolderFeedback,
    DeleteFileFeedback,
    NewOrDeleteFeedback
)
from ctitoolbox.src.feedback.schedule_operation import (
    AssignScheduleFeedback,
    AssignFileFeedback,
    SetMetaVariableFeedback,
    SetMetaVariableTimeSensitiveFeedback,
    GetMetaVariableFeedback
)
from ctitoolbox.src.feedback.system import (
    GetSerailNumberFeedback,
    GetMITSVersionFeedback,
    LoginFeedback
)