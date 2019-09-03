# make_stub_files: Tue 03 Sep 2019 at 17:05:43

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Pbhub:
    def __init__(self, port: Any, addr: Any=97) -> None: ...
    def _available(self) -> None: ...
    def digitalRead(self, num: Any, pos: Any) -> Any: ...
        #   0: return data
        # ? 0: return data
    def digitalWrite(self, num: Any, pos: Any, value: Any) -> None: ...
    def analogRead(self, num: Any) -> Any: ...
        #   0: return data
        # ? 0: return data
    def setRgbNum(self, num: Any, length: Any) -> None: ...
    def setColorPos(self, num: Any, pos: Any, color_in: Any) -> None: ...
    def setColor(self, num: Any, begin: Any, count: Any, color_in: Any) -> None: ...
    def setBrightness(self, num: Any, value: Any) -> None: ...
    def deinit(self) -> None: ...