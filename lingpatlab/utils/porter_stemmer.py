class PorterStemmer:
    def __init__(self):
        self._vowels = 'aeiou'
        self._step1_suffixes = ['sses', 'ies', 'ss', 's']
        self._step2_suffixes = ['eed', 'ed', 'ing']
        self._step3_suffixes = ['at', 'bl', 'iz']
        self._step4_suffixes = ['ational', 'tional', 'enci', 'anci', 'izer', 'bli', 'alli', 'entli', 'eli', 'ousli',
                                'ization', 'ation', 'ator', 'alism', 'iveness', 'fulness', 'ousness', 'aliti', 'iviti',
                                'biliti', 'logi']
        self._step5a_suffixes = ['icate', 'ative',
                                 'alize', 'iciti', 'ical', 'ful', 'ness']
        self._step5b_suffixes = ['al', 'ance', 'ence', 'er', 'ic', 'able', 'ible', 'ant', 'ement', 'ment', 'ent',
                                 'ou', 'ism', 'ate', 'iti', 'ous', 'ive', 'ize']

    def _get_measure(self, word: str) -> int:
        """Calculate the measure m of a word."""
        vowels = self._vowels
        word = word.lower()
        num_vowels = sum((char in vowels) for char in word)
        measure = 0
        prev_char_was_vowel = False
        for char in word:
            if char in vowels:
                if not prev_char_was_vowel:
                    measure += 1
                    prev_char_was_vowel = True
            else:
                prev_char_was_vowel = False
        return num_vowels, measure

    def _replace_suffix(self, word: str, suffix: str, replacement: str) -> str:
        """Replace a suffix of a word if the measure of the resulting word is > 0."""
        if word.endswith(suffix):
            stem = word[:-len(suffix)]
            if self._get_measure(stem)[1] > 0:
                return stem + replacement
        return word

    def stem(self, word: str) -> str:
        """Stem a word using the Porter Stemmer algorithm."""
        if len(word) <= 2:
            return word

        # Step 1
        for suffix in self._step1_suffixes:
            if word.endswith(suffix):
                return self._replace_suffix(word, suffix, '')

        # Step 2
        if word.endswith('y'):
            stem = word[:-1]
            if self._get_measure(stem)[1] > 0:
                return stem + 'i'
            else:
                return word
        for suffix in self._step2_suffixes:
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self._get_measure(stem)[1] > 0:
                    return stem
                else:
                    return word

        # Step 3
        for suffix in self._step3_suffixes:
            if word.endswith(suffix):
                return self._replace_suffix(word, suffix, 'e')

        # Step 4
        for suffix in self._step4_suffixes:
            if word.endswith(suffix):
                return self._replace_suffix(word, suffix, '')

        # Step 5a
        for suffix in self._step5a_suffixes:
            if word.endswith(suffix):
                return self._replace_suffix(word, suffix, '')

        # Step 5b
        for suffix in self._step5b_suffixes:
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self._get_measure(stem)[1] > 1:
                    return stem
                else:
                    return word

        return word
