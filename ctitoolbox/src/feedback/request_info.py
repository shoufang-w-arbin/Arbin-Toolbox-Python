import copy

import ArbinCTI.Core as ArbinCTI # type: ignore

from ctitoolbox.src.base import (
    DictReprBase,
    SafeIntEnumBase
)

"""""""""""""""""""""""""""
Request Info
- GetChannelDataFeedback
- GetResumeDataFeedback
- GetStartDataFeedback
"""""""""""""""""""""""""""

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

class GetMappingAuxFeedback(DictReprBase):
    class EAuxChannelType(SafeIntEnumBase):
        Voltage = 0
        Temperature = 1
        Pressure = 2
        DI = 3
        DO = 4
        ExternalCharge = 5
        Safety = 6
        Humidity = 7
        AO = 8
        CANBMS = 9
        SMB = 10

    class AuxChannelInfo(DictReprBase):
        def __init__(self, info: ArbinCTI.Common.GetMappingAux.AuxChannelInfo):
            self.aux_channel_type = GetMappingAuxFeedback.EAuxChannelType(int(info.AuxChannelType))
            self.aux_count        = int(info.AuxCount)

    class MappingInfo(DictReprBase):
        def __init__(self, info: ArbinCTI.Common.GetMappingAux.MappingInfo):
            self.channel_index    = int(info.ChannelIndex)
            self.aux_channel_info = [GetMappingAuxFeedback.AuxChannelInfo(info) for info in info.AuxChannelInfos]

    def __init__(self, feedback: ArbinCTI.ArbinCommandGetMappingAuxFeed):
        if not isinstance(feedback, ArbinCTI.ArbinCommandGetMappingAuxFeed):
            raise TypeError(f"'feedback' must be an instance of 'ArbinCTI.Core.ArbinCommandGetMappingAuxFeed', got '{type(feedback)}'")
        self.task_id      = int(feedback.TaskID)
        self.mapping_info = [GetMappingAuxFeedback.MappingInfo(info) for info in feedback.MappingInfos]