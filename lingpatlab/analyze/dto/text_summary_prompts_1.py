# !/usr/bin/env python
# -*- coding: UTF-8 -*-

from typing import List, Optional


SYSTEM_PROMPT_SUMMARY = "You are a helpful assistant who summarizes text and maintains tonality."

SYSTEM_PROMPT_TEMPLATE_1 = """
You are a helpful assistant who summarizes text.

You must follow these rules:
1. Your summary must use all my phrases.
2. You CAN NOT change my phrases when you use them.
3. You must only output the summary.  
4. Do not use phrases like "the author recalls" or "the text describes".  
5. Your summary must not sound like a summary.
6. Your summary must have the same tone as the original text.

CONTENT TO SUMMARIZE:
```
#SUMMARY
```

MY PHRASES:
```
#PHRASES
```
        """

SYSTEM_PROMPT_TEMPLATE_2 = """
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

SYSTEM_PROMPT_TEMPLATE_2 = """
You are a helpful assistant who condenses text.

You must follow these rules:
1. Subject-Verb Agreement: Ensure subjects and verbs match in number.
2. Proper Pronoun Usage: Match pronouns with their antecedents in gender, number, and person.
3. Sentence Structure: Maintain clear subject-verb-object order.
4. Active vs. Passive Voice: Prefer active voice for clarity and directness.
5. Tense Consistency: Use tenses consistently to indicate timing accurately.
6. Anaphora Resolution: Resolve anaphoric references to ensure clarity and coherence within a text.
7. Acronym Resolution: Clarify the meaning of acronyms when their definitions are provided in the text for better understanding.

CONTENT TO CONDENSE:
```
#SUMMARY
```
"""


SAMPLE_ORIGINAL_TEXT = """004-030": "hold your head up high. \"The Sounds of Silence\" over and over in my head: \"The words of the prophets are written on the subway walls and tenement halls.\" In \"Thinking in Pictures,\" I wrote about Led Zeppelin's \"Stairway to Heaven,\" which I listened to while driving away from the meat-packing plants. But the music I've loved since I was a child comes from musicals. I loved them then, and I love them now. In high school, my roommate played Carousel, Bye Bye Birdie, and Oklahoma! over and over. I sang \"The Farmer and the Cowman\" from Oklahoma! in the high school talent show. And when I graduated, I recited the words to \"You'll Never Walk Alone\" from Carousel. It was a song that made me think about my future. There may be storms, but when you get through them, there will be a bright future. I have gone through many doors, and in walking through them, I always come back to this song and the promise of a golden sky. Composer Richard Rodgers and lyricist Oscar Hammerstein were the musical team behind many of my favorite musicals, including Carousel and Oklahoma! Looking into their collaboration, I realized they were the perfect example of complementary minds. When they met, Rodgers already had a highly successful Broadway career. Hammerstein wasn't quite as successful but was widely respected.\n\nIt wasn't common for theater people to start collaborating at midlife, but from the moment the two men decided to work together, something magical happened. In The Sound of Their Music, Frederick Nolan quotes Rodgers as saying, \"What happened between Oscar and me was almost chemical. Put the right components together and an explosion takes place. Oscar and I hit it off from the day we started discussing the show.\" When you walk through a storm.\n","""


SAMPLE_PHRASES = [
    'start collaborating at midlife',
    'started discussing the show',
    'lyricist oscar hammerstein',
    'roommate played carousel',
    'explosion takes place',
    'school talent show'
]


SAMPLE_OUTPUT = """
The love for musicals, deeply rooted since childhood, resurfaces. High school memories include roommates playing Carousel, Bye Bye Birdie, and Oklahoma! on repeat. Participating in the school talent show, "The Farmer and the Cowman" from Oklahoma! was sung. Graduation was marked by reciting "You'll Never Walk Alone" from Carousel, symbolizing hope for the future amidst storms. Reflecting on Richard Rodgers and lyricist Oscar Hammerstein's partnership reveals their complementary minds. Their collaboration, starting at midlife, led to a magical synergy, as expressed by Rodgers in the quote, "What happened between Oscar and me was almost chemical."
"""


def generate_sample_prompt() -> str:
    return generate_prompt(input_text=SAMPLE_ORIGINAL_TEXT, phrases=SAMPLE_PHRASES)


def generate_prompt(input_text: str, phrases: Optional[List[str]] = None) -> str:
    if phrases and len(phrases):
        return SYSTEM_PROMPT_TEMPLATE_1.replace('#SUMMARY', input_text).replace(
            '#PHRASES', ', '.join(phrases))
    return SYSTEM_PROMPT_TEMPLATE_2.replace('#SUMMARY', input_text)
