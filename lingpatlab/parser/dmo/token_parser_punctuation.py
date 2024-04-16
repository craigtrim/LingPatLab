#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Add Punctuation Flag to Token """


from baseblock import BaseObject


class TokenParserPunctuation(BaseObject):
    """ Add Punctuation Flag to Token """

    __punkt = [
        '!', '?', ':', '.', '"', '-', '(', ')'
    ]

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
        """Add Punctuation Flag to tokens that are considered punctuation

        Args:
            tokens (list): list of tokens

        Returns:
            list: list of tokens
        """
        results = []

        for token in tokens:

            def ispunct(input_text: str) -> bool:
                return input_text in self.__punkt

            token['is_punct'] = ispunct(token['text'])
            results.append(token)

        return results
