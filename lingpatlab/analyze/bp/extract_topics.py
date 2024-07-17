#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract Part-of-Speech (POS) Patterns from Text """


from lingpatlab.baseblock import BaseObject
from typing import List, Dict, Optional
from lingpatlab.utils.dto import Sentences
from lingpatlab.analyze.svc import ExtractTopicEntities


class ExtractTopics(BaseObject):
    """ Extract Part-of-Speech (POS) Patterns from Text """

    def __init__(self):
        """ Change Log

        Created:
            28-Feb-2024
            craigtrim@gmail.com
            *   refactored out of a script in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/44
        Updated:
            14-Mar-2024
            craigtrim@gmail.com
            *   optionally pass in patterns
                https://github.com/craigtrim/datapipe-apis/issues/57
        Updated:
            19-Mar-2024
            craigtrim@gmail.com
            *   use exclude-people as a parameter in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/61#issuecomment-2008099602
        Updated:
            20-Mar-2024
            craigtrim@gmail.com
            *   renamed from 'extract-phrases' in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/62
        Updated:
            22-Mar-2024
            craigtrim@gmail.com
            *   refactored and based on 'extract-people'
                https://github.com/craigtrim/datapipe-apis/issues/63
        """
        BaseObject.__init__(self, __name__)
        self._extract_topics = ExtractTopicEntities().process

    def process(self,
                sentences: Sentences) -> Optional[Dict[str, List[str]]]:
        return self._extract_topics(sentences=sentences)
