#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import appier

import un1qnx

class ProductAPITest(unittest.TestCase):

    def setUp(self):
        self.base_url = appier.conf("TEST_BASE_URL", "https://un1qone-backend-test.azurewebsites.net/api/v2/")
        self.auth_url = appier.conf("TEST_AUTH_URL", "https://un1qone-identity-server-test.azurewebsites.net/")
        self.client_id = appier.conf("TEST_CLIENT_ID", None)
        self.client_secret = appier.conf("TEST_CLIENT_SECRET", None)
        self.grant_type = appier.conf("TEST_GRANT_TYPE", "client_credentials")

        if not self.client_id:
            if not hasattr(self, "skipTest"): return
            self.skipTest("TEST_CLIENT_ID not defined")

        if not self.client_secret:
            if not hasattr(self, "skipTest"): return
            self.skipTest("TEST_CLIENT_SECRET not defined")

        self.api = un1qnx.API(
            base_url = self.base_url,
            auth_url = self.auth_url,
            client_id = self.client_id,
            client_secret = self.client_secret,
            grant_type = self.grant_type
        )

    def tearDown(self):
        self.api = None

    def test_list_products(self):
        products = self.api.list_products()
        self.assertEqual("link" in products, True)
        self.assertEqual("total" in products, True)
        self.assertEqual("items" in products, True)
