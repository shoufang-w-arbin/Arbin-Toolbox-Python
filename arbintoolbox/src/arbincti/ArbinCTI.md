# Supported ArbinCTI Objects
## General Objects
See [EXAMPLE.md](../../../EXAMPLE.md#arbin-object-creation) for detailed usage.

| Wrapper Class                                | Required By                        | Original Object                                           |
|----------------------------------------------|------------------------------------|-----------------------------------------------------------|
| ***Arguments***                              |                                    |                                                           |
| StartResumeEx                                | *PostStartChannelEx*               | StartResumeEx                                             |
| MetaVariableInfo                             | *PostGetMetaVariables*             | ArbinCommandGetMetaVariablesFeed.MetaVariableInfo         |
| MetaVariableInfoEx                           | *PostUpdateMetaVariableAdvancedEx* | MetaVariableInfoEx                                        |
| AssignBarcodeInfoFeedback.ChannelBarcodeInfo | *PostAssignBarcodeInfo*            | ArbinCommandAssignBarcodeInfoFeed.ChannelBarcodeInfo      |
| GetBarcodeInfoFeedback.GetChannelBarcodeInfo | *PostGetBarcodeInfo*               | ArbinCommandGetBarcodeInfoFeed.GetChannelBarcodeInfo      |
| CMetavariableDataCodeApply                   | *PostApplyForUDPCommunication*     | ArbinCommandCMetavariableDataCodeApply                    |
| TimeSensitiveSetMVArgs                       | *PostTimeSensitiveSetMV*           | ArbinCommandTimeSensitiveSetMVArgs                        |
| StartChannelAdvancedArgs                     | *PostStartChannelAdvanced*         | Common.Start.StartChannelAdvancedArgs                     |
| GetMappingAuxArgs                            | *PostGetMappingAux*                | Common.GetMappingAux.GetMappingAuxArgs                    |
| ModifyScheduleArgs                           | *PostModifySchedule*               | Common.ModifySchedule.ModifyScheduleArgs                  |
| ***Enum Class***                             |                                    |                                                           |
| NewOrDeleteFeedback.ENewOrDeleteType         | *PostNewOrDelete*                  | ArbinCommandNewOrDeleteFeed.NEW_OR_DELETE_TYPE            |
| UploadFileFeedback.UploadFileResult          | *PostUpLoadFile*                   | ArbinCommandUpLoadFileFeed.CUpLoadFileResult              |
| AssignFileFeedback.EFileKind                 | *PostAssignFile*                   | ArbinCommandAssignFileFeed.EFileKind                      |
| GetChannelDataFeedback.EGetChannelType       | *PostGetChannelsData*              | ArbinCommandGetChannelFeed.GET_CHANNEL_TYPE               |
| AssignBarcodeInfoFeedback.EChannelType       | *PostAssignBarcodeInfo*            | ArbinCommandAssignBarcodeInfoFeed.EChannelType            |
| GetBarcodeInfoFeedback.EChannelType          | *PostGetBarcodeInfo*               | ArbinCommandGetBarcodeInfoFeed.EChannelType               |

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

> Ignoring namespace `ArbinCTI.Core` in the second column for simplicity.