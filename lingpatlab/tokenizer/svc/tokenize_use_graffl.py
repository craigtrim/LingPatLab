#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Graffl Tokenizer """


from typing import Optional, List
from lingpatlab.tokenizer.dmo import DictionaryFinder


class TokenizeUseGraffl(object):
    """ Graffl Tokenizer """

    __acronym_delimiter = '~~'

    def __init__(self):
        """ Change Log

        Created:
            29-Sept-2021
            craigtrim@gmail.com
        Updated:
            14-Oct-2021
            craigtrim@gmail.com
            *   added redelimit-spaces function
                https://github.com/grafflr/graffl-core/issues/48#issuecomment-943776908
        Updated:
            25-Aug-2022
            craigtrim@gmail.com
            *   keep underscored spaces together
                https://github.com/craigtrim/fast-sentence-tokenize/issues/1
            *   handle lingering squotes
                https://github.com/craigtrim/fast-sentence-tokenize/issues/2
        Updated:
            24-Jan-2024
            craigtrim@gmail.com
            *   avoid list index out of error exception
                https://github.com/craigtrim/modai/issues/3
        Updated:
            27-Feb-2024
            craigtrim@gmail.com
            *   migrate to spacy-core in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/43
        """
        pass

    def _replace_enclitics(self,
                           tokens: list) -> list:

        def transform(token: str) -> list:
            if "'" not in token:
                return [token]
            if token not in DictionaryFinder.enclitics():
                return [token]
            return DictionaryFinder.enclitics()[token]

        normalized = []
        for token in tokens:
            [normalized.append(x) for x in transform(token)]

        return normalized

    def _redelimit_acronyms(self,
                            tokens: list) -> list:

        def transform(token: str) -> str:
            if token.count('.') < 2:
                return token
            return token.replace('.', self.__acronym_delimiter)

        return [transform(x) for x in tokens]

    def _redelimit_abbreviations(self,
                                 tokens: list) -> list:

        def transform(token: str) -> str:
            if token not in DictionaryFinder.abbreviations():
                return token
            return DictionaryFinder.abbreviations()[token]

        return [transform(x) for x in tokens]

    def _undelimit_acronyms(self,
                            tokens: list) -> list:

        def transform(token: str) -> str:
            if self.__acronym_delimiter not in token:
                return token
            return token.replace(self.__acronym_delimiter, '.')

        return [transform(x) for x in tokens]

    def _handle_lingering_squotes(self,
                                  tokens: list) -> list:

        # -------------------------------------------------------------
        # Reference:    https://github.com/craigtrim/fast-sentence-tokenize/issues/2#issuecomment-1227902982
        # Purpose:      Handle first pattern
        # -------------------------------------------------------------
        normalized = []
        for token in tokens:

            if "'" not in token:
                normalized.append(token)

            # considered a valid suffix squote
            elif token.endswith("s' "):
                normalized.append(token)

            # considered an invalid suffix squot
            elif token.endswith("' "):
                normalized.append(f'{token[:-2]} ')
                normalized.append("'")

            else:
                normalized.append(token)

        tokens = normalized

        # -------------------------------------------------------------
        # Reference:    https://github.com/craigtrim/fast-sentence-tokenize/issues/2#issuecomment-1227905278
        # Purpose:      now find the more complex pattern
        # -------------------------------------------------------------
        squotes_pos = []
        squotes_suffix = []

        for i in range(len(tokens)):
            if tokens[i] == "'":
                squotes_pos.append(i)
            if len(tokens[i]) > 1 and tokens[i].strip().endswith("'"):
                squotes_suffix.append(i)

        # the issue does not exist
        if not squotes_suffix or not len(squotes_suffix):
            return tokens

        # -------------------------------------------------------------
        # Updated:          24-Jan-24
        # Reference:        https://github.com/craigtrim/modai/issues/3
        # Purpose:          Avoid List Index Out of Range Defect
        # -------------------------------------------------------------
        if not squotes_pos or not len(squotes_pos):
            return tokens

        # this implies there are an even-number of squotes, and thus,
        # it is likely that they are evenly balanced
        total_squotes = len(squotes_pos)
        if total_squotes > 0 and total_squotes % 2 != 1:
            return tokens

        # the standalone squote occurs after the suffix squote ...
        if squotes_pos[-1] > squotes_suffix[0]:
            return tokens

        normalized = []
        for i in range(len(tokens)):
            if i == squotes_suffix[0]:
                normalized.append(f'{tokens[i][:-1]} ')
                normalized.append("'")
            else:
                normalized.append(tokens[i])

        return normalized

    def _handle_punkt(self,
                      tokens: list) -> list:

        def transform(token: str) -> list:

            if token.isalpha():
                return [token]

            master = []
            buffer = []

            token_len = len(token)

            for i in range(token_len):

                def get_p1() -> Optional[str]:
                    if i - 1 >= 0:
                        return token[i - 1]

                def get_p2() -> Optional[str]:
                    if i - 2 >= 0:
                        return token[i - 2]

                def get_n1() -> Optional[str]:
                    if i + 1 < token_len:
                        return token[i + 1]

                def get_n2() -> Optional[str]:
                    if i + 2 < token_len:
                        return token[i + 2]

                p2 = get_p2()
                p1 = get_p1()
                ch = token[i]
                n1 = get_n1()
                n2 = get_n2()

                # fast-sentence-tokenize#1; keep underscored entities together
                if ch.isalpha() or ch.isnumeric() or ch in [' ', '_']:
                    buffer.append(ch)
                elif ch in ['.', ','] and p1 and p1.isnumeric():
                    buffer.append(ch)  # e.g., 1.06 or 325,000
                elif ch == "'" and p1 and p1.isalpha():
                    buffer.append(ch)  # e.g., Women's
                elif ch == '&' and p1 and p1.isalpha() and n1 and n1.isalpha():
                    buffer.append(ch)  # e.g., A&W
                else:
                    if len(buffer):
                        master.append(''.join(buffer))
                    if len(ch):
                        master.append(ch)
                    buffer = []

                i += 1

            if len(buffer):
                master.append(''.join(buffer))

            return master

        normalized = []
        for token in tokens:
            [normalized.append(x) for x in transform(token)]

        return normalized

    def _redelimit_spaces(self,
                          tokens: list) -> list:
        """Rejoin orphaned spaces with owning text

        Sample Input:
            ["health's ", 'management', ',', ' ', 'NPs']

        Sample Output
            ["health's ", 'management', ', ', 'NPs']

        Args:
            tokens (list): a list of tokens

        Returns:
            list: a normalized list of tokens
        """
        normalized = []

        i = 0
        while i < len(tokens):

            def next_token() -> Optional[str]:
                if i + 1 < len(tokens):
                    return tokens[i + 1]

            t_curr = tokens[i]
            t_next = next_token()

            if t_next and t_next == ' ':
                normalized.append(f'{t_curr} ')
                i += 1
            else:
                normalized.append(t_curr)

            i += 1

        return normalized

    def _split(self,
               input_text: str) -> list:
        master = []

        buffer = []
        for ch in input_text:
            buffer.append(ch)

            if ch in [' ']:
                master.append(''.join(buffer))
                buffer = []

        if len(buffer):
            master.append(''.join(buffer))

        return master

    def process(self,
                input_text: str) -> List[str]:

        tokens = self._split(input_text)
        tokens = self._replace_enclitics(tokens)
        tokens = self._redelimit_acronyms(tokens)
        tokens = self._redelimit_abbreviations(tokens)
        tokens = self._handle_punkt(tokens)
        tokens = self._redelimit_spaces(tokens)
        tokens = self._undelimit_acronyms(tokens)
        tokens = self._handle_lingering_squotes(tokens)

        return tokens
