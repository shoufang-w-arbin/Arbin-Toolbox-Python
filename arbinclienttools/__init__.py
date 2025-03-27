import os
import site
import shutil

dependencies = ["ArbinDataModel.dll"]
current_dir = os.path.dirname(os.path.abspath(__file__))

# Search runtime path and add dependent assemblies for dynamic loading
pythonnet_runtime_dir = None
for site_package_dir in site.getsitepackages():
    runtime_path = os.path.join(site_package_dir, 'pythonnet', 'runtime')
    if os.path.exists(runtime_path):
        pythonnet_runtime_dir = runtime_path
        break

for dep in dependencies:
    try:
        shutil.copy2(
            os.path.join(current_dir, "bin", dep), 
            os.path.join(pythonnet_runtime_dir, dep)
        )
    except Exception as e:
        raise RuntimeError(f"Failed to copy dependent assemblies to runtime - {dep}: {e}")
    
# Set pythonnet runtime and load main DLL
from pythonnet import load
load("coreclr")
import clr
clr.AddReference(os.path.join(current_dir, "bin", "ArbinDataModel"))
clr.AddReference(os.path.join(current_dir, "bin", "ArbinClient"))

# Expose classes to the package level
from arbinclienttools.src.common.cs_conv import CSConv

from arbinclienttools.src.enumeration import (
    EAIFileType,
    EBarcodeResult,
    EBarcodeType,
    EMetaVariableType,
    EEngagementResult,
    EFilterMonitorChannelType,
    EUploadFileResult,
)

from arbinclienttools.src.argument.channel_management import (
    ResumeChannelArgs,
    StartChannelArgs,
    ChannelResumeData,
    StopChannelArgs,
    JumpStepArgs,
    ResumeChannelArgs, 
    ContinueChannelArgs,
)

from arbinclienttools.src.argument.connection import (
    CreateArbinClientArgs,
)

from arbinclienttools.src.argument.common import (
    AIMetaVariableInfo,
    BarcodeInfo,
    GetBarcodeInfo,
)

from arbinclienttools.src.argument.request_info import (
    GetMonitorDataArgs,
    GetResumeDataArgs,
    GetStartDataArgs,
    GetMetaVariablesArgs,
    GetMappingAuxArgs,
    GetBarcodeInfoArgs,
    SubscribeMonitorDataArgs,
    SubscribeChannelDataArgs,
    SubscribeTestInfoDataArgs,
    SubscribeEventDataArgs,
    SubscribeDiagnosticEventDataArgs,
    SubscribeSPTTEQCellDataArgs,
)

from arbinclienttools.src.argument.ttest_management import (
    UploadFileArgs,
    BrowseFileListArgs,
    ModifyScheduleArgs,
    AssignFileArgs,
    UpdateMetaVariablesArgs,
    AssignBarcodeInfoArgs,
    SafetyScope,
    AuxChannelRequirement,
    AuxChannelRequirementBase,
    AuxSafetyRequirement,
    ScheduleModifyInfo,
)

from arbinclienttools.src.argument.formation_management import (
    GetEngagementStatusArgs,
    EngageTrayArgs,
    SPTTEngageTray,
)

"""
Wrapper classes for unpacking FDBK 
"""
from arbinclienttools.src.feedback.channel_management import (
    StartChannelFeedback,
    StopChannelFeedback,
    JumpStepFeedback,
    ResumeChannelFeedback,
    ContinueChannelFeedback,
)

from arbinclienttools.src.feedback.connection import (
    LoginFeedback,
)

from arbinclienttools.src.feedback.formation_management import (
    GetEngagementStatusFeedback,
    EngageTrayFeedback
)

from arbinclienttools.src.feedback.request_info import (
    GetStartDataFeedback,
    GetResumeDataFeedback,
    GetMonitorDataFeedback,
    GetBarcodeInfoFeedback,
    GetMappingAuxFeedback,
    SubscribeMonitorDataFeedback,
    SubscribeChannelDataFeedback,
    SubscribeTestInfoDataFeedback,
    SubscribeEventDataFeedback,
    SubscribeDiagnosticEventDataFeedback,
    SubscribeSPTTEQCellDataFeedback
)

from arbinclienttools.src.feedback.ttest_management import (
    BrowseFileListFeedback,
    AssignFileFeedback,
    UpdateMetaVariableFeedback,
    GetMetaVariablesFeedback,
    AssignBarcodeInfoFeedback,
    TimeSensitiveSetMVFeedback
)