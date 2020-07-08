Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ssd1608/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/ssd1608/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_SSD1608/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_SSD1608/actions/
    :alt: Build Status

CircuitPython `displayio` driver for SSD1608-based ePaper displays


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block:: python

    """Simple test script for 1.54" 200x200 monochrome display.

    Supported products:
      * Adafruit 1.54" Monochrome ePaper Display Breakout
        * https://www.adafruit.com/product/4196
      """

    import time
    import board
    import displayio
    import adafruit_ssd1608

    displayio.release_displays()

    # This pinout works on a Feather M4 and may need to be altered for other boards.
    spi = board.SPI() # Uses SCK and MOSI
    epd_cs = board.D9
    epd_dc = board.D10
    epd_reset = board.D5
    epd_busy = board.D6

    display_bus = displayio.FourWire(spi, command=epd_dc, chip_select=epd_cs, reset=epd_reset,
                                     baudrate=1000000)
    time.sleep(1)

    display = adafruit_ssd1608.SSD1608(display_bus, width=200, height=200, busy_pin=epd_busy)

    g = displayio.Group()

    f = open("/display-ruler.bmp", "rb")

    pic = displayio.OnDiskBitmap(f)
    t = displayio.TileGrid(pic, pixel_shader=displayio.ColorConverter())
    g.append(t)

    display.show(g)

    display.refresh()

    print("refreshed")

    time.sleep(120)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_SSD1608/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
