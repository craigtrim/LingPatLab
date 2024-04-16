# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab import LingPatLab


class TestPosSequenceExtractor(unittest.TestCase):

    def setUp(self) -> None:
        self.api = LingPatLab()
        assert self.api

    def tearDown(self) -> None:
        self.api = None

    def test_service(self):

        input_text = """
        "004-026": "Visual thinking associations. To a verbal thinker, these associations may appear random, but in my mind, I'm continuously sorting the images. Betsy, on the other hand, is a strictly linear verbal thinker. She needs a sentence to be grammatically correct before she can understand it and move on to the next. We learned that we think completely differently, but that difference became the cornerstone of our future collaborations. To the uninitiated verbal thinker, my initial draft would have looked like a disjointed series of chunks. Betsy takes my pictures and puts them in order. Here's our process: For each chapter, I write the initial draft. Then Betsy rearranges it. She is the master organizer of information, and I love how she teases out the stories behind my technical writing. Verbal thinkers love stories; things make sense to them when they can identify a beginning, middle, and end. As an object thinker, I pull disparate visual information together and organize it in my mind. Spatial visualizers make sense of the world using codes, patterns, and abstractions. Betsy also asks lots of questions, especially about how things work.\n\nThese things are obvious to me, but her questions show me how verbal thinkers process information and help me focus on explaining scientific and engineering stuff to them. It has been a learning experience for me to understand how a verbal writer thinks differently from me. She has made me better at explaining things. Again, the first step is accepting that all types of minds have their own unique way of contributing to solving problems and furthering knowledge.\n\nTwo geniuses are responsible for deciphering the Rosetta Stone, the famous tablet that had three languages engraved on it: Egyptian hieroglyphics, Egyptian simplified writing, and Greek. The stone included beautiful carved figures of birds, lions, and snakes interspersed with non-pictorial symbols. The story of how the hieroglyphs were deciphered is told in \"The Writing of the Gods: The Race to Decode the Rosetta Stone\" by Edward Dolnick.\n",
        """

        summary: str = self.api.generate_summary(input_text)
        self.assertIsNotNone(summary)
        self.assertTrue(isinstance(summary, str))

        print(summary)


if __name__ == "__main__":
    unittest.main()
