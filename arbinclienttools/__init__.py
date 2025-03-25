import os
import site
import shutil

current_dir = os.path.dirname(os.path.abspath(__file__))

# Search runtime path and add dependent assemblies for dynamic loading
pythonnet_runtime_dir = None
for site_package_dir in site.getsitepackages():
    runtime_path = os.path.join(site_package_dir, 'pythonnet', 'runtime')
    if os.path.exists(runtime_path):
        pythonnet_runtime_dir = runtime_path
        break
dependencies = ["ArbinDataModel.dll"]
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
from common.src.cs_conv import CSConv

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
    GetMetaVariableArgs,
    GetBarcodeInfo,
    SubscribeMonitorDataArgs,
    SubscribeChannelDataArgs,
    SubscribeTestInfoDataArgs,
    SubscribeEventDataArgs,
    SubscribeDiagnosticEventDataArgs,
    SubscribeSPTTEQCELLDataArgs,
)

from arbinclienttools.src.argument.ttest_management import (
    SafetyScope,
    AuxChannelRequirement,
    AuxChannelRequirementBase,
    AuxSafetyRequirement,
    ScheduleModifyInfo,
    UploadFileArgs,
    BrowseFileListArgs,
    ModifyScheduleArgs,
    AssignFileArgs,
    UpdateMetaVariableArgs,
    AssignBarcodeInfoArgs,
)

from arbinclienttools.src.argument.request_info import (
    GetMonitorDataArgs,
    GetResumeDataArgs,
    GetStartDataArgs,
)

from arbinclienttools.src.argument.formation_management import (
    AssignFileArgs,
    AIMetaVariableInfo,
    UpdateMetaVariableArgs,
    GetMetaVariableArgs,
    AssignBarcodeInfoArgs,
    BarcodeInfo, 
    GetBarcodeInfoArgs,
    GetBarcodeInfo,
    GetEngagementStatusArgs,
    EngageTrayArgs,
    SPTTEngageTray,
)

"""
Wrapper classes for unpacking FDBK 
"""
from arbinclienttools.src.feedback.data_stream import (
    CANMonitorInfo,
    SMBMonitorInfo,
    AuxData,
    SPTTEQMonitorData,
    SPTTCellMonitorData,
    SubChannelInfo,
    ShowUDSMessageValue,
    SimulationInfo,
    AuxMapping,
    SubscribeMonitorDataFeedback,
    SubscribeChannelDataFeedback,
    SubscribeTestInfoDataFeedback,
    SubscribeEventDataFeedback,
    SubscribeDiagnosticEventDataFeedback,
    SubscribeSPTTEQCELLDataFeedback
)

