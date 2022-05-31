#!/usr/bin/python
# -*- coding: utf-8 -*-


class ProductAPI(object):
    def list_products(self, *args, **kwargs):
        url = self.base_url + "products"
        contents = self.get(url, **kwargs)
        return contents

    def create_product(self, product):
        url = self.base_url + "products"
        contents = self.post(url, data_j=product)
        return contents

    def get_product(self, id, **kwargs):
        url = self.base_url + "products/%s" % id
        contents = self.get(url, **kwargs)
        return contents

    def update_product(self, id, product):
        url = self.base_url + "products/%s" % id
        contents = self.patch(url, data_j=product)
        return contents

    def delete_product(self, id):
        url = self.base_url + "products/%s" % id
        contents = self.delete(url)
        return contents
