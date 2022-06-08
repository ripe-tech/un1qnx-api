#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import appier

import un1qnx


class ProductAPITest(unittest.TestCase):
    def setUp(self):
        self.base_url = appier.conf(
            "TEST_BASE_URL", "https://un1qone-backend-test.azurewebsites.net/api/v3/"
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

    def test_list_products(self):
        products = self.api.list_products()
        self.assertEqual("link" in products, True)
        self.assertEqual("total" in products, True)
        self.assertEqual("items" in products, True)

    def test_create_product(self):
        try:
            product = self.api.create_product(
                dict(
                    tenantId=3,
                    brand="dummy",
                    name="product",
                    description="a test product",
                )
            )
            self.assertEqual(product["tenantId"], 3)
            self.assertEqual(product["brand"], "dummy")
            self.assertEqual(product["name"], "product")
            self.assertEqual(product["description"], "a test product")
        finally:
            self.api.delete_product(product["id"])

    def test_get_product(self):
        try:
            first_product = self.api.create_product(
                dict(
                    tenantId=3,
                    brand="dummy",
                    name="product",
                    description="a test product",
                )
            )
            second_product = self.api.get_product(first_product["id"])
            self.assertEqual(first_product["id"], second_product["id"])
            self.assertEqual(first_product["tenantId"], 3)
            self.assertEqual(first_product["brand"], "dummy")
            self.assertEqual(first_product["name"], "product")
            self.assertEqual(first_product["description"], "a test product")
            self.assertEqual(second_product["tenantId"], 3)
            self.assertEqual(second_product["brand"], "dummy")
            self.assertEqual(second_product["name"], "product")
            self.assertEqual(second_product["description"], "a test product")
        finally:
            self.api.delete_product(first_product["id"])

    def test_update_product(self):
        try:
            first_product = self.api.create_product(
                dict(
                    tenantId=3,
                    brand="dummy",
                    name="product",
                    description="a test product",
                )
            )
            self.api.update_product(
                first_product["id"],
                dict(name="updated product", description="an updated product"),
            )
            second_product = self.api.get_product(first_product["id"])
            self.assertEqual(first_product["id"], second_product["id"])
            self.assertEqual(first_product["tenantId"], 3)
            self.assertEqual(first_product["brand"], "dummy")
            self.assertEqual(first_product["name"], "product")
            self.assertEqual(first_product["description"], "a test product")
            self.assertEqual(second_product["tenantId"], 3)
            self.assertEqual(second_product["brand"], "dummy")
            self.assertEqual(second_product["name"], "updated product")
            self.assertEqual(second_product["description"], "an updated product")
        finally:
            self.api.delete_product(first_product["id"])

    def test_delete_product(self):
        try:
            product = self.api.create_product(
                dict(
                    tenantId=3,
                    brand="dummy",
                    name="product",
                    description="a test product",
                )
            )
            product = self.api.get_product(product["id"])

            self.api.delete_product(product["id"])
            self.assertRaises(
                appier.HTTPError, lambda: self.api.get_product(product["id"])
            )
        except:
            self.api.delete_product(product["id"])
