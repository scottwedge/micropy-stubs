# make_stub_files: Thu 20 Jun 2019 at 23:08:04

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class deque:
    def __init__(self, iterable: Any=None) -> None: ...
    def popleft(self) -> Any: ...
        #   0: return self.q.pop(0)
        # ? 0: return self.q.pop(number)
    def popright(self) -> Any: ...
        #   0: return self.q.pop()
        # ? 0: return self.q.pop()
    def pop(self) -> Any: ...
        #   0: return self.q.pop()
        # ? 0: return self.q.pop()
    def append(self, a: str) -> None: ...
    def appendleft(self, a: str) -> None: ...
    def extend(self, a: str) -> None: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool(self.q): ...
    def __iter__(self) -> None: ...
    def __str__(self) -> Any: ...
        #   0: return 'deque({})'.format(self.q)
        # ? 0: return str.format(self.q)
