# !/usr/bin/env python
# -*- coding: UTF-8 -*-


SYSTEM_PROMPT_SUMMARY = "You are a helpful assistant who condenses text and maintains tonality."


SYSTEM_PROMPT_TEMPLATE = """
You are a helpful assistant who summarizes text.

You must follow these rules:
1. You must only output the summary.  
2. Do not use phrases like "the author recalls" or "the text describes".  
3. Your summary must not sound like a summary.
4. Your summary must have the same tone as the original text.
5. Use phrases found in the original text for your summary.

CONTENT TO SUMMARIZE:
```
#SUMMARY
```
"""


SAMPLE_ORIGINAL_TEXT = """
inconsequential foes in any future war. Now many saw them as supermen who could appear anywhere at any time and in overwhelming force. Some alarmists predicted that they would target Hawaii or the Panama Canal, even the American West Coast. One particularly vulnerable American outpost was Samoa, exactly halfway between Hawaii and Australia (see Map 2). King told Nimitz that in addition to defending Hawaii, his primary task was to protect the line of communication to Australia. If the Japanese seized Samoa, as they had both Guam and Wake, it would sever that connection. In addition to its location, Samoa also hosted the best deepwater port in the South Pacific, at Pago Pago. Yet in January 1942, Samoa's garrison consisted of only about a hundred men of the 7th Marine Defense Battalion plus another hundred or so local militia known as the Fita Fita (Samoan for "soldier"). As if to demonstrate the garrison's vulnerability, an impertinent Japanese sub skipper surfaced off Samoa that month and shelled the island, though it turned out to be only a nuisance raid. To secure this invaluable outpost, King organized a convoy in San Diego to carry five thousand U.S. Marines there. Since the Yorktown was also in San Diego and bound for the Pacific, she and her escorts could accompany the convoy to protect it from Japanese interference.
The imminent arrival of the Yorktown in the Pacific was welcome news for Nimitz, and he challenged his staff to develop a scheme for the best use of this new resource, as well as the three other carrier task forces. Though he was never reluctant to make independent decisions, he always sought to obtain as much information as possible before doing so. In addition to Draemel and McMorris, therefore, he invited Pye to the morning conference. Pye had been deeply shocked by the Japanese attack on December 7, and that made him diffident now. He was also in the awkward position of being a senior vice admiral without a command.
Both Pye and Kimmel did their best to be helpful. Nimitz wrote Catherine that "everyone wants to help me, Pye and Kimmel most of all", but they were also sensitive about being in the way. At the morning meeting, Nimitz outlined the priorities that King had stipulated: defend Hawaii, protect the sea lanes to Australia, and suggested.
"""


SAMPLE_OUTPUT = """
Many viewed the Japanese as formidable adversaries, capable of striking anywhere with overwhelming force, causing concern about potential targets like Hawaii, the Panama Canal, and even the American West Coast. Samoa, positioned strategically between Hawaii and Australia, was identified as a vulnerable outpost crucial for communication. Its meager garrison of Marines and local militia underscored its vulnerability, highlighted by a minor Japanese raid. To reinforce Samoa, King arranged for a convoy carrying five thousand Marines from San Diego, coinciding with the departure of the Yorktown for the Pacific.
Nimitz eagerly anticipated the Yorktown's arrival, prompting strategic discussions with his staff, including Pye, who, despite his shock from the Pearl Harbor attack, contributed positively despite his lack of command. Nimitz emphasized King's priorities: defending Hawaii, safeguarding sea lanes to Australia, and proposing further actions.
"""


def generate_sample_prompt() -> str:
    return generate_prompt(input_text=SAMPLE_ORIGINAL_TEXT)


def generate_prompt(input_text: str) -> str:
    assert isinstance(input_text, str)
    return SYSTEM_PROMPT_TEMPLATE.replace('#SUMMARY', input_text)
