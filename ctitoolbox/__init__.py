import os
import clr

current_dir = os.path.dirname(os.path.abspath(__file__))

clr.AddReference("System")
clr.AddReference(os.path.join(current_dir, "bin", "ArbinCTI"))

from ctitoolbox.src.cs_type_converter import CSTypeConverter
from ctitoolbox.src.cs_type_converter import (
    TE_DATA_TYPE, 
    Enum_MvUd,
    EReadWriteMode,
    StartResumeEx,
    MetaVariableInfo,
    MetaVariableInfoEx,
    TimeSensitiveSetMV,
    TimeSensitiveSetMVArgs,
    CMetavariableDataCodeApply
)
