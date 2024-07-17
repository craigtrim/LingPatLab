#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Add Wordnet Flag to Token """


from lingpatlab.baseblock import BaseObject


class TokenParserResultSet(BaseObject):
    """ Add Wordnet Flag to Token """

    def __init__(self):
        """ Change Log

        Created:
            13-Oct-2021
            craigtrim@gmail.com
            *   refactored out of 'parse-input-tokens' in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        Updated:
            14-Oct-2021
            craig.@graffl.ai
            *   retokenize spaces back into owning tokens
                https://github.com/grafflr/graffl-core/issues/48#issuecomment-943793697
            *   ensure unique id and head values even when text is duplicated
                https://github.com/grafflr/graffl-core/issues/53#issuecomment-944001757
        Updated:
            2-Sept-2022
            craigtrim@gmail.com
            *   fix defect in ID-to-HEAD relationship
                https://github.com/craigtrim/spacy-token-parser/issues/1#issuecomment-1236046400
        Updated:
            16-Sept-2022
            craigtrim@gmail.com
            *   rename component
                https://github.com/craigtrim/spacy-token-parser/issues/3
        Updated:
            14-Jul-2023
            craigtrim@gmail.com
            *   Ensure Unique Token ID and HEAD values
                https://bai.atlassian.net/browse/COR-134
        Updated:
            22-Mar-2024
            craigtrim@gmail.com
            *   fix spacing issue
                https://github.com/craigtrim/datapipe-apis/issues/64
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                doc) -> list:
        """Transform spaCy doc into a result set

        Args:
            doc ([spacy]): a spaCy document

        Returns:
            list: a list of tokens
        """
        results = []

        i = 0

        tokens = [token for token in doc]
        while i < len(tokens):

            token = tokens[i]

            # ---------------------------------------------------------- ##
            # Purpose:    Reclaim Whitespace into Prior Tokens
            # Reference:  https://github.com/grafflr/graffl-core/issues/48#issuecomment-944003662
            # ---------------------------------------------------------- ##
            def has_trailing_space() -> bool:
                if i + 1 >= len(tokens):
                    return False
                return tokens[i + 1].text == ' '

            is_space_next = has_trailing_space()
            if is_space_next:
                i += 1

            def token_text() -> str:
                # ---------------------------------------------------------- ##
                # Purpose:    Fix Spacing
                # Reference:  https://github.com/craigtrim/datapipe-apis/issues/64
                # ---------------------------------------------------------- ##
                token_text: str = token.text
                if '\n' in token_text:
                    token_text = token_text.replace('\n', ' ')
                while '  ' in token_text:
                    token_text = token_text.replace('  ', ' ')
                if is_space_next and not token_text.endswith(' '):
                    return f'{token_text} '
                return token_text

            # ---------------------------------------------------------- ##
            # Purpose:      Ensure Unique IDs for duplicate text values
            # Reference:    https://github.com/grafflr/graffl-core/issues/53#issuecomment-944001757
            #
            # Updated:      Simplify ID and HEAD relationships
            #               https://github.com/craigtrim/spacy-token-parser/issues/1
            #
            # Updated:      Ensure Unique Token-ID and Token-HEAD Values
            #               https://bai.atlassian.net/browse/COR-134
            # ---------------------------------------------------------- ##
            token_id = f"{str(token.orth)}#{i}"
            token_head = f"{str(token.head.orth)}#{token.head.i}"

            d_morph = token.morph.to_dict()

            def tense() -> str:
                if 'Tense' in d_morph:
                    return d_morph['Tense'].lower()
                return ''

            def number() -> str:
                """ Plural vs Singular vs None """
                if 'Number' in d_morph:
                    n = d_morph['Number']
                    if n == 'Sing':
                        return 'singular'
                    elif n == 'Plur':
                        return 'plural'
                    raise NotImplementedError(n)  # I want to know!
                return ''

            def verb_form() -> str:
                """  """
                if 'VerbForm' in d_morph:
                    return d_morph['VerbForm'].lower()
                return ''

            results.append({
                'id': token_id,
                'text': token_text(),
                'lemma': token.lemma_,
                'tense': tense(),  # Past vs Future
                'noun_number': number(),  # Singular vs Plural
                'verb_form': verb_form(),  # Gerund vs Infinitive etc
                'sentiment': token.sentiment,
                'pos': token.pos_,
                'tag': token.tag_,
                'dep': token.dep_,
                'ent': token.ent_type_,
                'shape': token.shape_,
                'is_alpha': token.is_alpha,
                'is_stop': token.is_stop,
                'head': token_head,
                'other': {
                    'i': token.i,
                    'idx': token.idx,
                    'orth': token.orth,
                    'head_i': token.head.i,
                    'head_idx': token.head.idx,
                    'head_orth': token.head.orth,
                    'head_text': token.head.text
                },
            })

            i += 1

        return results
