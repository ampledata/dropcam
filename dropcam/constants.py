#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Constants for Dropcam Python Module."""

__author__ = 'Greg Albrecht <gba@onbeep.com>'
__copyright__ = 'Copyright 2014 OnBeep, Inc.'
__license__ = 'Apache License, Version 2.0'


import logging


LOG_LEVEL = logging.DEBUG
LOG_FORMAT = ('%(asctime)s %(levelname)s %(name)s.%(funcName)s:%(lineno)d'
              ' - %(message)s')

API_URL = 'https://www.dropcam.com'
NEXUSAPI_URL = 'https://nexusapi.dropcam.com'

API_PATH = 'api/v1'
CAMERAS_PATH = 'cameras.get_visible'
EVENT_PATH = 'get_cuepoint'
IMAGE_PATH = 'cameras.get_image'
LOGIN_PATH = 'login.login'
