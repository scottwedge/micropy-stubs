# make_stub_files: Fri 26 Jul 2019 at 03:02:41

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Pycoproc:
    def __init__(self, i2c: Any=None, sda: Any='P22', scl: Any='P21') -> None: ...
    def _write(self, data: Any, wait: Any=bool) -> None: ...
    def _read(self, size: Any) -> Any: ...
        #   0: return self.i2c.readfrom(I2C_SLAVE_ADDR,size+1)[1:size+1]
        # ? 0: return self.i2c.readfrom(I2C_SLAVE_ADDR, size+number)[number:size+number]
    def _wait(self) -> None: ...
    def _send_cmd(self, cmd: Any) -> None: ...
    def read_hw_version(self) -> Any: ...
        #   0: return d[1]<<8+d[0]
        # ? 0: return d[number]<<number+d[number]
    def read_fw_version(self) -> Any: ...
        #   0: return d[1]<<8+d[0]
        # ? 0: return d[number]<<number+d[number]
    def read_product_id(self) -> Any: ...
        #   0: return d[1]<<8+d[0]
        # ? 0: return d[number]<<number+d[number]
    def peek_memory(self, addr: Any) -> Any: ...
        #   0: return self._read(1)[0]
        # ? 0: return self._read(number)[number]
    def poke_memory(self, addr: Any, value: Any) -> None: ...
    def magic_write_read(self, addr: Any, _and: Any=255, _or: Any=0, _xor: Any=0) -> Any: ...
        #   0: return self._read(1)[0]
        # ? 0: return self._read(number)[number]
    def toggle_bits_in_memory(self, addr: Any, bits: Any) -> None: ...
    def mask_bits_in_memory(self, addr: Any, mask: Any) -> None: ...
    def set_bits_in_memory(self, addr: Any, bits: Any) -> None: ...
    def get_wake_reason(self) -> Any: ...
        #   0: return self.peek_memory(WAKE_REASON_ADDR)
        # ? 0: return self.peek_memory(WAKE_REASON_ADDR)
    def get_sleep_remaining(self) -> Any: ...
        #   0: return time_s
        # ? 0: return time_s
    def setup_sleep(self, time_s: Any) -> None: ...
    def go_to_sleep(self, gps: Any=bool) -> None: ...
    def calibrate_rtc(self) -> None: ...
    def button_pressed(self) -> bool: ...
    def read_battery_voltage(self) -> Any: ...
        #   0: return adc_val*3.3*280/1023/180+0.01
        # ? 0: return adc_val*number*number/number/number+number
    def setup_int_wake_up(self, rising: Any, falling: Any) -> None: ...
    def setup_int_pin_wake_up(self, rising_edge: Any=bool) -> None: ...
