# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab.utils.dmo import PorterStemmer


class TestPosSequenceExtractor(unittest.TestCase):

    def test_service(self):

        stem = PorterStemmer().stem
        assert stem

        words = [
            "caresses", "flies", "dies",
            "mules", "denied", "agreed",
            "owned", "humbled", "sized",
            "meeting", "stating", "siezing",
            "itemization", "sensational", "traditional",
            "reference", "colonizer", "plotted"
        ]

        for word in words:
            print(f"{word} -> {stem(word)}")


if __name__ == "__main__":
    unittest.main()
