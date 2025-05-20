import unittest

from arbinclienttools.src.argument.channel_management import (
    ChannelResumeData,
    StartChannelArgs,
    StopChannelArgs,
    JumpStepArgs,
    ResumeChannelArgs,
    ContinueChannelArgs
)

class TestChannelManagementArgs(unittest.TestCase):

    def test_channel_resume_data_to_cs(self): 
        data = ChannelResumeData(
            channel_id=1,
            test_id=123,
            test_names=["TestA", "TestB"],
            schedule_name="demo.sdx",
            step_id=10,
            sub_step_id=2,
            cycle_id=3,
            test_time=100.5,
            step_time=50.2,
            charge_capacity=1.1,
            discharge_capacity=2.2,
            charge_energy=3.3,
            discharge_energy=4.4,
            tc_time1=1.0,
            tc_charge_capacity1=10.1,
            tc_discharge_capacity1=11.1,
            tc_charge_energy1=12.1,
            tc_discharge_energy1=13.1,
            tc_counter1=0.5,
            charge_capacity_time=200.0,
            discharge_capacity_time=100.0,
            mvud1=9.9
        )

        cs = data.to_cs()

        self.assertEqual(cs.ChannelID, data.channel_id)
        self.assertEqual(cs.TestID, data.test_id)
        self.assertEqual(cs.TestNames, data.test_names)
        self.assertEqual(cs.ScheduleName, data.schedule_name)
        self.assertEqual(cs.StepID, data.step_id)
        self.assertEqual(cs.SubStepID, data.sub_step_id)
        self.assertEqual(cs.CycleID, data.cycle_id)
        self.assertAlmostEqual(cs.TestTime, data.test_time)
        self.assertAlmostEqual(cs.StepTime, data.step_time)
        self.assertAlmostEqual(cs.ChargeCapacity, data.charge_capacity)
        self.assertAlmostEqual(cs.DischargeCapacity, data.discharge_capacity)
        self.assertAlmostEqual(cs.ChargeEnergy, data.charge_energy)
        self.assertAlmostEqual(cs.DischargeEnergy, data.discharge_energy)
        self.assertAlmostEqual(cs.TC_Time1, data.tc_time1)
        self.assertAlmostEqual(cs.TC_ChargeCapacity1, data.tc_charge_capacity1)
        self.assertAlmostEqual(cs.TC_DischargeCapacity1, data.tc_discharge_capacity1)
        self.assertAlmostEqual(cs.TC_ChargeEnergy1, data.tc_charge_energy1)
        self.assertAlmostEqual(cs.TC_DischargeEnergy1, data.tc_discharge_energy1)
        self.assertAlmostEqual(cs.TC_Counter1, data.tc_counter1)
        self.assertAlmostEqual(cs.ChargeCapacityTime, data.charge_capacity_time)
        self.assertAlmostEqual(cs.DischargeCapacityTime, data.discharge_capacity_time)
        self.assertAlmostEqual(cs.MVUD1, data.mvud1)

    def test_start_channel_args_to_cs(self):
        resume_data = ChannelResumeData(channel_id=1, schedule_name="demo.sdx", test_names=["TestA"])
        args = StartChannelArgs(
            sn="SN001",
            creator="Tester",
            comment="Start test",
            channel_resume_data=[resume_data]
        )
        cs = args.to_cs()

        self.assertEqual(cs.SN, "SN001")
        self.assertEqual(cs.Creator, "Tester")
        self.assertEqual(cs.Comment, "Start test")
        self.assertEqual(cs.ChannelResumeData[0].ChannelID, 1)
        self.assertEqual(cs.ChannelResumeData[0].schedule_name, "demo.sdx")
        self.assertEqual(cs.ChannelResumeData[0].test_names, ["TestA"])

    def test_stop_channel_args_to_cs(self):
        args = StopChannelArgs(
            sn="SN002",
            channel_id=1,
            is_stop_all_channel=True
        )
        cs = args.to_cs()

        self.assertEqual(cs.SN, "SN002")
        self.assertEqual(cs.ChannelID, 1)
        self.assertTrue(cs.IsStopAllChannel)

    def test_jump_step_args_to_cs(self):
        args = JumpStepArgs(
            sn="SN003",
            step_id=10,
            sub_step_id=2,
            channel_id=7
        )
        cs = args.to_cs()

        self.assertEqual(cs.SN, "SN003")
        self.assertEqual(cs.StepID, 10)
        self.assertEqual(cs.SubStepID, 2)
        self.assertEqual(cs.ChannelID, 7)

    def test_resume_channel_args_to_cs(self):
        resume_data = ChannelResumeData(channel_id=2)
        args = ResumeChannelArgs(
            sn="SN004",
            resume_data=[resume_data]
        )
        cs = args.to_cs()

        self.assertEqual(cs.SN, "SN004")
        self.assertEqual(cs.ResumeDatas[0].ChannelID, 2)

    def test_continue_channel_args_to_cs(self):
        args = ContinueChannelArgs(
            sn="SN005",
            channel_id=[1, 2, 3]
        )
        cs = args.to_cs()

        self.assertEqual(cs.SN, "SN005")
        self.assertEqual(cs.ChannelID, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
