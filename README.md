# Supported ArbinCTI Objects
## I. General Objects
### Argument and Feedback Objects
| Wrapper Class                       | Required By                    | Original Object                                      |
|-------------------------------------|--------------------------------|------------------------------------------------------|
| ***Connection***                    |                                |                                                      |
| CreateArbinClientArgs               | Connect                        | ArbinClient.Core.CreateArbinClientArgs               |
| ***Channel Management***            |                                |                                                      |
| ContinueChannelArgs                 | ContinueChannel                | ChannelManagement.ContinueChannelArgs                |
| JumpStepArgs                        | JumpStep                       | ChannelManagement.JumpStepArgs                       |
| ResumeChannelArgs                   | ResumeChannel                  | ChannelManagement.ResumeChannelArgs                  |
| StartChannelArgs                    | StartChannel                   | ChannelManagement.StartChannelArgs                   |
| StartChannelAdvancedArgs            | StartChannel                   | ChannelManagement.StartChannelAdvancedArgs           |
| StopChannelArgs                     | StopChannel                    | ChannelManagement.StopChannelArgs                    |
| ***Formation Management***          |                                |                                                      |
| EngageTrayArgs                      | EngageTray                     | FormationManagement.EngageTrayArgs                   |
| GetEngagementStatusArgs             | GetEngagementStatus            | FormationManagement.GetEngagementStatusArgs          |
| ***Request Information***           |                                |                                                      |
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
| ***Test Management***               |                                |                                                      |
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

| Wrapper Class                | Required By                            | Original Object                          |
|------------------------------|----------------------------------------|------------------------------------------|
| AIMetaVariableInfo           | GetMetaVariablesArgs                   | Common.AIMetaVariableInfo                |
| AuxChannelRequirement        | ScheduleModifyInfo                     | TestManagement.AuxChannelRequirement     |
| AuxChannelRequirementBase    | ScheduleModifyInfo                     | TestManagement.AuxChannelRequirementBase |
| AuxSafetyRequirement         | ScheduleModifyInfo                     | TestManagement.AuxSafetyRequirement      |
| BarcodeInfo                  | AssignBarcodeInfoArgs                  | Common.BarcodeInfo                       |
| ChannelResumeData            | ResumeChannelArgs, StartChannelArgs    | ChannelManagement.ChannelResumeData      |
| GetBarcodeInfo               | GetBarcodeInfoArgs                     | Common.BarcodeInfo                       |
| SafetyScope                  | AuxChannelRequirement, AuxSafetyRequirement | TestManagement.SafetyScope          |
| ScheduleModifyInfo           | ModifyScheduleArgs                     | TestManagement.ModifyScheduleArgs        |
| SPTTEngageTray               | EngageTrayArgs                         | FormationManagement.SPTTEngageTray       |
| TimeSensitiveSetMV           | TimeSensitiveSetMVChannel              | TestManagement.TimeSensitiveSetMV        |
| TimeSensitiveSetMVChannel    | TimeSensitiveSetMVArgs                 | TestManagement.TimeSensitiveSetMVChannel |
| ***Enumeration***              |                                        |                                          |
| EAIFileType                  | AssignFileArgs, BrowseFileListArgs     | EAIFileType                              |
| EBarcodeType                 | BarcodeInfo, GetBarcodeInfo            | EBarcodeType                             |
| EEngagementResult            | SPTTEngageTray                         | EEngagementResult                        | 
| EFilterMonitorChannelType    | GetMonitorDataArgs                     | EFilterMonitorChannelType                |
| EMetaVariableType            | AIMetaVariableInfo                     | EMetaVariableType                        |
| ETimeSensitiveMVUD           | TimeSensitiveSetMV                     | ETimeSensitiveMVUD                       |

> Omitting namespace `Arbin.Library.DataModel` in the third columns for simplicity.

## II. Feedback Objects
The wrapper classes
- Convert C# ArbinCTI feedback objects to Python objects, allowing easy access to attributes
- Full serializability with quick inspection methods for these objects

| Wrapper Class                         | Original Object                                   |
|---------------------------------------|---------------------------------------------------|
| ***Connection***                      |                                                   |
| LoginFeedback                         | RequestInformation.LoginFDBK                      |
| ***Channel Control***                 |                                                   |
| ContinueChannelFeedback               | ChannelManagement.ContinueChannelFDBK             |
| JumpChannelFeedback                   | ChannelManagement.ResumeChannelFDBK               |
| ResumeChannelFeedback                 | ChannelManagement.JumpStepFDBK                    |
| StartChannelFeedback                  | ChannelManagement.StartChannelFDBK                |
| StopChannelFeedback                   | ChannelManagement.StopChannelFDBK                 |
| ***Formation Management***            |                                                   |
| EngageTrayFeedback                    | FormationManagement.EngageTrayFDBK                |
| GetEngagementStatusFeedback           | FormationManagement.GetEngagementStatusFDBK       |
| ***Request Information***             |                                                   |
| GetBarcodeInfoFeedback                | RequestInformation.GetBarcodeInfoFeedbakc         |
| GetMappingAuxFeedback                 | RequestInformation.GetMappingAuxFDBK              |
| GetMonitorDataFeedback                | RequestInformation.GetMonitorDataFDBK             |
| GetResumeDataFeedback                 | RequestInformation.GetResumeDataFDBK              |
| GetStartDataFeedback                  | RequestInformation.GetStartDataFDBK               |
| SubscribeChannelDataFeedback          | RequestInformation.SubscribeChannelDataFDBK       |
| SubscribeDiagnosticEventDataFeedback  | RequestInformation.SubscribeDiagnosticEventDataFDBK |
| SubscribeEventDataFeedback            | RequestInformation.SubscribeEventDataFDBK         |
| SubscribeMonitorDataFeedback          | RequestInformation.SubscribeMonitorDataFDBK       |
| SubscribeSPTTEQCellDataFeedback       | RequestInformation.SubscribeSPTTEQCellDataFDBK    |
| SubscribeTestInfoDataFeedback         | RequestInformation.SubscribeTestInfoDataFDBK      |
| ***Test Managemet***                  |                                                   |
| AssignBarcodeInfoFeedback             | TestManagement.AssignBarcodeInfoFDBK              |
| AssignFileFeedback                    | TestManagement.AssignFileFDBK                     |
| BrowseFileListFeedback                | TestManagement.BrowseFileListFDBK                 |
| GetMetaVariablesFeedback              | TestManagement.GetMetaVariablesFDBK               |
| TimeSensitiveSetMVFeedback            | TestManagement.TimeSensitiveSetMVFDBK             |
| UpdateMetaVariableFeedback            | TestManagement.UpdateMetaVariableFDBK             |

> Omitting namespace `Arbin.Library.DataModel` in the second column for simplicity.
