# make_stub_files: Tue 20 Aug 2019 at 15:46:00

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def STRUCT(typ: Any) -> Tuple[number, Any]: ...
def PTR(typ: Any) -> Tuple[Any, Any]: ...
def ARRAY(typ: Any, sz: Any) -> Union[Tuple[Any, Any, Any], Tuple[Any, Any]]: ...
def UNION(fields: Any) -> Any: ...
    #   0: return res
    # ? 0: return res
def BITFIELD(lsb: Any, len: Any, type: Any=None) -> Any: ...
    #   0: return off|type+uctypes.BFUINT8-uctypes.UINT8|lsb<<uctypes.BF_POS|len<<uctypes.BF_LEN
    # ? 0: return off|type+uctypes.BFUINT8-uctypes.UINT8|lsb<<uctypes.BF_POS|len<<uctypes.BF_LEN
def C_BITFIELD(len: Any, type: Any=None) -> Any: ...
    #   0: return ret
    # ? 0: return ret
