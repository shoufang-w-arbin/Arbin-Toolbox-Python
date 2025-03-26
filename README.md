# Supported ArbinCTI Objects
## General Objects
See [EXAMPLE.md](../../EXAMPLE.md#arbin-object-creation) for detailed usage.

### Argument and Feedback Objects
| Wrapper Class                       | Required By                    | Original Object                                      |
|-------------------------------------|--------------------------------|------------------------------------------------------|
| **Connection**                      |                                |                                                      |
| CreateArbinClientArgs               | Connect                        | ArbinClient.Core.CreateArbinClientArgs               |
| **Channel Management**              |                                |                                                      |
| ContinueChannelArgs                 | ContinueChannel                | ChannelManagement.ContinueChannelArgs                |
| JumpStepArgs                        | JumpStep                       | ChannelManagement.JumpStepArgs                       |
| ResumeChannelArgs                   | ResumeChannel                  | ChannelManagement.ResumeChannelArgs                  |
| StartChannelArgs                    | StartChannel                   | ChannelManagement.StartChannelArgs                   |
| StartChannelAdvancedArgs            | StartChannel                   | ChannelManagement.StartChannelAdvancedArgs           |
| StopChannelArgs                     | StopChannel                    | ChannelManagement.StopChannelArgs                    |
| **Formation Management**            |                                |                                                      |
| EngageTrayArgs                      | EngageTray                     | FormationManagement.EngageTrayArgs                   |
| GetEngagementStatusArgs             | GetEngagementStatus            | FormationManagement.GetEngagementStatusArgs          |
| **Request Information**             |                                |                                                      |
| GetBarcodeInfoArgs                  | GetBarcodeInfo                 | RequestInformation.GetBarcodeInfoArgs                |
| GetMappingAuxArgs                   | GetMappingAux                  | RequestInformation.GetMappingAuxArgs                 |
| GetMetaVariablesArgs                | GetMetaVariables               | RequestInformation.GetMetaVariableArgs               |
| GetMonitorDataArgs                  | GetMonitorData                 | RequestInformation.GetMonitorDataArgs                |
| GetResumeDataArgs                   | GetResumeData                  | RequestInformation.GetResumeDataArgs                 |
| GetStartDataArgs                    | GetStartData                   | RequestInformation.GetStartDataArgs                  |
| SubscribeChannelDataArgs            | SubscribeChannelData           | RequestInformation.SubscribeChannelDataArgs          |
| SubscribeDiagnosticEventDataArgs    | SubscribeDiagnosticEventData   | RequestInformation.SubscribeDiagnosticEventDataArgs  |
| SubscribeEventDataArgs              | SubscribeEventData             | RequestInformation.SubscribeEventDataArgs            |
| SubscribeMonitorDataArgs            | SubscribeMonitorData           | RequestInformation.SubscribeMonitorDataArgs          |
| SubscribeSPTTEQCELLDataArgs         | SubscribeSPTTEQCELLData        | RequestInformation.SubscribeSPTTEQCELLDataArgs       |
| SubscribeTestInfoDataArgs           | SubscribeTestInfoData          | RequestInformation.SubscribeTestInfoDataArgs         |
| **Test Management**                 |                                |                                                      |
| AssignBarcodeInfoArgs               | AssignBarcodeInfo              | TestManagement.AssignBarcodeInfoArgs                 |
| AssignFileArgs                      | AssignFile                     | TestManagement.AssignFileArgs                        |
| BrowseFileListArgs                  | BrowseFileList                 | TestManagement.BrowseFileListArgs                    |
| ModifyScheduleArgs                  | ModifySchedule                 | TestManagement.ModifySchedule                        |
| TimeSensitiveSetMVArgs              | TimeSensitiveSetMV             | TestManagement.TimeSensitiveSetMVArgs                |
| UpdateMetaVariablesArgs             | UpdateMetaVariables            | TestManagement.UpdateMetaVariableArgs                |
| UploadFileArgs                      | UploadFile                     | TestManagement.UploadFileArgs                        |

> Omitting namespace `Arbin.Library.DataModel` in the third columns for simplicity.

### Supplementary Objects
Additional objects and enums act as arguments to generate the above wrapper classes:

| Wrapper Class                          | Required By                            | Original Object                                      |
|----------------------------------------|----------------------------------------|------------------------------------------------------|
| Common objects............
|TimeSensitiveSetMVChannel| TimeSensitiveSetMVArgs| TestManagement.TimeSensitiveSetMVChannel|
| TimeSensitiveSetMV | TimeSensitiveSetMVChannel |TestManagement.TimeSensitiveSetMV|
| ChannelResumeData                       | ResumeChannelArgs,StartChannelArgs               | Common.ChannelResumeData                        |
| SPTTEngageTray                      | EngageTrayArgs                       | FormationManagement.SPTTEngageTray                       |

| ScheduleModifyInfo                     | ModifyScheduleArgs                     | Common.ModifySchedule.ModifyScheduleArgs             |
| AuxChannelRequirementBase              | ScheduleModifyInfo                     | Common.ModifySchedule.AuxChannelRequirementBase      |
| AuxChannelRequirement                  | ScheduleModifyInfo                     | Common.ModifySchedule.AuxChannelRequirement          |
| SafetyScope                            | AuxChannelRequirement, AuxSafetyRequirement | Common.ModifySchedule.SafetyScope               |

| **Enumeration**                     |                                |                                                      |

    EAIFileTyp| AssignFileArgs, BrowseFileListArgs|EAIFileTyp
    EBarcodeType|BarcodeInfo, GetBarcodeInfo|EBarcodeType
    EEngagementResult|SPTTEngageTray|EEngagementResult
    EFilterMonitorChannelType|GetMonitorDataArgs|EFilterMonitorChannelType
    EMetaVariableType| AIMetaVariableInfo|EMetaVariableType
    ETimeSensitiveMVUD |TimeSensitiveSetMV|ETimeSensitiveMVUD


> Omitting namespace `ArbinCTI.Core` in the third columns for simplicity.

## Feedback Objects
The wrapper classes
- Convert C# ArbinCTI feedback objects to Python objects, allowing easy access to attributes
- Offer quick inspection methods for these objects

See [EXAMPLE.md](../../../EXAMPLE.md#arbin-feedback-accessing) for detailed usage.

| Wrapper Class                         | Original Object                                   |
|---------------------------------------|---------------------------------------------------|
| ***Connection***                      |                                                   |
| LoginFeedback                         | ArbinCommandLoginFeed                             |
| LogicConnectFeedback                  | ArbinCommandLogicConnectFeed                      |
| ***Test Schedule***                   |                                                   |
| AssignScheduleFeedback                | ArbinCommandAssignScheduleFeed                    |
| AssignFileFeedback                    | ArbinCommandAssignFileFeed                        |
| SetMetaVariableFeedback               | ArbinCommandSetMetaVariableFeed                   |
| SetMetaVariableTimeSensitiveFeedback  | ArbinCommandTimeSensitiveSetMVFeed                |
| GetMetaVariableFeedback               | ArbinCommandGetMetaVariablesFeed                  |
| UpdateMetaVariableAdvancedFeedback    | ArbinCommandUpdateMetaVariableAdvancedFeed        |
| UpdateParameterFeedback               | ArbinCommandUpdateParamenterFeed                  |
| ModifyScheduleFeedback                | ArbinCommandModifyScheduleFeed                    |
| AssignBarcodeFeedback                 | ArbinCommandAssignBarcodeInfoFeed                 |
| GetBarcodeInfoFeedback                | ArbinCommandGetBarcodeInfoFeed                    |
| GetMachineTypeFeedback                | ArbinCommandGetMachineTypeFeed                    |
| GetTrayStatusFeedback                 | ArbinCommandGetTrayStatusFeed                     |
| EngageTrayFeedback                    | ArbinCommandEngageTrayFeed                        |
| SetIntervalTimeLogDataFeedback        | ArbinCommandSetIntervalTimeLogDataFeed            |
| ConvertToAnonymousOrNamedTOFeedback   | ArbinCommandConvertToAnonymousOrNamedTOFeed       |
| ***Channel Control***                 |                                                   |
| StartChannelFeedback                  | ArbinCommandStartChannelFeed                      |
| StartChannelAdvancedFeedback          | ArbinCommandStartChannelAdvancedFeed              |
| StopChannelFeedback                   | ArbinCommandStopChannelFeed                       |
| ResumeChannelFeedback                 | ArbinCommandResumeChannelFeed                     |
| JumpChannelFeedback                   | ArbinCommandJumpChannelFeed                       |
| ContinueChannelFeedback               | ArbinCommandContinueChannelFeed                   |
| ***File Operation***                  |                                                   |
| UploadFileFeedback                    | ArbinCommandUpLoadFileFeed                        |
| DownloadFileFeedback                  | ArbinCommandDownloadFileFeed                      |
| BrowseDirectoryFeedback               | ArbinCommandBrowseDirectoryFeed                   |
| CheckFileExistFeedback                | ArbinCommandCheckFileExFeed                       |
| NewFolderFeedback                     | ArbinCommandNewFolderFeed                         |
| DeleteFileFeedback                    | ArbinCommandDeleteFileFeed                        |
| NewOrDeleteFeedback                   | ArbinCommandNewOrDeleteFeed                       |
| ***Request Information***             |                                                   |
| GetChannelDataFeedback                | ArbinCommandGetChannelDataFeed                    |
| GetStartDataFeedback                  | ArbinCommandGetStartDataFeed                      |
| GetResumeDataFeedback                 | ArbinCommandGetResumeDataFeed                     |
| GetMappingAuxFeedback                 | ArbinCommandGetMappingAuxFeed                     |
| GetSerialNumberFeedback               | ArbinCommandGetSerialNumberFeed                   |
| GetChannelsDataMinimalistModeFeedback | ArbinCommandGetChannelDataMinimalistModeFeed      |
| GetChannelsDataSimpleModeFeedback     | ArbinCommandGetChannelDataSimpleModeFeed          |
| GetStringLimitLengthFeedback          | ArbinCommandGetStringLimitLengthFeed              |
| ***Miscellaneous***                   |                                                   |
| SendMsgToCTIFeedback                  | ArbinCommandSendMsgToCTIFeed                      |
| UnknownCommandFeedback                | ArbinCommandUnknownCommandFeed                    |
| StartAutomaticCalibrationFeedback     | ArbinCommandStartAutomaticCalibrationFeed         |


    EBarcodeResult,
    EUploadFileResult,

> Ignoring namespace `ArbinCTI.Core` in the second column for simplicity.