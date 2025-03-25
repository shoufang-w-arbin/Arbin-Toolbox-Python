__doc__ = """
[Test Management Feedback]
- UploadFileResult
- BrowseFileListFeedback
- AssignFileFeedback
- UpdateMetaVariableFeedback
- GetMetaVariablesFeedback
- AssignBarcodeInfoFeedback
- TimeSensitiveSetMVFeedback
"""

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.base import DictReprBase
from arbinclienttools.src.enumeration import (
    EUploadFileResult,
    EBrowseDirectoryResult,
    EAssignFileResult,
    EChannelStatus,
    ECommonResult,
)
from arbinclienttools.src.feedback.common import (
    AIMetaVariableInfo,
    BarcodeInfo,
)

class UploadFileResult(DictReprBase):
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.TestManagement.UploadFileResult):
            raise ValueError("'obj' must be of type ArbinDataModel.TestManagement.UploadFileResult")
        self.result                = str(obj.Result)
        self.upload_result         = EUploadFileResult(int(obj.UploadResult))
        self.is_cancel_upload_file = bool(obj.IsCancelUploadFile)
        self.progress_rate         = float(obj.ProgressRate)

class BrowseFileListFeedback(DictReprBase):
    class DirFileInfo(DictReprBase):
        def __init__(self, obj):
            self.type_          = str(obj.Type)
            self.dir_file_name  = str(obj.DirFileName)
            self.size           = int(obj.Size)
            self.modified_time  = str(obj.ModifiedTime)
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.TestManagement.BrowseFileListFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.TestManagement.BrowseFileListFDBK")
        self.result                     = str(obj.Result)
        self.browse_directory_result    = EBrowseDirectoryResult(int(obj.BrowseDirectoryResult))
        self.dir_file_info_list         = [self.DirFileInfo(x) for x in obj.DirFileInfoList]
        self.sn                         = int(obj.SN)
        
class AssignFileFeedback(DictReprBase):
    class AssignFileResult(DictReprBase):
        def __init__(self, obj):
            self.channel_id     = int(obj.ChannelID)
            self.result         = str(obj.Result)
            self.assign_result  = EAssignFileResult(int(obj.AssignFileResult))

    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.TestManagement.AssignFileFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.TestManagement.AssignFileFDBK")
        self.successful_channel_id  = list(obj.SuccessfulChannelIDs)
        self.failed_result          = [self.AssignFileResult(x) for x in obj.FailedResults]
        self.is_success             = bool(obj.IsSuccess)
        self.sn                     = int(obj.SN)
        
class UpdateMetaVariableFeedback(DictReprBase):
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.TestManagement.UpdateMetaVariableFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.TestManagement.UpdateMetaVariableFDBK")
        self.meta_variable_info = [AIMetaVariableInfo(x) for x in obj.MetaVariableInfos]
        self.sn                 = int(obj.SN)

class GetMetaVariablesFeedback(DictReprBase):
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.RequestInformation.GetMetaVariablesFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.TestManagement.GetMetaVariablesFDBK")
        self.meta_variable_info = [AIMetaVariableInfo(x) for x in obj.MetaVariableInfos]
        self.sn                 = int(obj.SN)

class AssignBarcodeInfoFeedback(DictReprBase):
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.TestManagement.AssignBarcodeInfoFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.TestManagement.AssignBarcodeInfoFDBK")
        self.barcode_info = [BarcodeInfo(x) for x in obj.BarcodeInfos]
        self.sn           = int(obj.SN)

class TimeSensitiveSetMVFeedback(DictReprBase):
    class SetMVResult(DictReprBase):
        def __init__(self, obj):
            self.result         = ECommonResult(int(obj.Result))
            self.channel_id     = int(obj.ChannelID)
            self.step_index     = int(obj.StepIndex)
            self.sub_step_index = int(obj.SubStepIndex)
            self.channel_status = EChannelStatus(int(obj.ChannelStatus))
            self.sample_current = float(obj.SampleCurrent)
            self.sample_voltage = float(obj.SampleVoltage)
            self.timestamp_utc  = str(obj.TimestampUtc.ToString())
            self.mvud_values    = [float(x) for x in obj.MVUDValues]

    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.TestManagement.TimeSensitiveSetMVFeedback):
            raise ValueError("'obj' must be of type ArbinDataModel.TestManagement.TimeSensitiveSetMVFeedback")
        self.sn                     = int(obj.SN)
        self.timeout                = float(obj.Timeout)
        self.set_meta_variable_list = [self.SetMVResult(x) for x in obj.SetMetaVariableList]