
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class sound:
    def beep(frequency: int=500, duration: int=100, volume: int=30) -> None: ...
    def beeps(number: int) -> None: ...
    def file(file_name: Union[(str, SoundFile)], volume: int=100) -> None: ...
class display:
    def clear() -> None: ...
    def image(file_name: Union[(str, ImageFile)], alignment: Align=Align.CENTER, coordinate: Tuple[(int, int)]=None, clear: bool=bool) -> None: ...
    def text(text: str, coordinate: Tuple[(int, int)]=None) -> None: ...
class battery:
    def current() -> number: ...
    def voltage() -> number: ...
def buttons() -> List: ...
def light(color: Color) -> None: ...
