#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Add Punctuation Flag to Token """


from baseblock import BaseObject


class TokenParserCoordinates(BaseObject):
    """ Add Punctuation Flag to Token """

    def __init__(self):
        """ Change Log

        Created:
            13-Oct-2021
            craigtrim@gmail.com
            *   refactored out of 'parse-input-tokens' in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        Updated:
            16-Sept-2022
            craigtrim@gmail.com
            *   rename component
                https://github.com/craigtrim/spacy-token-parser/issues/3
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                tokens: list) -> list:
        """Add (X,Y) coordinates to each token
            to represent the position of this token in the original string

        Args:
            tokens (list): list of tokens

        Raises:
            ValueError: Invalid Coordinate Positions

        Returns:
            list: list of tokens
        """
        results = []

        pos = 0
        last_y = None

        for token in tokens:
            token['x'] = pos

            token['y'] = pos + len(token['text'].strip())
            pos += len(token['text'])

            results.append(token)
            last_y = token['y']

        # ---------------------------------------------------------- ##
        # Purpose:    Validate Coordinate Positioning
        # Reference:  https://github.com/grafflr/graffl-core/issues/41#issuecomment-942803328
        # ---------------------------------------------------------- ##
        actual_len = sum([len(x['text']) for x in tokens])
        if last_y > actual_len:
            self.logger.error('\n'.join([
                'Coordinate Exceed Actual Length',
                f'\tTokens: {tokens}',
                f'\tActual Length: {actual_len}',
                f'\tLast Coordinate: {last_y}']))
            raise ValueError

        return results
