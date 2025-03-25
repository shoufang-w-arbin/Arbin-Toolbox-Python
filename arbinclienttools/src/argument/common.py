__doc__ = """
[Common Classes]
- AIMetaVariableInfo
- BarcodeInfo
- GetBarcodeInfo
"""

from dataclasses import (
    dataclass, 
    field,
)

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from arbinclienttools.src.common.cs_conv import CSConv
from arbinclienttools.src.enumeration import (
    EMetaVariableType,
    EBarcodeResult,
    EBarcodeType,
    EBarcodeType,
)

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