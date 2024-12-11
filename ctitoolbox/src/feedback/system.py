import json
from enum import IntEnum

import ArbinCTI.Core as ArbinCTI # type: ignore

"""""""""""""""""""""""""""
System & Connection
- GetSerailNumberFeedback
- GetMITSVersionFeedback
- LoginFeedback
"""""""""""""""""""""""""""
class GetSerailNumberFeedback:
    class ASSIGN_TOKEN(IntEnum):
        CTI_GET_SERAIL_SUCESS = 0,
        CTI_ASSIGN_ERROR = 0x10,

    def __init__(self, feedback: ArbinCTI.ArbinCommandGetSerialNumberFeed): 
        self.serial_number  = float(feedback.SerialNum)
        self.result         = GetSerailNumberFeedback.ASSIGN_TOKEN(int(feedback.Result))
    
    def to_json(self):
        return json.dumps(self.__dict__)

class GetMITSVersionFeedback:
    def __init__(self, feedback: ArbinCTI.ArbinCommandGetServerSoftwareVersionNumberFeed): 
        self.version = str(feedback.ServerVersionNumber)

    def to_json(self):
        return json.dumps(self.__dict__)
    
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

    def __init__(self, feedback: ArbinCTI.ArbinCommandLoginFeed): 
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
        self.server_info        = str(feedback.ServerInfo) if feedback.ServerInfo else None