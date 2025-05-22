__doc__ = """"
[Connection Arguments]
CreateArbinClientArgs
"""

from dataclasses import dataclass

import ArbinClient.Core as ArbinClient # type: ignore

@dataclass
class CreateArbinClientArgs:
    """
    Python wrapper of 'ArbinClient.Core.CreateArbinClientArgs'
    """
    timeout:    int = 0
    ip_address: str = ""
    user_name:  str = ""
    password:   str = ""

    def to_cs(self) -> ArbinClient.CreateArbinClientArgs:
        cs_instance = ArbinClient.CreateArbinClientArgs()
        cs_instance.Timeout     = self.timeout
        cs_instance.IPAddress   = self.ip_address
        cs_instance.UserName    = self.user_name
        cs_instance.Password    = self.password
        return cs_instance

