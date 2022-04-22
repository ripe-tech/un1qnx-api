#!/usr/bin/python
# -*- coding: utf-8 -*-

class TagAPI(object):

    def list_tags(self, *args, **kwargs):
        url = self.base_url + "tags"
        contents = self.get(url, **kwargs)
        return contents

    def get_tag(self, id):
        url = self.base_url + "tags/%s" % id
        contents = self.get(url)
        return contents

    def create_tag(self, id):
        return self.update_tag_state(id, "created")

    def activate_tag(self, id):
        return self.update_tag_state(id, "active")

    def inactivate_tag(self, id):
        return self.update_tag_state(id, "inactive")

    def disable_tag(self, id):
        return self.update_tag_state(id, "disabled")

    def expire_tag(self, id):
        return self.update_tag_state(id, "expired")

    def update_tag_state(self, id, state):
        url = self.base_url + "tags/%s/partial" % id
        data_j = dict(
            state = state
        )
        contents = self.patch(url, data_j = data_j)
        return contents
