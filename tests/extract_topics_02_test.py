# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentence, SpacyResult


class TestPosSequenceExtractor(unittest.TestCase):

    def setUp(self) -> None:
        self.api = LingPatLab()
        assert self.api

    def tearDown(self) -> None:
        self.api = None

    def test_service(self):

        sentence: Sentence = self.api.parse_input_text(
            "During the intense operations near Guadalcanal, Admiral Nimitz offered specific guidance to Rear Admiral Ghormley, suggesting strategic movements around Cape Esperance. Ghormley's subsequent actions led to a crucial ambush off Cape Esperance, resulting in significant losses for the Japanese. This victory served as redemption for previous events and prompted considerations of releasing past battle results to the public. As tensions escalated with Japanese naval strength in the region, concerns mounted, leading to Admiral Halsey replacing Ghormley. The intense conflicts, including the Battle of Cape Esperance, highlighted the challenging circumstances faced by American forces against overwhelming odds in the Pacific theater")
        assert sentence
        assert isinstance(sentence, Sentence)

        results = self.api.extract_topics(sentence)

        print(results)
        expected_results = {'Ghormley': ['Rear Admiral Ghormley', 'Admiral Ghormley'], 'Esperance': [
            'Cape Esperance', 'Battle of Cape Esperance'], 'Nimitz': ['Admiral Nimitz'], 'Halsey': ['Admiral Halsey']}
        self.assertEqual(results, expected_results)


if __name__ == "__main__":
    unittest.main()
