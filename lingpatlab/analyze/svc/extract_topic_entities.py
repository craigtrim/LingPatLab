#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract Topics (with Anaphora Linking) """


from typing import List, Optional
from lingpatlab.baseblock import BaseObject
from lingpatlab.utils.dto import Sentences
from lingpatlab.analyze.dmo import TopicSequenceExtractor, PeopleSequenceAnalysis


class ExtractTopicEntities(BaseObject):
    """ Extract Topics (with Anaphora Linking) """

    def __init__(self,
                 ):
        """ Change Log

        Created:
            22-Mar-2024
            craigtrim@gmail.com
            *   based on 'extract-person-entities' in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/63
        """
        BaseObject.__init__(self, __name__)
        self._extract_topics = TopicSequenceExtractor().process
        self._analyze_topics = PeopleSequenceAnalysis().process

    def process(self,
                sentences: Sentences = None) -> Optional[List[str]]:
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

            dmoresult = self._extract_topics(sentence)

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

        topics = self._analyze_topics(
            exact_matches=exact_matches,
            fuzzy_matches=fuzzy_matches)

        return topics
