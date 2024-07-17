#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Orchestrate Sentence Segmentation """


from typing import List
from functools import lru_cache
from lingpatlab.baseblock import BaseObject, Stopwatch, Enforcer

from lingpatlab.segmenter.svc import (
    PerformParagraphSegmentation,
    PerformSentenceSegmentation
)


class Segmenter(BaseObject):
    """ Orchestrate Sentence Segmentation """

    def __init__(self):
        """ Change Log

        Created:
            30-Sept-2021
            craigtrim@gmail.com
            *   created
        Updated:
            27-Mar-2024
            craigtrim@gmail.com
            *   migrated out of modai in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/72
        """
        BaseObject.__init__(self, __name__)
        self._segment_paragraphs = PerformParagraphSegmentation().process
        self._segment_sentences = PerformSentenceSegmentation().process

    def _input_text(self,
                    input_text: str) -> list:
        paragraphs = []

        for paragraph in self._segment_paragraphs(input_text):
            paragraphs.append(self._segment_sentences(paragraph))

        return paragraphs

    @lru_cache(maxsize=1024, typed=True)
    def input_text(self,
                   input_text: str) -> List[str]:
        """Segment Input Text into Paragraphs and Sentences

        Args:
            input_text (str): An input string of any length or type

        Raises:
            ValueError: input must be a string

        Returns:
            list:   returns a list of lists.
                    Each outer list is a paragraph.
                    Each inner list contains 1..* sentences
        """

        if self.isEnabledForDebug:
            Enforcer.is_str(input_text)

        sw = Stopwatch()

        paragraphs = self._input_text(input_text)

        if self.isEnabledForInfo:
            Enforcer.is_list_of_str(paragraphs)
            self.logger.info('\n'.join([
                "Segmentation of Input Text Complete",
                f"\tTotal Paragraphs: {len(paragraphs)}",
                f"\tTotal Time: {str(sw)}"]))

        return paragraphs
