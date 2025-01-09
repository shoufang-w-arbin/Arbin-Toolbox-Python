# ArbinCTI Toolbox
## Table of Contents
- [About](#about)
- [Requirements](#requirements)
- [Installation](#installation)
- [Supported ArbinCTI Objects](#supported-arbincti-objects)
- [Usage Examples](#usage-examples) 
- [Testing](#testing)
- [To-Do](#to-do)

## About
Wrappers of C# objects, providing a smoother and more Pythonic programming experience for users who want to use ArbinCTI in Python.

### Background
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

mv1 = TimeSensitiveSetMV(TimeSensitiveSetMV.EMVUD.MVUD1, 12.3)
mv2 = TimeSensitiveSetMV(TimeSensitiveSetMV.EMVUD.MVUD2, 4.56)










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

### Additional Benefits
- **Keyword arguments** are allowed in this toolbox, compared to using `pythonnet` directly. 
- **Attributes are discoverable by Pylance**, reducing human error when programming. \
    ![](resource/pylance.png)

> We are adding more wrapper classes. If you require immediate implementation of a certain CTI object, please create an issue or submit a pull request with your work.

## Requirements
- 64-bit Python >= 3.7
- System
    - Windows: .NET Framework >=4.7.2
    - Linux: Mono is used by default

## Installation
```bash
pip install {path}/ctitoolbox-{version}-py3-none-any.whl
```

## Supported ArbinCTI Objects
### General Objects
The ArbinCTI wrapper provides Python classes for objects commonly used in ArbinCTI commands. These wrapper classes:
- Allow object creation using Pythonic syntax and handle conversion to C# objects internally
- Eliminate the need for direct C# syntax in your Python code

| Wrapper Class              | Original Object                                           |
|----------------------------|-----------------------------------------------------------|
| StartResumeEx              | StartResumeEx                                             |
| MetaVariableInfo           | ArbinCommandGetMetaVariablesFeed.MetaVariableInfo         |
| MetaVariableInfoEx         | MetaVariableInfoEx                                        |
| TimeSensitiveSetMVArgs     | ArbinCommandTimeSensitiveSetMVArgs                        |
| CMetavariableDataCodeApply | ArbinCommandCMetavariableDataCodeApply                    |

Additional Objects/Enums required for generating the above wrapper classes are also provided in this toolbox:

| Wrapper Class           | Original Object       | Required By                                                      |
|-------------------------|-----------------------|------------------------------------------------------------------|
| TE_DATA_TYPE            | TE_DATA_TYPE          | MetaVariableInfo, MetaVariableInfoEx, CMetavariableDataCodeApply |
| TimeSensitiveSetMV      | TimeSensitiveSetMV    | TimeSensitiveSetMVArgs                                           |

> Ignoring namespace `ArbinCTI.Core` in the second column for simplicity.

### Feedback Objects
The wrapper class provides a convenient way to work with ArbinCTI feedback objects in Python.
- Convert C# ArbinCTI feedback objects to Python objects
- Offer quick inspection methods for these objects

See [EXAMPLE.md](EXAMPLE.md#arbincti-feedback-accessing) for detailed usage.

| Wrapper Class                        | Original Object                                   |
|--------------------------------------|---------------------------------------------------|
| ***Connection***                     |                                                   |
| LoginFeedback                        | ArbinCommandLoginFeed                             |
| ***Test Schedule***                  |                                                   |
| AssignScheduleFeedback               | ArbinCommandAssignScheduleFeed                    |
| AssignFileFeedback                   | ArbinCommandAssignFileFeed                        |
| SetMetaVariableFeedback              | ArbinCommandSetMetaVariableFeed                   |
| SetMetaVariableTimeSensitiveFeedback | ArbinCommandTimeSensitiveSetMVFeed                |
| GetMetaVariableFeedback              | ArbinCommandGetMetaVariablesFeed                  |
| ***Channel Control***                |                                                   |
| StartChannelFeedback                 | ArbinCommandStartChannelFeed                      |
| StopChannelFeedback                  | ArbinCommandStopChannelFeed                       |
| ResumeChannelFeedback                | ArbinCommandResumeChannelFeed                     |
| JumpChannelFeedback                  | ArbinCommandJumpChannelFeed                       |
| ContinueChannelFeedback              | ArbinCommandContinueChannelFeed                   |
| ***File Operation***                 |                                                   |
| UploadFileFeedback                   | ArbinCommandUpLoadFileFeed                        |
| DownloadFileFeedback                 | ArbinCommandDownloadFileFeed                      |
| BrowseDirectoryFeedback              | ArbinCommandBrowseDirectoryFeed                   |
| CheckFileExistFeedback               | ArbinCommandCheckFileExFeed                       |
| NewFolderFeedback                    | ArbinCommandNewFolderFeed                         |
| DeleteFileFeedback                   | ArbinCommandDeleteFileFeed                        |
| NewOrDeleteFeedback                  | ArbinCommandNewOrDeleteFeed                       |
| ***Request Information***            |                                                   |
| GetChannelDataFeedback               | ArbinCommandGetChannelDataFeed                    |
| GetStartDataFeedback                 | ArbinCommandGetStartDataFeed                      |
| GetResumeDataFeedback                | ArbinCommandGetResumeDataFeed                     |
| GetSerialNumberFeedback              | ArbinCommandGetSerialNumberFeed                   |
| GetMITSVersionFeedback               | ArbinCommandGetServerSoftwareVersionNumberFeed    |

> Ignoring namespace `ArbinCTI.Core` in the second column for simplicity.
|--------------------------------------|---------------------------------------------------|
| ***Connection***                     |                                                   |
| LoginFeedback                        | ArbinCommandLoginFeed                             |
| ***Test Schedule***                  |                                                   |
| AssignScheduleFeedback               | ArbinCommandAssignScheduleFeed                    |
| AssignFileFeedback                   | ArbinCommandAssignFileFeed                        |
| SetMetaVariableFeedback              | ArbinCommandSetMetaVariableFeed                   |
| SetMetaVariableTimeSensitiveFeedback | ArbinCommandTimeSensitiveSetMVFeed                |
| GetMetaVariableFeedback              | ArbinCommandGetMetaVariablesFeed                  |
| ***Channel Control***                |                                                   |
| StartChannelFeedback                 | ArbinCommandStartChannelFeed                      |
| StopChannelFeedback                  | ArbinCommandStopChannelFeed                       |
| ResumeChannelFeedback                | ArbinCommandResumeChannelFeed                     |
| JumpChannelFeedback                  | ArbinCommandJumpChannelFeed                       |
| ContinueChannelFeedback              | ArbinCommandContinueChannelFeed                   |
| ***File Operation***                 |                                                   |
| UploadFileFeedback                   | ArbinCommandUpLoadFileFeed                        |
| DownloadFileFeedback                 | ArbinCommandDownloadFileFeed                      |
| BrowseDirectoryFeedback              | ArbinCommandBrowseDirectoryFeed                   |
| CheckFileExistFeedback               | ArbinCommandCheckFileExFeed                       |
| NewFolderFeedback                    | ArbinCommandNewFolderFeed                         |
| DeleteFileFeedback                   | ArbinCommandDeleteFileFeed                        |
| NewOrDeleteFeedback                  | ArbinCommandNewOrDeleteFeed                       |
| ***Request Information***            |                                                   |
| GetChannelDataFeedback               | ArbinCommandGetChannelDataFeed                    |
| GetStartDataFeedback                 | ArbinCommandGetStartDataFeed                      |
| GetResumeDataFeedback                | ArbinCommandGetResumeDataFeed                     |
| GetSerialNumberFeedback              | ArbinCommandGetSerialNumberFeed                   |
| GetMITSVersionFeedback               | ArbinCommandGetServerSoftwareVersionNumberFeed    |

> Ignoring namespace `ArbinCTI.Core` in the second column for simplicity.

## Usage Examples
Please see `EXAMPLE.md`.

## Testing
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

## To-Do
- `CSTypeConvertor.to_cs_list` supports various types of iterables.
    - `PostApplyForUDPCommunication`: `List<CMetavariableDataCodeApply>`
- Add original Enum value to the result for debugging.
- Detect Null object when initializing
