# make_stub_files: Sat 31 Aug 2019 at 04:45:32

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class DriveBase:
    def __init__(self, left_motor: Motor, right_motor: Motor, wheel_diameter: int, axle_track: int) -> None: ...
    def drive(self, speed: float, steering: float) -> None: ...
    def drive_time(self, speed: float, steering: float, time: int) -> None: ...
    def stop(self, stop_type: Stop=Stop.COAST) -> None: ...