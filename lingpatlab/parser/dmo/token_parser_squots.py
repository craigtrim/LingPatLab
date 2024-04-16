#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Transform unigram squots into unigram dquots """


from baseblock import BaseObject


class TokenParserSquots(BaseObject):
    """ Transform unigram squots into unigram dquots """

    def __init__(self):
        """ Change Log

        Created:
            13-Oct-2021
            craigtrim@gmail.com
            *   refactored out of 'parse-input-tokens' in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        Updated:
            16-Sept-2022
            craigtrim@gmail.com
            *   rename component
                https://github.com/craigtrim/spacy-token-parser/issues/3
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                tokens: list) -> list:
        """Transform unigram squots into unigram dquots

        Reference:
             https://github.com/grafflr/graffl-core/issues/1#issuecomment-934967879

        Args:
            tokens (list): list of tokens

        Returns:
            list: list of token results
        """
        results = []

        # ---------------------------------------------------------- ##
        # Note:         Eliminate Trailing Whitespace for accurate dependency parsing
        # Reference:    https://github.com/craigtrim/fast-sentence-tokenize/issues/4#issuecomment-1236220669
        # ---------------------------------------------------------- ##
        # tokens = [x.strip() for x in tokens]
        # tokens = [x for x in tokens if x and len(x)]

        for token in tokens:
            if token == "'":
                token = '"'
            results.append(token)

        return results
