import copy

import ArbinCTI.Core as ArbinCTI # type: ignore

from arbintoolbox.src.base import (
    DictReprBase,
    SafeIntEnumBase
)

"""""""""""""""""""""""""""
Test Control
- StartChannelFeedback
- StopChannelFeedback
- ResumeChannelFeedback
- JumpChannelFeedback
- ContinueChannelFeedback
- GetChannelDataFeedback
- GetResumeDataFeedback
- GetStartDataFeedback
"""""""""""""""""""""""""""
class StartChannelFeedback(DictReprBase):
    class EStartToken(SafeIntEnumBase):
        CTI_START_SUCCESS = 0
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

    def __init__(self, feedback: ArbinCTI.ArbinCommandStartChannelFeed): 
        if not isinstance(feedback, ArbinCTI.ArbinCommandStartChannelFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandStartChannelFeed', got '{type(feedback)}'")
        self.result = StartChannelFeedback.EStartToken(int(feedback.Result))

class StopChannelFeedback(DictReprBase):
    class EStopToken(SafeIntEnumBase):
        SUCCESS = 0
        STOP_INDEX = 0x10
        STOP_ERROR = 0x11
        STOP_NOT_RUNNING = 0x12
        STOP_CHANNEL_NOT_CONNECT = 0x13

    def __init__(self, feedback: ArbinCTI.ArbinCommandStopChannelFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandStopChannelFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandStopChannelFeed', got '{type(feedback)}'")
        self.result = StopChannelFeedback.EStopToken(int(feedback.Result))

class ResumeChannelFeedback(DictReprBase):
    class EResumeToken(SafeIntEnumBase):
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

    def __init__(self, feedback: ArbinCTI.ArbinCommandResumeChannelFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandResumeChannelFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandResumeChannelFeed', got '{type(feedback)}'")
        self.result = ResumeChannelFeedback.EResumeToken(int(feedback.Result))

class JumpChannelFeedback(DictReprBase):
    class EJumpToken(SafeIntEnumBase):
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
        CTI_JUMP_CHANNEL_SUSPENT = 0x29,
        CTI_JUMP_ACIM_TESTING = 0x2A

    def __init__(self, feedback: ArbinCTI.ArbinCommandJumpChannelFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandJumpChannelFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandJumpChannelFeed', got '{type(feedback)}'")
        self.result        = JumpChannelFeedback.EJumpToken(int(feedback.Result))
        self.error_channel = int(feedback.errorChannel)

class ContinueChannelFeedback(DictReprBase):
    class EContinueToken(SafeIntEnumBase):
        CTI_CONTINUE_SUCCESS = 0
        CTI_CONTINUE_ERROR = 0x11
        CTI_CONTINUE_CHANNEL_RUNNING = 0x12
        CTI_CONTINUE_CHANNEL_NOT_CONNECT = 0x13
        CTI_CONTINUE_CHANNEL_CALIBRATING = 0x14
        CTI_CONTINUE_NOT_PAUSE_NORMAL = 0x15
        CTI_CONTINUE_CHANNEL_UNSAFE = 0x16
    
    def __init__(self, feedback: ArbinCTI.ArbinCommandContinueChannelFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandContinueChannelFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandContinueChannelFeed', got '{type(feedback)}'")
        self.result = ContinueChannelFeedback.EContinueToken(int(feedback.Result))

class GetChannelDataFeedback(DictReprBase):
    class EChannelNeedType(SafeIntEnumBase):
        THIRD_PARTY_GET_CHANNELS_INFO_NEED_TYPE_BMS = 0x100
        THIRD_PARTY_GET_CHANNELS_INFO_NEED_TYPE_SMB = 0x200
        THIRD_PARTY_GET_CHANNELS_INFO_NEED_TYPE_AUX = 0x400
        THIRD_PARTY_GET_CHANNELS_INFO_NEED_TYPE_EQ = 0x800
        THIRD_PARTY_GET_CHANNELS_INFO_NEED_TYPE_CELL = 0x1000
    
    class EGetChannelType(SafeIntEnumBase):
        ALLCHANNEL = 1
        RUNNING = 2
        UNSAFE = 3

        def to_cs(self) -> ArbinCTI.ArbinCommandGetChannelDataFeed.GET_CHANNEL_TYPE:
            """Convert to C# ArbinCommandGetChannelDataFeed.GET_CHANNEL_TYPE"""
            return ArbinCTI.ArbinCommandGetChannelDataFeed.GET_CHANNEL_TYPE(self.value)
    
    class EChannelStatus(SafeIntEnumBase):
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

    class ECTISPTTEQStatus(SafeIntEnumBase):
        Idle = 0
        Charging = 1
        Discharging = 2
        CurrentUnsafe = 3
        VoltageUnsafe = 4

    class ECTISPTTCellStatus(SafeIntEnumBase):
        Null = 0 
        UnUse = 1
        NoCell = 2
        Idle = 3
        Charging = 4
        Discharging = 5
        CurrentUnsafe = 6
        VoltageUnsafe = 7

    class AuxData(DictReprBase):
        def __init__(self, data: ArbinCTI.ArbinCommandGetChannelDataFeed.AuxData):
            self.value    = float(data.Value)
            self.value_dt = float(data.dtValue)

    class CANInfo(DictReprBase):
        def __init__(self, data: ArbinCTI.ArbinCommandGetChannelDataFeed.CANInfo):
            self.idx   = int(data.nIndex)
            self.value = float(data.Value)
            self.unit  = str(data.Unit)

    class SMBInfo(DictReprBase):
        def __init__(self, data: ArbinCTI.ArbinCommandGetChannelDataFeed.SMBInfo):
            self.idx   = int(data.nIndex)
            self.type  = int(data.nType)
            self.unit  = str(data.Unit)
            self.value = data.Value  # Keeping this generic as 'object'

    class CANMonitorInfo(DictReprBase):
        def __init__(self, data: ArbinCTI.ArbinCommandGetChannelDataFeed.CANMonitorInfo):
            self.is_offline = bool(data.IsOffline)
            self.alias_name = str(data.AliasName)
            self.meta_name  = str(data.MetaName)
            self.data_type  = int(data.DataType)
            self.value      = str(data.Value)

    class SMBMonitorInfo(DictReprBase):
        def __init__(self, data: ArbinCTI.ArbinCommandGetChannelDataFeed.SMBMonitorInfo):
            self.is_offline = bool(data.IsOffline)
            self.alias_name = str(data.AliasName)
            self.meta_name  = str(data.MetaName)
            self.data_type  = int(data.DataType)
            self.value      = str(data.Value)

    class AuxMonitorData(DictReprBase):
        def __init__(self, data: ArbinCTI.ArbinCommandGetChannelDataFeed.AuxMonitorData):
            self.aux_type          = str(data.AuxType)
            self.alias_name        = str(data.AliasName)
            self.aux_ch_global_id  = int(data.AuxChGlobalID)
            self.aux_ch_virtual_id = int(data.AuxChVirtualID)
            self.value             = float(data.Value)
            self.dxdt              = float(data.dxdt)

    class CTISPTTTrayMetaValue(DictReprBase):
        def __init__(self, data: ArbinCTI.Common.CTISPTTTrayMetaValue):
            self.value      = float(data.Value)
            self.alias_name = str(data.AliasName)

    class CTISPTTTrayData(DictReprBase):
        def __init__(self, data: ArbinCTI.Common.CTISPTTTrayData):
            self.global_index = int(data.GlobalIndex)
            self.barcode = str(data.Barcode)
            self.info = str(data.Info)
            self.data = [GetChannelDataFeedback.CTISPTTTrayMetaValue(item) for item in data.Datas]

    class CTISPTTEQData(DictReprBase):
        def __init__(self, data: ArbinCTI.Common.CTISPTTEQData):
            self.parent_tray_global_index  = int(data.ParentTrayGlobalIndex)
            self.global_index              = int(data.GlobalIndex)
            self.virtual_index_in_iv       = int(data.VirtualIndexInIV)
            self.voltage                   = float(data.Voltage)
            self.current                   = float(data.Current)
            self.power                     = float(data.Power)
            self.charge_capacity           = float(data.ChargeCapacity)
            self.discharge_capacity        = float(data.DischargeCapacity)
            self.charge_energy             = float(data.ChargeEnergy)
            self.discharge_energy          = float(data.DishargeEnergy) 
            self.internal_resistance       = float(data.InternalResistance)
            self.auxiliary_temperature     = float(data.AuxiliaryTemperature)
            self.status                    = GetChannelDataFeedback.ECTISPTTEQStatus(int(data.Status))
            self.barcode                   = str(data.Barcode)
            self.info                      = str(data.Info)
    
    class CTISPTTCellData(DictReprBase):
        def __init__(self, data: ArbinCTI.Common.CTISPTTCellData):
            self.parent_tray_global_index   = int(data.ParentTrayGlobalIndex)
            self.parent_eq_global_index     = int(data.ParentEQGlobalIndex)
            self.global_index               = int(data.GlobalIndex)
            self.virtual_index_in_iv        = int(data.VirtualIndexInIV)
            self.voltage                    = float(data.Voltage)
            self.current                    = float(data.Current)
            self.power                      = float(data.Power)
            self.charge_capacity            = float(data.ChargeCapacity)
            self.discharge_capacity         = float(data.DischargeCapacity)
            self.charge_energy              = float(data.ChargeEnergy)
            self.discharge_energy           = float(data.DishargeEnergy) 
            self.internal_resistance        = float(data.InternalResistance)
            self.auxiliary_temperature      = float(data.AuxiliaryTemperature)
            self.status                     = GetChannelDataFeedback.ECTISPTTCellStatus(int(data.Status))
            self.barcode                    = str(data.Barcode)
            self.info                       = str(data.Info)
            self.position_x                 = int(data.PositionX)
            self.position_y                 = int(data.PositionY)

    class ChannelInfo(DictReprBase):
        class AuxType(SafeIntEnumBase):
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
    
        def __init__(self, info: ArbinCTI.ArbinCommandGetChannelDataFeed.ChannelInfo):
            self.channel_index          = int(info.Channel)
            self.status                 = GetChannelDataFeedback.EChannelStatus(int(info.Status))
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
            self.eq_data   = [GetChannelDataFeedback.CTISPTTEQData(item) for item in info.EQDatas]
            self.cell_data = [GetChannelDataFeedback.CTISPTTCellData(item) for item in info.CellDatas]
            self.can       = [GetChannelDataFeedback.CANInfo(item) for item in info.CAN] if info.CAN else []            # default to 'null' in C#
            self.smb       = [GetChannelDataFeedback.SMBInfo(item) for item in info.SMB] if info.SMB else []            # default to 'null' in C#
            self.auxs  = [
                [GetChannelDataFeedback.AuxData(aux) for aux in aux_type] if aux_type else []
                for aux_type in info.Auxs
            ]
            # self.can_data  = [GetChannelDataFeedback.CANMonitorInfo(item) for item in info.CANs] if info.CANs else []   # default to 'null' in C#
            # self.smb_data  = [GetChannelDataFeedback.SMBMonitorInfo(item) for item in info.SMBs] if info.SMBs else []   # default to 'null' in C#
            # self.aux_data  = [
            #     [GetChannelDataFeedback.AuxMonitorData(item) for item in aux_list] if aux_list else []
            #     for aux_list in info.AuxeDatas
            # ]
            
        def to_dict(self):
            data = copy.deepcopy(self.__dict__)
            data['status']      = self.status.name
            data['cans']        = [can.to_dict() for can in self.can]
            data['smbs']        = [smb.to_dict() for smb in self.smb]
            data['eq_data']     = [eq.to_dict() for eq in self.eq_data]
            data['cell_data']   = [cell.to_dict() for cell in self.cell_data]
            data['auxs']        = [[aux.to_dict() for aux in aux_list] for aux_list in self.auxs]
            # data['can_data']    = [can.to_dict() for can in self.can_data]
            # data['smb_data']    = [smb.to_dict() for smb in self.smb_data]
            # data['aux_data']    = [[aux.to_dict() for aux in aux_list] for aux_list in self.aux_data]
            return data

    def __init__(self, feedback: ArbinCTI.ArbinCommandGetChannelDataFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandGetChannelDataFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandGetChannelDataFeed', got '{type(feedback)}'")
        
        self.channel_data = [GetChannelDataFeedback.ChannelInfo(info) for info in feedback.m_Channels]

class GetResumeDataFeedback(DictReprBase):
    class EResult(SafeIntEnumBase):
        SUCCESS = 0,
        ERROR = 0x10

    class ResumeDatalInfo(DictReprBase):
        class ResumeData(DictReprBase):
            def __init__(self, resume_data: ArbinCTI.ArbinCommandGetResumeDataFeed.ResumeDatalInfo):
                self.test_id                  = int(resume_data.TestID)
                self.cycle                    = int(resume_data.Cycle)
                self.step_index               = int(resume_data.StepIndex)
                self.test_time                = float(resume_data.TestTime)
                self.step_time                = float(resume_data.StepTime)
                self.c_capacity               = float(resume_data.CCapacity)
                self.d_capacity               = float(resume_data.DCapacity)
                self.c_energy                 = float(resume_data.CEnergy)
                self.d_energy                 = float(resume_data.DEnergy)
                self.tc_time1                 = float(resume_data.TC_Time1)
                self.tc_time2                 = float(resume_data.TC_Time2)
                self.tc_time3                 = float(resume_data.TC_Time3)
                self.tc_time4                 = float(resume_data.TC_Time4)
                self.tc_c_capacity1           = float(resume_data.TC_CCapacity1)
                self.tc_c_capacity2           = float(resume_data.TC_CCapacity2)
                self.tc_d_capacity1           = float(resume_data.TC_DCapacity1)
                self.tc_d_capacity2           = float(resume_data.TC_DCapacity2)
                self.tc_c_energy1             = float(resume_data.TC_CEnergy1)
                self.tc_c_energy2             = float(resume_data.TC_CEnergy2)
                self.tc_d_energy1             = float(resume_data.TC_DEnergy1)
                self.tc_d_energy2             = float(resume_data.TC_DEnergy2)
                self.tc_counter1              = float(resume_data.TC_Counter1)
                self.tc_counter2              = float(resume_data.TC_Counter2)
                self.tc_counter3              = float(resume_data.TC_Counter3)
                self.tc_counter4              = float(resume_data.TC_Counter4)
                self.tc_counter5              = float(resume_data.TC_Counter5)
                self.tc_counter6              = float(resume_data.TC_Counter6)
                self.tc_counter7              = float(resume_data.TC_Counter7)
                self.tc_counter8              = float(resume_data.TC_Counter8)
                self.charge_capacity_time     = float(resume_data.ChargeCapacityTime)
                self.discharge_capacity_time  = float(resume_data.DischargeCapacityTime)
                self.mvud1                    = float(resume_data.MVUD1)
                self.mvud2                    = float(resume_data.MVUD2)
                self.mvud3                    = float(resume_data.MVUD3)
                self.mvud4                    = float(resume_data.MVUD4)
                self.mvud5                    = float(resume_data.MVUD5)
                self.mvud6                    = float(resume_data.MVUD6)
                self.mvud7                    = float(resume_data.MVUD7)
                self.mvud8                    = float(resume_data.MVUD8)
                self.mvud9                    = float(resume_data.MVUD9)
                self.mvud10                   = float(resume_data.MVUD10)
                self.mvud11                   = float(resume_data.MVUD11)
                self.mvud12                   = float(resume_data.MVUD12)
                self.mvud13                   = float(resume_data.MVUD13)
                self.mvud14                   = float(resume_data.MVUD14)
                self.mvud15                   = float(resume_data.MVUD15)
                self.mvud16                   = float(resume_data.MVUD16)

        def __init__(self, info: ArbinCTI.ArbinCommandGetResumeDataFeed.ResumeDatalInfo):
            self.channel_index  = int(info.Channel)
            self.channel_code   = GetResumeDataFeedback.EResult(int(info.channelCode))
            self.resume_data    = GetResumeDataFeedback.ResumeDatalInfo.ResumeData(info.ResumeData)
            self.test_name      = str(info.TestName)
            self.schedule       = str(info.Schedule)
            self.creator        = str(info.Createor)
            self.comment        = str(info.Comment)
            self.start_time     = str(info.StartTime)
            self.step_names     = [str(step) for step in info.Steps]
    
    def __init__(self, feedback: ArbinCTI.ArbinCommandGetResumeDataFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandGetResumeDataFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandGetResumeDataFeed', got '{type(feedback)}'")
        self.channel_data = [GetResumeDataFeedback.ResumeDatalInfo(info) for info in feedback.m_Channels]

class GetStartDataFeedback(DictReprBase):
    """Get the channel assignments, including the channel number, channel code, schedule, MVs, and test names."""
    class EResult(SafeIntEnumBase):
        SUCCESS = 0,
        ERROR = 0x10

    class StartDataInfo(DictReprBase):
        def __init__(self, info: ArbinCTI.ArbinCommandGetStartDataFeed.StartDatalInfo):
            self.channel        = int(info.Channel)
            self.channel_code   = GetStartDataFeedback.EResult(int(info.channelCode))
            self.schedule       = str(info.Schedule)
            self.fMV_UD1        = float(info.fMV_UD1)
            self.fMV_UD2        = float(info.fMV_UD2)
            self.fMV_UD3        = float(info.fMV_UD3)
            self.fMV_UD4        = float(info.fMV_UD4)
            self.fMV_UD5        = float(info.fMV_UD5)
            self.fMV_UD6        = float(info.fMV_UD6)
            self.fMV_UD7        = float(info.fMV_UD7)
            self.fMV_UD8        = float(info.fMV_UD8)
            self.fMV_UD9        = float(info.fMV_UD9)
            self.fMV_UD10       = float(info.fMV_UD10)
            self.fMV_UD11       = float(info.fMV_UD11)
            self.fMV_UD12       = float(info.fMV_UD12)
            self.fMV_UD13       = float(info.fMV_UD13)
            self.fMV_UD14       = float(info.fMV_UD14)
            self.fMV_UD15       = float(info.fMV_UD15)
            self.fMV_UD16       = float(info.fMV_UD16)
            self.test_names     = [str(name) for name in info.TestNames]
            self.step_names     = [str(step) for step in info.Steps]

    def __init__(self, feedback: ArbinCTI.ArbinCommandGetStartDataFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandGetStartDataFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandGetStartDataFeed', got '{type(feedback)}'")
        self.channel_data = [GetStartDataFeedback.StartDataInfo(info) for info in feedback.m_Channels]