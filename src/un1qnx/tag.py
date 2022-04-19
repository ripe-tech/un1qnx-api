#!/usr/bin/python
# -*- coding: utf-8 -*-

class TagAPI(object):

    def list_tags(self, *args, **kwargs):
        url = self.base_url + "tags"
        contents = self.get(url, **kwargs)
        return contents

    def get_tag(self, id):
        url = self.base_url + "tags/%d" % id
        contents = self.get(url)
        return contents
