# make_stub_files: Mon 02 Sep 2019 at 04:30:14

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def setup_conn(port: Any, accept_handler: Any) -> Any: ...
    #   0: return listen_s
    # ? 0: return listen_s
def accept_conn(listen_sock: Any) -> None: ...
def stop() -> None: ...
def start(port: Any=8266, password: Any=None) -> None: ...
def start_foreground(port: Any=8266) -> None: ...
