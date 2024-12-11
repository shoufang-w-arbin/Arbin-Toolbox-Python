import os
import clr

current_dir = os.path.dirname(os.path.abspath(__file__))

clr.AddReference("System")
clr.AddReference(os.path.join(current_dir, "bin", "ArbinCTI"))

from ctitoolbox.src.data_type.cs_data_type import CSTypeConverter
from ctitoolbox.src.data_type.cti_data_type import (
    TE_DATA_TYPE, 
    EMVUD,
    EReadWriteMode,
    StartResumeEx,
    MetaVariableInfo,
    MetaVariableInfoEx,
    TimeSensitiveSetMV,
    TimeSensitiveSetMVArgs,
    CMetavariableDataCodeApply
)
