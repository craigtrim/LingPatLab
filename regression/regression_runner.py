# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import List
from lingpatlab import LingPatLab, Sentence
from baseblock import BaseObject, FileIO


class RegressionRunner(BaseObject):
    """ Run Regression Suite """

    def __init__(self):
        """ Change Log

        Created:
            27-Mar-2024
            craigtrim@gmail.com
            *   https://github.com/craigtrim/datapipe-apis/issues/71
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                input_number: str,
                show_parse_output: bool = False) -> None:

        api = LingPatLab()

        output_path = FileIO.join_cwd('regression/outputs')
        FileIO.exists_or_error(output_path)

        input_path = FileIO.join_cwd('regression/inputs')
        FileIO.exists_or_error(input_path)

        input_files = FileIO.load_all_files(directory=input_path)['txt']
        self.logger.info(f"Loaded {len(input_files)} files from {input_path}")

        def filter_input_files() -> List[str]:
            if input_number is None or input_number == '*':
                return input_files

            if not input_number.isnumeric():
                raise ValueError(input_number)

            return [
                input_file for input_file in input_files
                if f"{input_number}.txt" in input_file
            ]

        filtered_input_files = filter_input_files()

        if not filtered_input_files:
            self.logger.warning(
                f"No Input Files found for {input_number} from {input_files}")
            return None

        if len(filtered_input_files) == 1:
            show_parse_output = True

        for input_file in filter_input_files():

            def get_parse_type() -> str:
                file_name = FileIO.get_file_name(input_file).lower()
                if 'person-' in file_name or 'people-' in file_name:
                    return 'people'
                elif 'topics-' in file_name:
                    return 'topics'
                raise NotImplementedError(file_name)

            input_text = FileIO.read_string(input_file)
            parse_type = get_parse_type()

            def parse_text() -> List[str]:
                sentence: Sentence = api.parse_input_text(input_text)

                if show_parse_output:
                    for token in sentence:
                        print(
                            f"Text=`{token.text}`, POS=`{token.pos}`, ENT=`{token.ent}`")

                if parse_type == 'people':
                    return api.extract_people(sentence)
                elif parse_type == 'topics':
                    return api.extract_topics(sentence)
                else:
                    raise NotImplementedError(parse_type)

            def get_expected_entities() -> List[str]:
                output_file = FileIO.join(
                    output_path, f"{FileIO.get_file_name(input_file)}.json")
                FileIO.exists_or_error(output_file)
                return FileIO.read_json(output_file)

            d_expected_entities = get_expected_entities()
            expected_keys = sorted(d_expected_entities.keys())

            d_actual_entities = parse_text()
            self.logger.debug(
                f"Processed: {input_file}\nEntities: {d_actual_entities}")

            if not d_actual_entities and not d_expected_entities:
                self.logger.info(f"Success: {input_file}")
                continue

            if not d_actual_entities:
                self.logger.error(
                    f"No Entities Extracted: {input_file}\nExpected: {expected_keys}")
                break

            actual_keys = sorted(d_actual_entities.keys())

            if actual_keys != expected_keys:
                self.logger.error(
                    f"Key Failure: {input_file}\nExpected: {expected_keys}\nActual: {actual_keys}")
                break

            for actual_key in actual_keys:
                if sorted(d_actual_entities[actual_key]) != sorted(d_expected_entities[actual_key]):
                    self.logger.error(
                        f"Value Failure (Type 1): {input_file}\nExpected: {d_expected_entities[actual_key]}\nActual: {d_actual_entities[actual_key]}")
                    break

            for expected_key in expected_keys:
                if sorted(d_actual_entities[expected_key]) != sorted(d_expected_entities[expected_key]):
                    self.logger.error(
                        f"Value Failure (Type 2): {input_file}\nExpected: {d_expected_entities[expected_key]}\nActual: {d_actual_entities[expected_key]}")
                    break

            self.logger.info(f"Success: {input_file}")


def main(input_number):
    RegressionRunner().process(input_number)


if __name__ == "__main__":
    import plac

    plac.call(main)
