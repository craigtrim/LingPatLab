#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Add Wordnet Flag to Token """


from lingpatlab.baseblock import BaseObject
from lingpatlab.utils import is_wordnet_term


class TokenParserWordnet(BaseObject):
    """ Add Wordnet Flag to Token """

    def __init__(self):
        """ Change Log

        Created:
            13-Oct-2021
            craigtrim@gmail.com
            *   refactored out of 'parse-input-tokens' in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        Updated:
            31-Aug-2022
            craigtrim@gmail.com
            *   refactor to use 'is-wordnet-term' function
        Updated:
            16-Sept-2022
            craigtrim@gmail.com
            *   rename component
                https://github.com/craigtrim/spacy-token-parser/issues/3
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                tokens: list) -> list:
        """Add Wordnet Flag to tokens that are found in Wordnet
            these tokens are considered 'lexical'; that is,
            they are commonly known words in the english language
            as opposed to industry jargon

        Args:
            tokens (list): list of tokens

        Returns:
            list: list of tokens
        """
        results = []

        for token in tokens:

            def is_wordnet() -> bool:
                if token['is_punct']:
                    return False

                return is_wordnet_term(token['text'])

            token['is_wordnet'] = is_wordnet()
            results.append(token)

        return results
