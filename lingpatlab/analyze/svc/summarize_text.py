# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Summarize Text based on Extracted Patterns """


from typing import List, Optional
from baseblock import BaseObject, CryptoBase, Enforcer
from openai import OpenAI
from lingpatlab.analyze.dto import (
    generate_prompt,
    generate_sample_prompt,
    SAMPLE_OUTPUT,
    SYSTEM_PROMPT_SUMMARY,
)

decrypt_str = CryptoBase().decrypt_str


class SummarizeText(BaseObject):
    """ Summarize Text based on Extracted Patterns """

    __client = None
    __api_key = decrypt_str(
        'gAAAAABjxO3Q7tB8owXW8SGTBPQfd1qRumPCAkucg0Hq9oeTE5v2V7wVFbnMRcFOf9GA1UcqLcAPXiRBK2KW7Cce0ws7ZkGFEylxKTsivvRngv9l9am7MjEcAV6VXpmiU-J3NCHzbQHkFc6TsXG5wuSj3OrjDVPtLw==')
    __org_key = decrypt_str(
        'gAAAAABjxO38JjDj6YiBcOYoG5QeePp6Pv5nhiBBK_TDHeyS6nu9yMl_8zDY1UQAVy5n5ybZtvJ8kcXVMfHuTymCgEXfJWgN7PHSkFA0xWmx6ZqMbXCPLAI=')

    def __init__(self):
        """ Change Log:

        Created:
            28-Feb-2024
            craigtrim@gmail.com
            *   in pursuit of
                https://github.com/craigtrim/datapipe-apis/issues/44
        Updated:
            27-Mar-2024
            craigtrim@gmail.com
            *   add type-checking on i/o
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                input_text: str) -> str:
        """
        Process the input text and generate a summary using the OpenAI GPT-3.5 Turbo model.

        Args:
            input_text (str): The input text to be summarized.

        Returns:
            str: The generated summary.

        Raises:
            TypeError: If the input_text is not a string.

        """
        if self.isEnabledForDebug:
            Enforcer.is_str(input_text)

        if not self.__client:
            self.__client = OpenAI(
                api_key=self.__api_key,
                organization=self.__org_key)

        user_prompt = generate_prompt(input_text)

        completion = self.__client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT_SUMMARY},
                {"role": "user", "content": generate_sample_prompt()},
                {"role": "assistant", "content": SAMPLE_OUTPUT},
                {"role": "user", "content": user_prompt}
            ]
        )

        result = completion.choices[0].message.content

        if self.isEnabledForDebug:
            Enforcer.is_str(result)

        return result
