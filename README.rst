Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ssd1608/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/ssd1608/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_SSD1608.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_SSD1608
    :alt: Build Status

CircuitPython `displayio` driver for SSD1608-based ePaper displays


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-ssd1608/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-ssd1608

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-ssd1608

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-ssd1608

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
    import busio
    import displayio
    import adafruit_ssd1608

    displayio.release_displays()

    # This pinout works on a Metro and may need to be altered for other boards.

    # For breadboarding
    spi = busio.SPI(board.SCL, board.SDA)
    epd_cs = board.D9
    epd_dc = board.D8
    epd_reset = board.D7
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

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
