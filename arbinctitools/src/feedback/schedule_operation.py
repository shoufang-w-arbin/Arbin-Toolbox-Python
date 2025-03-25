import ArbinCTI.Core as ArbinCTI # type: ignore

from arbinctitools.src.common.base import (
    DictReprBase,
    SafeIntEnumBase
)
from arbinctitools.src.argument.argument import (
    TimeSensitiveSetMV,
    TE_DATA_TYPE,
    MetaVariableInfoEx,
)

"""""""""""""""""""""""""""
Schedule Operation
- AssignScheduleFeedback
- AssignFileFeedback
- SetMetaVariableFeedback
- SetMetaVariableTimeSensitiveFeedback
- GetMetaVariableFeedback
- UpdateMetaVariableAdvancedFeedback
- UpdateParameterFeedback
- ModifyScheduleFeedback
- AssignBarcodeInfoFeedback
- GetBarcodeInfoFeedback
- GetMachineTypeFeedback
- GetTrayStatusFeedback
- EngageTrayFeedback
- SetIntervalTimeLogDataFeedback
- ConvertToAnonymousOrNamedTOFeedback
"""""""""""""""""""""""""""
class AssignScheduleFeedback(DictReprBase):
    class EAssignToken(SafeIntEnumBase):
        CTI_ASSIGN_SUCCESS = 0
        CTI_ASSIGN_INDEX = 0x10
        CTI_ASSIGN_ERROR = 0x11
        CTI_ASSIGN_SCHEDULE_NAME_EMPTY_ERROR = 0x12
        CTI_ASSIGN_SCHEDULE_NOT_FIND_ERROR = 0x13
        CTI_ASSIGN_CHANNEL_RUNNING_ERROR = 0x14
        CTI_ASSIGN_CHANNEL_DOWNLOAD_ERROR = 0x15
        CTI_ASSIGN_BACTH_FILE_OPENED = 0x16
        CTI_ASSIGN_SDU_CANNOT_ASSIGN_SCHEDULE = 0x17
        CTI_ASSIGN_SDU_SAVE_FAILED = 0x18
        CTI_ASSIGN_FILE_UNSUPPORTED_FILE_TYPE = 0x19
        CTI_ASSIGN_FILE_NOT_ASSIGN_SCHEDULE = 0x1A
        CTI_ASSIGN_FILE_SCHEDULE_NOT_AUX_REQUIREMENT = 0x1B
        CTI_ASSIGN_FILE_SCHEDULE_IS_RUNNING = 0x1C
        CTI_ASSIGN_SCHEDULE_MUID_NOT_SAME = 0x1D
        CTI_ASSIGN_SCHEDULE_CLEAR = 0x1E

    def __init__(self, feedback: ArbinCTI.ArbinCommandAssignScheduleFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandAssignScheduleFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandAssignScheduleFeed', got '{type(feedback)}'")
        self.result = AssignScheduleFeedback.EAssignToken(int(feedback.Result))

class AssignFileFeedback(DictReprBase):
    class EFileKind(SafeIntEnumBase):
        None_ = -1
        Schedule = 0
        CANBMS = 1
        SMB = 2
        Simulation = 3
        BatterySimulation = 4
        TestObject = 5
        Chart = 6
        BaseFileCount = 6
        FileKindCount = 7

        def to_cs(self) -> ArbinCTI.ArbinCommandAssignFileFeed.EFileKind:
            """Convert to C# ArbinCommandAssignFileFeed.EFileKind"""
            return ArbinCTI.ArbinCommandAssignFileFeed.EFileKind(self.value)

    class EAssignToken(SafeIntEnumBase):
        CTI_ASSIGN_SUCCESS = 0
        CTI_ASSIGN_FAILED = 1
        CTI_ASSIGN_INDEX = 0x10
        CTI_ASSIGN_ERROR = 0x11
        CTI_ASSIGN_FILE_NAME_EMPTY_ERROR = 0x12
        CTI_ASSIGN_FILE_NOT_FIND_ERROR = 0x13
        CTI_ASSIGN_CHANNEL_RUNNING_ERROR = 0x14
        CTI_ASSIGN_CHANNEL_DOWNLOAD_ERROR = 0x15
        CTI_ASSIGN_BACTH_FILE_OPENED = 0x16
        CTI_ASSIGN_FILE_CANNOT_ASSIGN = 0x17
        CTI_ASSIGN_FILE_SAVE_FAILED = 0x18
        CTI_ASSIGN_FILE_UNSUPPORTED_FILE_TYPE = 0x19
        CTI_ASSIGN_FILE_NOT_ASSIGN_SCHEDULE = 0x1A
        CTI_ASSIGN_FILE_SCHEDULE_NOT_AUX_REQUIREMENT = 0x1B
        CTI_ASSIGN_FILE_SCHEDULE_IS_RUNNING = 0x1C
        CTI_ASSIGN_SCHEDULE_MUID_NOT_SAME = 0x1D
        CTI_ASSIGN_FILE_CLEAR = 0x1E

    def __init__(self, feedback: ArbinCTI.ArbinCommandAssignFileFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandAssignFileFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandAssignFileFeed', got '{type(feedback)}'")
        self.result              = AssignFileFeedback.EAssignToken(int(feedback.Result))
        self.reason              = str(feedback.Reason)
        self.channel_list_result = self._unpack_cs_sorted_dict(
            feedback.ChanListResultPairs, 
            (AssignFileFeedback.EAssignToken, list)
        )
    
    def to_dict(self):
        _channel_list_result = dict()
        for key, value in self.channel_list_result.items():
            _channel_list_result[key.name] = value
        return {
            "result": self.result.name,
            "channel_list_result": _channel_list_result
        }
    
class SetMetaVariableFeedback(DictReprBase):
    class EResult(SafeIntEnumBase):
        CTI_SET_MV_SUCCESS = 0
        CTI_SET_MV_FAILED = 16
        CTI_SET_MV_METACODE_NOTEXIST = 17
        CTI_SET_MV_CHANNEL_NOT_STARTED = 18
        CTI_SET_MV_METACODE_NOTEXIST_Pro7 = 19

    def __init__(self, feedback: ArbinCTI.ArbinCommandSetMetaVariableFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandSetMetaVariableFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandSetMetaVariableFeed', got '{type(feedback)}'")
        self.result = SetMetaVariableFeedback.EResult(int(feedback.Result))
    
class SetMetaVariableTimeSensitiveFeedback(DictReprBase):
    class EControlStatus(SafeIntEnumBase):
        Idle = 0
        Transition = 1
        Charge = 2
        Discharge = 3
        Rest = 4
        Wait = 5
        External_Charge = 6
        Calibration = 7
        Unsafe = 8
        Pulse = 9
        Internal_Resistance = 10
        AC_Impedance = 11
        ACI_Cell = 12
        Test_Settings = 13
        Error = 14
        Finished = 15
        Volt_Meter = 16
        Waiting_for_ACS = 17
        Pause = 18
        EMPTY = 19
        Idle_from_MCU = 20
        Start = 21
        Running = 22
        Step_Transfer = 23
        Resume = 24
        Go_Pause = 25
        Go_Stop = 26
        Go_Next_Step = 27
        Online_Update = 28
        Daq_Memory_Unsafe = 29
        ACR = 30
        CS_SUSPENT = 31

    class EResult(SafeIntEnumBase):
        SUCCESS = 0
        SUCCESS_NOTRUNNING = 1
        ERROR = 0x10
        DATATYPE_NOTSUPPORT = 0x11
        METACODE_NOTEXIST = 0x12
        CHANNEL_INDEX_ERROR = 0x13
        AUX_INDEX_ERROR = 0x14
        AUX_NOTASSIGN = 0x15
        CANBMS_INDEX_ERROR = 0x16
        CANBMS_NOTEXIST = 0x17
        CANBMS_DISABLED = 0x18
        NOT_CONNECT_DAQ = 0x19
        TIMEOUT = 0x1A
        MCU_ACK_FAILED = 0x1B
        NOT_ALLOW_CONTROL = 0x1C
        MCU_SOCKET_DISCONNECTED = 0x1D
 
    class TimeSensitiveSetMVResult(DictReprBase):
        def __init__(self, result: ArbinCTI.ArbinCommandTimeSensitiveSetMVFeed.TimeSensitiveSetMVResult):
            self.global_index   = int(result.GlobalIndex)
            self.step_index     = int(result.StepIndex)
            self.sub_step_index = int(result.SubStepIndex)
            self.machine_status = SetMetaVariableTimeSensitiveFeedback.EControlStatus(int(result.MachineStatus))
            self.result         = SetMetaVariableTimeSensitiveFeedback.EResult(int(result.Result))
            self.current        = float(result.Current)
            self.voltage        = float(result.Voltage)
            self.mvs            = [TimeSensitiveSetMV(mv) for mv in result.MVs]

    def __init__(self, feedback: ArbinCTI.ArbinCommandTimeSensitiveSetMVFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandTimeSensitiveSetMVFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandTimeSensitiveSetMVFeed', got '{type(feedback)}'")
        self.results = [SetMetaVariableTimeSensitiveFeedback.TimeSensitiveSetMVResult(result) for result in feedback.Results]

class GetMetaVariableFeedback(DictReprBase):
    class EResult(SafeIntEnumBase):
        CTI_GET_MV_SUCCESS = 0x0
        CTI_GET_MV_ERROR = 0x10
        CTI_GET_MV_DATATYPE_NOTSUPPORT = 0x11
        CTI_GET_MV_METACODE_NOTEXIST = 0x12
        CTI_GET_MV_CHANNEL_INDEX_ERROR = 0x13
        CTI_GET_MV_AUX_INDEX_ERROR = 0x14
        CTI_GET_MV_AUX_NOTASSIGN = 0x15
        CTI_GET_MV_CANBMS_INDEX_ERROR = 0x16
        CTI_GET_MV_CANBMS_NOTEXIST = 0x17
        CTI_GET_MV_CANBMS_DISABLED = 0x18
        CTI_GET_MV_NOT_CONNECT_DAQ = 0x19
        CTI_GET_MV_TIMEOUT = 0x1A
        CTI_GET_MV_MCU_ACK_FAILED = 0x1B
        CTI_GET_MV_METACODE_NOTSUPPORT = 0x1C
        CTI_GET_MV_SMB_NOTEXIST = 0x1D
        CTI_GET_MV_SMB_INDEX_ERROR = 0x1E
        CTI_GET_MV_SMB_NOTSUPPORT_STRING = 0x1F
        CTI_GET_MV_SMB_DISABLED = 0x20
        CTI_GET_MV_AUX_TYPE_ERROR = 0x21
        CTI_GET_MV_OBJ_NULL_ERROR = 0x22
        CTI_GET_MV_DCOM_ERROR = 0x23
        CTI_GET_MV_WRITE_NOT_SUPPORTED = 0x24
        CTI_GET_MV_EQ_INDEX_ERROR = 0x25
        CTI_GET_MV_CELL_INDEX_ERROR = 0x26

    class MetaVariableInfo(DictReprBase):
        def __init__(self, info: ArbinCTI.ArbinCommandGetMetaVariablesFeed.MetaVariableInfo):
            self.channel_index = int(info.m_Channel)
            self.mv_error      = GetMetaVariableFeedback.EResult(int(info.m_MV_Error))
            self.mv_data_type  = TE_DATA_TYPE(int(info.m_MV_DataType))
            self.mv_meta_code  = int(info.m_MV_MetaCode)
            self.value         = float(info.m_Value)
    
    def __init__(self, feedback: ArbinCTI.ArbinCommandGetMetaVariablesFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandGetMetaVariablesFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandGetMetaVariablesFeed', got '{type(feedback)}'")
        self.meta_variable_info = [GetMetaVariableFeedback.MetaVariableInfo(info) for info in feedback.MetaVariableInfos]

class UpdateMetaVariableAdvancedFeedback(DictReprBase):
    class ESetMVResult(SafeIntEnumBase):
        CTI_SET_MV_SUCCESS = 0
        CTI_SET_MV_FAILED = 16
        CTI_SET_MV_METACODE_NOTEXIST = 17
        CTI_SET_MV_CHANNEL_NOT_STARTED = 18
        CTI_SET_MV_METACODE_NOTEXIST_Pro7 = 19
        CTI_SET_MV_METACODE_UPDATE_TOO_FREQUENTLY_200MS = 20
        CTI_SET_MV_METACODE_DATATYPE_NOTSUPPORT = 21
        CTI_SET_MV_METACODE_NO_TEMPERATURE_CHAMBER = 22
        CTI_SET_MV_METACODE_NOT_CONTROLLED_AUXILIARY = 23
        CTI_SET_MV_METACODE_MCU_ACK_FAILED = 24

    def __init__(self, feedback: ArbinCTI.ArbinCommandUpdateMetaVariableAdvancedFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandUpdateMetaVariableAdvancedFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandUpdateMetaVariableAdvancedFeed', got '{type(feedback)}'")
        self.result = UpdateMetaVariableAdvancedFeedback.ESetMVResult(int(feedback.Result))

class UpdateMetaVariableAdvancedExFeedback(DictReprBase):
    class ESetMVResult(SafeIntEnumBase):
        CTI_SET_MV_SUCCESS = 0
        CTI_SET_MV_FAILED = 16
        CTI_SET_MV_METACODE_NOTEXIST = 17
        CTI_SET_MV_CHANNEL_NOT_STARTED = 18
        CTI_SET_MV_METACODE_NOTEXIST_Pro7 = 19
        CTI_SET_MV_METACODE_UPDATE_TOO_FREQUENTLY_200MS = 20
        CTI_SET_MV_METACODE_DATATYPE_NOTSUPPORT = 21
        CTI_SET_MV_METACODE_NO_TEMPERATURE_CHAMBER = 22
        CTI_SET_MV_METACODE_NOT_CONTROLLED_AUXILIARY = 23

    def __init__(self, feedback: ArbinCTI.ArbinCommandUpdateMetaVariableAdvancedExFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandUpdateMetaVariableAdvancedExFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandUpdateMetaVariableAdvancedExFeed', got '{type(feedback)}'")
        self.meta_variable_info = [MetaVariableInfoEx(mv) for mv in feedback.MetaVariableInfos]

class UpdateParameterFeedback(DictReprBase):
    class EUpdateToken(SafeIntEnumBase):
        CTI_UPDATE_SUCCESS = 0
        CTI_UPDATE_INDEX = 0x10
        CTI_UPDATE_ERROR = 0x11
        CTI_UPDATE_TESTOBJECT_NAME_EMPTY_ERROR = 0x12
        CTI_UPDATE_TESTOBJECT_NOT_FIND_ERROR = 0x13
        CTI_UPDATE_CHANNEL_RUNNING_ERROR = 0x14
        CTI_UPDATE_CHANNEL_DOWNLOAD_ERROR = 0x15
        CTI_UPDATE_BACTH_FILE_OPENED = 0x16
        CTI_UPDATE_TO_CANNOT_ASSIGN_TESTOBJECT = 0x17
        CTI_UPDATE_TESTOBJECT_SAVE_FAILED = 0x18
    
    class EParameterDataType(SafeIntEnumBase):
        NormCapacity = 0
        IMax = 1
        VMax = 2
        VMin = 3
        Mass = 4
        SCapacity = 5
        NIR = 6
        NVoltage = 7
        NCapacitance = 8
        IsAutoCalculate = 9

    def __init__(self, feedback: ArbinCTI.ArbinCommandUpdateParameterFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandUpdateParameterFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandUpdateParameterFeed', got '{type(feedback)}'")
        self.reason          = str(feedback.Reason)
        self.result          = UpdateParameterFeedback.EUpdateToken(int(feedback.Result))
        self.chan_list_pairs = self._unpack_cs_sorted_dict(
            feedback.ResultChanListPairs,
            (UpdateParameterFeedback.EUpdateToken, list)
        )
    
class ModifyScheduleFeedback(DictReprBase):
    class EModifyScheduleToken(SafeIntEnumBase):
        CTI_MODIFY_SUCCESS = 0
        CTI_MODIFY_ERROR = 0x10
        CTI_MODIFY_SCHEDUL_NAME_EMPTY_ERROR = 0x11
        CTI_MODIFY_SCHEDUL_NOT_EXIST_ERROR = 0x12
        CTI_MODIFY_SCHEDUL_RUNNING_ERROR = 0x13
        CTI_MODIFY_AUX_COUNT_EXCEED_MAPPING_ERROR = 0x14
        CTI_MODIFY_AUX_COUNT_EXCEED_SYSCONFIG_ERROR = 0x15
        CTI_MODIFY_AUX_SAFETY_SCOPE_ERROR = 0x16
        CTI_MODIFY_NO_SN_CYCLER_ERROR = 0x17
        CTI_MODIFY_NO_LOGIN_ERROR = 0x18
        CTI_MODIFY_NO_PERMISSION_ERROR = 0x19

    class ModifyScheduleResult(DictReprBase):
        def __init__(self, result: ArbinCTI.Common.ModifySchedule.ModifyScheduleResult):
            self.schedule_name  = str(result.ScheduleName)
            self.result         = ModifyScheduleFeedback.EModifyScheduleToken(int(result.Result))
            self.message        = str(result.Message)

    def __init__(self, feedback: ArbinCTI.ArbinCommandModifyScheduleFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandModifyScheduleFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandModifyScheduleFeed', got '{type(feedback)}'")
        self.task_id               = int(feedback.TaskID)
        self.schedule_modify_info  = [ModifyScheduleFeedback.ModifyScheduleResult(info) for info in feedback.ScheduleModifyInfos]

class AssignBarcodeInfoFeedback(DictReprBase):
    class EAssignBarcodeResult(SafeIntEnumBase):
        CTI_ASSIGN_BARCODE_SUCCESS = 0
        CTI_ASSIGN_BARCODE_ERROR = 0x10
        CTI_ASSIGN_BARCODE_CHANNEL_RUNNING = 0x11
        CTI_ASSIGN_BARCODE_CHANNEL_INDEX = 0x12
        CTI_ASSIGN_BARCODE_CHANNEL_TYPE_NOT_SUPPORT = 0x13
        CTI_ASSIGN_BARCODE_CELL_INDEX = 0x14
        CTI_ASSIGN_BARCODE_EQ_INDEX = 0x15
        CTI_ASSIGN_BARCODE_TRAY_INDEX = 0x16
        CTI_ASSIGN_BARCODE_SPTTMAPPING = 0x17
    
    class EChannelType(SafeIntEnumBase):
        IV = 1,
        EQ = 2,
        CELL = 3,
        TRAY = 4

        def to_cs(self) -> ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.EChannelType:
            """Convert to C# ArbinCommandAssignBarcodeInfoFeed.EChannelType"""
            return ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.EChannelType(self.value)

    class ChannelBarcodeInfo(DictReprBase):
        """Initialize with '(channel_type: AssignBarcodeInfoFeedback.EChannelType, global_index: int, barcode: str, info: str)' or an 'ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.ChannelBarcodeInfo' instance."""
        def __init__(self, *args):
            if len(args) == 1 and isinstance(args[0], ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.ChannelBarcodeInfo):
                info = args[0]
                self.channel_type   = AssignBarcodeInfoFeedback.EChannelType(int(info.ChannelType))
                self.global_index   = int(info.GlobalIndex)
                self.barcode        = str(info.Barcode)
                self.info           = str(info.Info)
                self.error          = AssignBarcodeInfoFeedback.EAssignBarcodeResult(int(info.Error))
            elif len(args) == 4:
                channel_type, global_index, barcode, info = args
                if not isinstance(channel_type, AssignBarcodeInfoFeedback.EChannelType):
                    raise TypeError(f"'channel_type' must be an instance of 'AssignBarcodeInfoFeedback.EChannelType', got '{type(channel_type)}'")
                if not isinstance(global_index, int):
                    raise TypeError(f"'global_index' must be an instance of 'int', got '{type(global_index)}'")
                if not isinstance(barcode, str):
                    raise TypeError(f"'barcode' must be an instance of 'str', got '{type(barcode)}'")
                if not isinstance(info, str):
                    raise TypeError(f"'info' must be an instance of 'str', got '{type(info)}'")
                self.channel_type   = channel_type
                self.global_index   = global_index
                self.barcode        = barcode
                self.info           = info
            else:
                raise TypeError(f"Expected 1 or 4 arguments, got {len(args)}")

        def to_cs(self) -> ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.ChannelBarcodeInfo:
            """Convert to C# ArbinCommandAssignBarcodeInfoFeed.ChannelBarcodeInfo"""
            cs_instance = ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.ChannelBarcodeInfo()
            cs_instance.ChannelType = self.channel_type.to_cs()
            cs_instance.GlobalIndex = self.global_index
            cs_instance.Barcode     = self.barcode
            cs_instance.Info        = self.info
            cs_instance.Error       = ArbinCTI.ArbinCommandAssignBarcodeInfoFeed.ASSIGN_BARCODE_RESULT.CTI_ASSIGN_BARCODE_SUCCESS
            return cs_instance

    def __init__(self, feedback: ArbinCTI.ArbinCommandAssignBarcodeInfoFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandAssignBarcodeInfoFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandAssignBarcodeInfoFeed', got '{type(feedback)}'")
        self.barcode_info = [AssignBarcodeInfoFeedback.ChannelBarcodeInfo(info) for info in feedback.BarcodeInfos]
        self.channel_type = AssignBarcodeInfoFeedback.EChannelType(int(feedback.ChannelType))

class GetBarcodeInfoFeedback(DictReprBase):
    class EGetBarcodeResult(SafeIntEnumBase):
        CTI_GET_BARCODE_SUCCESS = 0
        CTI_GET_BARCODE_ERROR = 0x10
        CTI_GET_BARCOD_CHANNEL_INDEX = 0x11
        CTI_GET_BARCODE_CHANNEL_TYPE_NOT_SUPPORT = 0x12
        CTI_GET_BARCODE_CELL_INDEX = 0x13
        CTI_GET_BARCODE_EQ_INDEX = 0x14
        CTI_GET_BARCODE_TRAY_INDEX = 0x15
        CTI_GET_BARCODE_SPTTMAPPING = 0x16

    class EChannelType(SafeIntEnumBase):
        IV = 1,
        EQ = 2,
        CELL = 3,
        TRAY = 4
        
        def to_cs(self) -> ArbinCTI.ArbinCommandGetBarcodeInfoFeed.EChannelType:
            """Convert to C# ArbinCommandGetBarcodeInfoFeed.EChannelType"""
            return ArbinCTI.ArbinCommandGetBarcodeInfoFeed.EChannelType(self.value)

    class GetChannelBarcodeInfo(DictReprBase):
        """Initialize the class with an integer or an ArbinCTI.ArbinCommandGetBarcodeInfoFeed.GetChannelBarcodeInfo instance."""
        def __init__(self, arg):
            if isinstance(arg, int):
                self.global_index = arg
            elif isinstance(arg, ArbinCTI.ArbinCommandGetBarcodeInfoFeed.GetChannelBarcodeInfo):
                self.global_index = int(arg.GlobalIndex)
            else:
                raise TypeError(f"'info' must be an instance of 'int' or 'ArbinCTI.ArbinCommandGetBarcodeInfoFeed.GetChannelBarcodeInfo', got '{type(info)}'")                

        def to_cs(self) -> ArbinCTI.ArbinCommandGetBarcodeInfoFeed.GetChannelBarcodeInfo:
            """Convert to C# ArbinCommandGetBarcodeInfoFeed.GetChannelBarcodeInfo"""
            return ArbinCTI.ArbinCommandGetBarcodeInfoFeed.GetChannelBarcodeInfo(self.global_index)
    
    class ChannelBarcodeInfo(DictReprBase):
        def __init__(self, info: ArbinCTI.ArbinCommandGetBarcodeInfoFeed.ChannelBarcodeInfo):
            self.channel_type   = GetBarcodeInfoFeedback.EChannelType(int(info.ChannelType))
            self.global_index   = int(info.GlobalIndex)
            self.barcode        = str(info.Barcode)
            self.info           = str(info.Info)
            self.error          = GetBarcodeInfoFeedback.EGetBarcodeResult(int(info.Error))
    
    def __init__(self, feedback: ArbinCTI.ArbinCommandGetBarcodeInfoFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandGetBarcodeInfoFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandGetBarcodeInfoFeed', got '{type(feedback)}'")
        self.barcode_info = [GetBarcodeInfoFeedback.ChannelBarcodeInfo(info) for info in feedback.BarcodeInfos]
        self.channel_type = GetBarcodeInfoFeedback.EChannelType(int(feedback.ChannelType))

class GetMachineTypeFeedback(DictReprBase):
    class EGetMachineResult(SafeIntEnumBase):
        CTI_GET_MACHINE_SUCCESS = 0
        CTI_GET_MACHINE_ERROR = 0x10

    class EMachineType(SafeIntEnumBase):
        IV = 1
        SPTT = 2
        ALL = IV | SPTT

    def __init__(self, feedback: ArbinCTI.ArbinCommandGetMachineTypeFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandGetMachineTypeFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandGetMachineTypeFeed', got '{type(feedback)}'")
        self.error          = GetMachineTypeFeedback.EGetMachineResult(int(feedback.m_Error))
        self.machine_type   = GetMachineTypeFeedback.EMachineType(int(feedback.MachineType))

class CSPTTTrayStatus(DictReprBase):
    class CSPTTTrayMetaValue(DictReprBase):
        def __init__(self, meta_value: ArbinCTI.Common.CSPTTTrayMetaValue):
            self.value      = float(meta_value.Value)
            self.alias_name = str(meta_value.AliasName)
            self.error      = int(meta_value.Error)

    def __init__(self, status: ArbinCTI.Common.CSPTTTrayStatus):
        self.global_index       = int(status.GlobalIndex)
        self.is_engagement_down = bool(status.IsEngagementDown)
        self.is_engagement_up   = bool(status.IsEngagementUp)
        self.is_tray_inserted   = bool(status.IsTrayInserted)
        self.error              = int(status.Error)
        self.meta_values        = [CSPTTTrayStatus.CSPTTTrayMetaValue(meta_value) for meta_value in status.MetaValues]

class GetTrayStatusFeedback(DictReprBase):
    class ETrayStatusResult(SafeIntEnumBase):
        CTI_GET_TRAY_STATUS_SUCCESS = 0
        CTI_GET_TRAY_STATUS_ERROR = 0x10
        CTI_GET_TRAY_INDEX_ERROR = 0x11
        CTI_GET_TRAY_STATUS_ERROR_NETWORK = 0x12
        CTI_GET_TRAY_STATUS_ERROR_UNIT = 0x13
        CTI_GET_TRAY_STATUS_ERROR_SPTTMAPPING_INDEX = 0x14

    def __init__(self, feedback: ArbinCTI.ArbinCommandGetTrayStatusFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandGetTrayStatusFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandGetTrayStatusFeed', got '{type(feedback)}'")
        self.tray_status_info = [CSPTTTrayStatus(status) for status in feedback.TrayStatusInfos]

class EngageTrayFeedback(DictReprBase):
    class EEngageTrayResult(SafeIntEnumBase):
        CTI_ENGAGE_TRAY_SUCCESS = 0
        CTI_ENGAGE_TRAY_ERROR = 0x10
        CTI_ENGAGE_TRAY_ERROR_INDEX = 0x11
        CTI_ENGAGE_TRAY_ERROR_NETWORK = 0x12
        CTI_ENGAGE_TRAY_ERROR_UNIT = 0x13
        CTI_ENGAGE_TRAY_ERROR_SPTTMAPPING_INDEX = 0x14
        CTI_ENGAGE_TRAY_ERROR_CHANNEL_NULL = 0x15
        CTI_ENGAGE_TRAY_ERROR_CHANNEL_RUNNING = 0x16
    
    class CSPTTEngageTray(DictReprBase):
        def __init__(self, engage_tray: ArbinCTI.Common.CSPTTEngageTray):
            self.global_index = int(engage_tray.GlobalIndex)
            self.engage       = bool(engage_tray.Engage)
            self.error        = int(engage_tray.Error)

    def __init__(self, feedback: ArbinCTI.ArbinCommandEngageTrayFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandEngageTrayFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandEngageTrayFeed', got '{type(feedback)}'")
        self.engage_tray_info = [EngageTrayFeedback.CSPTTEngageTray(status) for status in feedback.EngageTrayInfos]

class SetIntervalTimeLogDataFeedback(DictReprBase):
    class ESetIntervalTimeLogDataResult(SafeIntEnumBase):
        SET_INTERVALTIME_LOGDATA_DAQ_DISCONNECTED = -2
        SET_INTERVALTIME_LOGDATA_DCOM_FAILED = -1
        SET_INTERVALTIME_LOGDATA_SUCCESS = 0
        SET_INTERVALTIME_LOGDATA_PARTIAL_SUCCESS = 1
        SET_INTERVALTIME_LOGDATA_FAILED = 2
        SET_INTERVALTIME_LOGDATA_EXCEED_LIMIT = 3
    
    def __init__(self, feedback: ArbinCTI.ArbinCommandSetIntervalTimeLogDataFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandSetIntervalTimeLogDataFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandSetIntervalTimeLogDataFeed', got '{type(feedback)}'")
        self.result  = SetIntervalTimeLogDataFeedback.ESetIntervalTimeLogDataResult(int(feedback.Result))
        self.message = str(feedback.Message) 

class ConvertToAnonymousOrNamedTOFeedback(DictReprBase):
    class EConvertTestObjectResult(SafeIntEnumBase):
        CTI_CONVERT_SUCCESS = 0
        CTI_CONVERT_FAILED = 1
        CTI_CONVERT_CHANNEL_IS_RUNNING = 2
        CTI_CONVERT_NO_TEST_OBJECT_FILE = 4

    def __init__(self, feedback: ArbinCTI.ArbinCommandConvertToAnonymousOrNamedTOFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandConvertToAnonymousOrNamedTOFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandConvertToAnonymousOrNamedTOFeed', got '{type(feedback)}'")
        self.reason = str(feedback.Reason)
        self.result = ConvertToAnonymousOrNamedTOFeedback.EConvertTestObjectResult(int(feedback.Result))
        self.result_chan_list_pairs = self._unpack_cs_sorted_dict(
            feedback.ResultChanListPairs, 
            (ConvertToAnonymousOrNamedTOFeedback.EConvertTestObjectResult, list)
        )
    