#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Use spaCy to Parse Input Tokens """


from typing import List
from spacy.lang.en import English

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

    def __init__(self,
                 en_spacy_model: English | None = None):
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
        Updated:
            16-Aug-2024
            craigtrim@gmail.com
            *   optimize model instantiation
            *   pre-init class methods in init function
                https://github.com/craigtrim/LingPatLab/issues/2
        """
        BaseObject.__init__(self, __name__)
        self._parse_squots = TokenParserSquots().process
        self._spacy_parse = TokenParserSpacy(en_spacy_model).process
        self._parse_result_set = TokenParserResultSet().process
        self._parse_punkt = TokenParserPunctuation().process
        self._normalize_parse = TokenParserNormalize().process
        self._parse_coords = TokenParserCoordinates().process
        self._parse_wordnet = TokenParserWordnet().process
        self._post_process = TokenParserPostProcess().process

    def process(self,
                tokens: List[str]) -> Sentence | None:

        sw = Stopwatch()

        tokens = self._parse_squots(tokens)
        if not tokens or not len(tokens):
            return None

        doc = self._spacy_parse(' '.join(tokens))

        results = self._parse_result_set(doc)
        if not results or not len(results):
            return None

        results = self._parse_punkt(results)
        if not results or not len(results):
            return None

        results = self._normalize_parse(results)
        if not results or not len(results):
            return None

        results = self._parse_coords(results)
        if not results or not len(results):
            return None

        results = self._parse_wordnet(results)
        if not results or not len(results):
            return None

        results = self._post_process(results)
        if not results or not len(results):
            return None

        sentence = Sentence([
            SpacyResult(**token) for token in results
        ])

        if self.isEnabledForDebug:
            self.logger.debug(
                f'Input Parsing Completed: (total-tokens={sentence.size()}), (total-time={str(sw)})')

        return sentence
