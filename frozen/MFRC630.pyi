
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class MFRC630:
    def __init__(self, pyscan: Any=None, sda: Any='P22', scl: Any='P21', timeout: Any=None, debug: Any=bool) -> None: ...
    def print_debug(self, msg: Any) -> None: ...
    def mfrc630_read_reg(self, reg: Any) -> Any: ...
        #   0: return self.i2c.readfrom_mem(NFC_I2CADDR,reg,1)[0]
        # ? 0: return self.i2c.readfrom_mem(NFC_I2CADDR, reg, number)[number]
    def mfrc630_write_reg(self, reg: Any, data: Any) -> None: ...
    def mfrc630_write_regs(self, reg: Any, data: Any) -> None: ...
    def mfrc630_read_fifo(self, len: Any) -> Optional[Any]: ...
        #   0: return self.i2c.readfrom_mem(NFC_I2CADDR,MFRC630_REG_FIFODATA,len)
        # ? 0: return self.i2c.readfrom_mem(NFC_I2CADDR, MFRC630_REG_FIFODATA, len)
        #   1: return None
        #   1: return None
    def mfrc630_cmd_idle(self) -> None: ...
    def mfrc630_flush_fifo(self) -> None: ...
    def mfrc630_setup_fifo(self) -> None: ...
    def mfrc630_write_fifo(self, data: Any) -> None: ...
    def mfrc630_cmd_load_protocol(self, rx: Any, tx: Any) -> None: ...
    def mfrc630_cmd_transceive(self, data: Any) -> None: ...
    def mfrc630_cmd_init(self) -> None: ...
    def mfrc630_cmd_reset(self) -> None: ...
    def mfrc630_clear_irq0(self) -> None: ...
    def mfrc630_clear_irq1(self) -> None: ...
    def mfrc630_irq0(self) -> Any: ...
        #   0: return self.mfrc630_read_reg(MFRC630_REG_IRQ0)
        # ? 0: return self.mfrc630_read_reg(MFRC630_REG_IRQ0)
    def mfrc630_irq1(self) -> Any: ...
        #   0: return self.mfrc630_read_reg(MFRC630_REG_IRQ1)
        # ? 0: return self.mfrc630_read_reg(MFRC630_REG_IRQ1)
    def mfrc630_timer_set_control(self, timer: Any, value: Any) -> None: ...
    def mfrc630_timer_set_reload(self, timer: Any, value: Any) -> None: ...
    def mfrc630_timer_set_value(self, timer: Any, value: Any) -> None: ...
    def mfrc630_fifo_length(self) -> Any: ...
        #   0: return self.mfrc630_read_reg(MFRC630_REG_FIFOLENGTH)
        # ? 0: return self.mfrc630_read_reg(MFRC630_REG_FIFOLENGTH)
    def mfrc630_status(self) -> Any: ...
        #   0: return self.mfrc630_read_reg(MFRC630_REG_STATUS)
        # ? 0: return self.mfrc630_read_reg(MFRC630_REG_STATUS)
    def mfrc630_error(self) -> Any: ...
        #   0: return self.mfrc630_read_reg(MFRC630_REG_ERROR)
        # ? 0: return self.mfrc630_read_reg(MFRC630_REG_ERROR)
    def mfrc630_cmd_load_key(self, key: Any) -> None: ...
    def mfrc630_cmd_auth(self, key_type: Any, block_address: Any, card_uid: Any) -> None: ...
    def mfrc630_MF_read_block(self, block_address: Any, dest: Any) -> Union[Any, number]: ...
        #   0: return 0
        #   0: return number
        #   1: return 0
        #   1: return number
        #   2: return rx_len
        # ? 2: return rx_len
    def mfrc630_iso14443a_WUPA_REQA(self, instruction: Any) -> Union[Any, number]: ...
        #   0: return 0
        #   0: return number
        #   1: return self.mfrc630_fifo_length()
        # ? 1: return self.mfrc630_fifo_length()
        #   2: return res
        # ? 2: return res
        #   3: return 0
        #   3: return number
    def mfrc630_print_block(self, data: Any, len: Any) -> None: ...
    def mfrc630_format_block(self, data: Any, len: Any) -> Union[Any, str]: ...
        #   0: return ' '.join(<gen '{:02x}'.format(x) for x in data[:len_i]>).upper()
        # ? 0: return str.upper()
        #   1: return ' '.join(<gen '{:02x}'.format(x) for x in data>).upper()
        # ? 1: return str.upper()
        #   2: return 'Length: %d  Data: %s'%(len, binascii.hexlify(data,' '))
        #   2: return str
        #   3: return 'Data: %s with Length: %s'%(str(data), len)
        #   3: return str
    def mfrc630_iso14443a_select(self, uid: Any) -> Union[Any, number]: ...
        #   0: return 0
        #   0: return number
        #   1: return 0
        #   1: return number
        #   2: return 0
        #   2: return number
        #   3: return 0
        #   3: return number
        #   4: return cascade_level*3+1
        # ? 4: return cascade_level*number+number
        #   5: return 0
        #   5: return number
    def mfrc630_MF_auth(self, uid: Any, key_type: Any, block: Any) -> Union[Any, number]: ...
        #   0: return 0
        #   0: return number
        #   1: return status&MFRC630_STATUS_CRYPTO1_ON
        # ? 1: return status&MFRC630_STATUS_CRYPTO1_ON
    def mfrc630_MF_deauth(self) -> None: ...
    def format_block(self, block: Any, length: Any) -> Any: ...
        #   0: return ret_val.upper()
        # ? 0: return ret_val.upper()
