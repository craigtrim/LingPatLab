# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from pprint import pprint
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentences, Sentence
from baseblock import FileIO


class TestSpacyCoreAPI(unittest.TestCase):

    def test_extract_phrases_1(self):

        api = LingPatLab()
        assert api

        sentence: Sentence = api.parse_input_text("""
        Rear Admiral William
        """)

        for token in sentence.tokens:
            print(
                f"text=({token.text}), pos=({token.pos.strip()}), ent=({token.ent.strip()})")

        sentences: Sentences = Sentences(sentences=[sentence])

        people = api.extract_people(sentences=sentences)

        expected_results = {'William': ['Admiral William']}
        self.assertEqual(people, expected_results)

    def test_extract_phrases_02(self):

        api = LingPatLab()
        assert api

        sentence: Sentence = api.parse_input_text("""
        Rear Admiral William S. Pye
        """)

        for token in sentence.tokens:
            print(
                f"text=({token.text}), pos=({token.pos.strip()}), ent=({token.ent.strip()})")

        sentences: Sentences = Sentences(sentences=[sentence])

        # topics = api.extract_topics(sentences=sentences)
        people = api.extract_people(sentences=sentences)

        expected_people = {
            'Pye': ['Rear Admiral William S. Pye']
        }

        self.assertEqual(people, expected_people)

    def test_extract_phrases_03(self):

        api = LingPatLab()
        assert api

        sentence: Sentence = api.parse_input_text("""
        Rear Admiral William S. Pye briefly assumed command in January, with responsibilities in the Mariana Islands, including battleship forces. The strategic importance of these islands influenced military operations extensively. Additionally, there were instances of war crimes and strategic decisions involving the Mariana Islands that impacted the Pacific theater. The Mariana Islands played a crucial role in various naval operations and strategies during the wartime period. Rear Admiral Chester Nimitz's interactions and decisions related to the Mariana Islands shaped significant military maneuvers and responses. The Mariana Islands served as a focal point for various military figures, strategic planning, and historical events, underscoring their significance in naval and wartime activities.
        """)

        sentences: Sentences = Sentences(sentences=[sentence])

        people = api.extract_people(sentences=sentences)

        # expected_results = {
        #     'Nimitz': ['Rear Admiral Chester Nimitz', 'Chester Nimitz', 'Admiral Chester Nimitz'],
        #     'William': ['Admiral William']
        # }

        expected_results = {
            'Pye': ['Rear Admiral William S. Pye'],
            'Nimitz': ['Rear Admiral Chester Nimitz', 'Chester Nimitz', 'Admiral Chester Nimitz'],
            'Islands': ['Mariana Islands']
        }

        self.assertEqual(people, expected_results)


if __name__ == "__main__":
    unittest.main()
