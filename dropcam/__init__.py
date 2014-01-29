#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dropcam Python Module.

"""
Dropcam Python Module.
~~~~


:author: Greg Albrecht <gba@onbeep.com>
:copyright: Copyright 2014 OnBeep, Inc.
:license: Apache License, Version 2.0
:source: <https://github.com/ampledata/dropcam>

"""

__author__ = 'Greg Albrecht <gba@onbeep.com>'
__license__ = 'Apache License, Version 2.0'
__copyright__ = 'Copyright 2014 OnBeep, Inc.'


import logging

from .classes import Dropcam, Camera


# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        """Default logging handler to avoid "No handler found" warnings."""
        def emit(self, record):
            """Default logging handler to avoid "No handler found" warnings."""
            pass

logging.getLogger(__name__).addHandler(NullHandler())
