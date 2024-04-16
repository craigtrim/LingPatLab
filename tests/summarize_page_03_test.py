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
        "NIMITZ AT WAR headed for Morotai and maintaining radio silence, so Sutherland answered in his name: "I am prepared to move [to Leyte] immediately." One unresolved issue was the scheduled invasion of Peleliu. Halsey urged its cancellation, but Nimitz had promised MacArthur he would "provide strategic cover and support" for the move to Morotai, which was already underway. That included suppressing Japanese planes on Peleliu. In addition, by the time the new timetable was approved, D-Day on Peleliu was only hours away. The Underwater Demolition Teams (UDTs), known as "frogmen," were already ashore on Peleliu preparing the landing beaches. Cancelling the invasion now was likely to cause widespread confusion, if not chaos. Nimitz told King that it was not feasible to reorient the forces "as rapidly as Halsey appears to visualize." He radioed Halsey that he should "carry out the first phase of STALEMATE as planned on D-Day plus two, though by then it was, in the words of historian Ian Toll, "a burned-out scrapyard." After that, the Battle for Peleliu became a nightmare. When the Marines advanced inland, they discovered that ten thousand Japanese defenders had burrowed deep into hundreds of caves and tunnels. Instead of launching suicidal banzai charges, they remained in those caves and defied the Marines to come and get them. The Marines did, but at an enormous cost. This time the hell-for-leather tactics the Marines preferred were unsuitable to the circumstances. After the men of the 1st Marine Division suffered nearly 7,000 casualties in two weeks, the Army's 81st Division relieved them and initiated a more deliberate approach. In the end, it took six weeks to clear the island, with the Japanese again fighting to the last man: 10,000 enemy soldiers were killed and only 200 were taken prisoner. The Americans suffered too, with 8,000 total casualties, including more than 1,500 killed. Those losses were especially tragic in light of the fact that due to the changes in the strategic timetable, the island did not need to be taken at all. His grandfather's advice not to obsess over things he could not control made it possible for him to compartmentalize the various aspects. It was his biggest mistake of the war. The strategic objective on Peleliu was the airfield. The Marines seized it. If Nimitz regretted his decision to go ahead with Stalemate, he left no record of it."
        """

        summary = self.api.generate_summary(input_text)
        self.assertIsNotNone(summary)
        self.assertTrue(isinstance(summary, str))

        print(summary)


if __name__ == "__main__":
    unittest.main()
