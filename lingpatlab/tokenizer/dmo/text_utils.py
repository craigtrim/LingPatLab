# -*- coding: utf-8 -*-
""" Text Utility Methods: Common Functions without Special Libraries """


from os import sep
from statistics import mean
from typing import List, Optional

from unicodedata2 import category

STOPWORDS = [
    'a',
    'all',

    'for',
    'from',

    'of',

    'i',
    'in',
    'into',
    'is',

    'to',
    'the',
]

# TODO: Improve from https://github.com/craigtrim/baseblock
class TextUtils(object):
    """ Text Utility Methods: Common Functions without Special Libraries """

    @staticmethod
    def remove_duplicated_phrases(text_1: str,
                                  text_2: str) -> str:
        """ Remove Duplicated Phrases

        Purpose:
        -   Any Phrase in Text_2 that exists in Text_1 will cause
            that phrase to be removed from Text_1

        Args:
            text_1 (str): the text to modify
            text_2 (str): the read-only text to use for removal

        Returns:
            str: the modified text_1 (if applicable)
        """

        if text_2 in text_1:
            text_1 = text_1.replace(text_2, '').strip()

        return text_1

    """
    TODO: Write Test
    @staticmethod
    def cartesian(matches: list) -> list:
        ---
        Purpose:
            Find a list of candidate token sequences within the normalized_input_text
        Time per Call:
            0.5ms < x 1.0ms
        :param matches:
            a list of 1..* tokens forming a match pattern
        :return:
            a list of possible token sequences
        ---
        from itertools import product

        cartesian = []
        for element in product(*matches):
            cartesian.append(element)

        return cartesian
    """
    @staticmethod
    def sliding_window(tokens: List[str],
                       window_size: int) -> Optional[List[str]]:
        """ Perform Sliding Window (e.g., n-gram) extraction over a list of tokens

        Args:
            tokens (List[str]): the incoming tokens
            window_size (int): the window (e.g., n-gram) size

        Returns:
            Optional[List[str]]: the outgoing tokens (if any)
        """

        if window_size > len(tokens):
            return None

        if window_size == len(tokens):
            return [tokens]

        results = []
        total_tokens = len(tokens)

        for i in range(total_tokens):

            buffer = []

            x = 0
            while x < window_size:

                pos = x + i
                if pos < total_tokens:
                    buffer.append(tokens[pos])

                x += 1

            if len(buffer) == window_size:
                results.append(buffer)
                buffer = []

        return results

    @staticmethod
    def most_similar_phrase(tokens_1: List[str],
                            tokens_2: List[str],
                            window_size: int,
                            score_threshold: float,
                            debug: bool = False) -> dict:
        """ Find the Most Similar Phrase in Tokens-2 relative to Tokens-1

        Implementation Note:
            How is this different from 'longest-common-phrase'?

            In the example below, there are no common sequences between tokens-1 and tokens-2
            This function will find "nearly similar" sequences and return the most similar

        Args:
            tokens_1 (list): the first tokenized list
                ['where', 'is', 'the', 'library', '?']
            tokens_2 (list): the second tokenized list
                ['I', 'understand', 'you', 'want', 'to', 'know', 'where', 'the', 'library', 'is', '.']
            window_size (int, Optional): n-Gram window size for comparison.
            score_threshold (float): when threshold is met, return the results (if any)
            debug (bool, Optional): When True, print results to console. default is False.

        Returns:
            the most similar span (list) with similarity score
        """

        tokens_1 = [x.lower().strip() for x in tokens_1]
        tokens_2 = [x.lower().strip() for x in tokens_2]

        t1 = TextUtils.sliding_window(
            tokens_1,
            window_size=window_size)

        t2 = TextUtils.sliding_window(
            tokens_2,
            window_size=window_size)

        d_results = {}

        for item_1 in [' '.join(x) for x in t1]:
            for item_2 in [' '.join(x) for x in t2]:

                if item_1 == item_2:
                    return {100: {'tokens_1': item_1, 'tokens_2': item_2}}

                score = TextUtils.jaccard_similarity(item_1, item_2)
                if debug:
                    print(f'({item_1}) vs. ({item_2}) = {score}')

                if score >= score_threshold:
                    d_results[score] = {'tokens_1': item_1, 'tokens_2': item_2}

        return d_results

    @staticmethod
    def longest_common_phrase(tokens_1: List[str],
                              tokens_2: List[str]) -> Optional[List[str]]:
        """ Find the Longest Common Phrase in Tokens-2 relative to Tokens-1

        Args:
            tokens_1 (list): the first tokenized list
                ['what', 'is', 'the', 'earliest', 'known', 'age', 'of', 'fossils', '?']
            tokens_2 (list): the second tokenized list
                ['the', 'earliest', 'known', 'age', 'of', 'fossils', 'is', '3.7', 'billion', 'years', 'old', '.']

        Returns:
            Optional[List[str]]: the common span (if any)
                ['the', 'earliest', 'known', 'age', 'of', 'fossils']
        """

        text_2 = ' '.join(tokens_2).strip()

        def extract(tokens: list,
                    gram_size: int) -> set:
            results = []

            if gram_size == len(tokens):
                return set([' '.join(x) for x in tokens])

            # Never call
            #if gram_size == 1:
            #    return set([' '.join(x) for x in tokens])

            x = 0
            y = x + gram_size

            while y <= len(tokens):
                results.append(tokens[x: y])

                x += 1
                y = x + gram_size

            return set([' '.join(x) for x in results])

        max_tokens = min([len(tokens_1), len(tokens_2)])

        while max_tokens > 2:

            extracts_1 = extract(tokens_1, max_tokens)
            extracts_2 = extract(tokens_2, max_tokens)

            common = extracts_1.intersection(extracts_2)
            if common:

                common_phrase = list(common)[0]
                if common_phrase not in text_2.lower():
                    return None

                x = text_2.lower().index(common_phrase)
                y = x + len(common_phrase)

                return text_2[x: y].split()

            max_tokens -= 1

        return None

    @ staticmethod
    def is_punctuation(char: str) -> bool:
        """ Checks whether `char` is a punctuation character.

        Args:
            char (str): any incoming character
                if the length of the parameter exceeds 1, this method will return False immediately

        Returns:
            bool: True if the character is punctuation
        """

        # not testing if 'has_punctuation'
        if len(char) > 1:
            return False

        cp = ord(char)

        # We treat all non-letter/number ASCII as punctuation.
        # Characters such as "^", "$", and "`" are not in the Unicode
        # Punctuation class but we treat them as punctuation anyways, for consistency.
        result = False
        if (cp >= 33 and cp <= 47) or (cp >= 58 and cp <= 64) or (cp >= 91 and cp <= 96) or (cp >= 123 and cp <= 126):
            result = True

        cat = category(char)
        if cat.startswith('P'):
            result = True

        return result

    @ staticmethod
    def has_punctuation(input_text: str):
        """Checks whether the input text has any punctuation characters."""

        for ch in input_text:
            if TextUtils.is_punctuation(ch):
                return True

        return False

    @ staticmethod
    def remove_punctuation(input_text: str):
        """Checks whether the input text has any punctuation characters."""

        buffer = []
        for ch in input_text:
            if not TextUtils.is_punctuation(ch):
                buffer.append(ch)

        return ''.join(buffer)

    @ staticmethod
    def find_subsumed_tokens(tokens: list) -> list:
        """ Find Subsumed Tokens (if any)

        Version:
            >= 0.1.6

        For Example:
            '1 pm' contains 'pm' thus '1 pm' subsumes (asorbs) 'pm'

        Reference:


        Args:
            tokens (list): the incoming tokens
            Sample Input:
                ['tomorrow', 'meeting', '1 pm', 'pm']

        Returns:
            list: the subsumed tokens (if any)
            Sample Output:
                ['pm']
        """

        def exists(item_1: str, item_2: str) -> bool:
            token_lr = f' {item_1} '
            if token_lr in item_2:
                return True

            token_l = f' {item_1}'
            if item_2.endswith(token_l):
                return True

            token_r = f'{item_1} '
            if item_2.startswith(token_r):
                return True

            return False

        pairs = []
        for i1 in tokens:
            for i2 in [x for x in tokens if i1 != x]:
                pairs.append(sorted({i1, i2}, reverse=False))

        excludes = set()
        for pair in pairs:
            if exists(pair[0], pair[1]):
                excludes.add(pair[0])

        if not len(excludes):
            return []

        return sorted(excludes)

    """
    TODO: Fail Test... Fix Test First
    def choose_random_line(input_text: str) -> str:
        ---
        Choose Random Line from Long Input String

        The function will segment the input text and if only one line exists, this will be returned
        if multiple lines exist, the function will randomly choose a single line, assuming the length
            of that line is near the mean

        Use Case:

            Assume the input text is:
                "Hi!  How are you doing?  I'm here to help you"

            This segments into three sentences:
                [
                    "Hi!",
                    "How are you doing?",
                    "I'm here to help you",
                ]

            Either of the last two sentences will be chosen

        Args:
            input_text (str): the incoming text string

        Returns:
            str: a random segment from the incoming text string
        ---

        def random_line(lines: list) -> Optional[str]:
            try:
                d = {len(x): x for x in lines}
                _mean = mean(d)
                lines = list(reversed(d.values()))
                for i in len(lines):
                    if len(lines[i]) >= _mean - 2:
                        return lines[i]

                return lines[0]
            except Exception:
                print(lines)
                raise ValueError

        lines = TextUtils.split_on_punctuation(input_text)
        if len(lines) == 1:
            return lines[0]
        return random_line(lines)
    """

    @ staticmethod
    def jaccard_similarity(x: str, y: str) -> float:
        """ returns the jaccard similarity between two lists

        Args:
            x (str): the first string to compare
            y (str): the second string to compare

        Raises:
            ValueError: final score is less than 0.0
            ValueError: final score is greater than 0.0
            ValueError: final score is not of type float

        Returns:
            float: the Jaccard similarity score (0.0 <= x <= 1.0)
        """
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        sim = intersection_cardinality / float(union_cardinality)
        result = round(sim, 3)

        # this is our contract to the consumer!
        if result < 0.0:
            raise ValueError
        if result > 1.0:
            raise ValueError
        if type(result) != float:
            raise ValueError

        return result

    @ staticmethod
    def split_on_len(input_text: str,
                     threshold: int = 7) -> Optional[str]:
        """Insert New Lines into Label Text
        This constrains the text to fit into a small box on a diagram

        Args:
            input_text (str): The text that will be displayed
            threshold (int, optional): The relative position to set a line break. Defaults to 7.

        Returns:
            Optional[str]: the input text with zero-or-more line breaks inserted
                only return None if the input is None
        """
        if input_text is None:
            return None

        if len(input_text) <= threshold:
            return input_text

        tokens = [x.strip() for x in input_text.split(' ')]

        master = []
        buffer = []
        for i in range(len(tokens)):
            buffer.append(tokens[i])

            temp = ' '.join(buffer).strip()
            if len(temp) >= threshold:
                master.append(temp)
                buffer = []

        if len(buffer):
            master.append(' '.join(buffer).strip())

        return sep.join(master).strip()

    @ staticmethod
    def ends_with_punctuation(input_text: str) -> bool:
        """ Determine if Input Text ends with punctuation

        Args:
            input_text (str): any input text of any length

        Returns:
            bool: True if punctuation ends the input text
        """
        if input_text is None or not len(input_text):
            return False

        return input_text[-1] in ['.', '?', '!']  # common ending punctuation

    @ staticmethod
    def remove_ending_punctuation(input_text: str) -> str:
        """ Remove Ending (terminating sequence) Punctuation

        Args:
            input_text (str): the input text of any length
            Sample Input:
                How are you doing?

        Returns:
            str: the input text with ending punctuation (if any) removed
            Sample Output:
                How are you doing
        """
        if TextUtils.ends_with_punctuation(input_text):
            return input_text[:-1]
        return input_text

    @ staticmethod
    def split_on_punctuation(input_text: str,
                             punkt: list = ['!', '?']) -> list:
        """ Split (segment) a line on common punctuation

        Args:
            input_text (str): the input text of any length
            punkt (list, optional): the punctuation to split on. Defaults to ['!', '?'].

        Returns:
            list: the split (segmented) input text
        """

        for p in punkt:
            input_text = input_text.replace(p, '.')

        lines = input_text.split('.')
        lines = [x.strip() for x in lines]
        lines = [x for x in lines if x and len(x)]

        return lines

    @ staticmethod
    def update_spacing(input_text: str) -> str:
        """ Correct Syntactical Spacing Inconsistencies

        Args:
            input_text (str): the input text of any length

        Returns:
            str: the corrected input string
        """
        input_text = input_text.replace(' !', '!')
        input_text = input_text.replace('.?', '?')
        input_text = input_text.replace('.!', '!')
        input_text = input_text.replace('. .', '. ').strip()

        while '  ' in input_text:
            input_text = input_text.replace('  ', ' ')

        return input_text

    @ staticmethod
    def remove_double_spaces(input_text: str) -> str:
        """ Remove Double Spaces in a String

        Args:
            input_text (str): the input text of any length

        Returns:
            str: the corrected input string
        """
        while '  ' in input_text:
            input_text = input_text.replace('  ', ' ')

        return input_text

    @ staticmethod
    def update_csvs(input_text: str) -> str:
        """ Synatically correct Comma Separated values in Natural Language
        TODO Write Test
        Samples:
            1.  Input:      meetings, presentations and speeches
                Output:     meetings, presentations, and speeches
            2.  Input:      the telephone, and electronic mail
                Output:     the telephone and electronic mail

        Args:
            input_text (str): the input text of any length

        Returns:
            str: the corrected input string
        """
        return input_text

    @ staticmethod
    def update_determiners(input_text: str) -> str:
        """ Update Determiners in a text string

        Args:
            input_text (str): the input text of any length
            Sample Input:
                "I see a elephant!"

        Returns:
            str: the corrected input string
            Sample Output:
                "I see an elephant!"
        """
        if ' ' not in input_text:
            return input_text

        results = []
        tokens = input_text.split(' ')

        for i in range(len(tokens)):

            def use_an() -> bool:
                if tokens[i].lower() != 'a':
                    return False

                if i + 1 >= len(tokens):
                    return False

                return TextUtils.startswith_vowel(tokens[i + 1])

            def an() -> str:
                if tokens[i].isupper():
                    return 'An'
                return 'an'

            if use_an():
                results.append(an())
            else:
                results.append(tokens[i])

        return ' '.join(results).strip()

    @ staticmethod
    def startswith_vowel(input_text: str) -> str:
        """ Determine if Input Text starts with a vowel

        Args:
            input_text (str): the input text of any length

        Returns:
            str: True if the input text does start with a vowel
        """
        vowels = ['a', 'e', 'i', 'o', 'u']

        if input_text[0] in ["'", '"'] and len(input_text) > 1:
            return input_text[1].lower() in vowels

        return input_text[0].lower() in vowels

    @ staticmethod
    def lower_case(input_text: str) -> str:
        """ Perform Lower Casing on Input

        Args:
            input_text (str): the input text of any length
            Sample Input:
                'The Quick Brown Fox Jumped OVER the Lazy Dog'

        Returns:
            str: the corrected input string
            Sample Output:
                'the quick brown fox jumped over the lazy dog'
        """
        if ' ' not in input_text:
            return input_text.lower()

        tokens = [x.lower() for x in input_text.split(' ')]

        return ' '.join(tokens).strip()

    @ staticmethod
    def sentence_case(input_text: str) -> str:
        """ Perform Sentence Casing on Input

        Args:
            input_text (str): the input text of any length
            Sample Input:
                'the quick brown fox jumped over the lazy dog'

        Returns:
            str: the corrected input string
            Sample Output:
                'The quick brown fox jumped over the lazy dog'
        """
        def case(value: str) -> str:
            return f'{value[:1].upper()}{value[1:]}'

        if ' ' not in input_text:
            return case(input_text)

        def conditional_case(value: str) -> str:

            # careful not to lowercase an acronym ...
            result = value
            if len(value) > 1 and not value.isupper():
                result = value.lower()

            return result

        tokens = input_text.split(' ')
        results = \
            [case(tokens[0])] + \
            [conditional_case(x) for x in tokens[1:]]

        return ' '.join(results).strip()

    @ staticmethod
    def title_case(input_text: str) -> str:
        """ Perform Title Casing on Input

        Args:
            input_text (str): the input text of any length
            Sample Input:
                'the quick brown fox jumped over the lazy dog'

        Returns:
            str: the corrected input string
            Sample Output:
                'The Quick Brown Fox Jumped Over the Lazy Dog'
        """
        def case(value: str) -> str:
            return f'{value[:1].upper()}{value[1:]}'

        def conditional_case(value: str) -> str:
            if value.lower().strip() in STOPWORDS:

                # careful not to lowercase an acronym ...
                if len(value) > 1 and not value.isupper():
                    return value.lower()

            return case(value)

        if ' ' not in input_text:
            return case(input_text)

        tokens = input_text.split(' ')
        results = \
            [case(tokens[0])] + \
            [conditional_case(x) for x in tokens[1:]]

        return ' '.join(results).strip()
