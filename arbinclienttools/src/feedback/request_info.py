__doc__ = """
[Request Information Feedback]
- GetStartDataFeedback
- GetResumeDataFeedback 
- GetMonitorDataFeedback
- GetBarcodeInfoFeedback
- GetMappingAuxFeedback (not supported yet)
- SubscribeMonitorDataFeedback
- SubscribeChannelDataFeedback
- SubscribeTestInfoDataFeedback
- SubscribeEventDataFeedback
- SubscribeDiagnosticEventDataFeedback
- SubscribeSPTTEQCELLDataFeedback

[Subsidary Classes]
- ChannelData
- TestInfoData
- TestInfoSPTTEngagement
- TestInfoSPTTEQ
- TestInfoSPTTCell
- ChannelEvents
- ChannelDiagnosticEventData
- SPTTLogData
"""

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from common.src.base import (
    DictReprBase,
)
from arbinclienttools.src.enumeration import (
    EGetMonitorDataResult,
)
from arbinclienttools.src.feedback.common import (
    ChannelMonitorData,
    ResumeDataInfo,
    BarcodeInfo,
    CANMonitorInfo,
    SMBMonitorInfo,
    AuxData,
    SimulationInfo,
    AuxMapping,
)

class GetStartDataFeedback(DictReprBase):
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.RequestInformation.GetStartDataFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.RequestInformation.GetStartDataFDBK")
        self.start_data = [ResumeDataInfo(x) for x in obj.StartDatas]
        self.sn         = int(obj.SN)

class GetResumeDataFeedback(DictReprBase):
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.RequestInformation.GetResumeDataFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.RequestInformation.GetResumeDataFDBK")
        self.resume_data_info   = [ResumeDataInfo(x) for x in obj.ResumeDatalInfos]
        self.sn                 = int(obj.SN)

class GetMonitorDataFeedback(DictReprBase):
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.RequestInformation.GetMonitorDataFDBK):
            raise ValueError("'obj' must be of type ArbinDataModel.RequestInformation.GetMonitorDataFDBK")
        self.channel_monitor_data    = [ChannelMonitorData(x) for x in obj.MonitorDatas]
        self.result                  = str(obj.Result)
        self.get_monitor_data_result = EGetMonitorDataResult(int(obj.GetMonitorDataResult))
        self.sn                      = int(obj.SN)

class GetBarcodeInfoFeedback(DictReprBase):
    def __init__(self, obj):
        if not isinstance(obj, ArbinDataModel.RequestInformation.GetBarcodeInfoFeedbakc):
            raise ValueError("'obj' must be of type ArbinDataModel.RequestInformation.GetBarcodeInfoFeedbakc")
        self.barcode_info = [BarcodeInfo(x) for x in obj.BarcodeInfos]
        self.sn     = int(obj.SN)

class GetMappingAuxFeedback(DictReprBase):
    pass

class SubscribeMonitorDataFeedback(DictReprBase):
    def __init__(self, feedback: ArbinDataModel.SubscribeMonitorDataFDBK):
        if not isinstance(feedback, ArbinDataModel.SubscribeMonitorDataFDBK):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeMonitorDataFDBK', got '{type(feedback)}'")
        self.id_                  = str(feedback.ID)
        self.task_id              = int(feedback.TaskID)
        self.channel_monitor_data = [ChannelMonitorData(x) for x in feedback.ChannelMonitorDatas]

class SubscribeChannelDataFeedback(DictReprBase):
    class ChannelData(DictReprBase):
        def __init__(self, data: ArbinDataModel.ChannelData):
            self.sn                 = str(data.SN)
            self.channel_id         = int(data.ChannelID)
            self.barcode            = str(data.Barcode)
            self.test_name          = str(data.TestName)
            self.test_id            = int(data.TestID)
            self.date_time          = int(data.DateTime)
            self.data_point         = int(data.DataPoint)
            self.status             = str(data.Status)
            self.test_time          = float(data.TestTime)
            self.step_time          = float(data.StepTime)
            self.step_id            = int(data.StepID)
            self.sub_step_id        = int(data.SubStepID)
            self.cycle_id           = int(data.CycleID)
            self.voltage            = float(data.Voltage)
            self.current            = float(data.Current)
            self.power              = float(data.Power)
            self.charge_capacity    = float(data.ChargeCapacity)
            self.discharge_capacity = float(data.DischargeCapacity)
            self.charge_energy      = float(data.ChargeEnergy)
            self.discharge_energy   = float(data.DischargeEnergy)
            self.internal_resistance= float(data.InternalResistance)
            self.dv_dt              = float(data.dVdt)
            self.dq_dv              = float(data.dQdV)
            self.dv_dq              = float(data.dVdQ)
            self.data_flags         = int(data.DataFlags)
            self.limit_id           = float(data.LimitID)
            self.mvuds              = list(data.MVUDs)
            self.tc_counters        = list(data.TCCounters)
            self.cans               = [CANMonitorInfo(x) for x in data.CANs]
            self.smbs               = [SMBMonitorInfo(x) for x in data.SMBs]
            self.auxs               = [AuxData(x) for x in data.Auxs]
            self.dnlc               = float(data.DNLC)
            self.dnc                = float(data.DNC)

    def __init__(self, feedback: ArbinDataModel.SubscribeChannelDataFDBK):
        if not isinstance(feedback, ArbinDataModel.SubscribeChannelDataFDBK):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeChannelDataFDBK', got '{type(feedback)}'")
        self.id_ = str(feedback.ID)
        self.task_id = int(feedback.TaskID)
        self.channel_data = [self.ChannelData(x) for x in feedback.ChannelDatas]

class SubscribeTestInfoDataFeedback(DictReprBase):
    class TestInfoData(DictReprBase):
        class TestInfoSPTTEngagement(DictReprBase):
            def __init__(self, obj):
                self.engagement_id = int(obj.EngagementID)
                self.barcode       = str(obj.Barcode)

        class TestInfoSPTTEQ(DictReprBase):
            def __init__(self, obj):
                self.parent_engagement_id = int(obj.ParentEngagementID)
                self.eq_virtual_id_iv     = int(obj.EQVirtualIDInIV)
                self.eq_global_id         = int(obj.EQGlobalID)

        class TestInfoSPTTCell(DictReprBase):
            def __init__(self, obj):
                self.parent_engagement_id   = int(obj.ParentEngagementID)
                self.parent_eq_global_id    = int(obj.ParentEQGlobalID)
                self.cell_virtual_id_in_iv  = int(obj.CellVirtualIDInIV)
                self.cell_global_id         = int(obj.CellGlobalID)
                self.position_x             = int(obj.PositionX)
                self.position_y             = int(obj.PositionY)
                self.barcode                = str(obj.Barcode)

        def __init__(self, data: ArbinDataModel.TestInfoData):
            self.sn                      = str(data.SN)
            self.channel_id              = int(data.ChannelID)
            self.barcode                 = str(data.Barcode)
            self.test_name               = str(data.TestName)
            self.test_id                 = int(data.TestID)
            self.start_file_time         = int(data.StartFileTime)
            self.start_date_time         = str(data.StartDateTime)
            self.creator                 = str(data.Creator)
            self.comment                 = str(data.Comment)
            self.schedule_name           = str(data.ScheduleName)
            self.test_object_name        = str(data.TestObjectName)
            self.can_bms_name            = str(data.CANBMSName)
            self.can_bms_file_content    = data.CANBMSFileContent # not implemented yet
            self.smb_name                = str(data.SMBName)
            self.smb_file_content        = data.SMBFileContent    # not implemented yet
            self.capacity                = float(data.Capacity)
            self.specific_capacity       = float(data.SpecificCapacity)
            self.specific_mass           = float(data.SpecificMass)
            self.software_version        = str(data.SoftwareVersion)
            self.firmware_version        = str(data.FirmwareVersion)
            self.simulation_file_names   = [SimulationInfo(x) for x in data.SimulationFileNames]
            self.mappings                = [AuxMapping(x) for x in data.Mappings]
            self.engagements             = [self.TestInfoSPTTEngagement(x) for x in data.Engagements]
            self.eq_datas                = [self.TestInfoSPTTEQ(x) for x in data.EQDatas]
            self.cell_datas              = [self.TestInfoSPTTCell(x) for x in data.CellDatas]

    def __init__(self, feedback: ArbinDataModel.SubscribeTestInfoDataFDBK):
        if not isinstance(feedback, ArbinDataModel.SubscribeTestInfoDataFDBK):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeTestInfoDataFDBK', got '{type(feedback)}'")
        self.id_                = str(feedback.ID)
        self.task_id            = int(feedback.TaskID)
        self.channel_test_info  = [self.TestInfoData(x) for x in feedback.ChannelTestInfos]

class SubscribeEventDataFeedback(DictReprBase):
    class ChannelEvents(DictReprBase):
        def __init__(self, obj):
            self.id_         = str(obj.SN)
            self.channel_id  = int(obj.ChannelID)
            self.test_id     = int(obj.TestID)
            self.date_time   = int(obj.DateTime)
            self.event_type  = int(obj.EventType)
            self.event_desc  = str(obj.EventDesc)
            self.test_time   = float(obj.TestTime)
            self.step_time   = float(obj.StepTime)
            self.cycle_id    = int(obj.CycleID)
            self.step_id     = int(obj.StepID)
            self.sub_step_id = int(obj.SubStepID)
            self.limit_id    = int(obj.LimitID)
            self.tc_counter1 = int(obj.TCCounter1)
            self.tc_counter2 = int(obj.TCCounter2)
            self.tc_counter3 = int(obj.TCCounter3)
            self.tc_counter4 = int(obj.TCCounter4)
            self.tc_counter5 = int(obj.TCCounter5)
            self.tc_counter6 = int(obj.TCCounter6)
            self.tc_counter7 = int(obj.TCCounter7)
            self.tc_counter8 = int(obj.TCCounter8)
            self.tc_timer1   = float(obj.TCTimer1)
            self.tc_timer2   = float(obj.TCTimer2)
            self.tc_timer3   = float(obj.TCTimer3)
            self.tc_timer4   = float(obj.TCTimer4)
    def __init__(self, feedback: ArbinDataModel.SubscribeEventDataFDBK):
        if not isinstance(feedback, ArbinDataModel.SubscribeEventDataFDBK):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeEventDataFDBK', got '{type(feedback)}'")
        self.id_            = str(feedback.ID)
        self.task_id        = int(feedback.TaskID)
        self.channel_event  = [self.ChannelEvents(x) for x in feedback.ChannelEvents]

class SubscribeDiagnosticEventDataFeedback(DictReprBase):
    class ChannelDiagnosticEventData(DictReprBase):
        def __init__(self, obj):
            self.sn                   = str(obj.SN)
            self.channel_id           = int(obj.ChannelID)
            self.diagnostic_envet_msg = str(obj.DiagnosticEventMsg)

    def __init__(self, feedback: ArbinDataModel.SubscribeDiagnosticEventDataFDBK):
        if not isinstance(feedback, ArbinDataModel.SubscribeDiagnosticEventDataFDBK):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeDiagnosticEventDataFDBK', got '{type(feedback)}'")
        self.id_                      = str(feedback.ID)
        self.task_id                  = int(feedback.TaskID)
        self.channel_diagnostic_event = [self.ChannelDiagnosticEventData(x) for x in feedback.ChannelDiagnosticEvents]

class SubscribeSPTTEQCELLDataFeedback(DictReprBase):
    class SPTTLogData(DictReprBase):
        def __init__(self, obj):
            self.barcode            = str(obj.Barcode)
            self.test_id            = int(obj.TestID)
            self.channel_id         = int(obj.ChannelID)
            self.eq_virtual_id      = int(obj.EQVirtualID)
            self.eq_global_id       = int(obj.EQGlobalID)
            self.cell_virtual_id    = int(obj.CellVirtualID)
            self.cell_global_id     = int(obj.CellGlobalID)
            self.tray_id            = int(obj.TrayID)
            self.status             = str(obj.Status)
            self.position_x         = int(obj.PositionX)
            self.position_y         = int(obj.PositionY)
            self.date_time          = int(obj.DateTime)
            self.data_point         = int(obj.DataPoint)
            self.test_time          = float(obj.TestTime)
            self.step_time          = float(obj.StepTime)
            self.cycle_id           = int(obj.CycleID)
            self.step_id            = int(obj.StepID)
            self.sub_step_id        = int(obj.SubStepID)
            self.current            = float(obj.Current)
            self.voltage            = float(obj.Voltage)
            self.temperature        = float(obj.Temperature)
            self.charge_capacity    = float(obj.ChargeCapacity)
            self.discharge_capacity = float(obj.DischargeCapacity)
            self.charge_energy      = float(obj.ChargeEnergy)
            self.discharge_energy   = float(obj.DischargeEnergy)
            self.data_flags         = int(obj.DataFlags)

    def __init__(self, feedback: ArbinDataModel.SubscribeSPTTEQCELLDataFeedback):
        if not isinstance(feedback, ArbinDataModel.SubscribeSPTTEQCELLDataFeedback):
            raise TypeError(f"'feedback' must be an instance of 'Arin.Library.DataModel.SubscribeSPTTEQCELLDataFeedback', got '{type(feedback)}'")
        self.id_        = str(feedback.ID)
        self.task_id    = int(feedback.TaskID)
        self.eq_data    = [self.SPTTLogData(x) for x in feedback.EQDatas]
        self.cell_dasta = [self.SPTTLogData(x) for x in feedback.CellDatas]