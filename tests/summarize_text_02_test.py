# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab.analyze.svc import SummarizeText


class TestPosSequenceExtractor(unittest.TestCase):

    def test_service(self):

        summarizer = SummarizeText().process
        assert summarizer

        input_text = """
        "007-019": "Animal consciousness and visual thinking: The thalamus regulates consciousness and arousal.\n\nIt is also a relay station. Another key step toward building a brain that may become conscious is the ability of mammals and other animals to perform cross-modal transfers, such as displaying, watching, or continuing grazing. This is the beginning of flexible decision-making for both sensory and motor signals. The thalamus and the PAG alone do not entirely explain consciousness.\n\nThere is another major information hub in the parietal lobe adjacent to the occipital cortex that integrates sensory and emotional information.\n\nDissection of human brains shows that huge bundles of nerve fibers provide wide-ranging connections between both local and long-distance cortical areas. Christof Koch at the Allen Institute for Brain Science in Seattle theorizes that all conscious experience in people originates in this \"hotzone.\" ability to perform cross-modal transfers between different sources of incoming information.\n\nThis is a fancy way of saying that information that enters the brain via one sense organ, such as the eyes, can be combined with information from another sensory system, such as touch, to create a unified understanding. In humans, these visual and tactile inputs are linked from birth but continue to develop over time. An example of cross-modal transfer in people is the ability to identify coins in your pocket by feel.\n\nCockpit controls in many airplanes have handles with distinct shapes so that pilots can fly partially by feel, reducing the chances they mistakenly engage the wrong control. A child learning to ride a bike uses sensory input simultaneously from both the eyes and the vestibular balance system. These tasks, from simple to more challenging, depend on a complex cognitive ability: great capacities for navigation and memory, both of which require an ability to integrate different kinds of information. Pigeons use landmarks on the ground and compass headings to get back home. Some birds can remember where they've hidden nuts. These are all great feats of sensory-based cognition.\n",
        """

        result = summarizer(input_text)
        print(result)


if __name__ == "__main__":
    unittest.main()
