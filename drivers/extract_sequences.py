# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint
from itertools import product
from typing import List
from lingpatlab.baseblock import FileIO, Stopwatch
from lingpatlab import LingPatLab


def extract_sequences(sentence: List[List[str]], pattern: List[str]) -> List[List[str]]:
    """
    Extract sequences from the given data based on the provided pattern.

    Args:
        data (List[List[str]]): The input data in List[List[str]] format.
        pattern (str): The pattern to match.

    Returns:
        List[List[str]]: List of sequences that match the given pattern.
    """
    matching_sequences = []

    for i, token in enumerate(sentence):
        if token[-1] != pattern[0]:
            continue

        if len(pattern) + i >= len(sentence):
            continue

        def has_match() -> bool:
            for j in range(len(pattern)):

                if pattern[j] == '*':
                    continue

                elif pattern[j] in ['NOUN', 'PROPN']:
                    if sentence[i + j][-1] not in ['NOUN', 'PROPN']:
                        return False

                if pattern[j] == 'PUNCT' and sentence[i + j][2] != '-':
                    return False

                elif pattern[j] != sentence[i + j][-1]:
                    return False

            return True

        if has_match():
            matching_sequences.append(' '.join([
                token[2] for token in sentence[i:i+len(pattern)]
            ]).strip())

    return matching_sequences


def expand_pattern(pattern: str) -> List[str]:
    """
    Expand the given pattern by repeating tokens followed by '+' up to 4 times.

    Args:
        pattern (str): The pattern to expand.

    Returns:
        List[str]: List of expanded patterns.
    """
    expanded_patterns = []

    # Split the pattern into parts
    pattern_parts = pattern.split()

    # Iterate through each part
    for part in pattern_parts:
        if '+' in part:
            # If part contains '+', split it and expand
            token, repeat = part.split('+')
            # min(4, int(repeat))  # Limit repetition to 4 times
            repeat = int(repeat)
            expanded_part = [' '.join([token] * i)
                             for i in range(1, repeat + 1)]
            expanded_patterns.append(expanded_part)
        else:
            # If part doesn't contain '+', keep it unchanged
            expanded_patterns.append([part])

    # Get all combinations of expanded parts
    all_combinations = product(*expanded_patterns)

    # Join combinations into strings and append to the result list
    result = [' '.join(combination) for combination in all_combinations]

    return result


def reduce_strings(string_list):
    """
    Reduce the list of strings by removing strings that are contained by another string.

    Args:
        string_list (List[str]): The list of strings.

    Returns:
        List[str]: The reduced list of strings.
    """

    # Convert the list to a set for efficient membership testing
    string_set = set(string_list)

    reduced_list = []

    # Iterate through each string in the original list
    for string in string_list:
        # Check if any other string in the set contains the current string
        if any(s != string and string in s for s in string_set):
            continue
        else:
            # If the string is not contained by any other string, add it to the reduced list
            reduced_list.append(string)

    return reduced_list


def test_service():

    sw = Stopwatch()

    api = LingPatLab()
    assert api

    file_path = FileIO.join(FileIO.local_directory(),
                            'visual_thinking_results.json')
    FileIO.exists_or_error(file_path)

    d_parsed = FileIO.read_json(file_path)

    patterns = [
        "NOUN NOUN NOUN+2",
        "ADJ ADJ+2 NOUN+3",
        "VERB VERB+2 NOUN+3",
        "NOUN * VERB CCONJ VERB",
        "NOUN * ADV CCONJ ADV",
        "VERB * NOUN CCONJ NOUN",
        "ADJ PUNCT NOUN+4",
        "ADJ NOUN ADP VERB NOUN",
    ]

    # d_master = {}
    d_matches = {}

    for original_pattern in patterns:

        for pattern in expand_pattern(original_pattern):

            for key in d_parsed:
                sentence = d_parsed[key]

                results = extract_sequences(
                    sentence=sentence, pattern=pattern.split())

                if not results or not len(results):
                    continue

                _key = f"{key}-{original_pattern}"
                if key not in d_matches:
                    d_matches[key] = []

                d_matches[key].append(results)

        d_matches = {
            key: [
                reduce_strings(x) for x in d_matches[key]
            ] for key in d_matches
        }

    pprint(d_matches)


def main():
    test_service()


if __name__ == "__main__":
    main()
