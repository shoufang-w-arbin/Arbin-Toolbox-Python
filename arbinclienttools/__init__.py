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

from arbinclienttools.src.argument.data_stream import (
    SubscribeMonitorDataArgs,
    SubscribeChannelDataArgs,
    SubscribeTestInfoDataArgs,
    SubscribeEventDataArgs,
    SubscribeDiagnosticEventDataArgs,
    SubscribeSPTTEQCELLDataArgs,
)

