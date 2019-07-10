# make_stub_files: Wed 10 Jul 2019 at 04:06:24

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Logger:
    def __init__(self, name: str) -> None: ...
    def _level_str(self, level: Any) -> Union[Any, str]: ...
        #   0: return l
        # ? 0: return l
        #   1: return 'LVL%s'%level
        #   1: return str
    def setLevel(self, level: Any) -> None: ...
    def isEnabledFor(self, level: Any) -> bool: ...
    def log(self, level: Any, msg: Any, *args) -> None: ...
    def debug(self, msg: Any, *args) -> None: ...
    def info(self, msg: Any, *args) -> None: ...
    def warning(self, msg: Any, *args) -> None: ...
    def error(self, msg: Any, *args) -> None: ...
    def critical(self, msg: Any, *args) -> None: ...
    def exc(self, e: Any, msg: Any, *args) -> None: ...
    def exception(self, msg: Any, *args) -> None: ...
    def addHandler(self, hdlr: Any) -> None: ...
def getLogger(name: str=None) -> Any: ...
    #   0: return _loggers[name]
    # ? 0: return _loggers[str]
    #   1: return l
    # ? 1: return l
def info(msg: Any, *args) -> None: ...
def debug(msg: Any, *args) -> None: ...
def basicConfig(level: Any=INFO, filename: str=None, stream: Any=None, format: Any=None, style: Any='%') -> None: ...
class Handler:
    def __init__(self) -> None: ...
    def setFormatter(self, fmt: Any) -> None: ...
class StreamHandler(Handler):
    def __init__(self, stream: Any=None) -> None: ...
    def emit(self, record: Any) -> None: ...
    def flush(self) -> None: ...
class FileHandler(Handler):
    def __init__(self, filename: str, mode: Any='a', encoding: Any=None, delay: Any=bool) -> None: ...
    def emit(self, record: Any) -> None: ...
    def close(self) -> None: ...
class Formatter:
    def __init__(self, fmt: Any=None, datefmt: Any=None, style: Any='%') -> None: ...
    def usesTime(self) -> bool: ...
    def format(self, record: Any) -> Any: ...
        #   0: return self.fmt%record.__dict__
        # ? 0: return self.fmt%record.__dict__
        #   1: return self.fmt.format(None=record.__dict__)
        # ? 1: return self.fmt.format(None=record.__dict__)
    def formatTime(self, record: Any, datefmt: Any=None) -> Any: ...
        #   0: return '{0}-{1}-{2} {3}:{4}:{5}'.format(*ct)
        # ? 0: return str.format(*ct)
    def formatException(self, exc_info: Any) -> None: ...
    def formatStack(self, stack_info: Any) -> None: ...
class LogRecord:
    def __init__(self, name: str, level: Any, pathname: Any, lineno: Any, msg: Any, args: Any, exc_info: Any, func: Any=None, sinfo: Any=None) -> None: ...
