__doc__ = """
Schedule Operation
- Assign File:   AssignFileArgs
- Meta Variable: AIMetaVariableInfo, UpdateMetaVariableArgs, GetMetaVariableArgs
- Barcode:       AssignBarcodeInfoArgs (BarcodeInfo), GetBarcodeInfoArgs (GetBarcodeInfo)
- Formation:     GetEngagementStatusArgs, EngageTrayArgs (SPTTEngageTray)
"""

from dataclasses import (
    dataclass, 
    field,
)

import ArbinClient.Core as ArbinClient # type: ignore
import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.cs_conv import CSConv
from common.src.base import DictReprBase
from arbinclienttools.src.common.enumeration import (
    EAIFileType,
    EBarcodeResult,
    EBarcodeType,
    EMetaVariableType,
    EEngagementResult,
)

@dataclass
class AssignFileArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.AssignFileArgs'
    """
    sn:         str          = ""
    channel_id: list         = field(default_factory=list)
    file_name:  str          = ""
    file_type:  EAIFileType  = EAIFileType.None_

    def to_cs(self) -> ArbinClient.AssignFileArgs:
        cs_instance = ArbinClient.AssignFileArgs()
        cs_instance.ChannelIDs  = CSConv.to_list(self.channel_id, CSConv.EDataType.INT)
        cs_instance.FileName    = CSConv.to_string(self.file_name)
        cs_instance.FileType    = ArbinDataModel.EAIFileType(self.file_type.value)
        cs_instance.SN          = CSConv.to_string(self.sn)
        return cs_instance
    
@dataclass
class AIMetaVariableInfo:
    """
    Wrapper class of of 'Arbin.Library.DataModel.Common.AIMetaVariableInfo'
    """
    global_id:           int                 = field(default=-1)
    meta_variable_type:  EMetaVariableType   = field(default=EMetaVariableType.MetaCode_MV_UD1)
    index_:              int                 = field(default=0)
    value:               float               = field(default=0.0)

    def to_cs(self) -> ArbinDataModel.Common.AIMetaVariableInfo:
        return ArbinDataModel.Common.AIMetaVariableInfo(
            CSConv.to_int(self.global_id),
            self.meta_variable_type.to_cs(),
            CSConv.to_int(self.index_),
            CSConv.to_float(self.value)
        )

@dataclass
class UpdateMetaVariableArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.UpdateMetaVariableArgs'
    """
    sn:                 int  = 0
    meta_variable_info: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.TestManagement.UpdateMetaVariableArgs:
        if not all([isinstance(info, AIMetaVariableInfo) for info in self.meta_variable_info]):
            raise TypeError("'meta_variable_info' must be a list of 'AIMetaVariableInfo'")
        
        cs_instance = ArbinDataModel.TestManagement.UpdateMetaVariableArgs()
        cs_instance.MetaVariableInfos = CSConv.to_list(self.meta_variable_info)
        cs_instance.SN = CSConv.to_int(self.sn)
        return cs_instance
    
@dataclass
class GetMetaVariableArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.RequestInformation.GetMetaVariableArgs'
    """
    sn:                 int  = 0
    meta_variable_type: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.RequestInformation.GetMetaVariableArgs:
        if not all([isinstance(info, AIMetaVariableInfo) for info in self.meta_variable_type]):
            raise TypeError("'meta_variable_type' must be a list of 'arbinclienttools.EMetaVariableType'")
        
        cs_instance = ArbinDataModel.RequestInformation.GetMetaVariableArgs()
        cs_instance.SN = CSConv.to_int(self.sn)
        cs_instance.MetaVariableTypes = CSConv.to_list(self.meta_variable_type)
        return cs_instance

@dataclass
class BarcodeInfo:
    """
    Wrapper class of of 'Arbin.Library.DataModel.Common.BarcodeInfo'.
    """
    barcode_type:   EBarcodeType   = EBarcodeType.IV
    barcode:        str            = ""    
    global_id:      int            = -1
    info:           str            = ""
    result:         str            = EBarcodeResult.Success.name
    barcode_result: EBarcodeResult = EBarcodeResult.Success

    def to_cs(self) -> ArbinDataModel.Common.BarcodeInfo:
        cs_instance = ArbinDataModel.Common.BarcodeInfo()
        cs_instance.BarcodeType   = ArbinDataModel.EBarcodeType(self.barcode_type.value)
        cs_instance.Barcode       = CSConv.to_string(self.barcode)
        cs_instance.GlobalID      = CSConv.to_int(self.global_id)
        cs_instance.Info          = CSConv.to_string(self.info)
        cs_instance.Result        = CSConv.to_string(self.result)
        cs_instance.BarcodeResult = ArbinDataModel.EBarcodeResult(self.barcode_result.value)
        return cs_instance

@dataclass
class GetBarcodeInfo:
    """
    Wrapper class of of 'Arbin.Library.DataModel.RequestInformation.GetBarcodeInfo'
    """
    barcode_type: EBarcodeType
    global_id:    int

    def to_cs(self) -> ArbinDataModel.RequestInformation.GetBarcodeInfo:
        cs_instance = ArbinDataModel.RequestInformation.GetBarcodeInfo()
        cs_instance.BarcodeType = ArbinDataModel.EBarcodeType(self.barcode_type.value)
        cs_instance.GlobalID    = CSConv.to_int(self.global_id)
        return cs_instance

@dataclass
class AssignBarcodeInfoArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.TestManagement.AssignBarcodeInfoArgs'
    """
    sn:           str  = field(default="")
    barcode_info: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.TestManagement.AssignBarcodeInfoArgs:
        if not all([isinstance(info, BarcodeInfo) for info in self.barcode_info]):
            raise TypeError("'barcode_info' must be a list of 'arbinclienttools.BarcodeInfo'")
        
        cs_instance = ArbinDataModel.TestManagement.AssignBarcodeInfoArgs()
        cs_instance.SN           = CSConv.to_string(self.sn)
        cs_instance.BarcodeInfos = CSConv.to_list(self.barcode_info)
        return cs_instance

@dataclass
class GetBarcodeInfoArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.RequestInformation.GetBarcodeInfoArgs'
    """
    sn:             str  = ""
    barcode_info:   list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.RequestInformation.GetBarcodeInfoArgs:
        if not all([isinstance(info, GetBarcodeInfo) for info in self.barcode_info]):
            raise TypeError("'barcode_info' must be a list of 'arbinclienttools.GetBarcodeInfo'")
        
        cs_instance = ArbinDataModel.RequestInformation.GetBarcodeInfoArgs()
        cs_instance = CSConv.to_string(self.sn)
        cs_instance = CSConv.to_list(self.barcode_info)
        return cs_instance
    
@dataclass
class GetEngagementStatusArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.FormationManagement.GetEngagementStatusArgs'
    """
    sn:             str  = ""
    engagement_id:  list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.FormationManagement.GetEngagementStatusArgs:
        cs_instance = ArbinDataModel.FormationManagement.GetEngagementStatusArgs()
        cs_instance.EngagementIDs = CSConv.to_list(self.engagement_id, CSConv.EDataType.INT)
        cs_instance.SN            = CSConv.to_string(self.sn)
        return cs_instance

@dataclass
class SPTTEngageTray():
    global_id:         int               = -1
    engage:            bool              = True
    result:            str               = ""
    engagement_result: EEngagementResult = EEngagementResult.Success

    def to_cs(self) -> ArbinDataModel.FormationManagement.SPTTEngageTray:
        cs_instance = ArbinDataModel.FormationManagement.SPTTEngageTray()
        cs_instance.GlobalID = CSConv.to_int(self.global_id)
        cs_instance.Engage   = CSConv.to_bool(self.engage)
        cs_instance.Result   = CSConv.to_string(self.result)
        cs_instance.EngagementResult = ArbinDataModel.EEngagementResult(self.engagement_result.value)
        return cs_instance

@dataclass
class EngageTrayArgs:
    sn:          str  = ""
    engage_tray: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.FormationManagement.EngageTrayArgs:
        if not all([isinstance(info, SPTTEngageTray) for info in self.engage_tray]):
            raise TypeError("'engage_tray' must be a list of 'arbinclienttools.SPTTEngageTray'")
        
        cs_instance = ArbinDataModel.FormationManagement.EngageTrayArgs()
        cs_instance.EngageTrays = CSConv.to_list(self.engage_tray)
        cs_instance.SN          = CSConv.to_string(self.sn)
        return cs_instance
    