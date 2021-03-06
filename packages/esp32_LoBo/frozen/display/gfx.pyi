
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class GFX:
    def __init__(self, width: Any, height: Any, pixel: Any, hline: Any=None, vline: Any=None) -> None: ...
    def _slow_hline(self, x0: Any, y0: Any, width: Any, *args, **kwargs) -> None: ...
    def _slow_vline(self, x0: Any, y0: Any, height: Any, *args, **kwargs) -> None: ...
    def rect(self, x0: Any, y0: Any, width: Any, height: Any, *args, **kwargs) -> None: ...
    def fill_rect(self, x0: Any, y0: Any, width: Any, height: Any, *args, **kwargs) -> None: ...
    def line(self, x0: Any, y0: Any, x1: Any, y1: Any, *args, **kwargs) -> None: ...
    def circle(self, x0: Any, y0: Any, radius: Any, *args, **kwargs) -> None: ...
    def fill_circle(self, x0: Any, y0: Any, radius: Any, *args, **kwargs) -> None: ...
    def triangle(self, x0: Any, y0: Any, x1: Any, y1: Any, x2: Any, y2: Any, *args, **kwargs) -> None: ...
    def fill_triangle(self, x0: Any, y0: Any, x1: Any, y1: Any, x2: Any, y2: Any, *args, **kwargs) -> None: ...
