#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Anaphora Resolution on Extracted People """


from typing import List
from collections import defaultdict
from lingpatlab.baseblock import BaseObject, Stopwatch


LAST_TOKEN_BLACKLIST = [
    'the'
]


class PeopleSequenceAnalysis(BaseObject):
    """ Perform Anaphora Resolution on Extracted People """

    def __init__(self):
        """ Change Log

        Created:
            19-Mar-2024
            craigtrim@gmail.com
            *   in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/61
        Updated:
            27-Mar-2024
            craigtrim@gmail.com
            *   rewrite core algorithm in pursuit of testing 
                https://github.com/craigtrim/datapipe-apis/issues/71
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def _cleanse(person: str) -> str:
        person = person.strip()
        if person.endswith("'s"):
            return person[:-2]
        return person

    def remove_subsumed_spans(self,
                              d_people: dict) -> dict:
        """
        Remove subsumed spans from the given dictionary.

        Args:
            d_people (dict): Dictionary containing people and their names.

        Returns:
            dict: Dictionary with subsumed spans removed.
        """

        for person_1, names_1 in d_people.items():
            for person_2, names_2 in d_people.items():
                if person_1 == person_2:
                    continue

                for name_1 in names_1:
                    for name_2 in names_2:

                        if name_1 == name_2:
                            d_people[person_1] = [
                                name for name in names_1 if name != name_2
                            ]

                        elif name_1 in name_2:
                            d_people[person_1] = [
                                name for name in names_1 if name_1 not in name_2
                            ]

                        elif name_2 in name_1:
                            d_people[person_2] = [
                                name for name in names_2 if name_2 not in name_1
                            ]

        return {
            k: d_people[k]
            for k in d_people
            if d_people[k]
        }

    @staticmethod
    def aggregate_last_tokens(d_people: dict) -> dict:
        """

        These shouldall be considered the same person:
            "Navy Frank Knox", "Frank Knox", "Secretary Knox"

        """

        d_aggregate_keys = defaultdict(list)

        for person in d_people:

            tokens = person.split()
            if len(tokens) == 1:
                d_aggregate_keys[person] = []
                continue

            last_token = tokens[-1]
            if last_token.lower() in ['jr'] and len(tokens) >= 2:
                last_token = tokens[-2]

            if last_token.lower() in LAST_TOKEN_BLACKLIST:
                continue

            d_aggregate_keys[last_token].append(person)

        return dict(d_aggregate_keys)

    @staticmethod
    def index_by_last_token(unigrams: List[str],
                            ngrams: List[str]) -> dict:
        """
        Indexes ngrams by their last token.

        Args:
            unigrams (List[str]): A list of individual tokens.
            Sample Input:
                ['Yorktown', 'Yatsushiro', "Yamato's", ... ]

            ngrams (List[str]): A list of ngrams.
            Sample Input:
                ['William Halsey', 'Soc McMorris', 'Robert Sherrod', ... ]

        Returns:
            dict: A dictionary where the keys are ngrams and the values are sets of last tokens.
            Sample Output:
                {'William Halsey': {'Halsey'}, 'Soc McMorris': {'McMorris'}, ... }
        """
        d_people = defaultdict(set)

        for ngram in ngrams:
            last_token = ngram.split()[-1]

            if last_token in unigrams:
                d_people[ngram].add(last_token)
            else:
                d_people[ngram] = []

        return dict(d_people)

    @staticmethod
    def cleanse(d_normalized: dict) -> dict:
        d_clean = {}

        for k in d_normalized:
            d_clean[k] = [
                person.replace(' . ', '. ').strip()
                for person in d_normalized[k]
            ]

        return d_clean

    def process(self,
                exact_matches: List[str],
                fuzzy_matches: List[str]) -> List[str]:
        """
        Process the exact and fuzzy matches to perform anaphora resolution on extracted people.

        Args:
            exact_matches (List[str]): A list of exact matches.
            fuzzy_matches (List[str]): A list of fuzzy matches.

        Returns:
            List[str]: A list of resolved people names.
        """
        sw = Stopwatch()

        people = exact_matches + fuzzy_matches

        people = [
            person for person in people
            if len(person) > 1 and len(person.split()[-1]) > 1
        ]

        unigrams = [
            person for person in people
            if len(person.split()) == 1
        ]

        ngrams = [
            person for person in people
            if person not in unigrams
        ]

        # Index ngrams by their last token
        d_people = self.index_by_last_token(unigrams, ngrams)

        # Aggregate people with the same last token
        d_aggregate = self.aggregate_last_tokens(d_people)

        # Remove subsumed spans from the aggregated people
        d_normalized = self.remove_subsumed_spans(d_aggregate)

        d_normalized = self.cleanse(d_normalized)

        if self.isEnabledForDebug and len(d_normalized):
            self.logger.debug(
                f"Anaphora Resolution: {d_normalized} in ({str(sw)})")

        return d_normalized
