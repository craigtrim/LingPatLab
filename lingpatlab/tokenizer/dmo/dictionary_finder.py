# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Facade to find Dictionaries on Disk """
from lingpatlab.baseblock import BaseObject


class DictionaryFinder(BaseObject):
    """ Facade to find Dictionaries on Disk """

    def __init__(self):
        """
        Created:
            25-Aug-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def hyphens() -> dict:
        from lingpatlab.tokenizer.dto import d_hyphens
        return d_hyphens

    @staticmethod
    def currency() -> dict:
        from lingpatlab.tokenizer.dto import d_currency
        return d_currency

    @staticmethod
    def squotes() -> dict:
        from lingpatlab.tokenizer.dto import squotes
        return squotes

    @staticmethod
    def dquotes() -> dict:
        from lingpatlab.tokenizer.dto import dquotes
        return dquotes

    @staticmethod
    def enclitics() -> dict:
        from lingpatlab.tokenizer.dto import d_enclictics
        return d_enclictics

    @staticmethod
    def abbreviations() -> dict:
        from lingpatlab.tokenizer.dto import d_abbreviations
        return d_abbreviations
