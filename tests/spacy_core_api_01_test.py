# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentence


class TestPosSequenceExtractor(unittest.TestCase):

    def test_service(self):

        api = LingPatLab()
        assert api

        sentence: Sentence = api.parse_input_text(
            "But COVID didn't create the crisis: a 2008 report from the Association of Schools of Public Health had already forecast a workforce crisis that would result in a shortfall of 250,000 public health workers by 2020. Here we are. It all adds up to what I call the failure to launch.")
        assert sentence
        assert isinstance(sentence, Sentence)

        print(sentence.to_string())
        print(sentence.sentence_text())


if __name__ == "__main__":
    unittest.main()
