#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import appier

import un1qnx


class APITest(unittest.TestCase):
    def setUp(self):
        self.base_url = appier.conf(
            "TEST_BASE_URL", "https://un1qone-backend-test.azurewebsites.net/api/v2/"
        )
        self.auth_url = appier.conf(
            "TEST_AUTH_URL", "https://un1qone-identity-server-test.azurewebsites.net/"
        )
        self.client_id = appier.conf("TEST_CLIENT_ID", None)
        self.client_secret = appier.conf("TEST_CLIENT_SECRET", None)
        self.grant_type = appier.conf("TEST_GRANT_TYPE", "client_credentials")

        if not self.client_id:
            if not hasattr(self, "skipTest"):
                return
            self.skipTest("TEST_CLIENT_ID not defined")

        if not self.client_secret:
            if not hasattr(self, "skipTest"):
                return
            self.skipTest("TEST_CLIENT_SECRET not defined")

        self.api = un1qnx.API(
            base_url=self.base_url,
            auth_url=self.auth_url,
            client_id=self.client_id,
            client_secret=self.client_secret,
            grant_type=self.grant_type,
        )

    def tearDown(self):
        self.api = None

    def test_init(self):
        self.assertEqual(
            self.api.base_url, "https://un1qone-backend-test.azurewebsites.net/api/v2/"
        )
        self.assertEqual(
            self.api.auth_url, "https://un1qone-identity-server-test.azurewebsites.net/"
        )
        self.assertEqual(self.api.token, None)
        self.assertEqual(self.api.client_id, self.client_id)
        self.assertEqual(self.api.client_secret, self.client_secret)
        self.assertEqual(self.api.grant_type, self.grant_type)

    def test_build(self):
        headers = dict()
        self.api.build("GET", "", headers=headers, kwargs=dict(auth=False))
        self.assertEqual(headers, dict())

        self.api.build("GET", "", headers=headers, kwargs=dict())
        self.assertEqual(headers, {"Authorization": "Bearer %s" % self.api.token})

    def test_get_token(self):
        self.assertEqual(self.api.token, None)

        first_token = self.api.get_token()
        self.assertEqual(self.api.token, first_token)

        second_token = self.api.get_token()
        self.assertEqual(self.api.token, first_token)
        self.assertEqual(first_token, second_token)

    def test_auth_callback(self):
        self.api.token = "token"
        self.assertEqual(self.api.token, "token")

        headers = dict()
        # pylint: disable-next=not-callable
        self.api.auth_callback(dict(), headers)
        self.assertEqual(headers, {"Authorization": "Bearer %s" % self.api.token})

    def test_auth_header(self):
        self.api.token = "token"
        self.assertEqual(self.api.token, "token")

        header = self.api.auth_header()
        self.assertEqual(header, "Bearer token")
