# Supported ArbinCTI Objects
## I. General Objects
| Wrapper Class                                | Required By                        | Original Object                                           |
|----------------------------------------------|------------------------------------|-----------------------------------------------------------|
| ***Arguments***                              |                                    |                                                           |
| AssignBarcodeInfoFeedback.ChannelBarcodeInfo | *PostAssignBarcodeInfo*            | ArbinCommandAssignBarcodeInfoFeed.ChannelBarcodeInfo      |
| CMetavariableDataCodeApply                   | *PostApplyForUDPCommunication*     | ArbinCommandCMetavariableDataCodeApply                    |
| GetBarcodeInfoFeedback.GetChannelBarcodeInfo | *PostGetBarcodeInfo*               | ArbinCommandGetBarcodeInfoFeed.GetChannelBarcodeInfo      |
| GetMappingAuxArgs                            | *PostGetMappingAux*                | Common.GetMappingAux.GetMappingAuxArgs                    |
| MetaVariableInfo                             | *PostGetMetaVariables*             | ArbinCommandGetMetaVariablesFeed.MetaVariableInfo         |
| MetaVariableInfoEx                           | *PostUpdateMetaVariableAdvancedEx* | MetaVariableInfoEx                                        |
| ModifyScheduleArgs                           | *PostModifySchedule*               | Common.ModifySchedule.ModifyScheduleArgs                  |
| StartChannelAdvancedArgs                     | *PostStartChannelAdvanced*         | Common.Start.StartChannelAdvancedArgs                     |
| StartResumeEx                                | *PostStartChannelEx*               | StartResumeEx                                             |
| TimeSensitiveSetMVArgs                       | *PostTimeSensitiveSetMV*           | ArbinCommandTimeSensitiveSetMVArgs                        |
| ***Enum Class***                             |                                    |                                                           |
| AssignBarcodeInfoFeedback.EChannelType       | *PostAssignBarcodeInfo*            | ArbinCommandAssignBarcodeInfoFeed.EChannelType            |
| AssignFileFeedback.EFileKind                 | *PostAssignFile*                   | ArbinCommandAssignFileFeed.EFileKind                      |
| GetBarcodeInfoFeedback.EChannelType          | *PostGetBarcodeInfo*               | ArbinCommandGetBarcodeInfoFeed.EChannelType               |
| GetChannelDataFeedback.EGetChannelType       | *PostGetChannelsData*              | ArbinCommandGetChannelFeed.GET_CHANNEL_TYPE               |
| NewOrDeleteFeedback.ENewOrDeleteType         | *PostNewOrDelete*                  | ArbinCommandNewOrDeleteFeed.NEW_OR_DELETE_TYPE            |
| UploadFileFeedback.UploadFileResult          | *PostUpLoadFile*                   | ArbinCommandUpLoadFileFeed.CUpLoadFileResult              |

### Supplementary Objects
Additional objects and enums act as arguments to generate the above wrapper classes:

| Wrapper Class                          | Required By                            | Original Object                                      |
|----------------------------------------|----------------------------------------|------------------------------------------------------|
| AuxChannelRequirement                  | ScheduleModifyInfo                     | Common.ModifySchedule.AuxChannelRequirement          |
| AuxChannelRequirementBase              | ScheduleModifyInfo                     | Common.ModifySchedule.AuxChannelRequirementBase      |
| SafetyScope                            | AuxChannelRequirement, AuxSafetyRequirement | Common.ModifySchedule.SafetyScope               |
| ScheduleModifyInfo                     | ModifyScheduleArgs                     | Common.ModifySchedule.ModifyScheduleArgs             |
| StartChannelInfo                       | StartChannelAdvancedArgs               | Common.Start.StartChannelInfo                        |
| TE_DATA_TYPE                           | MetaVariableInfo, MetaVariableInfoEx, CMetavariableDataCodeApply | TE_DATA_TYPE               |
| TestObjectSetting                      | StartChannelInfo                       | Common.Start.TestObjectSetting                       |
| TimeSensitiveSetMV                     | TimeSensitiveSetMVArgs                 | TimeSensitiveSetMV                                   |

> Omitting namespace `ArbinCTI.Core` in the third columns for simplicity.

## II. Feedback Objects
The wrapper classes
- Convert C# ArbinCTI feedback objects to Python objects, allowing easy access to attributes
- Full serializability with quick inspection methods for these objects

| Wrapper Class                         | Original Object                                   |
|---------------------------------------|---------------------------------------------------|
| ***Connection***                      |                                                   |
| LogicConnectFeedback                  | ArbinCommandLogicConnectFeed                      |
| LoginFeedback                         | ArbinCommandLoginFeed                             |
| ***Test Schedule***                   |                                                   |
| AssignBarcodeFeedback                 | ArbinCommandAssignBarcodeInfoFeed                 |
| AssignFileFeedback                    | ArbinCommandAssignFileFeed                        |
| AssignScheduleFeedback                | ArbinCommandAssignScheduleFeed                    |
| ConvertToAnonymousOrNamedTOFeedback   | ArbinCommandConvertToAnonymousOrNamedTOFeed       |
| EngageTrayFeedback                    | ArbinCommandEngageTrayFeed                        |
| GetBarcodeInfoFeedback                | ArbinCommandGetBarcodeInfoFeed                    |
| GetMachineTypeFeedback                | ArbinCommandGetMachineTypeFeed                    |
| GetMetaVariableFeedback               | ArbinCommandGetMetaVariablesFeed                  |
| GetTrayStatusFeedback                 | ArbinCommandGetTrayStatusFeed                     |
| ModifyScheduleFeedback                | ArbinCommandModifyScheduleFeed                    |
| SetIntervalTimeLogDataFeedback        | ArbinCommandSetIntervalTimeLogDataFeed            |
| SetMetaVariableFeedback               | ArbinCommandSetMetaVariableFeed                   |
| SetMetaVariableTimeSensitiveFeedback  | ArbinCommandTimeSensitiveSetMVFeed                |
| UpdateMetaVariableAdvancedFeedback    | ArbinCommandUpdateMetaVariableAdvancedFeed        |
| UpdateParameterFeedback               | ArbinCommandUpdateParamenterFeed                  |
| ***Channel Control***                 |                                                   |
| ContinueChannelFeedback               | ArbinCommandContinueChannelFeed                   |
| JumpChannelFeedback                   | ArbinCommandJumpChannelFeed                       |
| ResumeChannelFeedback                 | ArbinCommandResumeChannelFeed                     |
| StartChannelAdvancedFeedback          | ArbinCommandStartChannelAdvancedFeed              |
| StartChannelFeedback                  | ArbinCommandStartChannelFeed                      |
| StopChannelFeedback                   | ArbinCommandStopChannelFeed                       |
| ***File Operation***                  |                                                   |
| BrowseDirectoryFeedback               | ArbinCommandBrowseDirectoryFeed                   |
| CheckFileExistFeedback                | ArbinCommandCheckFileExFeed                       |
| DeleteFileFeedback                    | ArbinCommandDeleteFileFeed                        |
| DownloadFileFeedback                  | ArbinCommandDownloadFileFeed                      |
| NewFolderFeedback                     | ArbinCommandNewFolderFeed                         |
| NewOrDeleteFeedback                   | ArbinCommandNewOrDeleteFeed                       |
| UploadFileFeedback                    | ArbinCommandUpLoadFileFeed                        |
| ***Request Information***             |                                                   |
| GetChannelDataFeedback                | ArbinCommandGetChannelDataFeed                    |
| GetChannelInfoExFeedback              | ArbinCommandGetChannelInfoExFeed                  |
| GetChannelsDataMinimalistModeFeedback | ArbinCommandGetChannelDataMinimalistModeFeed      |
| GetChannelsDataSimpleModeFeedback     | ArbinCommandGetChannelDataSimpleModeFeed          |
| GetMappingAuxFeedback                 | ArbinCommandGetMappingAuxFeed                     |
| GetResumeDataFeedback                 | ArbinCommandGetResumeDataFeed                     |
| GetSerialNumberFeedback               | ArbinCommandGetSerialNumberFeed                   |
| GetStartDataFeedback                  | ArbinCommandGetStartDataFeed                      |
| GetStringLimitLengthFeedback          | ArbinCommandGetStringLimitLengthFeed              |
| ***Miscellaneous***                   |                                                   |
| SendMsgToCTIFeedback                  | ArbinCommandSendMsgToCTIFeed                      |
| StartAutomaticCalibrationFeedback     | ArbinCommandStartAutomaticCalibrationFeed         |
| UnknownCommandFeedback                | ArbinCommandUnknownCommandFeed                    |

> Omitting namespace `ArbinCTI.Core` in the second column for simplicity.