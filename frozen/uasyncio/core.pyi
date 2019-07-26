# make_stub_files: Thu 25 Jul 2019 at 22:36:49

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def set_debug(val: Any) -> None: ...
class CancelledError(Exception): ...
class TimeoutError(CancelledError): ...
class EventLoop:
    def __init__(self, runq_len: smallint=16, waitq_len: smallint=16) -> None: ...
    def time(self) -> Any: ...
        #   0: return time.ticks_ms()
        # ? 0: return time.ticks_ms()
    def create_task(self, coro: Any) -> None: ...
    def call_soon(self, callback: Any, *args) -> None: ...
    def call_later(self, delay: Any, callback: Any, *args) -> None: ...
    def call_later_ms(self, delay: Any, callback: Any, *args) -> Any: ...
        #   0: return self.call_soon(callback,*args)
        # ? 0: return self.call_soon(callback, *args)
    def call_at_(self, time: Any, callback: Any, args: Any=()) -> None: ...
    def wait(self, delay: Any) -> None: ...
    def run_forever(self) -> Any: ...
        #   0: return arg
        # ? 0: return arg
    def run_until_complete(self, coro: Any) -> None:
        def _run_and_stop() -> None: ...
    def stop(self) -> None: ...
    def close(self) -> None: ...
class SysCall:
    def __init__(self, *args) -> None: ...
    def handle(self) -> None: ...
class SysCall1(SysCall):
    def __init__(self, arg: Any) -> None: ...
class StopLoop(SysCall1): ...
class IORead(SysCall1): ...
class IOWrite(SysCall1): ...
class IOReadDone(SysCall1): ...
class IOWriteDone(SysCall1): ...
def get_event_loop(runq_len: smallint=16, waitq_len: smallint=16) -> Any: ...
    #   0: return _event_loop
    # ? 0: return _event_loop
def sleep(secs: Any) -> None: ...
class SleepMs(SysCall1):
    def __init__(self) -> None: ...
    def __call__(self, arg: Any) -> Any: ...
        #   0: return self
        # ? 0: return self
    def __iter__(self) -> Any: ...
        #   0: return self
        # ? 0: return self
    def __next__(self) -> Any: ...
        #   0: return self
        # ? 0: return self
def cancel(coro: Any) -> None: ...
class TimeoutObj:
    def __init__(self, coro: Any) -> None: ...
def wait_for_ms(coro: Any, timeout: Any) -> Any:
    #   0: return yield from waiter(coro,timeout_obj)
    # ? 0: return yield from waiter(coro, timeout_obj)
    def waiter(coro: Any, timeout_obj: Any) -> Any: ...
        #   0: return res
        # ? 0: return res
    def timeout_func(timeout_obj: Any) -> None: ...
def wait_for(coro: Any, timeout: Any) -> Any: ...
    #   0: return wait_for_ms(coro,int(timeout*1000))
    # ? 0: return wait_for_ms(coro, int)
def coroutine(f: Any) -> Any: ...
    #   0: return f
    # ? 0: return f
def ensure_future(coro: Any, loop: Any=_event_loop) -> Any: ...
    #   0: return coro
    # ? 0: return coro
def Task(coro: Any, loop: Any=_event_loop) -> None: ...
