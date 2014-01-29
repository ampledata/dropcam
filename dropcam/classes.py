#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Dropcam Core Classes."""

__author__ = 'Greg Albrecht <gba@onbeep.com>'
__copyright__ = 'Copyright 2014 OnBeep, Inc.'
__license__ = 'Apache License, Version 2.0'


import logging
import requests
import simplejson

import dropcam.constants


class Dropcam(object):

    """Dropcam Object Class."""

    logger = logging.getLogger(__name__)
    logger.setLevel(dropcam.constants.LOG_LEVEL)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(dropcam.constants.LOG_LEVEL)
    formatter = logging.Formatter(dropcam.constants.LOG_FORMAT)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.propagate = False

    def __init__(self, username, password):
        """
        Creates a new dropcam API instance.

        :param username: Dropcam account username.
        :param password: Dropcam account password.
        """
        self.username = username
        self.password = password
        self.cookies = None
        self._login()

    def _request(self, path):
        return requests.get(
            '/'.join([dropcam.constants.API_URL, dropcam.constants.API_PATH, path]), cookies=self.cookies)
    
    def _login(self):
        login_url = '/'.join([dropcam.constants.API_URL, dropcam.constants.API_PATH, dropcam.constants.LOGIN_PATH])
        params = {'username': self.username, 'password': self.password}
        r = requests.get(login_url, params=params)
        self.cookies = r.cookies

    def cameras(self):
        """
        Returns a list of dropcam Camera objects attached to
        this account.
        """
        response = self._request(dropcam.constants.CAMERAS_PATH)
        json_data = simplejson.loads(response.text)
        return [Camera(i, self.cookies) for i in json_data.get('items')]


class Camera(object):

    """Dropcam Camera Object Class."""

    logger = logging.getLogger(__name__)
    logger.setLevel(dropcam.constants.LOG_LEVEL)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(dropcam.constants.LOG_LEVEL)
    formatter = logging.Formatter(dropcam.constants.LOG_FORMAT)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.propagate = False

    def __init__(self, params, cookies):
        """
        :param params: Dictionary of dropcam camera attributes.
        """
        self.__dict__.update(params)
        self.cookies = cookies
    
    def _request(self, req_url, params={}):
        return requests.get(req_url, params=params, cookies=self.cookies)

    def _api_request(self, path, params={}):
        return self._request('/'.join([dropcam.constants.API_URL, dropcam.constants.API_PATH, path]), params)

    def _nexusapi_request(self, path, params={}):
        return self._request('/'.join([dropcam.constants.NEXUSAPI_URL, path]), params)
    
    def events(self, start, end):
        """
        Returns a list of camera events for a given time period:

        :param start: start time in seconds since epoch
        :param end: end time in seconds since epoch
        """
        params = {
            'uuid': self.uuid,
            'start_time': start,
            'end_time': end,
            'human': False
        }
        response = self._nexusapi_request(
            dropcam.constants.EVENT_PATH, params)
        return simplejson.loads(response.text)
    
    def get_image(self, width=720, event_time=None):
        """
        Requests a camera image, returns response object.
        
        :param width: image width or X resolution
        :param time: time of image capture (in seconds from epoch)
        """
        params = {
            'uuid': self.uuid,
            'width': width
        }
        if event_time:
            params.update(time=event_time)
        
        return self._api_request(dropcam.constants.IMAGE_PATH, params)

    def save_image(self, image_path, width=720, event_time=None):
        """
        Saves a camera image to disc. 

        :param path: file path to save image
        :param width: image width or X resolution
        :param time: time of image capture (in seconds from epoch)
        """
        with open(image_path, 'wb') as image_file:
            response = self.get_image(width, event_time)
            image_file.write(response.content)
