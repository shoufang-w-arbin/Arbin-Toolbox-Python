__all__ = [
    "GetSerailNumberFeedback",
    "GetMITSVersionFeedback",
    "LoginFeedback",
    "UploadFileFeedback",
    "DownloadFileFeedback",
    "BrowseDirectoryFeedback",
    "AssignScheduleFeedback",
    "AssignFileFeedback",
    "SetMetaVariableFeedback",
    "StartTestFeedback",
    "StopTestFeedback",
    "ResumeTestFeedback",
    "JumpStepFeedback",
    "ProceedTestFeedback",
    "GetChannelDataFeedback",
    "GetResumeDataFeedback",
    "GetChannelAssignmentFeedback",
    "SetMetaVariableTimeSensitiveFeedback",
    "GetMetaVariableFeedback",
]

import json
from enum import IntEnum
from typing import Optional
import clr

clr.AddReference("arbincti/bin/ArbinCTI")
from ArbinCTI.Core import ( # type: ignore
    ArbinCommandGetSerialNumberFeed,
    ArbinCommandGetServerSoftwareVersionNumberFeed,
    ArbinCommandLoginFeed,
    ArbinCommandUpLoadFileFeed,
    ArbinCommandDownLoadFileFeed,
    ArbinCommandBrowseDirectoryFeed,
    ArbinCommandAssignScheduleFeed,
    ArbinCommandAssignFileFeed,
    ArbinCommandSetMetaVariableFeed,
    ArbinCommandGetMetaVariablesFeed,
    ArbinCommandTimeSensitiveSetMVFeed,
    ArbinCommandStartChannelFeed,
    ArbinCommandStopChannelFeed,
    ArbinCommandResumeChannelFeed,
    ArbinCommandJumpChannelFeed,
    ArbinCommandContinueChannelFeed,
    ArbinCommandGetChannelDataFeed,
    ArbinCommandGetResumeDataFeed,
    ArbinCommandGetStartDataFeed,
    ArbinCommandGetSerialNumberFeed,
)

from arbincti.src.utils.data_type_wrapper import CSTypeConverter

"""""""""""""""""""""""""""
System
"""""""""""""""""""""""""""
class GetSerailNumberFeedback:
    class ASSIGN_TOKEN(IntEnum):
        CTI_GET_SERAIL_SUCESS = 0,
        CTI_ASSIGN_ERROR = 0x10,

    def __init__(self, feedback: ArbinCommandGetSerialNumberFeed): # type: ignore
        self.serial_number  = float(feedback.SerialNum)
        self.result         = GetSerailNumberFeedback.ASSIGN_TOKEN(int(feedback.Result))

class GetMITSVersionFeedback:
    def __init__(self, feedback: ArbinCommandGetServerSoftwareVersionNumberFeed): # type: ignore
        self.version = str(feedback.ServerVersionNumber)

"""""""""""""""""""""""""""
Connection and Authentication
"""""""""""""""""""""""""""
class LoginFeedback:
    class CTIVersion(IntEnum):
        NONE = 0
        CTI_PRO7 = 0
        CTI_PRO8 = 1
        Pro8_2 = 2
        MitsX_1 = 0x01000001
        MitsX_2 = 0x01000002
        MitsX_3 = 0x01000003
        MitsX_SPTT = 0x01001001
        Pro7_MVUD = 0x02000001
        TY_Pro7_2 = 0x02000002
        TY_Pro7_3 = 0x02000003
        TY_Pro8_1 = 0x04000001
        TY_Pro8_2 = 0x04000002
        TY_Pro8_SPTT = 0x04001001
        ZY_Pro8_GX = 0x08000001

    class LoginResult(IntEnum):
        CTI_LOGIN_SUCCESS = 1
        CTI_LOGIN_FAILED = 2
        CTI_LOGIN_BEFORE_SUCCESS = 3

    def __init__(self, feedback: ArbinCommandLoginFeed): # type: ignore
        self.result             = LoginFeedback.LoginResult(int(feedback.Result))
        self.user_type          = int(feedback.UserType)
        self.serial_number      = str(feedback.SN)
        self.note               = str(feedback.Note)
        self.nickname           = str(feedback.NickName)
        self.location           = str(feedback.Location)
        self.emergency_contact  = str(feedback.EmergencyContactNameAndPhoneNumber)
        self.other_comments     = str(feedback.OtherComments)
        self.email              = str(feedback.Email)
        self.itac               = int(feedback.ITAC)
        self.call               = str(feedback.CALL)
        self.channel_count      = int(feedback.ChannelNum)
        self.version            = LoginFeedback.CTIVersion(int(feedback.Version))
        # self.img: Optional[Image.Image] = feedback.Img if isinstance(feedback.Img, Image.Image) else None
        self.server_info: Optional[str]   = feedback.ServerInfo

"""""""""""""""""""""""""""
File Management
"""""""""""""""""""""""""""
class UploadFileFeedback:
    class UploadResult(IntEnum):
        CTI_UPLOAD_SUCCESS = 1
        CTI_UPLOAD_FAILED = 2
        CTI_UPLOAD_MD5_ERR = 3
        CTI_UPLOAD_FAILED_TEXT_RUNNING = 4
        CTI_UPLOAD_FILE_EXIST_WITH_DIFFERENT_MD5 = 5
        CTI_UPLOAD_FILE_EXIST_WITH_SAME_MD5 = 6
        CTI_UPLOAD_FILE_EXIST_NOT_OVERRIDE = 7
        CTI_UPLOAD_FAILED_USER_CANCEL = 8
        CTI_UPLOAD_FAILED_TIMEOUT = 9
        CTI_UPLOAD_FAILED_CHECK_FILE_TIMEOUT = 10
        CTI_UPLOAD_IN_PROGRESS = 11

    class UploadFileResult:
        def __init__(self, upload_file_result: ArbinCommandUpLoadFileFeed.CUpLoadFileResult): # type: ignore
            self.result_code    = upload_file_result.ResultCode
            self.cancel         = upload_file_result.IsCancelUploadFile
            self.progress_rate  = upload_file_result.ProgressRate

    def __init__(self, feedback: ArbinCommandUpLoadFileFeed): # type: ignore
        self.result       = UploadFileFeedback.UploadResult(int(feedback.Result))
        self.upload_time  = float(feedback.UploadTime)
        self.packet_count = int(feedback.uGeneralPackage)
        self.packet_index = int(feedback.uPackageIndex)
    
class DownloadFileFeedback:
    class DownloadResult(IntEnum):
        CTI_DOWNLOAD_SUCCESS = 1,
        CTI_DOWNLOAD_FAILED = 2,
        CTI_DOWNLOAD_MD5_ERR = 3,
        CTI_DOWNLOAD_MAX_LENGTH_ERR = 4

    def __init__(self, feedback: ArbinCommandDownLoadFileFeed): # type: ignore
        self.result         = DownloadFileFeedback.DownloadResult(int(feedback.Result))
        self.md5            = str(feedback.m_md5)
        self.file_length    = int(feedback.dw_file_length)
        self.data           = bytearray(feedback.by_data)
        self.download_time  = float(feedback.download_time)
        self.upload_time    = float(feedback.upload_time)
        self.package_count  = int(feedback.u_general_package)
        self.package_index  = int(feedback.u_package_index)

class BrowseDirectoryFeedback:
    class BrowseDirectoryResult(IntEnum):
        CTI_BROWSE_DIRECTORY_SUCCESS = 1,
        CTI_BROWSE_SCHEDULE_SUCCESS = 2,
        CTI_BROWSE_SCHEDULE_VERSION1_SUCCESS = 3,
        CTI_BROWSE_DIRECTORY_FAILED = 4
    
    class DirFileInfo:
        def __init__(self, info: ArbinCommandBrowseDirectoryFeed.DirFileInfo): # type: ignore
            self.type = info.Type
            self.parent_dir_path = info.DirFileName
            self.size = info.dwSize
            self.last_modify_time = info.wcModified

    def __init__(self, feedback: ArbinCommandBrowseDirectoryFeed): # type: ignore
        self.result         = BrowseDirectoryFeedback.BrowseDirectoryResult(int(feedback.Result))
        self.dir_file_info  = [BrowseDirectoryFeedback.DirFileInfo(info) for info in feedback.DirFileInfo]

"""""""""""""""""""""""""""
Test Configuration
"""""""""""""""""""""""""""
class AssignScheduleFeedback:
    class AssignToken(IntEnum):
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

    def __init__(self, feedback: ArbinCommandAssignScheduleFeed): # type: ignore
        self.result = AssignScheduleFeedback.AssignToken(int(feedback.Result))

class AssignFileFeedback:
    class AssignToken(IntEnum):
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

    def __init__(self, feedback: ArbinCommandAssignFileFeed): # type: ignore
        self.result = AssignFileFeedback.AssignToken(int(feedback.Result))
        self.channel_list_result = self._unpack_channel_result(feedback.ChanListResultPairs)
        self.reason = str(feedback.Reason)

    def _unpack_channel_result(self, cs_dict):
        python_dict = {}
        for pair in cs_dict:
            token = AssignFileFeedback.AssignToken(pair.Key)
            channels = list(pair.Value)
            python_dict[token] = channels
        return python_dict

class SetMetaVariableFeedback:
    class SetMVResult(IntEnum):
        CTI_SET_MV_SUCCESS = 0
        CTI_SET_MV_FAILED = 16
        CTI_SET_MV_METACODE_NOTEXIST = 17
        CTI_SET_MV_CHANNEL_NOT_STARTED = 18
        CTI_SET_MV_METACODE_NOTEXIST_Pro7 = 19

    def __init__(self, feedback: ArbinCommandSetMetaVariableFeed): # type: ignore
        self.result = SetMetaVariableFeedback.SetMVResult(int(feedback.Result))
        
    def __repr__(self):
        return f"SetMetaVariableFeedback(result={self.result})"

    def to_json(self):
        return json.dumps({"result": self.result.name})
    
from arbincti.src.utils.data_type_wrapper import TimeSensitiveSetMVArgs
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
        def __init__(self, result: ArbinCommandTimeSensitiveSetMVFeed.TimeSensitiveSetMVResult):
            self.global_index   = int(result.GlobalIndex)
            self.step_index     = int(result.StepIndex)
            self.sub_step_index = int(result.SubStepIndex)
            self.machine_status = SetMetaVariableTimeSensitiveFeedback.EControlStatus(result.MachineStatus)
            self.result         = SetMetaVariableTimeSensitiveFeedback.EResult(result.Result)
            self.current        = float(result.Current)
            self.voltage        = float(result.Voltage)
            self.mvs            = [TimeSensitiveSetMVArgs.TimeSensitiveSetMV(mv) for mv in result.MVs]

    def __init__(self, feedback: ArbinCommandTimeSensitiveSetMVFeed): # type: ignore
        self.result = [SetMetaVariableTimeSensitiveFeedback.TimeSensitiveSetMVResult(result) for result in feedback.Results]

class GetMetaVariableFeedback:
    class GetMVResult(IntEnum):
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
        def __init__(self, info: ArbinCommandGetMetaVariablesFeed.MetaVariableInfo): # type: ignore
            self.channel_index  = int(info.m_Channel)
            self.mv_error     = GetMetaVariableFeedback.GetMVResult(int(info.m_MV_Error))
            self.mv_data_type = CSTypeConverter.TEDataType(int(info.m_MV_DataType))
            self.mv_data_code = int(info.m_MV_MetaCode)
            self.value        = float(info.m_Value)
    
    def __init__(self, feedback: ArbinCommandGetMetaVariablesFeed): # type: ignore
        self.meta_variable_info = [GetMetaVariableFeedback.MetaVariableInfo(info) for info in feedback.MetaVariableInfos]

"""""""""""""""""""""""""""
Test Control
"""""""""""""""""""""""""""
class StartTestFeedback:
    class StartToken(IntEnum):
        CTI_START_SUCCESS = 1
        CTI_START_INDEX = 0x10
        CTI_START_ERROR = 0x11
        CTI_START_CHANNEL_RUNNING = 0x12
        CTI_START_CHANNEL_NOT_CONNECT = 0x13
        CTI_START_SCHEDULE_VALID = 0x14
        CTI_START_NO_SCHEDULE_ASSIGNED = 0x15
        CTI_START_SCHEDULE_VERSION = 0x16
        CTI_START_POWER_PROTECTED = 0x17
        CTI_START_RESULTS_FILE_SIZE_LIMIT = 0x18
        CTI_START_STEP_NUMBER = 0x19
        CTI_START_NO_CAN_CONFIGURATON_ASSIGNED = 0x1A
        CTI_START_AUX_CHANNEL_MAP = 0x1B
        CTI_START_BUILD_AUX_COUNT = 0x1C
        CTI_START_POWER_CLAMP_CHECK = 0x1D
        CTI_START_AI = 0x1E
        CTI_START_SAFOR_GROUPCHAN = 0x1F
        CTI_START_BT6000RUNNINGGROUP = 0x20
        CTI_START_CHANNEL_DOWNLOADING_SCHEDULE = 0x21
        CTI_START_DATABASE_QUERY_TEST_NAME_ERROR = 0x22
        CTI_START_TEXTNAME_EXITS = 0x23
        CTI_START_GO_STEP = 0x24
        CTI_START_INVALID_PARALLEL = 0x25
        CTI_START_SAFETY = 0x26
        CTI_START_SECHEDULE_NAME_DIFFERENT = 0x27
        CTI_START_BATTERYSIMULATION_NOT_PARALLEL = 0x28
        CTI_START_CSV_WAIT_TIME = 0x29
        CTI_START_CHANNEL_SUSPENT = 0x2A
        CTI_START_TESTNAME_TOO_LONG = 0x2B

    def __init__(self, feedback: ArbinCommandStartChannelFeed): # type: ignore
        self.result =StartTestFeedback.StartToken(int(feedback.Result))

class StopTestFeedback:
    class StopToken(IntEnum):
        SUCCESS = 0
        STOP_INDEX = 0x10
        STOP_ERROR = 0x11
        STOP_NOT_RUNNING = 0x12
        STOP_CHANNEL_NOT_CONNECT = 0x13

    def __init__(self, feedback: ArbinCommandStopChannelFeed): # type: ignore
        self.result = StopTestFeedback.StopToken(int(feedback.Result))

class ResumeTestFeedback:
    class ResumeToken(IntEnum):
        RESUME_SUCCESS = 0
        RESUME_INDEX = 0x10
        RESUME_ERROR = 0x11
        RESUME_CHANNEL_RUNNING = 0x12
        RESUME_CHANNEL_NOT_CONNECT = 0x13
        RESUME_SCHEDULE_VALID = 0x14
        RESUME_NO_SCHEDULE_ASSIGNED = 0x15
        RESUME_SCHEDULE_VERSION = 0x16
        RESUME_POWER_PROTECTED = 0x17
        RESUME_RESULTS_FILE_SIZE_LIMIT = 0x18
        RESUME_STEP_NUMBER = 0x19
        RESUME_NO_CAN_CONFIGURATON_ASSIGNED = 0x1A
        RESUME_AUX_CHANNEL_MAP = 0x1B
        RESUME_BUILD_AUX_COUNT = 0x1C
        RESUME_POWER_CLAMP_CHECK = 0x1D
        RESUME_AI = 0x1E
        RESUME_SAFOR_GROUPCHAN = 0x1F
        RESUME_BT6000RUNNINGGROUP = 0x20
        RESUME_CHANNEL_DOWNLOADING_SCHEDULE = 0x21
        RESUME_DATABASE_QUERY_TEST_NAME_ERROR = 0x22
        RESUME_NO_TEST_NAME = 0x23
        RESUME_LOAD_RESUME = 0x24
        RESUME_MAX_MULTIPLE_RESULT = 0x25
        CTI_RESUME_SAFETY = 0x26
        CTI_RESUME_BATTERYSIMULATION_NOT_PARALLEL = 0x27
        CTI_RESUME_CHANNEL_SUSPENT = 0x28

    def __init__(self, feedback: ArbinCommandResumeChannelFeed): # type: ignore
        self.result = ResumeTestFeedback.ResumeToken(int(feedback.Result))

class JumpStepFeedback:
    class JumpToken(IntEnum):
        CTI_JUMP_SUCCESS = 0
        CTI_JUMP_INDEX = 0x10
        CTI_JUMP_ERROR = 0x11
        CTI_JUMP_CHANNEL_RUNNING = 0x12
        CTI_JUMP_CHANNEL_NOT_CONNECT = 0x13
        CTI_JUMP_SCHEDULE_VALID = 0x14
        CTI_JUMP_NO_SCHEDULE_ASSIGNED = 0x15
        CTI_JUMP_SCHEDULE_VERSION = 0x16
        CTI_JUMP_POWER_PROTECTED = 0x17
        CTI_JUMP_RESULTS_FILE_SIZE_LIMIT = 0x18
        CTI_JUMP_STEP_NUMBER = 0x19
        CTI_JUMP_NO_CAN_CONFIGURATON_ASSIGNED = 0x1A
        CTI_JUMP_AUX_CHANNEL_MAP = 0x1B
        CTI_JUMP_BUILD_AUX_COUNT = 0x1C
        CTI_JUMP_POWER_CLAMP_CHECK = 0x1D
        CTI_JUMP_AI = 0x1E
        CTI_JUMP_SAFOR_GROUPCHAN = 0x1F
        CTI_JUMP_BT6000RUNNINGGROUP = 0x20
        CTI_JUMP_CHANNEL_DOWNLOADING_SCHEDULE = 0x21
        CTI_JUMP_DATABASE_QUERY_TEST_NAME_ERROR = 0x22
        CTI_JUMP_TEXTNAME_EXITS = 0x23
        CTI_JUMP_GO_STEP = 0x24
        CTI_JUMP_INVALID_PARALLEL = 0x25
        CTI_JUMP_SAFETY = 0x26
        CTI_JUMP_SECHEDULE_NAME_DIFFERENT = 0x27
        CTI_JUMP_BATTERYSIMULATION_NOT_PARALLEL = 0x28
        CTI_JUMP_CHANNEL_SUSPENT = 0x29

    def __init__(self, feedback: ArbinCommandJumpChannelFeed): # type: ignore
        self.result                 = JumpStepFeedback.JumpToken(int(feedback.Result))
        self.error_channel_index    = int(feedback.ErrorChannelIndex)

class ProceedTestFeedback:
    class ProceedToken(IntEnum):
        CTI_PROCEED_SUCCESS = 0
        CTI_PROCEED_INDEX = 0x10
        CTI_PROCEED_ERROR = 0x11
        CTI_PROCEED_CHANNEL_RUNNING = 0x12
        CTI_PROCEED_CHANNEL_NOT_CONNECT = 0x13
        CTI_PROCEED_CHANNEL_CALIBRATING = 0x14
        CTI_PROCEED_NOT_PAUSE_NORMAL = 0x15
        CTI_PROCEED_CHANNEL_UNSAFE = 0x16
    
    def __init__(self, feedback: ArbinCommandContinueChannelFeed): # type: ignore
        self.result = ProceedTestFeedback.ProceedToken(int(feedback.Result))
    
class GetChannelDataFeedback:
    class GetChannelsInfoNeedType(IntEnum):
        THIRD_PARTY_GET_CHANNELS_INFO_NEED_TYPE_BMS = 0x100
        THIRD_PARTY_GET_CHANNELS_INFO_NEED_TYPE_SMB = 0x200
        THIRD_PARTY_GET_CHANNELS_INFO_NEED_TYPE_AUX = 0x400
        THIRD_PARTY_GET_CHANNELS_INFO_NEED_TYPE_EQ = 0x800
        THIRD_PARTY_GET_CHANNELS_INFO_NEED_TYPE_CELL = 0x1000
    
    class GetChannelType(IntEnum):
        ALLCHANNEL = 1
        RUNNING = 2
        UNSAFE = 3
    
    class ChannelStatus(IntEnum):
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
        Runing = 22
        Step_Transfer = 23
        Resume = 24
        Go_Pause = 25
        Go_Stop = 26
        Go_Next_Step = 27
        Online_Update = 28
        Daq_Memory_Unsafe = 29
        ACR = 30
        CS_SUSPENT = 31

    class AuxData:
        def __init__(self, data: ArbinCommandGetChannelDataFeed.AuxData): # type: ignore
            self.value    = float(data.Value)
            self.value_dt = float(data.DTValue)

    class CANInfo:
        def __init__(self, data: ArbinCommandGetChannelDataFeed.CANInfo): # type: ignore
            self.index = int(data.nIndex)
            self.value = float(data.Value)
            self.unit  = str(data.Unit)

    class SMBInfo:
        def __init__(self, data: ArbinCommandGetChannelDataFeed.SMBInfo): # type: ignore
            self.index = int(data.nIndex)
            self.type  = int(data.nType)
            self.unit  = str(data.Unit)
            self.value = data.Value  # Keeping this generic as 'object'

    class CANMonitorInfo:
        def __init__(self, data: ArbinCommandGetChannelDataFeed.CANMonitorInfo):  # type: ignore
            self.is_offline = bool(data.IsOffline)
            self.alias_name = str(data.AliasName)
            self.meta_name  = str(data.MetaName)
            self.data_type  = int(data.DataType)
            self.value      = str(data.Value)

    class SMBMonitorInfo:
        def __init__(self, data: ArbinCommandGetChannelDataFeed.SMBMonitorInfo):  # type: ignore
            self.is_offline = bool(data.IsOffline)
            self.alias_name = str(data.AliasName)
            self.meta_name  = str(data.MetaName)
            self.data_type  = int(data.DataType)
            self.value      = str(data.Value)

    class AuxMonitorData:
        def __init__(self, data: ArbinCommandGetChannelDataFeed.AuxMonitorData):  # type: ignore
            self.aux_type = str(data.AuxType)
            self.alias_name = str(data.AliasName)
            self.aux_ch_global_id = int(data.AuxChGlobalID)
            self.aux_ch_virtual_id = int(data.AuxChVirtualID)
            self.value = float(data.Value)
            self.dxdt = float(data.dxdt)

    class ChannelInfo:
        class AuxType(IntEnum):
            AuxV = 0
            T = 1
            P = 2
            pH = 3
            FR = 4
            Conc = 5
            DI = 6
            DO = 7
            EC = 8
            Safety = 9
            Humidity = 10
            AO = 11
            MAX_NUM = 12
    
        def __init__(self, info: ArbinCommandGetChannelDataFeed.ChannelInfo):  # type: ignore
            self.channel_index          = int(info.Channel)
            self.status                 = GetChannelDataFeedback.ChannelStatus(int(info.Status))
            self.comm_failure           = bool(info.CommFailure)
            self.schedule               = str(info.Schedule)
            self.can_cfg                = str(info.CANCfg)
            self.smb_cfg                = str(info.SMBCfg)
            self.chart                  = str(info.Chart)
            self.test_name              = str(info.Testname)
            self.exit_condition         = str(info.ExitCondition)
            self.step_and_cycle         = str(info.StepAndCycle)
            self.step_index             = int(info.StepIndex)
            self.cycle_index            = int(info.CycleIndex)
            self.barcode                = str(info.Barcode)
            self.master_channel         = int(info.MasterChannel)
            self.test_time              = float(info.TestTime)
            self.step_time              = float(info.StepTime)
            self.voltage                = float(info.Voltage)
            self.current                = float(info.Current)
            self.power                  = float(info.Power)
            self.test_object            = str(info.TestObject)
            self.nominal_capacity       = float(info.NominalCapacity)
            self.imax                   = float(info.Imax)
            self.vmax                   = float(info.Vmax)
            self.vmin                   = float(info.Vmin)
            self.nominal_voltage        = float(info.NominalVoltage)
            self.nominal_capacitance    = float(info.NominalCapacitance)
            self.nominal_ir             = float(info.NominalIR)
            self.specific_capacity      = float(info.SpecificCapacity)
            self.is_auto_calculate      = bool(info.IsAutoCalculate)
            self.mass                   = float(info.Mass)
            self.charge_capacity        = float(info.ChargeCapacity)
            self.discharge_capacity     = float(info.DischargeCapacity)
            self.charge_energy          = float(info.ChargeEnergy)
            self.discharge_energy       = float(info.DishargeEnergy)
            self.internal_resistance    = float(info.InternalResistance)
            self.dvdt                   = float(info.dvdt)
            self.dvdq                   = float(info.dvdq)
            self.dqdv                   = float(info.dqdv)
            self.acr                    = float(info.ACR)
            self.aci                    = float(info.ACI)
            self.aci_phase              = float(info.ACIPhase)
            self.can_data               = [GetChannelDataFeedback.CANInfo(item) for item in info.CANs]
            self.smb_data               = [GetChannelDataFeedback.SMBInfo(item) for item in info.SMBs]
            self.aux_data               = [[GetChannelDataFeedback.AuxData(aux) for aux in group] for group in info.AuxeDatas]
            # self.eq_data              = None
            # self.cell_data            = None

    def __init__(self, feedback: ArbinCommandGetChannelDataFeed):  # type: ignore
        self.channel_data = [GetChannelDataFeedback.ChannelInfo(info) for info in feedback.m_Channels]

class GetResumeDataFeedback:
    class EGetDataResult(IntEnum):
        SUCCESS = 0,
        ERROR = 0x10

    class ResumeDatalInfo:
        class ResumeData:
            def __init__(self, resume_data: ArbinCommandGetResumeDataFeed.ResumeDatalInfo): # type: ignore
                self.test_id = resume_data.TestID
                self.cycle = resume_data.Cycle
                self.step_index = resume_data.StepIndex
                self.test_time = resume_data.TestTime
                self.step_time = resume_data.StepTime
                self.c_capacity = resume_data.CCapacity
                self.d_capacity = resume_data.DCapacity
                self.c_energy = resume_data.CEnergy
                self.d_energy = resume_data.DEnergy
                self.tc_time1 = resume_data.TC_Time1
                self.tc_time2 = resume_data.TC_Time2
                self.tc_time3 = resume_data.TC_Time3
                self.tc_time4 = resume_data.TC_Time4
                self.tc_c_capacity1 = resume_data.TC_CCapacity1
                self.tc_c_capacity2 = resume_data.TC_CCapacity2
                self.tc_d_capacity1 = resume_data.TC_DCapacity1
                self.tc_d_capacity2 = resume_data.TC_DCapacity2
                self.tc_c_energy1 = resume_data.TC_CEnergy1
                self.tc_c_energy2 = resume_data.TC_CEnergy2
                self.tc_d_energy1 = resume_data.TC_DEnergy1
                self.tc_d_energy2 = resume_data.TC_DEnergy2
                self.tc_counter1 = resume_data.TC_Counter1
                self.tc_counter2 = resume_data.TC_Counter2
                self.tc_counter3 = resume_data.TC_Counter3
                self.tc_counter4 = resume_data.TC_Counter4
                self.tc_counter5 = resume_data.TC_Counter5
                self.tc_counter6 = resume_data.TC_Counter6
                self.tc_counter7 = resume_data.TC_Counter7
                self.tc_counter8 = resume_data.TC_Counter8
                self.charge_capacity_time = resume_data.ChargeCapacityTime
                self.discharge_capacity_time = resume_data.DischargeCapacityTime
                self.mvud1 = resume_data.MVUD1
                self.mvud2 = resume_data.MVUD2
                self.mvud3 = resume_data.MVUD3
                self.mvud4 = resume_data.MVUD4
                self.mvud5 = resume_data.MVUD5
                self.mvud6 = resume_data.MVUD6
                self.mvud7 = resume_data.MVUD7
                self.mvud8 = resume_data.MVUD8
                self.mvud9 = resume_data.MVUD9
                self.mvud10 = resume_data.MVUD10
                self.mvud11 = resume_data.MVUD11
                self.mvud12 = resume_data.MVUD12
                self.mvud13 = resume_data.MVUD13
                self.mvud14 = resume_data.MVUD14
                self.mvud15 = resume_data.MVUD15
                self.mvud16 = resume_data.MVUD16
        def __init__(self, info: ArbinCommandGetResumeDataFeed.ResumeDatalInfo): # type: ignore
            self.channel_index = int(info.Channel)
            self.channel_code = GetResumeDataFeedback.EGetDataResult(int(info.channelCode))
            self.resume_data = GetResumeDataFeedback.ResumeDatalInfo.ResumeData(info.ResumeData)
            self.test_name = str(info.TestName)
            self.schedule = str(info.Schedule)
            self.creator = str(info.Createor)
            self.comment = str(info.Comment)
            self.start_time = str(info.StartTime)
            self.step_names = [str(step) for step in info.Steps]
    
    def __init__(self, feedback: ArbinCommandGetResumeDataFeed): # type: ignore
        self.channel_data = [GetResumeDataFeedback.ResumeDatalInfo(info) for info in feedback.m_Channels]

class GetChannelAssignmentFeedback:
    class EGetDataResult(IntEnum):
        SUCCESS = 0,
        ERROR = 0x10

    class ChannelAssignmentInfo:
        def __init__(self, info: ArbinCommandGetStartDataFeed.StartDatalInfo): # type: ignore
            self.channel = int(info.Channel)
            self.channel_code = GetChannelAssignmentFeedback.EGetDataResult(int(info.channelCode))
            self.schedule = str(info.Schedule)
            self.fMV_UD1 = float(info.fMV_UD1)
            self.fMV_UD2 = float(info.fMV_UD2)
            self.fMV_UD3 = float(info.fMV_UD3)
            self.fMV_UD4 = float(info.fMV_UD4)
            self.fMV_UD5 = float(info.fMV_UD5)
            self.fMV_UD6 = float(info.fMV_UD6)
            self.fMV_UD7 = float(info.fMV_UD7)
            self.fMV_UD8 = float(info.fMV_UD8)
            self.fMV_UD9 = float(info.fMV_UD9)
            self.fMV_UD10 = float(info.fMV_UD10)
            self.fMV_UD11 = float(info.fMV_UD11)
            self.fMV_UD12 = float(info.fMV_UD12)
            self.fMV_UD13 = float(info.fMV_UD13)
            self.fMV_UD14 = float(info.fMV_UD14)
            self.fMV_UD15 = float(info.fMV_UD15)
            self.fMV_UD16 = float(info.fMV_UD16)
            self.test_names = [str(name) for name in info.TestNames]
            self.step_names = [str(step) for step in info.Steps]

    def __init__(self, feedback: ArbinCommandGetStartDataFeed): # type: ignore
        self.channel_data = [GetChannelAssignmentFeedback.ChannelAssignmentInfo(info) for info in feedback.m_Channels]