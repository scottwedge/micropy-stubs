
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Makey:
    def __init__(self, port: Any) -> None: ...
    def _available(self) -> None: ...
    def _updateValue(self) -> Any: ...
        #   0: return value
        # ? 0: return value
    def valueAll(self) -> Any: ...
        #   0: return self._updateValue()
        # ? 0: return self._updateValue()
    def value(self) -> number: ...
    def deinit(self) -> None: ...
