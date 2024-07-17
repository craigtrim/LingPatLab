#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract People (with Anaphora Linking) """


from typing import List, Optional
from lingpatlab.baseblock import BaseObject
from lingpatlab.utils.dto import Sentences
from lingpatlab.analyze.dmo import PeopleSequenceExtractor, PeopleSequenceAnalysis


class ExtractPersonEntities(BaseObject):
    """ Extract People (with Anaphora Linking) """

    def __init__(self,
                 ):
        """ Change Log

        Created:
            19-Mar-2024
            craigtrim@gmail.com
            *   in pursuit of 
                https://github.com/craigtrim/datapipe-apis/issues/61
        """
        BaseObject.__init__(self, __name__)
        self._extract_people = PeopleSequenceExtractor().process
        self._analyze_people = PeopleSequenceAnalysis().process

    def process(self,
                sentences: Sentences) -> Optional[List[str]]:
        """
        Process the given sentences and extract phrases based on the specified parameters.

        Args:
            sentences (Sentences): The sentences to be processed.

        Returns:
            Optional[List[str]]: A list of extracted phrases, or None if no phrases are found.
        """
        if not isinstance(sentences, Sentences):
            raise TypeError(type(sentences))

        exact_matches = set()
        fuzzy_matches = set()

        for sentence in sentences.sentences:

            dmoresult = self._extract_people(sentence)

            [
                exact_matches.add(person)
                for person in dmoresult['exact']
            ]

            [
                fuzzy_matches.add(person)
                for person in dmoresult['fuzzy']
            ]

        if not exact_matches and not fuzzy_matches:
            return None

        exact_matches = sorted(exact_matches, reverse=True)
        fuzzy_matches = sorted(fuzzy_matches, reverse=True)

        people = self._analyze_people(
            exact_matches=exact_matches,
            fuzzy_matches=fuzzy_matches)

        return people
