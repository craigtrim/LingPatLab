# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab import LingPatLab


class ParseInputTextTest(unittest.TestCase):

    def setUp(self) -> None:
        self.api = LingPatLab()

    def tearDown(self) -> None:
        self.api = None

    def test_service(self):
        results = self.api.parse_input_text("sem1 sem2 credit american government year: 2019-2020")
        print (results)


if __name__ == "__main__":
    unittest.main()
