__doc__ = """
[Channel Management Arguments]
- StartChannelArgs 
- StopChannelArgs
- JumpStepArgs 
- ResumeChannelArgs 
- ContinueChannelArgs

[Subsidary Classes]
- ChannelResumeData
"""

from dataclasses import (
    dataclass, 
    field,
)

import Arbin.Library.DataModel as ArbinDataModel # type: ignore

from arbinclienttools.src.common.cs_conv import CSConv

@dataclass
class ChannelResumeData:
    """
    Wrapper class of of 'Arbin.Library.DataModel.ChannelManagement.ChannelResumeData'
    """
    channel_id:                int    = -1
    test_id:                   int    = -1
    test_names:                list   = field(default_factory=list)
    schedule_name:             str    = ""
    step_id:                   int    = -1
    sub_step_id:               int    = -1
    cycle_id:                  int    = -1
    test_time:                 float  = 0.0
    step_time:                 float  = 0.0
    charge_capacity:           float  = 0.0
    discharge_capacity:        float  = 0.0
    charge_energy:             float  = 0.0
    discharge_energy:          float  = 0.0
    tc_time1:                  float  = 0.0
    tc_time2:                  float  = 0.0
    tc_time3:                  float  = 0.0
    tc_time4:                  float  = 0.0
    tc_charge_capacity1:       float  = 0.0
    tc_charge_capacity2:       float  = 0.0
    tc_discharge_capacity1:    float  = 0.0
    tc_discharge_capacity2:    float  = 0.0
    tc_charge_energy1:         float  = 0.0
    tc_charge_energy2:         float  = 0.0
    tc_discharge_energy1:      float  = 0.0
    tc_discharge_energy2:      float  = 0.0
    tc_counter1:               float  = 0.0
    tc_counter2:               float  = 0.0
    tc_counter3:               float  = 0.0
    tc_counter4:               float  = 0.0
    tc_counter5:               float  = 0.0
    tc_counter6:               float  = 0.0
    tc_counter7:               float  = 0.0
    tc_counter8:               float  = 0.0
    charge_capacity_time:      float  = 0.0
    discharge_capacity_time:   float  = 0.0
    mvud1:                     float  = 0.0
    mvud2:                     float  = 0.0
    mvud3:                     float  = 0.0
    mvud4:                     float  = 0.0
    mvud5:                     float  = 0.0
    mvud6:                     float  = 0.0
    mvud7:                     float  = 0.0
    mvud8:                     float  = 0.0
    mvud9:                     float  = 0.0
    mvud10:                    float  = 0.0
    mvud11:                    float  = 0.0
    mvud12:                    float  = 0.0
    mvud13:                    float  = 0.0
    mvud14:                    float  = 0.0
    mvud15:                    float  = 0.0
    mvud16:                    float  = 0.0

    def to_cs(self) -> ArbinDataModel.ChannelManagement.ChannelResumeData:
        cs_instance = ArbinDataModel.ChannelManagement.ChannelResumeData()
        cs_instance.ChannelID              = CSConv.to_int(self.channel_id)
        cs_instance.TestID                 = CSConv.to_int(self.test_id)
        cs_instance.TestNames              = CSConv.to_list(self.test_names, CSConv.EDataType.STRING)
        cs_instance.ScheduleName           = CSConv.to_string(self.schedule_name)
        cs_instance.StepID                 = CSConv.to_int(self.step_id)
        cs_instance.SubStepID              = CSConv.to_int(self.sub_step_id)
        cs_instance.CycleID                = CSConv.to_int(self.cycle_id)
        cs_instance.TestTime               = CSConv.to_double(self.test_time)
        cs_instance.StepTime               = CSConv.to_double(self.step_time)
        cs_instance.ChargeCapacity         = CSConv.to_double(self.charge_capacity)
        cs_instance.DischargeCapacity      = CSConv.to_double(self.discharge_capacity)
        cs_instance.ChargeEnergy           = CSConv.to_double(self.charge_energy)
        cs_instance.DischargeEnergy        = CSConv.to_double(self.discharge_energy)
        cs_instance.TC_Time1               = CSConv.to_double(self.tc_time1)
        cs_instance.TC_Time2               = CSConv.to_double(self.tc_time2)
        cs_instance.TC_Time3               = CSConv.to_double(self.tc_time3)
        cs_instance.TC_Time4               = CSConv.to_double(self.tc_time4)
        cs_instance.TC_ChargeCapacity1     = CSConv.to_double(self.tc_charge_capacity1)
        cs_instance.TC_ChargeCapacity2     = CSConv.to_double(self.tc_charge_capacity2)
        cs_instance.TC_DishargeCapacity1   = CSConv.to_double(self.tc_discharge_capacity1)
        cs_instance.TC_DishargeCapacity2   = CSConv.to_double(self.tc_discharge_capacity2)
        cs_instance.TC_ChargeEnergy1       = CSConv.to_double(self.tc_charge_energy1)
        cs_instance.TC_ChargeEnergy2       = CSConv.to_double(self.tc_charge_energy2)
        cs_instance.TC_DischargeEnergy1    = CSConv.to_double(self.tc_discharge_energy1)
        cs_instance.TC_DischargeEnergy2    = CSConv.to_double(self.tc_discharge_energy2)
        cs_instance.TC_Counter1            = CSConv.to_float(self.tc_counter1)
        cs_instance.TC_Counter2            = CSConv.to_float(self.tc_counter2)
        cs_instance.TC_Counter3            = CSConv.to_float(self.tc_counter3)
        cs_instance.TC_Counter4            = CSConv.to_float(self.tc_counter4)
        cs_instance.TC_Counter5            = CSConv.to_float(self.tc_counter5)
        cs_instance.TC_Counter6            = CSConv.to_float(self.tc_counter6)
        cs_instance.TC_Counter7            = CSConv.to_float(self.tc_counter7)
        cs_instance.TC_Counter8            = CSConv.to_float(self.tc_counter8)
        cs_instance.ChargeCapacityTime     = CSConv.to_double(self.charge_capacity_time)
        cs_instance.DischargeCapacityTime  = CSConv.to_double(self.discharge_capacity_time)
        cs_instance.MVUD1                  = CSConv.to_double(self.mvud1)
        cs_instance.MVUD2                  = CSConv.to_double(self.mvud2)
        cs_instance.MVUD3                  = CSConv.to_double(self.mvud3)
        cs_instance.MVUD4                  = CSConv.to_double(self.mvud4)
        cs_instance.MVUD5                  = CSConv.to_double(self.mvud5)
        cs_instance.MVUD6                  = CSConv.to_double(self.mvud6)
        cs_instance.MVUD7                  = CSConv.to_double(self.mvud7)
        cs_instance.MVUD8                  = CSConv.to_double(self.mvud8)
        cs_instance.MVUD9                  = CSConv.to_double(self.mvud9)
        cs_instance.MVUD10                 = CSConv.to_double(self.mvud10)
        cs_instance.MVUD11                 = CSConv.to_double(self.mvud11)
        cs_instance.MVUD12                 = CSConv.to_double(self.mvud12)
        cs_instance.MVUD13                 = CSConv.to_double(self.mvud13)
        cs_instance.MVUD14                 = CSConv.to_double(self.mvud14)
        cs_instance.MVUD15                 = CSConv.to_double(self.mvud15)
        cs_instance.MVUD16                 = CSConv.to_double(self.mvud16)
        return cs_instance

@dataclass
class StartChannelArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.ChannelManagement.StartChannelArgs'
    """
    sn:                     str  = ""
    creator:                str  = ""
    comment:                str  = ""
    channel_resume_data:    list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.ChannelManagement.StartChannelArgs:
        if not all([isinstance(data, ChannelResumeData) for data in self.channel_resume_data]):
            raise TypeError("'channel_resume_data' must be a list of 'arbinclienttools.ChannelResumeData'")
        cs_instance = ArbinDataModel.ChannelManagement.StartChannelArgs()
        cs_instance.SN                = CSConv.to_string(self.sn)
        cs_instance.Creator           = CSConv.to_string(self.creator)
        cs_instance.Comment           = CSConv.to_string(self.comment)
        cs_instance.ChannelResumeData = CSConv.to_list(self.channel_resume_data)
        return cs_instance

@dataclass
class StopChannelArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.ChannelManagement.StopChannelArgs'
    """
    sn:                  str  = ""
    channel_id:          int  = -1
    is_stop_all_channel: bool = False

    def to_cs(self) -> ArbinDataModel.ChannelManagement.StopChannelArgs:
        cs_instance = ArbinDataModel.ChannelManagement.StopChannelArgs()
        cs_instance.SN               = CSConv.to_string(self.sn)
        cs_instance.ChannelID        = CSConv.to_int(self.channel_id)
        cs_instance.IsStopAllChannel = CSConv.to_bool(self.is_stop_all_channel)
        return cs_instance
    
@dataclass
class JumpStepArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.ChannelManagement.JumpStepArgs'
    """
    sn:          str = ""
    step_id:     int = -1
    sub_step_id: int = -1
    channel_id:  int = -1

    def to_cs(self) -> ArbinDataModel.ChannelManagement.JumpStepArgs:
        cs_instance = ArbinDataModel.ChannelManagement.JumpStepArgs()
        cs_instance.SN         = CSConv.to_string(self.sn)
        cs_instance.StepID     = CSConv.to_int(self.step_id)
        cs_instance.SubStepID  = CSConv.to_int(self.sub_step_id)
        cs_instance.ChannelID  = CSConv.to_int(self.channel_id)
        return cs_instance

@dataclass
class ResumeChannelArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.ChannelManagement.ResumeChannelArgs'
    """
    sn:          str = ""
    resume_data: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.ChannelManagement.ResumeChannelArgs:
        if not all([isinstance(data, ChannelResumeData) for data in self.resume_data]):
            raise TypeError("'resume_data' must be a list of 'arbinclienttools.ChannelResumeData'")
        cs_instance = ArbinDataModel.ChannelManagement.ResumeChannelArgs()
        cs_instance.SN          = CSConv.to_string(self.sn)
        cs_instance.ResumeDatas = CSConv.to_list(self.resume_data)
        return cs_instance

@dataclass
class ContinueChannelArgs:
    """
    Wrapper class of of 'Arbin.Library.DataModel.ChannelManagement.ContinueChannelArgs'
    """
    sn:         str  = ""
    channel_id: list = field(default_factory=list)

    def to_cs(self) -> ArbinDataModel.ChannelManagement.ContinueChannelArgs:
        cs_instance = ArbinDataModel.ChannelManagement.ContinueChannelArgs()
        cs_instance.SN        = CSConv.to_string(self.sn)
        cs_instance.ChannelID = CSConv.to_list(self.channel_id, CSConv.EDataType.INT)
        return cs_instance