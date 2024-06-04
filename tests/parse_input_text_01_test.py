# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab.parser.svc import ParseInputTokens


class ParseInputTextTest(unittest.TestCase):

    def test_service(self):

        parse = ParseInputTokens()
        assert parse


if __name__ == "__main__":
    unittest.main()
