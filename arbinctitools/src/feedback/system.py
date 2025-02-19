import ArbinCTI.Core as ArbinCTI # type: ignore

from common.src.base import (
    DictReprBase,
    SafeIntEnumBase
)

"""""""""""""""""""""""""""
System & Connection
- LoginFeedback
- LogicConnectFeedback
- SendMsgToCTIFeedBack
- UnknownCommandFeedback
- StartAutomaticCalibrationFeedback
"""""""""""""""""""""""""""
  
class LoginFeedback(DictReprBase):
    class ECTIVersion(SafeIntEnumBase):
        None_ = 0
        CTI_PRO7 = 0
        CTI_PRO8 = 1
        Pro8_2 = 2
        MitsX_1 = 0x01000001
        MitsX_2 = 0x01000002
        MitsX_3 = 0x01000003
        MitsX_4 = 0x01000004
        MitsX_5 = 0x01000005
        MitsX_6 = 0x01000006
        MitsX_7 = 0x01000007
        MitsX_8 = 0x01000008
        MitsX_SPTT = 0x01001001
        Pro7_MVUD = 0x02000001
        TY_Pro7_2 = 0x02000002
        TY_Pro7_3 = 0x02000003
        TY_Pro8_1 = 0x04000001
        TY_Pro8_2 = 0x04000002
        TY_Pro8_SPTT = 0x04001001
        ZY_Pro8_GX = 0x08000001

    class ELoginResult(SafeIntEnumBase):
        CTI_LOGIN_SUCCESS = 1
        CTI_LOGIN_FAILED = 2
        CTI_LOGIN_BEFORE_SUCCESS = 3

    def __init__(self, feedback: ArbinCTI.ArbinCommandLoginFeed): 
        if not isinstance(feedback, ArbinCTI.ArbinCommandLoginFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandLoginFeed', got '{type(feedback)}'")
        self.result              = LoginFeedback.ELoginResult(int(feedback.Result))
        self.user_type           = int(feedback.UserType)
        self.serial_number       = str(feedback.SN)
        self.note                = str(feedback.Note)
        self.nickname            = str(feedback.NickName)
        self.location            = str(feedback.Location)
        self.emergency_contact   = str(feedback.EmergencyContactNameAndPhoneNumber)
        self.other_comments      = str(feedback.OtherComments)
        self.email               = str(feedback.Email)
        self.itac                = int(feedback.ITAC)
        self.call                = str(feedback.CALL)
        self.is_allow_to_control = int(feedback.IsAllowToControl)
        self.channel_count       = int(feedback.ChannelNum)
        self.version             = LoginFeedback.ECTIVersion(int(feedback.Version))
        # self.img: Optional[Image.Image] = feedback.Img if isinstance(feedback.Img, Image.Image) else None
        self.server_info         = str(feedback.ServerInfo) if feedback.ServerInfo else None

class LogicConnectFeedback(DictReprBase):
    def __init__(self, feedback: ArbinCTI.ArbinCommandLogicConnectFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandLogicConnectFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandLogicConnectFeed', got '{type(feedback)}'")
        self.dwSetKickOut    = int(feedback.dwSetKickOut)
        self.dwConnectResult = int(feedback.dwConnectResult)

class SendMsgToCTIFeedback(DictReprBase):
    class EResult(SafeIntEnumBase):
        CTI_SEND_MSG_SUCCESS = 1
        CTI_SEND_MSG_FAILED = 2

    def __init__(self, feedback: ArbinCTI.ArbinCommandSendMsgToCTIFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandSendMsgToCTIFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandSendMsgToCTIFeed', got '{type(feedback)}'")
        self.result = SendMsgToCTIFeedback.EResult(int(feedback.Result))

class UnknownCommandFeedback(DictReprBase):
    def __init__(self, feedback: ArbinCTI.ArbinCommandUnknownCommandFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandUnknownCommandFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandUnknownFeed', got '{type(feedback)}'")
        self.unknown_commnad        = int(feedback.UnknownCMD)
        self.unknown_commnad_extend = int(feedback.UnknownCMDExtend)
    
class StartAutomaticCalibrationFeedback(DictReprBase):
    class EResult(SafeIntEnumBase):
        CTI_AUTOCALI_START_SUCCESS = 1
        CTI_AUTOCALI_START_FAILED = 2

    def __init__(self, feedback: ArbinCTI.ArbinCommandStartAutomaticCalibrationFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandStartAutomaticCalibrationFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandStartAutomaticCalibrationFeed', got '{type(feedback)}'")
        self.result = StartAutomaticCalibrationFeedback.EResult(int(feedback.Result))