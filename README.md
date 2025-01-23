# ArbinCTI Toolbox
## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Supported ArbinCTI Objects](#supported-arbincti-objects)
- [Usage Examples](#usage-examples)
- [Developing `ctitoolbox`](#developing-ctitoolbox)
    - [Requirements](#requirements)
    - [Testing](#testing)
    - [To-Do](#to-do)

## About
Wrappers of C# objects built on top of Pythonnet, providing a smoother and more Pythonic programming experience for users who want to use ArbinCTI in Python.

### Background
When calling `public bool PostTimeSensitiveSetMV(IArbinSocket socket, TimeSensitiveSetMVArgs args)`, creating a `TimeSensitiveSetMVArgs` object in Python without the toolbox can be quite cumbersome:

![](resource/compare.png)

As you can see, the toolbox provides a smoother and more Pythonic way to interact with C# objects, making your code cleaner and easier to maintain.

### Additional Benefits
- **Py-C# Data structure conversions** are backed by `CSTypeConverter` in this toolbox.
- **Keyword arguments are allowed**, compared to using `pythonnet` directly. 
- **Object Attributes are discoverable by Pylance**, reducing human error when programming. \
    ![](resource/pylance.png)

> We are adding more wrapper classes. If you require immediate implementation of a certain CTI object, please create an issue or submit a pull request with your work.

## Installation
### Requirements
- 64-bit Python >= 3.7
- System
    - Windows: .NET Framework >=4.7.2
    - Linux: Mono is used by default
- ArbinCTI permission on MITS
### Install from Wheel
```bash
pip install dist/ctitoolbox-{version}-py3-none-any.whl
```

## Supported ArbinCTI Objects
### General Objects
The ArbinCTI wrapper provides Python classes for objects commonly used in ArbinCTI commands. These wrapper classes allow object creation using Pythonic syntax and handle conversion to C# objects internally. 

See [EXAMPLE.md](EXAMPLE.md#arbincti-object-creation) for detailed usage.

| Wrapper Class                          | Required By                            | Original Object                                           |
|----------------------------------------|----------------------------------------|-----------------------------------------------------------|
| ***Arguments***                        |                                        |                                                           | 
| StartResumeEx                          | *PostStartChannelEx*                   | StartResumeEx                                             |
| MetaVariableInfo                       | *PostGetMetaVariables*                 | ArbinCommandGetMetaVariablesFeed.MetaVariableInfo         |
| MetaVariableInfoEx                     | *PostUpdateMetaVariableAdvancedEx*     | MetaVariableInfoEx                                        |
| TimeSensitiveSetMVArgs                 | *PostTimeSensitiveSetMV*               | ArbinCommandTimeSensitiveSetMVArgs                        |
| StartChannelAdvancedArgs               | *PostStartChannelAdvanced*             | Common.Start.StartChannelAdvancedArgs                     |
|GetMappingAuxArgs| *PostGetMappingAux* |Common.GetMappingAux.GetMappingAuxArgs|
| CMetavariableDataCodeApply             | *PostApplyForUDPCommunication*         | ArbinCommandCMetavariableDataCodeApply                    |
| ***Enum Class***                       |                                        |                                                           | 
| NewOrDeleteFeedback.ENewOrDeleteType   | *PostNewOrDelete*                      | ArbinCommandNewOrDeleteFeed.NEW_OR_DELETE_TYPE            |
| UploadFileFeedback.UploadFileResult    | *PostUpLoadFile*                       | ArbinCommandUpLoadFileFeed.CUpLoadFileResult              |
| AssignFileFeedback.EFileKind           | *PostAssignFile*                       | ArbinCommandAssignFileFeed.EFileKind                      |
| GetChannelDataFeedback.EGetChannelType | *PostGetChannelsData*                  | ArbinCommandGetChannelFeed.GET_CHANNEL_TYPE               |

### Additional Objects/Enums
Additional Objects/Enums required for generating the above wrapper classes and sending ArbinCTI commands are also provided in this toolbox:

| Wrapper Class                          | Required By                            | Original Object                                      |
|----------------------------------------|----------------------------------------|------------------------------------------------------|
| TE_DATA_TYPE                           | MetaVariableInfo, MetaVariableInfoEx, CMetavariableDataCodeApply | TE_DATA_TYPE               |
| TimeSensitiveSetMV                     | TimeSensitiveSetMVArgs                 | TimeSensitiveSetMV                                   |
| TestObjectSetting                      | StartChannelInfo          | Common.Start.TestObjectSetting                       |
| StartChannelInfo                       | StartChannelAdvancedArgs  | Common.Start.StartChannelInfo                        |

> Ignoring namespace `ArbinCTI.Core` in the third columns for simplicity.

### Feedback Objects
The wrapper class provides a convenient way to work with ArbinCTI feedback objects in Python.
- Convert C# ArbinCTI feedback objects to Python objects
- Offer quick inspection methods for these objects

See [EXAMPLE.md](EXAMPLE.md#arbincti-feedback-accessing) for detailed usage.

| Wrapper Class                        | Original Object                                   |
|--------------------------------------|---------------------------------------------------|
| ***Connection***                     |                                                   |
| LoginFeedback                        | ArbinCommandLoginFeed                             |
| LogicConnectFeedback                 | ArbinCommandLogicConnectFeed                      |
| ***Test Schedule***                  |                                                   |
| AssignScheduleFeedback               | ArbinCommandAssignScheduleFeed                    |
| AssignFileFeedback                   | ArbinCommandAssignFileFeed                        |
| SetMetaVariableFeedback              | ArbinCommandSetMetaVariableFeed                   |
| SetMetaVariableTimeSensitiveFeedback | ArbinCommandTimeSensitiveSetMVFeed                |
| GetMetaVariableFeedback              | ArbinCommandGetMetaVariablesFeed                  |
| UpdateParameterFeedback              | ArbinCommandUpdateParamenterFeed                  |
| ***Channel Control***                |                                                   |
| StartChannelFeedback                 | ArbinCommandStartChannelFeed                      |
| StopChannelFeedback                  | ArbinCommandStopChannelFeed                       |
| ResumeChannelFeedback                | ArbinCommandResumeChannelFeed                     |
| JumpChannelFeedback                  | ArbinCommandJumpChannelFeed                       |
| ContinueChannelFeedback              | ArbinCommandContinueChannelFeed                   |
| StartChannelAdvancedFeedback         | ArbinCommandStartChannelAdvancedFeed              |
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
| GetMappingAuxFeedback                | ArbinCommandGetMappingAuxFeed                     |
| GetSerialNumberFeedback              | ArbinCommandGetSerialNumberFeed                   |
| GetMITSVersionFeedback               | ArbinCommandGetServerSoftwareVersionNumberFeed    |

> Ignoring namespace `ArbinCTI.Core` in the second column for simplicity.

## Usage Examples
Please see [EXAMPLE.md](EXAMPLE.md).

## Developing `ctitoolbox`
### Testing
To run unittest
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

### To-Do
- Add original Enum value to the result for debugging.
