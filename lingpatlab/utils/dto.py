from typing import List, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class OtherInfo:
    """
    Represents additional information associated with a token processed by Spacy.
    This includes both the token's own information and its relationship to the "head" token in dependency parsing.

    Attributes:
        i (int): The token's index in the sentence.
        idx (int): Duplicate of `i` for convenience, representing the token's index.
        orth (int): The orthographic representation of the token, typically used as a hash value.
        head_i (int): The index of the token's head in dependency parsing.
        head_idx (int): Duplicate of `head_i`, for consistency with token indexing attributes.
        head_orth (int): The orthographic representation (hash) of the head token.
        head_text (str): The textual representation of the head token.
    """
    i: int
    idx: int
    orth: int
    head_i: int
    head_idx: int
    head_orth: int
    head_text: str


@dataclass
class SpacyResult:
    """
    Represents a token parsed by a custom Spacy parser, encapsulating various linguistic features.

    Relationships:
        - Each SpacyResult contains exactly one OtherInfo instance, detailing further morphological and dependency information.

    Attributes:
        id (str): Unique identifier for the token.
        text (str): The actual text of the token.
        tense (str): The tense of the token, if applicable.
        noun_number (str): Singular or plural for nouns.
        verb_form (str): The form of the verb (e.g., base, past).
        sentiment (float): Sentiment score associated with the token.
        pos (str): Part of speech.
        tag (str): Detailed part-of-speech tag.
        dep (str): Syntactic dependency relation.
        ent (str): Named entity type, if any.
        shape (str): The shape representation of the token (e.g., "Xxxx" for capitalization).
        is_alpha (bool): Whether the token is alphabetic.
        is_stop (bool): Whether the token is a stop word.
        head (str): The textual representation of the token's syntactic head.
        other (OtherInfo): Additional information about the token.
        is_punct (bool): Whether the token is punctuation.
        x (int), y (int): Coordinates for graphical representation or spatial analysis.
        is_wordnet (bool): Whether the token is found in WordNet.
        normal (str): The normalized form of the token.
        stem (str): The stemmed version of the token.

    Methods:
        to_string: Returns a simplified string representation combining text and POS.
        is_noun: Determines if the token is a noun (common or proper).
        is_hyphen: Checks if the token is a hyphen.
    """
    id: str
    text: str
    tense: str
    noun_number: str
    verb_form: str
    sentiment: float
    pos: str
    tag: str
    dep: str
    ent: str
    shape: str
    is_alpha: bool
    is_stop: bool
    head: str
    other: OtherInfo
    is_punct: bool
    x: int
    y: int
    is_wordnet: bool
    normal: str
    stem: str

    def to_string(self) -> str:
        """Returns a simplified string representation combining text and POS."""
        text_pos = f"{self.text.strip()}/{self.pos.upper()}"
        if len(self.ent):
            return f"{text_pos}/{self.ent.upper()}"
        return text_pos

    def is_noun(self) -> bool:
        """Determines if the token is a noun (common or proper)."""
        return self.pos.upper() in ['NOUN', 'PROPN']

    def is_hyphen(self) -> bool:
        """Checks if the token is a hyphen."""
        return self.text.strip() == '-'

    def to_json(self) -> dict:
        return asdict(self)


def to_spacy_result(data: Dict[str, Any]) -> SpacyResult:
    other_info_data = data.pop('other')
    other_info = OtherInfo(**other_info_data)
    return SpacyResult(other=other_info, **data)


@dataclass
class Sentence:
    """
    Represents a sentence composed of multiple SpacyResult tokens.

    Relationships:
        - A Sentence consists of one or more SpacyResult instances, each representing a parsed token.

    Attributes:
        tokens (List[SpacyResult]): The list of tokens (SpacyResult instances) that make up the sentence.

    Methods:
        to_string: Returns a string representation of the sentence, showing each token's text and POS.
        sentence_text: Concatenates the text of all tokens into a single string representing the sentence.
        size: Returns the number of tokens in the sentence.
    """
    tokens: List[SpacyResult]

    def __post_init__(self):
        if not isinstance(self.tokens, list):
            raise TypeError(
                f"Tokens must be 'List[SpacyResult]', got {type(self.tokens)}")
        for token in self.tokens:
            if not isinstance(token, SpacyResult):
                raise TypeError(
                    f"All tokens must be of type 'SpacyResult', got {type(token)}")

    def __iter__(self):
        return iter(self.tokens)

    def to_string(self) -> str:
        """Returns a string representation of the sentence, showing each token's text and POS."""
        return ' '.join([token.to_string() for token in self.tokens])

    def sentence_text(self) -> str:
        """Concatenates the text of all tokens into a single string representing the sentence."""
        return ''.join([token.text for token in self.tokens])

    def size(self) -> int:
        """Returns the number of tokens in the sentence."""
        return len(self.tokens)

    def to_json(self) -> list:
        return [
            token.to_json() for token in self.tokens
        ]


@dataclass
class Sentences:
    """
    Represents a collection of Sentence instances, effectively modeling a paragraph or a collection of sentences.

    Relationships:
        - Consists of one or more Sentence instances, each representing a parsed sentence.

    Attributes:
        sentences (List[Sentence]): The list of Sentence instances in the collection.

    Methods:
        to_string: Returns a string representation of all sentences, separated by new lines.
        sentence_text: Concatenates the text of all sentences into a single string, with sentences separated by new lines.
        size: Returns the number of Sentence instances in the collection.
    """
    sentences: List[Sentence]

    def __post_init__(self):
        if not isinstance(self.sentences, list):
            raise TypeError(
                f"Tokens must be 'List[Sentence]', got {type(self.sentences)}")
        for sentence in self.sentences:
            if not isinstance(sentence, Sentence):
                raise TypeError(
                    f"All tokens must be of type 'Sentence', got {type(sentence)}")

    def __iter__(self):
        return iter(self.sentences)

    def to_string(self):
        """Returns a string representation of all sentences, separated by new lines."""
        return '\n\n'.join([sentence.to_string() for sentence in self.sentences])

    def sentence_text(self) -> str:
        """Concatenates the text of all sentences into a single string, with sentences separated by new lines."""
        return [
            sentence.sentence_text()
            for sentence in self.sentences
        ]

    def size(self) -> int:
        """Returns the number of Sentence instances in the collection."""
        return len(self.sentences)

    def to_json(self) -> list:
        return [
            sentence.to_json() for sentence in self.sentences
        ]


def transform_parse_results_to_sentences(parse_results: list) -> Sentences:
    """ Assumes that a prior instance of Sentences was persisted to file using <Sentences>.to_json()
    this will restore the json form to a Sentences instance
    """
    sentence_results = []
    for _sentence in parse_results:
        spacy_results = []
        for _token in _sentence:
            spacy_results.append(SpacyResult(**_token))
        sentence_results.append(Sentence(spacy_results))
    return Sentences(sentence_results)


@dataclass
class SentencePhrases:
    """
    Contains a Sentence instance and a list of phrases extracted from that sentence.

    Relationships:
        - Directly associated with one Sentence instance.

    Attributes:
        sentence (Sentence): The Sentence from which phrases are extracted.
        phrases (List[str]): The extracted phrases from the sentence.
    """
    sentence: Sentence
    phrases: List[str]

    def __post_init__(self):
        if not isinstance(self.sentence, Sentence):
            raise TypeError(
                f"Tokens must be 'Sentence', got {type(self.sentence)}")
        if not isinstance(self.phrases, list):
            raise TypeError(
                f"Tokens must be 'List[str]', got {type(self.phrases)}")
        for phrase in self.phrases:
            if not isinstance(phrase, str):
                raise TypeError(
                    f"All phrases must be of type 'str', got {type(phrase)}")
