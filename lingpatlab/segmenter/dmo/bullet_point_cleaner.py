#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Prevent Bullet Points from Triggering False Positive Segmentation """


from lingpatlab.baseblock import BaseObject


class BulletPointCleaner(BaseObject):
    """ Prevent Bullet Points from Triggering False Positive Segmentation """

    def __init__(self):
        """ Change Log

        Created:
            30-Sept-2021
            craigtrim@gmail.com
            *   created
        Updated:
            19-Oct-2022
            craigtrim@gmail.com
            *   clean up for segment_text_3_test.py
        Updated:
            27-Mar-2024
            craigtrim@gmail.com
            *   migrated out of modai in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/72
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def process(input_text: str) -> str:
        """
        Purpose:
            prevent numbered bullet points from triggering sentence detection
        :param input_text:
            any input text
        :return:
            preprocessed input text
        """
        if input_text.startswith("-"):
            input_text = input_text[1:]  # segment_text_3_test.py

        if "  " in input_text:
            input_text = input_text.replace("  ", " ")

        # the replacement routine above leaves double '..' in the text
        # this replacement will solve that
        while ".." in input_text:
            input_text = input_text.replace("..", ".")

        while ". -" in input_text:  # segment_text_3_test.py
            input_text = input_text.replace(". -", ". ")

        while ". . " in input_text:
            input_text = input_text.replace(". . ", ".")

        while '  ' in input_text:
            input_text = input_text.replace('  ', ' ')

        return input_text
