# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from pprint import pprint
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentences, Sentence
from lingpatlab.baseblock import FileIO


class TestSpacyCoreAPI(unittest.TestCase):

    def test_extract_phrases_1(self):

        api = LingPatLab()
        assert api

        sentence: Sentence = api.parse_input_text("""
        School: Greensboro High School
        """)

        for token in sentence.tokens:
            print(
                f"text=({token.text}), pos=({token.pos.strip()}), ent=({token.ent.strip()})")

        sentences: Sentences = Sentences(sentences=[sentence])

        d_topics = api.extract_topics(sentences=sentences)
        schools: set[str] = set()
        [
            [
                schools.add(school) for school in d_topics[k]
            ] for k in d_topics
        ]

        self.assertEqual(sorted(schools), [
                         'Greensboro High School', 'High School'])


if __name__ == "__main__":
    unittest.main()
