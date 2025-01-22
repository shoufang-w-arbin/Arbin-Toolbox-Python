import os
import clr

current_dir = os.path.dirname(os.path.abspath(__file__))

clr.AddReference("System")
clr.AddReference(os.path.join(current_dir, "bin", "ArbinCTI"))

from arbintoolbox.src.cs_conv import CSConv
from arbintoolbox.src.arbincti.data_type.cti_data_type import (
    TE_DATA_TYPE, 
    StartResumeEx,
    MetaVariableInfo,
    MetaVariableInfoEx,
    TimeSensitiveSetMV,
    TimeSensitiveSetMVArgs,
    CMetavariableDataCodeApply
)
from arbintoolbox.src.arbincti.feedback.channel_control import (
    StartChannelFeedback,
    StopChannelFeedback,
    ResumeChannelFeedback,
    JumpChannelFeedback,
    ContinueChannelFeedback,
    GetChannelDataFeedback,
    GetResumeDataFeedback,
    GetStartDataFeedback
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
    GetMetaVariableFeedback
)
from arbintoolbox.src.arbincti.feedback.system import (
    GetSerailNumberFeedback,
    GetMITSVersionFeedback,
    LoginFeedback
)