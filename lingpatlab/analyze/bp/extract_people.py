#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract People (with Anaphora Linking) """


from lingpatlab.baseblock import BaseObject, Enforcer
from typing import List, Dict, Optional
from lingpatlab.utils.dto import Sentences
from lingpatlab.analyze.svc import ExtractPersonEntities


class ExtractPeople(BaseObject):
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
        self._extract_people = ExtractPersonEntities().process

    def process(self,
                sentences: Sentences) -> Optional[Dict[str, List[str]]]:

        result = self._extract_people(sentences)

        if self.isEnabledForDebug and result:
            Enforcer.is_dict(result)
            for k in result:
                Enforcer.is_str(k)
                Enforcer.is_list_of_str(result[k])

        return result
