# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from typing import List, Dict
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentences
from lingpatlab.analyze.bp import ExtractTopics


class ExtractSequencesTest(unittest.TestCase):

    def test_service(self):

        api = LingPatLab()
        assert api

        bp = ExtractTopics()
        assert bp

        input_text = """
        "006-039": "VISUALIZING RISK TO PREVENT DISASTERS. More recently, it has come to light that the rollout of 5G cell phone service has brought about concerns. I thought, 5G cell service is already in use in Europe, and there have been no issues. However, in a transportation system where human lives are at stake, such an oversight could create enormous vulnerability. What if a hacker took control and commanded electric trains to crash into each other?\n\nFor the same reason, self-driving cars must be hacker-proof with a mechanical kill switch accessible to the driver in an emergency and not connected to the internet. After the computer is disabled, the car should have a mechanical emergency brake and be steerable so the driver can get it off the road. I think we've become so reliant on computers and blindly trusting of them that we no longer see the inherent dangers. In a literal way, they are hidden from us unless you're the kid who loves taking them apart. Most of us have no idea how our devices work. To most people, the internet is an abstraction. That's dangerous. The United States might be a risk to aviation safety. Signals from 5G cell phones and cell towers may interfere with radar altimeters on airplanes. These devices enable airplanes to safely land during foggy weather when the pilot cannot see the runway. For safety, the altitude measurements must be very accurate. Safety issues, so why all the fuss in the United States? What is different? Pictures again flashed into my imagination. I see an aircraft taking off from New York and flying to Paris. The same aircraft is flying around in both the United States and Europe. Both the US and Europe use a system called frequency sharing for 5G service, which allows many users to be on the same frequency simultaneously.\nMy mind then saw pictures of some of the standards I have written for animal welfare, such as the North American Meat Institute's Recommended Animal Handling Guidelines and Audit Guide. That's how my mind associated the idea of standards. Maybe there is a difference in the standards for managing radio-frequency use in Europe and the United States. I looked for standards and found a paper by Maria Massaro of Chalmers University of Technology in Sweden that explained the difference. It became clear that the.\n",
        """

        input_lines = input_text.split('\n\n')
        input_lines = [
            input_line.strip() for input_line in input_lines
            if input_line and len(input_line)
        ]

        sentences: Sentences = api.parse_input_lines(input_lines)
        assert isinstance(sentences, Sentences)

        phrases: Dict[str, List[str]] = bp.process(sentences)
        print(phrases)
        assert isinstance(phrases, dict)

        # FileIO.write_json(data=sentences.to_json(), file_path=FileIO.join(
        #     FileIO.local_directory(), 'sentences.json'))
        # print (FileIO.join(
        #     FileIO.local_directory(), 'sentences.json'))


if __name__ == "__main__":
    unittest.main()
