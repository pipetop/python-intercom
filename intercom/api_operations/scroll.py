# -*- coding: utf-8 -*-

from intercom import utils
from intercom.scroll_proxy import ScrollProxy


class Scroll(object):

    @classmethod
    def scroll(cls):
        collection = utils.resource_class_to_collection_name(cls)
        scroll_url = "/%s/scroll" % (collection)
        return ScrollProxy(cls, collection, scroll_url)
