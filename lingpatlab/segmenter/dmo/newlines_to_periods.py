#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Convert New Lines into Periods """


from lingpatlab.baseblock import BaseObject


class NewlinesToPeriods(BaseObject):
    """ Convert New Lines into Periods """

    def __init__(self):
        """
        Created:
            30-Sept-2021
            craigtrim@gmail.com
            *   created
        Updated:
            27-Mar-2024
            craigtrim@gmail.com
            *   migrated out of modai in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/72
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def process(input_text: str):
        """
        Purpose:
            Take a CSV list and transform to sentences
        :param input_text:
        :return:
        """

        # def replace(input_text: str,
        #             variant: str,
        #             canon: str) -> str:

        #     v1 = f" {variant} "
        #     if v1 in input_text:
        #         return input_text.replace(
        #             v1, f" {canon} ")

        #     v2 = f"{variant} "
        #     if v2 in input_text:
        #         return input_text.replace(
        #             v2, f"{canon} ")

        #     v3 = f" {variant}"
        #     if v3 in input_text:
        #         return input_text.replace(
        #             v3, f" {canon}")

        #     return input_text

        # result = replace(input_text=input_text,
        #                  variant='\n',
        #                  canon=' . ')
        result = input_text.replace('\n', ' . ')

        return result
