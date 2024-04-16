# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from typing import List
from pprint import pprint
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentences, Sentence
from baseblock import FileIO


class TestSpacyCoreAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.api = LingPatLab()
        assert self.api

    def tearDown(self) -> None:
        self.api = None

    def extract_topics(self,
                       input_text: str) -> List[str]:

        sentence: Sentence = self.api.parse_input_text(input_text)
        for token in sentence.tokens:
            print(
                f"text=({token.text}), pos=({token.pos.strip()}), ent=({token.ent.strip()})")

        return self.api.extract_topics(sentence)

    def test_extract_topics_1(self):

        input_text = """
        With no carriers available to confront this new threat, Kelly Turner sent Rear Admiral Dan Callaghan, lately Ghormley's chief of staff, with a scratch force of cruisers and destroyers to interpose itself between the enemy battleships and the critical airstrip. It was a near-hopeless mismatch. The first phase of it took place in the middle of the night in a violent thunderstorm. Reports were even more fragmentary than usual, in part because both Callaghan and his second-in-command, Norman Scott (the recent victor in the Battle of Cape Esperance), were both killed early on. As a result, Nimitz passed the night without any definitive information either way.
        """

        topics = self.extract_topics(input_text)

        expected_results = {
            'Dan': ['Rear Admiral Dan', 'Admiral Dan'],
            'Turner': ['Kelly Turner'],
            'Esperance': ['Cape Esperance', 'Battle of Cape Esperance']
        }

        self.assertEqual(topics, expected_results)

    def test_extract_topics_2(self):

        input_text = """
        Battle of Cape Esperance
        """

        topics = self.extract_topics(input_text)

        expected_results = {
            'Esperance': ['Cape Esperance', 'Battle of Cape Esperance']
        }

        self.assertEqual(topics, expected_results)

    def extract_people(self,
                       input_text: str) -> List[str]:

        sentence: Sentence = self.api.parse_input_text(input_text)
        # for token in sentence.tokens:
        #     print(
        #         f"text=({token.text}), pos=({token.pos.strip()}), ent=({token.ent.strip()})")

        return self.api.extract_people(sentence)

    def test_extract_people_1(self):

        input_text = """
        With no carriers available to confront this new threat, Kelly Turner sent Rear Admiral Dan Callaghan, lately Ghormley's chief of staff, with a scratch force of cruisers and destroyers to interpose itself between the enemy battleships and the critical airstrip. It was a near-hopeless mismatch. The first phase of it took place in the middle of the night in a violent thunderstorm. Reports were even more fragmentary than usual, in part because both Callaghan and his second-in-command, Norman Scott (the recent victor in the Battle of Cape Esperance), were both killed early on. As a result, Nimitz passed the night without any definitive information either way.
        """

        people = self.extract_people(input_text)
        print(f"Extracted People: {people}")

        # expected_results = {
        #     'Callaghan': ['Rear Admiral Dan Callaghan', 'Dan Callaghan', 'Admiral Dan Callaghan'],
        #     'Scott': ['Norman Scott']
        # }

        expected_results = {
            'Callaghan': ['Rear Admiral Dan Callaghan', 'Dan Callaghan', 'Admiral Dan Callaghan'],
            'Scott': ['Norman Scott'],
            'Turner': ['Kelly Turner']
        }

        self.assertEqual(people, expected_results)


if __name__ == "__main__":
    unittest.main()
