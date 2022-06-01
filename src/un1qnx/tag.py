#!/usr/bin/python
# -*- coding: utf-8 -*-


class TagAPI(object):
    def list_tags(self, *args, **kwargs):
        url = self.base_url + "tags"
        contents = self.get(url, **kwargs)
        return contents

    def get_tag(self, id, **kwargs):
        url = self.base_url + "tags/%s" % id
        contents = self.get(url, **kwargs)
        return contents

    def create_tag(self, id):
        return self.update_tag(id, dict(state="created"))

    def activate_tag(self, id):
        return self.update_tag(id, dict(state="active"))

    def inactivate_tag(self, id):
        return self.update_tag(id, dict(state="inactive"))

    def disable_tag(self, id):
        return self.update_tag(id, dict(state="disabled"))

    def expire_tag(self, id):
        return self.update_tag(id, dict(state="expired"))

    def create_tag_by_code(self, code):
        return self.update_tag_by_code(code, dict(state="created"))

    def activate_tag_by_code(self, code):
        return self.update_tag_by_code(code, dict(state="active"))

    def inactivate_tag_by_code(self, code):
        return self.update_tag_by_code(code, dict(state="inactive"))

    def disable_tag_by_code(self, code):
        return self.update_tag_by_code(code, dict(state="disabled"))

    def expire_tag_by_code(self, code):
        return self.update_tag_by_code(code, dict(state="expired"))

    def update_tag(self, id, tag):
        url = self.base_url + "tags/%s/partial" % id
        contents = self.patch(url, data_j=tag)
        return contents

    def update_tag_by_code(self, code, tag):
        url = self.base_url + "tags/byCode/%s/partial" % code
        contents = self.patch(url, data_j=tag)
        return contents
