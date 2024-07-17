#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract People Patterns from Text """


from typing import List, Dict
from lingpatlab.utils.dto import Sentence
from lingpatlab.baseblock import BaseObject, Stopwatch


PATTERNS_1: List[str] = [
    'PERSON PERSON',
    'PERSON PERSON PERSON',
    'PERSON PERSON PERSON PERSON',
    'PERSON PERSON PERSON PERSON PERSON',

    'PROPN PERSON PERSON',
    'PROPN PROPN PERSON PERSON',

    'PROPN PROPN PERSON PERSON',
    'PROPN PROPN PERSON PERSON PERSON',
    'PROPN PROPN PERSON PERSON PERSON PERSON',
    'PROPN PROPN PERSON PERSON PERSON PERSON PERSON',

    # Rear/PROPN Admiral/PROPN William/PERSON F/PERSON ./PUNCT Halsey/PERSON Jr/PERSON
    # reference case: tests/extract_people_08_test.py
    'PROPN PROPN PERSON PERSON PUNCT PERSON PERSON',

    # Rear/PROPN Admiral/PROPN William/PERSON S/PERSON ./PUNCT Pye/NOUN
    # reference case: tests/extract_people_10_test.py
    'PROPN PROPN PERSON PERSON PUNCT NOUN',

    # Kelly/PROPN/PERSON Turner/PROPN/ORG
    # reference case: regression/inputs/People-0003.txt
    'PERSON ORG',

    # Rear/PROPN Admiral/PROPN William/PERSON S/PERSON ./PUNCT Pye/AUX
    # reference case: regression/inputs/People-0005.txt
    'PROPN PROPN PERSON PERSON PUNCT AUX'
]


PATTERNS_2: List[str] = [
    '* PERSON',
    '* PERSON PERSON',
    'PERSON * PERSON',
    '* PERSON PERSON PERSON',
    'PERSON PERSON * PERSON PERSON',
    '* PERSON PERSON PERSON PERSON',
    'PERSON PERSON PERSON * PERSON',
]


class PeopleSequenceExtractor(BaseObject):
    """ Extract Topic Patterns from Text """

    def __init__(self,
                 isEnabledForTrace: bool = False):
        """ Change Log

        Created:
            22-Mar-2024
            craigtrim@gmail.com
            *   based on 'person-sequence-extractor'
                https://github.com/craigtrim/datapipe-apis/issues/63
            *   fix defect in PERSON entity matching
                https://github.com/craigtrim/datapipe-apis/issues/65
        """
        BaseObject.__init__(self, __name__)
        self.isEnabledForTrace = isEnabledForTrace

    @staticmethod
    def _cleanse(input_text: str) -> str:
        """ Cleanse the input text """
        while '  ' in input_text:
            input_text = input_text.replace('  ', ' ')

        input_text = input_text.replace("'s", "")

        return input_text.strip()

    def _create_matching_sequence(self,
                                  sentence: Sentence,
                                  pattern: List[str],
                                  i: int) -> str:
        """
        Create a matching sequence from the given sentence, pattern, and index.

        Args:
            sentence (Sentence): The sentence object.
            pattern (List[str]): The pattern to match.
            i (int): The starting index of the matching sequence.

        Returns:
            str: The matching sequence.

        """
        matching_sequence = ' '.join([
            token.text
            for token in sentence.tokens[i:i+len(pattern)]
        ]).strip()

        while '  ' in matching_sequence:
            matching_sequence = matching_sequence.replace(
                '  ', ' ').strip()

        while ' . ' in matching_sequence:
            matching_sequence = matching_sequence.replace(
                ' . ', '. ').strip()

        if self.isEnabledForDebug:
            self.logger.debug(
                f"Found Pattern Match: `{matching_sequence}` from {pattern}")

        return matching_sequence

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

                if sentence.tokens[i].pos in ['DET']:
                    continue

                if self.isEnabledForTrace:
                    self.logger.debug(
                        f"Begin analysis at i={i} with {pattern}")

                def has_match() -> bool:

                    for j in range(len(pattern)):

                        if self.isEnabledForTrace:
                            self.logger.debug(
                                f"Analyze Token: (text={sentence.tokens[i + j].text}), (pos={sentence.tokens[i + j].pos}), (ent={sentence.tokens[i + j].ent}) for {pattern[j]}")

                        def has_pos_match() -> bool:
                            return pattern[j] != sentence.tokens[i + j].pos

                        def has_ent_match() -> bool:
                            return pattern[j] != sentence.tokens[i + j].ent

                        # don't match wildcards at the start of a sentence; anecdotal observation
                        if pattern[j] == '*' and i != 0:
                            continue

                        # ------------------------------------------------------------------
                        # Purpose:      The 'smoothing' of PROPN/NOUN holds true when
                        #               extracting topics, but not people
                        # Updated:      27-Mar-2024
                        #
                        # elif pattern[j] == 'NOUN' and sentence.tokens[i + j].pos == 'PROPN':
                        #     continue
                        # elif pattern[j] == 'PROPN' and sentence.tokens[i + j].pos == 'NOUN':
                        #     continue
                        # ------------------------------------------------------------------

                        elif pattern[j] == 'PUNCT' and sentence.tokens[i + j].text.strip() == '.':
                            continue

                        elif not has_ent_match() and not has_pos_match():
                            if self.isEnabledForTrace:
                                self.logger.debug(
                                    f"\tToken Failure: (text={sentence.tokens[i + j].text}), (pos={sentence.tokens[i + j].pos}), (ent={sentence.tokens[i + j].ent}) for {pattern[j]}")
                            return False

                        if pattern[j] != sentence.tokens[i + j].pos and pattern[j] != sentence.tokens[i + j].ent:
                            return False

                    def has_person_ent() -> bool:
                        # ------------------------------------------------------------------
                        # Purpose:      Ensure that the sequence has enough PERSON entities
                        # Reference:    https://github.com/craigtrim/datapipe-apis/issues/65
                        # Updated:      22-Mar-2024
                        # ------------------------------------------------------------------
                        person_ctr = 0
                        for j in range(len(pattern)):
                            if sentence.tokens[i + j].ent == 'PERSON':
                                person_ctr += 1
                        if len(pattern) <= 3 and person_ctr >= 1:
                            return True
                        if len(pattern) <= 6 and person_ctr >= 2:
                            return True
                        return person_ctr >= 3

                    return has_person_ent()

                if has_match():
                    matching_sequences.append(self._create_matching_sequence(
                        sentence=sentence, pattern=pattern, i=i))

        def is_upper(ch: str) -> bool:
            if ch in [
                '.'
            ]:
                return True
            return ch.isupper()

        matching_sequences = [
            self._cleanse(sequence)
            for sequence in matching_sequences
            if sum([
                is_upper(gram[0])
                for gram in sequence.split()
            ]) == len(sequence.split())
        ]

        matching_sequences = [
            sequence
            for sequence in matching_sequences
            if not sequence.strip().startswith('.')
        ]

        return matching_sequences

    @staticmethod
    def _filter_matches(matches: List[str]) -> List[str]:
        normalized: List[str] = []

        def has_initial_start(match_tokens: List[str]) -> bool:

            # Prevent sequences like 'F. Halsey' from being included
            if len(match_tokens[0]) == 2 and match_tokens[0][-1] == '.':
                return True
            return False

        for match in matches:
            tokens = match.split()

            if has_initial_start(tokens):
                continue

            normalized.append(match)

        return normalized

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

        exact_matches = self._filter_matches(
            sorted(set(exact_matches), reverse=True))

        fuzzy_matches = self._filter_matches(sorted(set([
            fuzzy_match for fuzzy_match in fuzzy_matches
            if fuzzy_match not in exact_matches
        ]), reverse=True))

        result = {
            "exact": exact_matches,
            "fuzzy": fuzzy_matches,
        }

        total_matches = len(exact_matches) + len(fuzzy_matches)

        if self.isEnabledForDebug and total_matches > 0:
            self.logger.debug(
                f"Extracted Topic Sequences: {total_matches} in ({str(sw)})")

        return result
