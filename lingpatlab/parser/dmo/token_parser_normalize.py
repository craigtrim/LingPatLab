#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Apply Trailing Spaces to Text where appropriate """


from baseblock import BaseObject


class TokenParserNormalize(BaseObject):
    """ Apply Trailing Spaces to Text where appropriate """

    def __init__(self):
        """ Change Log

        Created:
            13-Oct-2021
            craigtrim@gmail.com
            *   refactored out of 'parse-input-tokens' in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        Updated:
            14-Oct-2021
            craigtrim@gmail.com
            *   remove coordinate repositioning logic
                https://github.com/grafflr/graffl-core/issues/48#issuecomment-943793697
        Updated:
            16-Sept-2022
            craigtrim@gmail.com
            *   rename component
                https://github.com/craigtrim/spacy-token-parser/issues/3
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    def process(tokens: list) -> list:
        """Add Trailing Spaces to Text Attribute where appropriate

        This algorithm permits a function like this
            ''.join([x['text'] for x in results])
        to produce properly formatted output like this
            "every" time ("Test's") for now!

        where a naive join like this
            ' '.join([x['text'] for x in results])
        would create output like this
            " every " time ( " Test's " ) for now !

        Args:
            tokens (list): list of tokens

        Returns:
            list: list of tokens
        """
        results = []

        dquot_ctr = 0
        for i in range(len(tokens)):

            has_next_token = i + 1 < len(tokens)

            text = tokens[i]['text']

            # ---------------------------------------------------------- ##
            # Purpose:    Remove Coordinate Positioning Logic
            #             this has been placed into the upstream component 'graffl-parser-resultset'
            # Reference:  https://github.com/grafflr/graffl-core/issues/48#issuecomment-943793697
            # ---------------------------------------------------------- ##
            # def fmt_text() -> str:
            #     # ---------------------------------------------------------- ##
            #     # Purpose:    Improve Coordinate Positioning
            #     # Reference:  https://github.com/grafflr/graffl-core/issues/41#issuecomment-942808974
            #     # ---------------------------------------------------------- ##
            #     if text.strip() == '(':
            #         return text.strip()
            #     if not has_next_token:
            #         return text.strip()
            #     return f"{text} "

            tokens[i]['text'] = text

            if text == '"':
                dquot_ctr += 1
                if dquot_ctr % 2 == 1:
                    tokens[i]['text'] = text

            if has_next_token:
                if tokens[i + 1]['text'] in [')', '"', '!', '?']:
                    tokens[i]['text'] = tokens[i]['text'].strip()

            results.append(tokens[i])

        return results
