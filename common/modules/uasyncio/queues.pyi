# make_stub_files: Thu 20 Jun 2019 at 18:35:20

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class QueueEmpty(Exception): ...
class QueueFull(Exception): ...
class Queue:
    def __init__(self, maxsize: Any=0) -> None: ...
    def _get(self) -> Any: ...
        #   0: return self._queue.popleft()
        # ? 0: return self._queue.popleft()
    def get(self) -> Any: ...
        #   0: return self._get()
        # ? 0: return self._get()
    def get_nowait(self) -> Any: ...
        #   0: return self._get()
        # ? 0: return self._get()
    def _put(self, val: Any) -> None: ...
    def put(self, val: Any) -> None: ...
    def put_nowait(self, val: Any) -> None: ...
    def qsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
