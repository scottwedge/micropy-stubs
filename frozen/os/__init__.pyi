# make_stub_files: Thu 25 Jul 2019 at 22:36:50

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def check_error(ret: Any) -> bool: ...
def raise_error() -> None: ...
def getcwd() -> Any: ...
    #   0: return getcwd_(buf,512)
    # ? 0: return getcwd_(buf, number)
def mkdir(name: str, mode: Any=511) -> None: ...
def rename(old: Any, new: Any) -> None: ...
def unlink(name: str) -> None: ...
def rmdir(name: str) -> None: ...
def makedirs(name: str, mode: Any=511, exist_ok: Any=bool) -> None: ...
def ilistdir(path: Any='.') -> None: ...
def listdir(path: Any='.') -> Any: ...
    #   0: return res
    # ? 0: return res
def walk(top: Any, topdown: Any=bool) -> None: ...
def open(n: int, flags: Any, mode: Any=511) -> Any: ...
    #   0: return r
    # ? 0: return r
def read(fd: Any, n: int) -> bytes(buf[:r]): ...
def write(fd: Any, buf: Any) -> Any: ...
    #   0: return r
    # ? 0: return r
def close(fd: Any) -> Any: ...
    #   0: return r
    # ? 0: return r
def dup(fd: Any) -> Any: ...
    #   0: return r
    # ? 0: return r
def access(path: Any, mode: Any) -> bool: ...
def chdir(dir: Any) -> None: ...
def fork() -> Any: ...
    #   0: return r
    # ? 0: return r
def pipe() -> Tuple[str, str]: ...
def _exit(n: int) -> None: ...
def execvp(f: Any, args: Any) -> None: ...
def getpid() -> Any: ...
    #   0: return getpid_()
    # ? 0: return getpid_()
def waitpid(pid: Any, opts: Any) -> Tuple[Any, str]: ...
def kill(pid: Any, sig: Any) -> None: ...
def system(command: Any) -> Any: ...
    #   0: return r
    # ? 0: return r
def getenv(var: Any, default: Any=None) -> Any: ...
    #   0: return default
    # ? 0: return default
    #   1: return var
    # ? 1: return var
def fsencode(s: str) -> Union[bytes(str, str), str]: ...
def fsdecode(s: str) -> Union[str, str(str, str)]: ...
def urandom(n: int) -> Any: ...
    #   0: return f.read(n)
    # ? 0: return f.read(int)
def popen(cmd: Any, mode: Any='r') -> Any: ...
    #   0: return builtins.open(i,mode)
    # ? 0: return builtins.open(int, mode)
def spawnvp(mode: Any, file: Any, args: Any) -> Any: ...
    #   0: return pid
    # ? 0: return pid
    #   1: return rc>>8
    # ? 1: return rc>>number
    #   2: return -sig
    # ? 2: return sig
