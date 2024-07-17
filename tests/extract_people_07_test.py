# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab.baseblock import FileIO
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentences


class TestSpacyCoreAPI(unittest.TestCase):

    def test_extract_phrases(self):

        input_path = FileIO.join_cwd(
            'tests/support/nimitz_at_war_summaries.txt')
        FileIO.exists_or_error(input_path)

        input_lines = FileIO.read_lines(input_path)
        input_lines = [
            input_line.strip() for input_line in input_lines
            if len(input_line.strip())
        ]

        api = LingPatLab()
        assert api

        sentences: Sentences = api.parse_input_lines(input_lines)
        results = api.extract_people(sentences=sentences)

        print(results)

        # it's not important to assert results
        # this test case is for manual testing prior to bumping a version and re-deploying ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'Admiral Nimitz', 'Acknowledging Nimitz'], 'Austin': ['Commander Bernard Austin'], 'Maru': ['Awa Maru'], 'Walker': ['Alexander Walker'], 'Muliwai': ['Visiting Muliwai'], 'Kelly': ['Richmond Kelly'], 'Iceberg': ['Operation Iceberg'], 'Frank': ['Navy Frank', 'Admiral Frank'], 'Richardson': ['General Richardson', 'Admiral Richardson'], 'Joseph': ['Commander Joseph'], 'Bernard': ['Commander Bernard'], 'Elliott': ['Captain Elliott'], 'Yatsushiro': ['Admiral Yatsushiro'], 'William': ['Admiral William'], 'Richard': ['Admiral Richard'], 'Norman': ['Admiral Norman'], 'Milo': ['Admiral Milo'], 'Herbert': ['Admiral Herbert'], 'Harold': ['Admiral Harold'], 'Ghormley': ['Admiral Ghormley'], 'Charles': ['Admiral Charles'], 'Bloch': ['Admiral Bloch'], 'Arthur': ['Admiral Arthur']}


if __name__ == "__main__":
    unittest.main()
