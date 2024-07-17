from .utils import *
from .parser import *
from .tokenizer import *
from .analyze import *

from .utils.dto import Sentences
from .lingpatlab import LingPatLab
from .segmenter import Segmenter


from typing import List
from lingpatlab.baseblock import Enforcer


def tokenize_input_text(input_text: str) -> List[str]:
    """
    Tokenizes the input text into sentences.

    Args:
        input_text (str): The input text to be tokenized.

    Returns:
        List[str]: A list of sentences.

    Raises:
        TypeError: If the input_text is not a string.
        TypeError: If the sentences are not a list of strings.
    """
    Enforcer.is_str(input_text)

    sentences: List[str] = Tokenizer().input_text(input_text)

    Enforcer.is_list_of_str(sentences)

    return sentences


def segment_input_text(input_text: str) -> List[str]:
    """
    Segments the input text into sentences.

    Args:
        input_text (str): The input text to be segmented.

    Returns:
        List[str]: A list of segmented sentences.

    Raises:
        TypeError: If the input_text is not a string.

    """
    Enforcer.is_str(input_text)

    sentences: List[str] = Segmenter().input_text(input_text)

    Enforcer.is_list_of_str(sentences)

    return sentences
