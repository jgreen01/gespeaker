Gespeaker - A GTK frontend for espeak  
Author: Fabio Castelli <muflone@vbsimple.net>
Website: http://www.muflone.com/gespeaker/
Source code: https://github.com/muflone/gespeaker

# LICENSE

Copyright: 2009-2015 Fabio Castelli
License: GPL-2+
This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation; either version 2 of the License, or (at your option)
any later version.
 
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

# INTRODUCTION

Gespeaker is a free GTK+ frontend for espeak.
It allows you to play a text in many languages with settings for voice, pitch,
volume and speed.
The text readed can also be recorded to WAV file for future listening.
Since version 0.6 it supports the speech synthesizer MBROLA for a better speech
experience.

# INSTALLATION

Install dependencies for pycairo. See their getting started guide for instructions.
 - https://pycairo.readthedocs.io/en/latest/getting_started.html

Install dependencies for pygobect. See their getting started guide for instructions.
 - https://pygobject.readthedocs.io/en/latest/getting_started.html

The following dependencies are needed to let Gespeaker work:
 - python3: all the whole code is written for Python
    - optionally: install pyenv
 - espeak: main speaking system
 - librsvg: needed for SVG loading
 - pygtk: needed for all the UI related code
 - python-dbus-common: needed by dbus interface
 - python3-xdg: needed to store configuration
 - alsa-utils: needed for aplay player

Optionall you can install the following to enhance the speech
 - mbrola: for enhanced mbrola voices support
 - mbrola-voices (like mbrola-it3, mbrola-en1 and so on)

The installation is pretty simple, just to execute from the sources directory:
```sh
poetry install
poetry shell
python main.py
```