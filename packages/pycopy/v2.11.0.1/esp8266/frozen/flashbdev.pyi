# make_stub_files: Thu 25 Jul 2019 at 22:20:19

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class FlashBdev:
    def __init__(self, blocks: Any=NUM_BLK) -> None: ...
    def readblocks(self, n: int, buf: Any) -> None: ...
    def writeblocks(self, n: int, buf: Any) -> None: ...
    def ioctl(self, op: Any, arg: Any) -> Any: ...
        #   0: return self.blocks
        # ? 0: return self.blocks
        #   1: return self.SEC_SIZE
        # ? 1: return self.SEC_SIZE
