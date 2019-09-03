# make_stub_files: Tue 03 Sep 2019 at 17:05:43

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Adc:
    def __init__(self, port: Any) -> None: ...
    def _write_u8(self, value: Any=None) -> Any: ...
        #   0: return self.i2c.writeto(ADDRESS,buf)
        # ? 0: return self.i2c.writeto(ADDRESS, buf)
    def _read_u16(self, value: Any=None, buf: Any=bytearray(2)) -> Any: ...
        #   0: return struct.unpack('>h',buf)[0]
        # ? 0: return struct.unpack(str, buf)[number]
    def _available(self) -> None: ...
    def measure_set(self, mode: Any=None, rate: Any=None, gain: Any=None) -> None: ...
    def voltage(self) -> Any: ...
        #   0: return round(vol,3)
        # ? 0: return round(vol, number)
    def deinit(self) -> None: ...