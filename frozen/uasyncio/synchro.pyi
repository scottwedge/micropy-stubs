# make_stub_files: Thu 25 Jul 2019 at 22:20:16

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Lock:
    def __init__(self) -> None: ...
    def release(self) -> None: ...
    def acquire(self) -> bool: ...
