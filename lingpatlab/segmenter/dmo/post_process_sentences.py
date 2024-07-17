#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Post Process Sentences """


from lingpatlab.baseblock import BaseObject


class PostProcessStructure(BaseObject):
    """ Post Process Sentences """

    __replace = {
        '..': '. ',
        '. .': '. ',

        '!.': '! ',
        '! .': '! ',

        '?.': '? ',
        '? .': '? ',

        ':.': ': ',
        ': .': ': ',
    }

    def __init__(self):
        """ Change Log:
        
        Created:
            1-Oct-2021
            craigtrim@gmail.com
            *   https://github.com/craigtrim/fast-sentence-segment/issues/1
        Updated:
            27-Mar-2024
            craigtrim@gmail.com
            *   migrated out of modai in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/72
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                sentences: list) -> list:
        normalized = []

        for sentence in sentences:

            for k in self.__replace:
                if k in sentence:
                    sentence = sentence.replace(k, self.__replace[k]).strip()

            normalized.append(sentence)

        return normalized
