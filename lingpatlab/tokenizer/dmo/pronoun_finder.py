# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Pronouns """
from lingpatlab.baseblock import BaseObject


class PronounFinder(BaseObject):
    """ Generic Facade to interact with Pronouns """

    __all = None
    __alphabet = [(chr(ord('a') + i)) for i in range(26)]

    _d_pronouns = {
        '1': [
            'i',
            'me',
            'my',
            'mine',
            'myself',
            'we',
            'us',
            'our',
            'ourselves'
        ],
        '2': [
            'you'
        ],
        '3': [
            'she',
            'her',
            'he',
            'him',
            'it',
            'they',
            'them'
        ]
    }

    def __init__(self):
        """ Change Log:

        Created:
            3-May-2022
            craigtrim@gmail.com
            *   https://github.com/grafflr/graffl-core/issues/345
        """
        BaseObject.__init__(self, __name__)

    def all(self) -> list:
        """
        Returns:
            list: a sorted list of all pronouns
        """
        if not self.__all:
            s = set()

            [s.add(x) for x in self._d_pronouns['1']]  # 1st-Person Pronouns
            [s.add(x) for x in self._d_pronouns['2']]  # 2nd-Person Pronouns
            [s.add(x) for x in self._d_pronouns['3']]  # 3rd-Person Pronouns

            self.__all = sorted(s)

        return self.__all

    def has_pronoun(self,
                    input_text: str) -> bool:
        """ Check if a Pronoun is contained within the Input Text

        Args:
            input_text (str): any input text of any length

        Returns:
            bool: True if a pronoun exists in the input text
        """

        input_text = [ch for ch in input_text.lower()
                      if ch in self.__alphabet or ch == ' ']

        tokens = ''.join(input_text).split()
        tokens = [x.strip().lower() for x in tokens if x.isalpha()]
        tokens = [x for x in tokens if x in self.all()]

        return len(tokens)
