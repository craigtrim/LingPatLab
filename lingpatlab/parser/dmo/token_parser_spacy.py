#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform spaCy parse and retokenization """


import spacy
from spacy.tokens import Doc
from spacy.lang.en import English
from lingpatlab.baseblock import BaseObject


class TokenParserSpacy(BaseObject):
    """ Perform spaCy parse and retokenization """

    def __init__(self,
                 en_spacy_model: English | None = None):
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
        Updated:
            16-Aug-2024
            craigtrim@gmail.com
            *   optimize model instantiation
                https://github.com/craigtrim/LingPatLab/issues/2
        """
        BaseObject.__init__(self, __name__)
        if en_spacy_model is not None:
            self._nlp = en_spacy_model
        else:
            self._nlp = spacy.load('en_core_web_sm')

    def process(self,
                input_text: str) -> Doc:
        """Perform actual spaCy parse and retokenize input

        Args:
            tokens (list): list of tokens

        Returns:
            Doc: spacy doc
        """
        doc = self._nlp(input_text)

        # ----------------------------------------------------------------------------------
        # Purpose:    Perform Retokenization
        # Reference:  https://github.com/grafflr/graffl-core/issues/1#issuecomment-935048135
        # Updated:    22-Nov-2021
        # ----------------------------------------------------------------------------------
        position = [
            token.i for token in doc
            if token.i != 0 and "'" in token.text
        ]

        with doc.retokenize() as retokenizer:
            for pos in position:

                spans = doc[pos - 1:pos + 1]

                # --------------------------------------------------------------
                # Purpose:      I don't really understand the error ...
                # Reference:    https://spacy.io/api/top-level#util.filter_spans
                # Updated:      27-Feb-2024
                # --------------------------------------------------------------
                try:
                    retokenizer.merge(spans)
                except ValueError as e:
                    self.logger.error(e)

        return doc
