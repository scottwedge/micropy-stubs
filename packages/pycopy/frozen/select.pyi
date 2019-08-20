# make_stub_files: Tue 20 Aug 2019 at 15:46:00

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Epoll:
    def __init__(self, epfd: Any) -> None: ...
    def register(self, fd: Any, eventmask: Any=EPOLLIN|EPOLLPRI|EPOLLOUT, retval: Any=None) -> None: ...
    def unregister(self, fd: Any) -> None: ...
    def poll_ms(self, timeout: Any=-1) -> Any: ...
        #   0: return res
        # ? 0: return res
    def poll(self, timeout: Any=-1) -> Any: ...
        #   0: return self.poll_ms(-1 if timeout==-1 else math.ceil(timeout*1000) )
        # ? 0: return self.poll_ms(Union[Any, number])
    def close(self) -> None: ...
def epoll(sizehint: Any=4) -> Any: ...
    #   0: return Epoll(fd)
    # ? 0: return Epoll(fd)