# The MIT License (MIT)
#
# Copyright (c) 2019 Scott Shawcroft for Adafruit Industries LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_ssd1608`
================================================================================

CircuitPython `displayio` driver for SSD1608-based ePaper displays


* Author(s): Scott Shawcroft

Implementation Notes
--------------------

**Hardware:**

* `Adafruit 1.54" Monochrome ePaper Display Breakout <https://www.adafruit.com/product/4196>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware (version 5+) for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

import displayio

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_SSD1608.git"

_START_SEQUENCE = (
    b"\x12\x00" # Software reset
    b"\x01\x03\x00\x00\x00" # driver output control
    b"\x3a\x01\x1b" # Set dummy line period
    b"\x3b\x01\x0b" # Set gate line width
    b"\x11\x01\x03" # Data entry sequence
    b"\x2c\x01\x70" # Vcom Voltage
    b"\x32\x1e\x02\x02\x01\x11\x12\x12\x22\x22\x66\x69\x69\x59\x58\x99\x99\x88\x00\x00\x00\x00\xf8"
    b"\xb4\x13\x51\x35\x51\x51\x19\x01\x00" # LUT
    b"\x22\x01\xc7" # Set DISP ctrl2
)

_STOP_SEQUENCE = (
    b"\x10\x01\x01" # Enter deep sleep
)

# pylint: disable=too-few-public-methods
class SSD1608(displayio.EPaperDisplay):
    """SSD1608 driver"""
    def __init__(self, bus, **kwargs):
        color_command = None
        start_sequence = bytearray(_START_SEQUENCE)
        width = kwargs["width"]
        start_sequence[4] = width - 1
        start_sequence[5] = (width - 1) >> 8

        super().__init__(bus, start_sequence, _STOP_SEQUENCE, **kwargs,
                         ram_width=240, ram_height=320,
                         set_column_window_command=0x44, set_row_window_command=0x45,
                         set_current_column_command=0x4e, set_current_row_command=0x4f,
                         write_black_ram_command=0x24,
                         refresh_display_command=0x20)
