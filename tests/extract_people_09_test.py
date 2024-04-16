# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentences, Sentence, to_spacy_result
from baseblock import FileIO


class TestSpacyCoreAPI(unittest.TestCase):

    def test_extract_phrases(self):

        input_path = FileIO.join_cwd(
            'tests/support/extract-people-09-test.json')
        FileIO.exists_or_error(input_path)

        parse_results = FileIO.read_json(input_path)
        assert isinstance(parse_results, list)

        sentences = Sentences(sentences=[
            Sentence([
                to_spacy_result(token) for token in parse_results
            ])
        ])

        assert isinstance(sentences, Sentences)

        api = LingPatLab()
        assert api

        # print(sentences.to_string())

        topics = api.extract_topics(sentences=sentences)
        people = api.extract_people(sentences=sentences)

        print(topics)
        print(people)

        # print(results)
        # assert results == {
        #     'Jr': ['William F. Halsey Jr', 'Halsey Jr'],
        #     'William': ['Admiral William'],
        # }

        # # it's not important to assert results
        # # this test case is for manual testing prior to bumping a version and re-deploying ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'Admiral Nimitz', 'Acknowledging Nimitz'], 'Austin': ['Commander Bernard Austin'], 'Maru': ['Awa Maru'], 'Walker': ['Alexander Walker'], 'Muliwai': ['Visiting Muliwai'], 'Kelly': ['Richmond Kelly'], 'Iceberg': ['Operation Iceberg'], 'Frank': ['Navy Frank', 'Admiral Frank'], 'Richardson': ['General Richardson', 'Admiral Richardson'], 'Joseph': ['Commander Joseph'], 'Bernard': ['Commander Bernard'], 'Elliott': ['Captain Elliott'], 'Yatsushiro': ['Admiral Yatsushiro'], 'William': ['Admiral William'], 'Richard': ['Admiral Richard'], 'Norman': ['Admiral Norman'], 'Milo': ['Admiral Milo'], 'Herbert': ['Admiral Herbert'], 'Harold': ['Admiral Harold'], 'Ghormley': ['Admiral Ghormley'], 'Charles': ['Admiral Charles'], 'Bloch': ['Admiral Bloch'], 'Arthur': ['Admiral Arthur']}


if __name__ == "__main__":
    unittest.main()
