#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import tag
from . import product

UN1QNX_BASE_URL = "http://un1qone-backend-test.azurewebsites.net/api/v2/"
""" The default base URL to be used when no other
base URL value is provided to the constructor """

UN1QNX_AUTH_URL = "http://un1qone-identity-server-test.azurewebsites.net/"
""" The default auth URL to be used when no other
auth URL value is provided to the constructor """

class API(
    appier.API,
    tag.TagAPI,
    product.ProductAPI
):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.base_url = appier.conf("UN1QNX_BASE_URL", UN1QNX_BASE_URL)
        self.auth_url = appier.conf("UN1QNX_AUTH_URL", UN1QNX_AUTH_URL)

        self.base_url = kwargs.get("base_url", self.base_url)
        self.auth_url = kwargs.get("auth_url", self.auth_url)
