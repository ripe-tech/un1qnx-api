#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import appier

import un1qnx

class TagAPITest(unittest.TestCase):

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

    def test_list_tags(self):
        tags = self.api.list_tags()
        self.assertEqual("link" in tags, True)
        self.assertEqual("total" in tags, True)
        self.assertEqual("items" in tags, True)

    def test_get_tag(self):
        first_tag = self._get_test_tag()
        second_tag = self.api.get_tag(first_tag["id"])
        self.assertEqual(first_tag, second_tag)

    def test_create_tag(self):
        tag = self._get_test_tag()
        self.api.create_tag(tag["id"])
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Created")

    def test_activate_tag(self):
        tag = self._get_test_tag()
        self.api.activate_tag(tag["id"])
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Active")

    def test_inactivate_tag(self):
        tag = self._get_test_tag()
        self.api.inactivate_tag(tag["id"])
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Inactive")

    def test_disable_tag(self):
        tag = self._get_test_tag()
        self.api.disable_tag(tag["id"])
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Disabled")

    def test_expire_tag(self):
        tag = self._get_test_tag()
        self.api.expire_tag(tag["id"])
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Expired")

    def create_tag_by_code(self):
        tag = self._get_test_tag()
        self.api.create_tag_by_code(tag["barcode"])
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Created")

    def test_activate_tag_by_code(self):
        tag = self._get_test_tag()
        self.api.activate_tag_by_code(tag["barcode"])
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Active")

    def test_inactivate_tag_by_code(self):
        tag = self._get_test_tag()
        self.api.inactivate_tag_by_code(tag["barcode"])
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Inactive")

    def test_disable_tag_by_code(self):
        tag = self._get_test_tag()
        self.api.disable_tag_by_code(tag["barcode"])
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Disabled")

    def test_expire_tag_by_code(self):
        tag = self._get_test_tag()
        self.api.expire_tag_by_code(tag["barcode"])
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Expired")

    def test_update_tag_state(self):
        tag = self._get_test_tag()
        self.api.update_tag_state(tag["id"], "Expired")
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Expired")

    def test_update_tag_state_by_code(self):
        tag = self._get_test_tag()
        self.api.update_tag_state_by_code(tag["barcode"], "Expired")
        tag = self.api.get_tag(tag["id"])
        self.assertEqual(tag["state"], "Expired")

    def _get_test_tag(self):
        # tags can't be created via API so we try
        # to retrieve an existing one
        tags = self.api.list_tags()
        tag = tags["items"][0] if "items" in tags and len(tags["items"]) > 0 else None
        if not tag:
            if not hasattr(self, "skipTest"): return
            self.skipTest("No available UN1QNX tags to test")
        return tag
