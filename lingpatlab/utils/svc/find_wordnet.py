# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Facade to find Wordnet Data on Disk """


from string import ascii_lowercase

from lingpatlab.baseblock import BaseObject
from lingpatlab.utils.os import (
    wordnet_terms_a, wordnet_terms_b,
    wordnet_terms_c, wordnet_terms_d,
    wordnet_terms_e, wordnet_terms_f,
    wordnet_terms_g, wordnet_terms_h,
    wordnet_terms_i, wordnet_terms_j,
    wordnet_terms_k, wordnet_terms_l,
    wordnet_terms_m, wordnet_terms_n,
    wordnet_terms_o, wordnet_terms_p,
    wordnet_terms_q, wordnet_terms_r,
    wordnet_terms_s, wordnet_terms_t,
    wordnet_terms_u, wordnet_terms_v,
    wordnet_terms_w, wordnet_terms_x,
    wordnet_terms_y, wordnet_terms_z
)


class FindWordnet(BaseObject):
    """ Facade to find Wordnet Data on Disk """

    def __init__(self):
        """
        Created:
            5-Oct-2021
            craigtrim@gmail.com
            *   https://github.com/grafflr/graffl-core/issues/2
        Updated:
            31-Aug-2022
            craigtrim@gmail.com
            *   migrate to solo repo
        Updated:
            27-Feb-2024
            craigtrim@gmail.com
            *   migrate to spacy-core
                https://github.com/craigtrim/datapipe-apis/issues/43
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def _exists(input_text: str) -> bool:

        if not input_text or input_text is None or not len(input_text):
            return False

        first_char = input_text[0]
        if first_char not in ascii_lowercase:
            return False

        if first_char == 'a':
            return input_text in wordnet_terms_a
        if first_char == 'b':
            return input_text in wordnet_terms_b
        if first_char == 'c':
            return input_text in wordnet_terms_c
        if first_char == 'd':
            return input_text in wordnet_terms_d
        if first_char == 'e':
            return input_text in wordnet_terms_e
        if first_char == 'f':
            return input_text in wordnet_terms_f
        if first_char == 'g':
            return input_text in wordnet_terms_g
        if first_char == 'h':
            return input_text in wordnet_terms_h
        if first_char == 'i':
            return input_text in wordnet_terms_i
        if first_char == 'j':
            return input_text in wordnet_terms_j
        if first_char == 'k':
            return input_text in wordnet_terms_k
        if first_char == 'l':
            return input_text in wordnet_terms_l
        if first_char == 'm':
            return input_text in wordnet_terms_m
        if first_char == 'n':
            return input_text in wordnet_terms_n
        if first_char == 'o':
            return input_text in wordnet_terms_o
        if first_char == 'p':
            return input_text in wordnet_terms_p
        if first_char == 'q':
            return input_text in wordnet_terms_q
        if first_char == 'r':
            return input_text in wordnet_terms_r
        if first_char == 's':
            return input_text in wordnet_terms_s
        if first_char == 't':
            return input_text in wordnet_terms_t
        if first_char == 'u':
            return input_text in wordnet_terms_u
        if first_char == 'v':
            return input_text in wordnet_terms_v
        if first_char == 'w':
            return input_text in wordnet_terms_w
        if first_char == 'x':
            return input_text in wordnet_terms_x
        if first_char == 'y':
            return input_text in wordnet_terms_y
        if first_char == 'z':
            return input_text in wordnet_terms_z

        raise ValueError(input_text)

    def exists(self,
               input_text: str) -> bool:

        input_text = input_text.lower().strip()

        if self._exists(input_text):
            return True

        if input_text.endswith('s') and len(input_text) > 3:
            if self._exists(input_text[:-1]):
                return True

        return False
