# Table of Contents
- [About](#about)
- [Requirements](#requirements)
- [Installation](#installation)
- [Supported ArbinCTI Objects](#supported-arbincti-objects)
- [Usage Examples](#usage-examples) 
- [Testing](#testing)
- [To-Do](#to-do)

# About
Wrappers of C# objects, providing a smoother and more Pythonic programming experience for users who want to use ArbinCTI in Python.

## Background
When calling `public bool PostTimeSensitiveSetMV(IArbinSocket socket, TimeSensitiveSetMVArgs args)`, creating a `TimeSensitiveSetMVArgs` object in Python without the toolbox can be quite cumbersome. Here's an example:

<table>
<thead>
<tr>
<th>Without Toolbox</th>
<th>With Toolbox</th>
</tr>
</thead>
<tbody>
<tr>
<td style="vertical-align: top;">

```python
import clr
clr.AddReference("ArbinCTI")

from System.Collections.Generic import List
from ArbinCTI.Core import (
    TimeSensitiveSetMVArgs, 
    TimeSensitiveSetMV
)

mv1 = TimeSensitiveSetMV()
mv1.MVUD  = TimeSensitiveSetMV.EMVUD.MVUD1
mv1.Value = 12.3

mv2 = TimeSensitiveSetMV()
mv2.MVUD  = TimeSensitiveSetMV.EMVUD.MVUD2
mv2.Value = 5.46

mv_list = List[TimeSensitiveSetMV]()
mv_list.Add(mv1)
mv_list.Add(mv2)

mv_channel1 = TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel(
    1,
    mv_list, 
    True
)

mv_args = TimeSensitiveSetMVArgs()
mv_args.Timeout = 5.0
mv_args.Channels.Add(mv_channel1)

control.PostTimeSensitiveSetMV(client, mv_args)
```

</td>
<td style="vertical-align: top;">

```python
‎ 


from ctitoolbox import (
    TimeSensitiveSetMVArgs,
    TimeSensitiveSetMV
)


mv1 = TimeSensitiveSetMV(EMVUD.MVUD1, 12.3)
mv2 = TimeSensitiveSetMV(EMVUD.MVUD2, 4.56)










mv_channel1 = TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel(
    1, 
    [mv1, mv2], 
    True
)

mv_args = TimeSensitiveSetMVArgs(5.0, [mv_channel1])



control.PostTimeSensitiveSetMV(client, mv_args.to_cs())
```

</td>
</tr>
</tbody>
</table>



As you can see, the toolbox provides a smoother and more Pythonic way to interact with C# objects, making your code cleaner and easier to maintain.

## Additional Benefits
- **Keyword arguments** are allowed in this toolbox, compared to using `pythonnet` directly. 
- **Attributes are discoverable by Pylance**, reducing human error when programming. \
    ![](resource/pylance.png)

> We are adding more wrapper classes. If you require immediate implementation of a certain CTI object, please create an issue or submit a pull request with your work.

# Requirements
- 64-bit Python >= 3.7
- System
    - Windows: .NET Framework >=4.7.2
    - Linux: Mono is used by default

# Installation
```bash
pip install {path}/ctitoolbox-{version}-py3-none-any.whl
```

# Supported ArbinCTI Objects
## General Objects
These objects include objects that may be required when sending ArbinCTI commands. The wrapper classes allow for creating objects in a Pythonic way and then converting them to C# objects, eliminating the need to use C# syntax.
- `to_cs` converts the object to a C# object, which is required by commands.
- (to-do) uses CSTypeConverter to convert to C# List object

| Wrapper Class           | Original Object Name                                      |
|-------------------------|-----------------------------------------------------------|
| StartResumeEx           | ArbinCTI.Core.StartResumeEx                               |
| MetaVariableInfo        | ArbinCTI.Core.ArbinCommandGetMetaVariablesFeed.MetaVariableInfo |
| MetaVariableInfoEx      | ArbinCTI.Core.MetaVariableInfoEx                          |
| TimeSensitiveSetMVArgs  | ArbinCTI.Core.ArbinCommandTimeSensitiveSetMVArgs          |
| CMetavariableDataCodeApply | ArbinCTI.Core.ArbinCommandCMetavariableDataCodeApply   |

Additional Objects/Enums may be required when generating the above wrapper classes:

| Wrapper Class           | Original Object Name                                      | Required By                           |
|-------------------------|-----------------------------------------------------------|---------------------------------------|
| TE_DATA_TYPE            | TE_DATA_TYPE                                              | MetaVariableInfo, MetaVariableInfoEx, CMetavariableDataCodeApply |
| TimeSensitiveSetMV      | TimeSensitiveSetMV                                        | TimeSensitiveSetMVArgs                |

## Feedback Objects
The wrapper class converts C# ArbinCTI feedback objects to Python objects, enabling user-friendly access. Additionally, all wrapper classes come with two methods:
- `to_dict` converts object to a serializable format, easily transformable to JSON, with enum objects represented by their names.
- `__repr__` is defined for quick data inspection.

| Wrapper Class                        | Original Object Name                              |
|--------------------------------------|---------------------------------------------------|
| **Connection**                       |                                                   |
| LoginFeedback                        | ArbinCommandLoginFeed                             |
| **Test Schedule**                    |                                                   |
| AssignScheduleFeedback               | ArbinCommandAssignScheduleFeed                    |
| AssignFileFeedback                   | ArbinCommandAssignFileFeed                        |
| SetMetaVariableFeedback              | ArbinCommandSetMetaVariableFeed                   |
| SetMetaVariableTimeSensitiveFeedback | ArbinCommandTimeSensitiveSetMVFeed                |
| GetMetaVariableFeedback              | ArbinCommandGetMetaVariablesFeed                  |
| **Channel Control**                  |                                                   |
| StartChannelFeedback                 | ArbinCommandStartChannelFeed                      |
| StopChannelFeedback                  | ArbinCommandStopChannelFeed                       |
| ResumeChannelFeedback                | ArbinCommandResumeChannelFeed                     |
| JumpChannelFeedback                  | ArbinCommandJumpChannelFeed                       |
| ContinueChannelFeedback              | ArbinCommandContinueChannelFeed                   |
| **File Operation**                   |                                                   |
| UploadFileFeedback                   | ArbinCommandUpLoadFileFeed                        |
| DownloadFileFeedback                 | ArbinCommandDownloadFileFeed                      |
| BrowseDirectoryFeedback              | ArbinCommandBrowseDirectoryFeed                   |
| CheckFileExistFeedback               | ArbinCommandCheckFileExFeed                       |
| NewFolderFeedback                    | ArbinCommandNewFolderFeed                         |
| DeleteFileFeedback                   | ArbinCommandDeleteFileFeed                        |
| NewOrDeleteFeedback                  | ArbinCommandNewOrDeleteFeed                       |
| **Request Information**              |                                                   |
| GetChannelDataFeedback               | ArbinCommandGetChannelDataFeed                    |
| GetStartDataFeedback                 | ArbinCommandGetStartDataFeed                      |
| GetResumeDataFeedback                | ArbinCommandGetResumeDataFeed                     |
| GetSerialNumberFeedback              | ArbinCommandGetSerialNumberFeed                   |
| GetMITSVersionFeedback               | ArbinCommandGetServerSoftwareVersionNumberFeed    |

> Ignoring `ArbinCTI.Core` namespace in the second column for simplicity.

# Usage Examples
## Example 1: Feedback Accessing
```python
from ctitoolbox import BrowseDirectoryFeedback

def OnBrowseDirectoryBack(feedback):
    feedback = BrowseDirectoryFeedback(feedback)

    # access attributes
    result        = feedback.result
    dir_file_info = feedback.dir_file_info
    for i in range(len(dir_file_info)):
        info = dir_file_info[i]
        s = info.size
        l = info.last_modify_time

    # verify result by enum type
    if feedback.result == BrowseDirectoryFeedback.EResult.CTI_BROWSE_DIRECTORY_SUCCESS:

        # export as a JSON string
        print("Feedback instance:\n", feedback, "\n") 
        
        # export as a Python dictionary
        print("Python dictionary:\n", feedback.to_dict())
```

Output
```
Feedback instance
{
  "result": "CTI_BROWSE_DIRECTORY_SUCCESS",
  "dir_file_info": [
    {
      "type": 1,
      "parent_dir_path": "file1.txt",
      "size": 2048,
      "last_modify_time": "2024-01-01T12:00:00"
    },
    {
      "type": 0,
      "parent_dir_path": "folder1",
      "size": 0,
      "last_modify_time": "2024-01-02T15:30:00"
    }
  ]
}

Python dictionary: 
{'result': 'CTI_BROWSE_DIRECTORY_SUCCESS', 'dir_file_info': [{'type': 1, 'parent_dir_path': 'file1.txt', 'size': 2048, 'last_modify_time': '2024-01-01T12:00:00'}, {'type': 0, 'parent_dir_path': 'folder1', 'size': 0, 'last_modify_time': '2024-01-02T15:30:00'}]}
```

# Testing
Run unittest
```sh
python -m unittest
```

To view feedback output while running test, set env variable before running unittest:
- Windows Powershell
    ```sh
    $env:UNITTEST_VIEW_DICT="True"
    ```
- Linux Cmd
    ```sh
    UNITTEST_VIEW_DICT="True"
    ```

# To-Do
- Abstract feedback classes: base class with `to_dict` and `__repr__` definition.
- `CSTypeConvertor.to_cs_list` supports various types of iterables.
    - `PostApplyForUDPCommunication`: `List<CMetavariableDataCodeApply>`
