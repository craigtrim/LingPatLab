# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentences


class TestSpacyCoreAPI(unittest.TestCase):

    def test_extract_phrases(self):

        api = LingPatLab()
        assert api

        input_lines = [
            "Rear Admiral William F. Halsey Jr."
        ]

        sentences: Sentences = api.parse_input_lines(input_lines)

        print(sentences.to_string())
        people = api.extract_people(sentences=sentences)

        print(people)
        expected_results = {
            'Halsey': ['Rear Admiral William F. Halsey Jr', 'Halsey Jr', 'William F. Halsey Jr']
        }

        self.assertEqual(people, expected_results)


if __name__ == "__main__":
    unittest.main()
