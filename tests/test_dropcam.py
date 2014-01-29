#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Dropcam Util Module."""

__author__ = 'Greg Albrecht <gba@onbeep.com>'
__copyright__ = 'Copyright 2014 OnBeep, Inc.'
__license__ = 'Apache License, Version 2.0'


import time
import unittest

from .context import dropcam


# pylint: disable=R0904,C0103
class DropcamTestCase(unittest.TestCase):

    """Test class for Dropcam Python Module."""

    @unittest.skip('Write an actual test :).')
    def test_dropcam(self):
        d = dropcam.Dropcam('xxx', 'yyy')
        c = d.cameras()
        now = int(time.time())
        e = c[0].events(start=now-600, end=now)
        for event in e:
            event_time = event['time']
            c[0].save_image("%s.jpg" % event_time, event_time=event_time)


if __name__ == '__main__':
    unittest.main()
