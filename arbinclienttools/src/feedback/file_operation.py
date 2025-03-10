from dataclasses import (
    dataclass, 
    field,
)

import ArbinClient.Core as ArbinClient # type: ignore
import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.cs_conv import CSConv
from arbinclienttools.src.common.enumeration import (
    EUploadFileResult,
    EAIFileType,
)

@dataclass
class UploadFileResult:
    result:                str                = ""
    upload_result:         EUploadFileResult  = EUploadFileResult.InProgress
    is_cancel_upload_file: bool               = False
    progress_rate:         float              = 0.0

    def to_cs(self) -> ArbinDataModel.TestManagement.UploadFileResult:
        cs_instance                    = ArbinDataModel.TestManagement.UploadFileResult()
        cs_instance.Result             = CSConv.to_string(self.result)
        cs_instance.UploadResult       = ArbinDataModel.EUploadFileResult(self.upload_result.value)
        cs_instance.IsCancelUploadFile = CSConv.to_bool(self.is_cancel_upload_file)
        cs_instance.ProgressRate       = CSConv.to_float(self.progress_rate)
        return cs_instance
