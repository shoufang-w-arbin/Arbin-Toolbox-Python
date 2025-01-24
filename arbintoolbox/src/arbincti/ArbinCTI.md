# Supported ArbinCTI Objects
## General Objects
See [EXAMPLE.md](../../../EXAMPLE.md#arbin-object-creation) for detailed usage.

| Wrapper Class                          | Required By                            | Original Object                                           |
|----------------------------------------|----------------------------------------|-----------------------------------------------------------|
| ***Arguments***                        |                                        |                                                           | 
| StartResumeEx                          | *PostStartChannelEx*                   | StartResumeEx                                             |
| MetaVariableInfo                       | *PostGetMetaVariables*                 | ArbinCommandGetMetaVariablesFeed.MetaVariableInfo         |
| MetaVariableInfoEx                     | *PostUpdateMetaVariableAdvancedEx*     | MetaVariableInfoEx                                        |
| CMetavariableDataCodeApply             | *PostApplyForUDPCommunication*         | ArbinCommandCMetavariableDataCodeApply                    |
| TimeSensitiveSetMVArgs                 | *PostTimeSensitiveSetMV*               | ArbinCommandTimeSensitiveSetMVArgs                        |
| StartChannelAdvancedArgs               | *PostStartChannelAdvanced*             | Common.Start.StartChannelAdvancedArgs                     |
| GetMappingAuxArgs                      | *PostGetMappingAux*                    | Common.GetMappingAux.GetMappingAuxArgs                    |
| ModifyScheduleArgs                     | *PostModifySchedule*                   | Common.ModifySchedule.ModifyScheduleArgs                  |
| ***Enum Class***                       |                                        |                                                           | 
| NewOrDeleteFeedback.ENewOrDeleteType   | *PostNewOrDelete*                      | ArbinCommandNewOrDeleteFeed.NEW_OR_DELETE_TYPE            |
| UploadFileFeedback.UploadFileResult    | *PostUpLoadFile*                       | ArbinCommandUpLoadFileFeed.CUpLoadFileResult              |
| AssignFileFeedback.EFileKind           | *PostAssignFile*                       | ArbinCommandAssignFileFeed.EFileKind                      |
| GetChannelDataFeedback.EGetChannelType | *PostGetChannelsData*                  | ArbinCommandGetChannelFeed.GET_CHANNEL_TYPE               |

### Supplementary Objects
Additional objects and enums act as arguments to generate the above wrapper classes:

| Wrapper Class                          | Required By                            | Original Object                                      |
|----------------------------------------|----------------------------------------|------------------------------------------------------|
| TE_DATA_TYPE                           | MetaVariableInfo, MetaVariableInfoEx, CMetavariableDataCodeApply | TE_DATA_TYPE               |
| TimeSensitiveSetMV                     | TimeSensitiveSetMVArgs                 | TimeSensitiveSetMV                                   |
| StartChannelInfo                       | StartChannelAdvancedArgs               | Common.Start.StartChannelInfo                        |
| TestObjectSetting                      | StartChannelInfo                       | Common.Start.TestObjectSetting                       |
| ScheduleModifyInfo                     | ModifyScheduleArgs                     | Common.ModifySchedule.ModifyScheduleArgs             |
| AuxChannelRequirementBase              | ScheduleModifyInfo                     | Common.ModifySchedule.AuxChannelRequirementBase      |
| AuxChannelRequirement                  | ScheduleModifyInfo                     | Common.ModifySchedule.AuxChannelRequirement          |
| SafetyScope                            | AuxChannelRequirement, AuxSafetyRequirement | Common.ModifySchedule.SafetyScope               |

> Ignoring namespace `ArbinCTI.Core` in the third columns for simplicity.

## Feedback Objects
The wrapper classes
- Convert C# ArbinCTI feedback objects to Python objects, allowing easy access to attributes
- Offer quick inspection methods for these objects

See [EXAMPLE.md](../../../EXAMPLE.md#arbin-feedback-accessing) for detailed usage.

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
| ModifyScheduleFeedback               | ArbinCommandModifyScheduleFeed                    |
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