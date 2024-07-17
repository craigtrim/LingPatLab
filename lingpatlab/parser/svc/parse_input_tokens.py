#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Use spaCy to Parse Input Tokens """


from typing import List

from lingpatlab.baseblock import (
    BaseObject,
    Stopwatch
)

from lingpatlab.parser.dmo import (
    TokenParserCoordinates,
    TokenParserNormalize,
    TokenParserPostProcess,
    TokenParserPunctuation,
    TokenParserResultSet,
    TokenParserSpacy,
    TokenParserSquots,
    TokenParserWordnet
)
from lingpatlab.utils.dto import (
    Sentence,
    SpacyResult,
)


class ParseInputTokens(BaseObject):
    """ Use spaCy to Parse Input Tokens """

    def __init__(self):
        """ Change Log

        Created:
            1-Oct-2021
            craigtrim@gmail.com
        Updated:
            13-Oct-2021
            craigtrim@gmail.com
            *   refactored into component parts in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        Updated:
            16-Sept-2022
            craigtrim@gmail.com
            *   integrate 'token-parser-postprocess'
                https://github.com/craigtrim/spacy-token-parser/issues/3
            *   rename all components
                https://github.com/craigtrim/spacy-token-parser/issues/3
        Updated:
            29-Feb-2024
            craigtrim@gmail.com
            *   change dataflow
                https://github.com/craigtrim/datapipe-apis/issues/45
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                tokens: List[str]) -> Sentence:

        sw = Stopwatch()

        tokens = TokenParserSquots().process(tokens)
        doc = TokenParserSpacy().process(' '.join(tokens))

        results = TokenParserResultSet().process(doc)
        results = TokenParserPunctuation().process(results)
        results = TokenParserNormalize().process(results)
        results = TokenParserCoordinates().process(results)
        results = TokenParserWordnet().process(results)
        results = TokenParserPostProcess().process(results)

        sentence = Sentence([
            SpacyResult(**token) for token in results
        ])

        if self.isEnabledForDebug:
            self.logger.debug(
                f'Input Parsing Completed: (total-tokens={sentence.size()}), (total-time={str(sw)})')

        return sentence
