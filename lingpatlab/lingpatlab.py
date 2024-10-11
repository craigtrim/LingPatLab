# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" API for spaCy Core Functionality """


from spacy.lang.en import English

from lingpatlab.baseblock import (
    BaseObject,
    Stopwatch,
    Enforcer
)

from lingpatlab.tokenizer.bp import Tokenizer
from lingpatlab.parser.svc import ParseInputTokens

from lingpatlab.analyze.bp import (
    ExtractTopics,
    ExtractPeople
)

from lingpatlab.utils.dto import (
    Sentence,
    Sentences
)


class LingPatLab(BaseObject):
    """
    Provides an API interface for core functionalities of a spaCy-based NLP pipeline, including tokenization,
    parsing, phrase extraction, and summarization of input text.

    This API orchestrates the workflow from raw text to structured data representations suitable for further NLP tasks.
    """

    __tokenize = None
    __parse = None
    __topics = None
    __people = None
    __summarize = None

    def __init__(self):
        """
        Initializes the SpacyCoreAPI by setting up the base object and preparing internal components for NLP tasks.

        Created:
            27-Feb-2024
            craigtrim@gmail.com
            *   https://github.com/craigtrim/datapipe-apis/issues/43
        Updated:
            19-Mar-2024
            craigtrim@gmail.com
            *   https://github.com/craigtrim/datapipe-apis/issues/61
        """
        BaseObject.__init__(self, __name__)

    def extract_people(self,
                       sentences: Sentence | Sentences) -> list[str]:
        """
        Extracts people from the given sentences.

        Args:
            sentences (Union[Sentence, Sentences]): The input sentences from which to extract people.

        Returns:
            List[str]: A list of extracted people names.

        Raises:
            TypeError: If the input sentences are not of type Sentence or Sentences.
        """
        if not self.__people:
            self.__people = ExtractPeople().process

        if type(sentences) == Sentence:
            sentences = Sentences([sentences])

        if not type(sentences) == Sentences:
            raise TypeError(type(sentences))

        return self.__people(sentences=sentences)

    def extract_topics(self,
                       sentences: Sentence | Sentences = None) -> list[str]:
        """
        Extracts phrases from the given structured Sentences object, which is a collection of parsed sentences.

        Parameters:
            sentences (Union[Sentence, Sentences]): A structured collection of sentences to extract phrases from.

        Returns:
            List[str]: A list of extracted phrases.
        """
        if not self.__topics:
            self.__topics = ExtractTopics().process

        if type(sentences) == Sentence:
            sentences = Sentences([sentences])

        if not type(sentences) == Sentences:
            raise TypeError(type(sentences))

        return self.__topics(sentences=sentences)

    def parse_input_text(self,
                         input_text: str,
                         en_spacy_model: English | None = None) -> Sentence:
        """
        Parses the given input text into a structured Sentence object, encapsulating the parsed tokens and their relations.

        Parameters:
            input_text (str): The text to parse.

        Returns:
            Sentence: A structured representation of the parsed sentence.

        Raises:
            TypeError: If the input_text is not a string.
        """
        if not isinstance(input_text, str):
            raise TypeError(type(input_text))

        sw = Stopwatch()

        if not self.__tokenize:
            self.__tokenize = Tokenizer().input_text

        if not self.__parse:
            self.__parse = ParseInputTokens(en_spacy_model).process

        input_tokens: list[str] = self.__tokenize(input_text)
        parse_results: Sentence = self.__parse(input_tokens)

        if self.isEnabledForDebug:
            self.logger.debug(
                f"Parse Completed (total-results = {parse_results.size()}), (total-time = {str(sw)})")

        return parse_results

    def parse_input_lines(self,
                          input_lines: list[str],
                          en_spacy_model: English | None = None) -> Sentences:
        """
        Parses a list of input lines (strings), each into a Sentence object, and returns them as a Sentences object.

        This function is ideal for parsing multiple sentences or lines of text, providing a structured representation for each.

        Parameters:
            input_lines (List[str]): A list of strings, each representing a line of text to parse.

        Returns:
            Sentences: A collection of Sentence objects parsed from the input lines.

        Raises:
            TypeError: If the input_lines is not a list of strings.
        """
        if not isinstance(input_lines, list):
            raise TypeError(type(input_lines))

        sentences = []

        for input_text in input_lines:
            sentences.append(self.parse_input_text(
                input_text=input_text,
                en_spacy_model=en_spacy_model
            ))

        return Sentences(sentences)
