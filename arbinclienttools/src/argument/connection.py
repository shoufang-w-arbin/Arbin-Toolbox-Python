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
        return ArbinClient.CreateArbinClientArgs(
            self.timeout,
            self.ip_address,
            self.user_name,
            self.password
        )

