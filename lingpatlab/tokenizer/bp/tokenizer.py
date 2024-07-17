#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Text Tokenization API """


from typing import List
from lingpatlab.baseblock import BaseObject, Stopwatch, Enforcer
from functools import lru_cache


class Tokenizer(BaseObject):
    """ Text Tokenization API """

    def __init__(self):
        """ Change Log

        Updated:
            27-Mar-2024
            craigtrim@gmail.com
            *   migrated out of modai in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/72
        """
        BaseObject.__init__(self, __name__)
        self._custom = None

    @lru_cache
    def input_text(self,
                   input_text: str) -> List[str]:
        """Tokenize with Custom Tokenizer

        Args:
            input_text (str): input text of any length

        Returns:
            list: list of tokens
        """

        sw = Stopwatch()

        if self.isEnabledForDebug:
            Enforcer.is_str(input_text)

        if not self._custom:
            from lingpatlab.tokenizer.svc import TokenizeUseGraffl
            self._custom = TokenizeUseGraffl().process

        tokens: List[str] = self._custom(input_text)

        if self.isEnabledForDebug:
            Enforcer.is_list_of_str(tokens)
            self.logger.debug(
                f"Tokenized input text into {len(tokens)} tokens in {str(sw)}")

        return tokens
