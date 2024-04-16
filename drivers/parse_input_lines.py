# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import List
from baseblock import FileIO, Stopwatch
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentence, Sentences


def test_service():

    sw = Stopwatch()

    api = LingPatLab()
    assert api

    file_path = FileIO.join(FileIO.local_directory(), 'visual_thinking.json')
    FileIO.exists_or_error(file_path)

    d_file = FileIO.read_json(file_path)
    d_output = {}

    for key in d_file:

        print()
        print(key, str(sw))

        input_lines = d_file[key].split('\n\n')
        input_lines = [
            x.strip() for x in input_lines
            if x and len(x.strip())
        ]

        sentences: Sentences = api.parse_input_lines(input_lines)

        line_output = []
        for sentence in sentences:
            for token in sentence:
                line_output.append([
                    token.dep,
                    token.ent,
                    token.normal,
                    token.pos
                ])

        d_output[key] = line_output

    output_path = FileIO.join(FileIO.local_directory(),
                              'visual_thinking_results.json')

    FileIO.write_json(data=d_output, file_path=output_path)


def main():
    test_service()


if __name__ == "__main__":
    main()
