__doc__ = """
Channel Control
- UploadFileResult
- UpLoadFileArgs
- BrowseFileListArgs
"""

from dataclasses import (
    dataclass, 
)

import ArbinClient.Core as ArbinClient # type: ignore
import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.cs_conv import CSConv
from arbinclienttools.src.common.enumeration import (
    EAIFileType,
)


@dataclass
class UploadFileArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.UpLoadFileArgs'. 
    """
    remote_relative_file_name: str      = ""
    local_full_file_name:      str      = ""
    is_overwrite:              bool     = True
    callback_func:             callable = lambda x: None

    def to_cs(self) -> ArbinDataModel.TestManagement.UploadFileArgs:
        if not callable(self.callback_func):
            raise TypeError("'callback_func' must be callable")
        if self.callback_func.__code__.co_argcount != 1:
            raise ValueError("'callback_func' must accept one argument, which will be an instance of 'Arbin.Library.DataModel.TestManagement.UploadFileResult'")
        
        cs_instance = ArbinDataModel.TestManagement.UploadFileArgs()
        cs_instance.RemoteRelativeFileName = CSConv.to_string(self.remote_relative_file_name)
        cs_instance.LocalFullFileName      = CSConv.to_string(self.local_full_file_name)
        cs_instance.IsOverride             = CSConv.to_bool(self.is_overwrite)
        cs_instance.OnUploadFileResult     = ArbinDataModel.TestManagement.UploadFileResultEventHandler(self.callback_func)
        return cs_instance

@dataclass
class BrowseFileListArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.BrowseFileListArgs'. 
    """
    sn:         str         = ""
    file_type:  EAIFileType = EAIFileType.Schedule

    def to_cs(self) -> ArbinDataModel.TestManagement.BrowseFileListArgs:
        cs_instance = ArbinDataModel.TestManagement.BrowseFileListArgs()
        cs_instance.SN       = CSConv.to_string(self.sn)
        cs_instance.FileType = ArbinDataModel.EAIFileType(self.file_type.value)
        return cs_instance