# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab import Sentence, SpacyResult
from lingpatlab.baseblock import FileIO
from lingpatlab.utils.dto import (
    SpacyResult,
    Sentence,
    Sentences,
    transform_parse_results_to_sentences
)


class ParseResultsToSentencesTest(unittest.TestCase):

    def test_service(self):

        input_path = FileIO.join_cwd('tests/support/CH03_001.json')
        FileIO.exists_or_error(input_path)
        parse_results = FileIO.read_json(input_path)

        sentences: Sentences = transform_parse_results_to_sentences(
            parse_results)
        for sentence in sentences:
            assert isinstance(sentence, Sentence)
            for token in sentence:
                assert isinstance(token, SpacyResult)


if __name__ == "__main__":
    unittest.main()
