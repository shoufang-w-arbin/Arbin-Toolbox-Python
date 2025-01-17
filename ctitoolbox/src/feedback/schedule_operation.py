from enum import IntEnum

import ArbinCTI.Core as ArbinCTI # type: ignore

from ctitoolbox.src.feedback.dict_repr_base import DictReprBase
from ctitoolbox.src.data_type.cti_data_type import (
    TimeSensitiveSetMV,
    TE_DATA_TYPE
)

"""""""""""""""""""""""""""
Schedule Operation
- AssignScheduleFeedback
- AssignFileFeedback
- SetMetaVariableFeedback
- SetMetaVariableTimeSensitiveFeedback
- GetMetaVariableFeedback
- UpdateParameterFeedback
"""""""""""""""""""""""""""
class AssignScheduleFeedback(DictReprBase):
    class EAssignToken(IntEnum):
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
    class EFileKind(IntEnum):
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

    class EAssignToken(IntEnum):
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
        self.channel_list_result = self._unpack_channel_result(feedback.ChanListResultPairs)
        self.reason              = str(feedback.Reason)

    def _unpack_channel_result(self, cs_dict):
        _python_dict = dict()
        for pair in cs_dict:
            token              = AssignFileFeedback.EAssignToken(int(pair.Key))
            channels           = list(pair.Value)
            _python_dict[token] = channels
        return _python_dict
    
    def to_dict(self):
        _channel_list_result = dict()
        for key, value in self.channel_list_result.items():
            _channel_list_result[key.name] = value
        return {
            "result": self.result.name,
            "channel_list_result": _channel_list_result
        }
    
class SetMetaVariableFeedback(DictReprBase):
    class EResult(IntEnum):
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
    class EControlStatus(IntEnum):
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

    class EResult(IntEnum):
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
    class EResult(IntEnum):
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

class UpdateParameterFeedback(DictReprBase):
    class EUpdateToken(IntEnum):
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
    
    class EParameterDataType(IntEnum):
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
        self.chan_list_pairs = self._unpack_channel_list(feedback.ResultChanListPairs)

    def _unpack_channel_list(self, result):
        _python_dict = dict()
        for pair in result:
            token = UpdateParameterFeedback.EUpdateToken(int(pair.Key))
            channels = list(pair.Value)
            _python_dict[token] = channels
        return _python_dict