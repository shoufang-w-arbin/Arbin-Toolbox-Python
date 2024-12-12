import json
import copy
from enum import IntEnum

import ArbinCTI.Core as ArbinCTI # type: ignore
from ctitoolbox.src.data_type.cti_data_type import (
    TimeSensitiveSetMV,
    TE_DATA_TYPE
)
from ctitoolbox.src.data_type.cs_data_type import CSTypeConverter

"""""""""""""""""""""""""""
Schedule Operation
- AssignScheduleFeedback
- AssignFileFeedback
- SetMetaVariableFeedback
- SetMetaVariableTimeSensitiveFeedback
- GetMetaVariableFeedback
"""""""""""""""""""""""""""
class AssignScheduleFeedback:
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
        self.result = AssignScheduleFeedback.EAssignToken(int(feedback.Result))
    
    def to_json(self):
        return json.dumps(self.__dict__)

class AssignFileFeedback:
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

    def __init__(self, feedback: ArbinCTI.ArbinCommandAssignFileFeed):  
        self.result              = AssignFileFeedback.EAssignToken(int(feedback.Result))
        self.channel_list_result = self._unpack_channel_result(feedback.ChanListResultPairs)
        self.reason              = str(feedback.Reason)

    def _unpack_channel_result(self, cs_dict):
        python_dict = {}
        for pair in cs_dict:
            token              = AssignFileFeedback.EAssignToken(int(pair.Key))
            channels           = list(pair.Value)
            python_dict[token] = channels
        return python_dict
    
    def to_json(self):
        result_dict = copy.deepcopy(self.__dict__)
        result_dict['result'] = self.result.name
        channel_list_result = dict()
        for key, value in result_dict['channel_list_result'].items():
            channel_list_result[key.name] = value
        result_dict['channel_list_result'] = channel_list_result
        return json.dumps(result_dict)

class SetMetaVariableFeedback:
    class EResult(IntEnum):
        CTI_SET_MV_SUCCESS = 0
        CTI_SET_MV_FAILED = 16
        CTI_SET_MV_METACODE_NOTEXIST = 17
        CTI_SET_MV_CHANNEL_NOT_STARTED = 18
        CTI_SET_MV_METACODE_NOTEXIST_Pro7 = 19

    def __init__(self, feedback: ArbinCTI.ArbinCommandSetMetaVariableFeed):
        self.result = SetMetaVariableFeedback.EResult(int(feedback.Result))

    def to_json(self):
        return json.dumps({
            "result": self.result.name
        })
class SetMetaVariableTimeSensitiveFeedback:
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
 
    class TimeSensitiveSetMVResult:
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
        self.results = [SetMetaVariableTimeSensitiveFeedback.TimeSensitiveSetMVResult(result) for result in feedback.Results]

    def to_json(self):
        temp = copy.deepcopy(self.results)

        for res in temp:
            res.machine_status = res.machine_status.name
            res.result = res.result.name
            res.mvs = [mv.__dict__ for mv in res.mvs]

        return json.dumps({
            "result": [res.__dict__ for res in temp]
        })

class GetMetaVariableFeedback:
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

    class MetaVariableInfo:
        def __init__(self, info: ArbinCTI.ArbinCommandGetMetaVariablesFeed.MetaVariableInfo):
            self.channel_index = int(info.m_Channel)
            self.mv_error      = GetMetaVariableFeedback.EResult(int(info.m_MV_Error))
            self.mv_data_type  = TE_DATA_TYPE(int(info.m_MV_DataType))
            self.mv_meta_code  = int(info.m_MV_MetaCode)
            self.value         = float(info.m_Value)
    
    def __init__(self, feedback: ArbinCTI.ArbinCommandGetMetaVariablesFeed):
        self.meta_variable_info = [GetMetaVariableFeedback.MetaVariableInfo(info) for info in feedback.MetaVariableInfos]

    def to_json(self):
        temp = copy.deepcopy(self.meta_variable_info)

        for info in temp:
            info.mv_error = info.mv_error.name
            info.mv_data_type = info.mv_data_type.name

        return json.dumps({
            "meta_variable_info": [info.__dict__ for info in temp]
        })