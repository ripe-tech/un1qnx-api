#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

UN1QNX_BASE_URL = "http://un1qone-backend-test.azurewebsites.net/api/"
""" The default base URL to be used when no other
base URL value is provided to the constructor """

class API(
    appier.API
):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.base_url = appier.conf("UN1QNX_BASE_URL", UN1QNX_BASE_URL)
