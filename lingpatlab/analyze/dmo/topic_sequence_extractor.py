#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract People Patterns from Text """


from typing import List, Dict
from lingpatlab.utils.dto import Sentence, SpacyResult
from lingpatlab.baseblock import BaseObject, Stopwatch


PATTERNS_1: List[str] = [
    'ADJ NOUN',  # this works well assuming title case of bigram
    'NOUN NOUN',
    'NOUN NOUN NOUN',
    'NOUN NOUN NOUN NOUN',
    'NOUN NOUN NOUN NOUN NOUN',
    'NOUN NOUN NOUN NOUN NOUN NOUN',
    'NOUN NOUN NOUN NOUN NOUN NOUN NOUN',
    'PROPN PROPN NUM',
    'PROPN ADP PROPN PROPN',
    'NOUN NOUN NOUN NOUN PUNCT NOUN',

    # Battle/PROPN of/ADP Cape/PROPN Esperance/PROPN
    # reference case: tests/extract_topics_01_test.py
    'PROPN ADP PROPN PROPN',
]


PATTERNS_2: List[str] = [
]


class TopicSequenceExtractor(BaseObject):
    """ Extract Topic Patterns from Text """

    def __init__(self):
        """ Change Log

        Created:
            22-Mar-2024
            craigtrim@gmail.com
            *   based on 'person-sequence-extractor'
                https://github.com/craigtrim/datapipe-apis/issues/63
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def _filter(matching_sequences: List[str]) -> List[str]:
        """
        Filters the given list of matching sequences and returns a new list
        containing only the sequences that meet the specified criteria.

        Args:
            matching_sequences (List[str]): A list of matching sequences to be filtered.

        Returns:
            List[str]: A new list containing only the sequences that meet the criteria.
        """
        normalized = []

        for matching_sequence in matching_sequences:

            # no valid pattern can start with a period ...
            if matching_sequence.strip().startswith('.'):
                continue

            tokens = [
                token.strip() for token in
                matching_sequence.split()
            ]

            def is_upper() -> bool:

                # all tokens must be uppercased
                for token in tokens:

                    # an exception is made for tokens in this list
                    if not token[0].isupper() and not token in [
                        '.', 'of'
                    ]:
                        return False

                return True

            if is_upper():
                normalized.append(matching_sequence)

        return normalized

    @staticmethod
    def _cleanse(matching_tokens: List[SpacyResult]) -> str:
        """
        Cleanses the matching tokens by removing unnecessary characters and spaces.

        Args:
            matching_tokens (List[SpacyResult]): A list of SpacyResult objects representing the matching tokens.

        Returns:
            str: The cleansed sequence of tokens.

        """
        sequence = ' '.join([
            token.text for token
            in matching_tokens
        ])

        while '  ' in sequence:
            sequence = sequence.replace('  ', ' ')

        sequence = sequence.replace("'s", "")

        return sequence.strip()

    @staticmethod
    def _is_person(matching_tokens: List[SpacyResult]) -> bool:
        """
        Check if the given sequence of tokens represents a person.

        Args:
            matching_tokens (List[dict]): A list of tokens to be checked.

        Returns:
            bool: True if the sequence represents a person, False otherwise.
        """
        ents = ' '.join([
            token.ent for token in matching_tokens
        ])

        # if at least two ent=PERSON tags exist in this matching sequence
        # this is likely a PERSON and should be discarded as a topical match
        # since the PERSON extractor will likely pick it up
        return 'PERSON PERSON' in ents

    def _extract_patterns(self,
                          sentence: Sentence,
                          patterns: List[str]) -> List[str]:
        """
        Extract sequences from the given data based on the provided pattern.

        Args:
            data (List[List[str]]): The input data in List[List[str]] format.
            pattern (str): The pattern to match.

        Returns:
            List[List[str]]: List of sequences that match the given pattern.
        """

        matching_sequences = []

        for pattern in patterns:

            pattern: List[str] = pattern.split()

            for i, _ in enumerate(sentence.tokens):

                if len(pattern) + i > sentence.size():
                    continue

                if sentence.tokens[i].pos in [
                    'DET',
                ]:
                    continue

                def has_match() -> bool:

                    for j in range(len(pattern)):

                        if pattern[j] == '*':
                            continue

                        elif pattern[j] == 'NOUN' and sentence.tokens[i + j].pos == 'PROPN':
                            continue

                        elif pattern[j] == 'PROPN' and sentence.tokens[i + j].pos == 'NOUN':
                            continue

                        elif pattern[j] == 'PUNCT' and sentence.tokens[i + j].text.strip() == '.':
                            continue

                        elif pattern[j] != sentence.tokens[i + j].pos:
                            return False

                    return True

                is_person = self._is_person(sentence.tokens[i:i+len(pattern)])

                if has_match() and not is_person:
                    matching_sequences.append(
                        self._cleanse(
                            sentence.tokens[i: i + len(pattern)]
                        )
                    )

        matching_sequences = self._filter(matching_sequences)

        return matching_sequences

    def process(self,
                sentence: Sentence) -> Dict[str, List[str]]:
        """
        Process the given sentence and extract people sequences using exact and fuzzy matching patterns.

        Args:
            sentence (Sentence): The input sentence to process.

        Returns:
            Dict[str, List[str]]: A dictionary containing the extracted people sequences.
                The keys are "exact" and "fuzzy", and the values are lists of strings representing the matches.
        """
        sw = Stopwatch()
        assert isinstance(sentence, Sentence)

        exact_matches: List[str] = self._extract_patterns(
            sentence=sentence, patterns=PATTERNS_1)

        fuzzy_matches: List[str] = self._extract_patterns(
            sentence=sentence, patterns=PATTERNS_2)

        result = {
            "exact": exact_matches,
            "fuzzy": fuzzy_matches
        }

        total_matches = len(exact_matches) + len(fuzzy_matches)

        if self.isEnabledForDebug and total_matches > 0:
            self.logger.debug(
                f"Extracted Topic Sequences: {total_matches} in ({str(sw)})")

        return result
