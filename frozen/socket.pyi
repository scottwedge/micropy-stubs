# make_stub_files: Wed 10 Jul 2019 at 04:06:24

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def _resolve_addr(addr: Any) -> Union[Any, str]: ...
    #   0: return addr
    # ? 0: return addr
    #   1: return a[0][4]
    #   1: return str
def inet_aton(addr: Any) -> Any: ...
    #   0: return inet_pton(AF_INET,addr)
    # ? 0: return inet_pton(AF_INET, addr)
def create_connection(addr: Any, timeout: Any=None, source_address: Any=None) -> str: ...
class socket(_socket.socket):
    def accept(self) -> Tuple[str, Any, Any, Any]: ...
    def bind(self, addr: Any) -> Any: ...
        #   0: return super().bind(_resolve_addr(addr))
        # ? 0: return super().bind(_resolve_addr(addr))
    def connect(self, addr: Any) -> Any: ...
        #   0: return super().connect(_resolve_addr(addr))
        # ? 0: return super().connect(_resolve_addr(addr))
    def sendall(self, *args) -> Any: ...
        #   0: return self.send(*args)
        # ? 0: return self.send(*args)
    def sendto(self, data: Any, addr: Any) -> Any: ...
        #   0: return super().sendto(data,_resolve_addr(addr))
        # ? 0: return super().sendto(data, _resolve_addr(addr))
