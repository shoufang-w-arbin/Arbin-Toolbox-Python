import unittest
from arbinclienttools.src.argument.connection import CreateArbinClientArgs

class TestConnectionArgs(unittest.TestCase):

    def test_create_arbin_client_args_to_cs(self):
        data = CreateArbinClientArgs(
            timeout=60,
            ip_address="192.168.1.100",
            user_name="admin",
            password="pass123"
        )
        cs = data.to_cs()

        self.assertEqual(cs.Timeout, 60)
        self.assertEqual(cs.IPAddress, "192.168.1.100")
        self.assertEqual(cs.UserName, "admin")
        self.assertEqual(cs.Password, "pass123")

if __name__ == '__main__':
    unittest.main()
