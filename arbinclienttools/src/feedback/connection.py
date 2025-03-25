__doc__ = """
[Channel Management Feedback]
- LoginFeedback

[Subsidary Classes]
- UserInfo
- SystemConfigFile
- ServerInfo
- SysCfgCycler (not implemented yet)
"""

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.base import (
    DictReprBase,
)

from arbinclienttools.src.enumeration import ELoginResult

class LoginFeedback(DictReprBase):
    class UserInfo(DictReprBase):
        def __init__(self, obj):
            self.user_role          = str(obj.UserRole)
            self.user_permission    = str(obj.UserPermission)
            self.user_name          = str(obj.UserName)
            self.user_image_base64  = str(obj.UserImageBase64)
            self.comments           = str(obj.Comments)
            self.email_address      = str(obj.EmailAddress)
            self.telephone_number   = str(obj.TelephoneNumber)
            self.channel_number     = self._unpack_cs_sorted_dict(obj.ChannelNumber, (str, int))

    class SystemConfigFile(DictReprBase):
        class SysCfgGlobal(DictReprBase):
            def __init__(self, obj):
                self.customer                   = str(obj.Customer)
                self.company                    = str(obj.Company)
                self.customer_note              = str(obj.CustomerNote)
                self.data_log_speed             = int(obj.DataLogSpeed)
                self.ups_enabled                = bool(obj.UPSEnabled)
                self.ups_use_positive_signal    = bool(obj.UPSUsePositiveSignal)
                self.ups_shutdown_computer      = bool(obj.UPSShutdownComputer)
                self.ups_auto_resume_test       = bool(obj.UpsAutoResumeTest)
                self.ups_threshold_min          = int(obj.UpsThresholdMin)
                self.current_range_count        = int(obj.CurrentRangeCount)
                self.voltage_range_count        = int(obj.VoltageRangeCount)

        class SysCfgCycler(DictReprBase):
            def __init__(self, obj):
                raise NotImplementedError("SysCfgCycler is not implemented yet")

        def __init__(self, obj):
            self.version        = str(obj.Version)
            self.muid           = str(obj.MUID)
            self.global_config  = LoginFeedback.SystemConfigFile.SysCfgGlobal(obj.Global)
            self.cyclers        = obj.Cyclers # Not implemented yet
            self.time_id        = str(obj.TimeID.ToString())
        
    class ServerInfo(DictReprBase):
        def __init__(self, obj):
            self.user_info              = LoginFeedback.UserInfo(obj.UserInfo)
            self.server_version_number  = str(obj.ServerVersionNumber)
            self.system_config          = LoginFeedback.SystemConfigFile(obj.SystemConfig) if obj.SystemConfig else None
            
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.RequestInformation.LoginFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.RequestInformation.LoginFDBK")
        self.login_reusult      = ELoginResult(int(obj.LoginResult))
        self.result             = str(obj.Result)
        self.server_information = self.ServerInfo(obj.ServerInformation) if obj.ServerInformation else None
