from typing import List

# from .text_summary_prompts import (
#     SYSTEM_PROMPT_SUMMARY,
#     SYSTEM_PROMPT_TEMPLATE_1,
#     SYSTEM_PROMPT_TEMPLATE_2,
#     SAMPLE_ORIGINAL_TEXT,
#     SAMPLE_PHRASES,
#     SAMPLE_OUTPUT,
#     generate_prompt,
#     generate_sample_prompt,
# )

from .text_summary_prompts_2 import (
    SYSTEM_PROMPT_SUMMARY,
    SYSTEM_PROMPT_TEMPLATE,
    SAMPLE_ORIGINAL_TEXT,
    SAMPLE_OUTPUT,
    generate_sample_prompt,
    generate_prompt,
)


def filter_title_phrases(phrases: List[str]) -> List[str]:
    """
    Cleanses a list of phrases by removing possessive suffixes and filtering out phrases that are not capitalized.

    Args:
        phrases (List[str]): A list of phrases to be cleansed.

    Returns:
        List[str]: A list of cleansed phrases.

    """
    def cleanse(input_text: str) -> str:
        if input_text[-2:] == "'s":
            return input_text[:-2]
        return input_text

    phrases = [
        cleanse(phrase) for phrase in phrases
    ]

    def all_upper(phrase: str) -> bool:
        return sum([
            (token[0].isupper() or token.isnumeric()) and len(token) > 1
            for token in phrase.split()
        ]) == len(phrase.split())

    def acceptable_title_case(phrase: str) -> bool:
        tokens = phrase.split()
        if len(tokens) < 3:
            return False

        for token in tokens:
            if token == 'of':
                continue
            if not token[0].isupper():
                return False

        return True

    phrases = [
        phrase for phrase in phrases
        if all_upper(phrase) or acceptable_title_case(phrase)
    ]

    return phrases
