# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import List
from lingpatlab.baseblock import FileIO, Stopwatch
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentences, Sentence


def test_service():

    sw = Stopwatch()

    api = LingPatLab()
    assert api

    input_lines = [
        'Visual Thinking is an article in CEO Magazine that states, "Dyslexics are great explorers of information." Famous dyslexic businesspeople include Sir Richard Branson of the Virgin Group and celebrity chef Jamie Oliver. Ingvar Kamprad, the creator of IKEA, was also dyslexic. He developed a naming system to easily visualize and organize his furniture inventory in his warehouses.', "Large furniture had the names of Swedish places; medium-sized furniture, such as desks and chairs, received men's names; and outdoor furniture received the names of Swedish islands. There is evidence that dyslexia and creativity may be linked. Picasso claimed not to have read before the age of ten and could not recall the correct order of the alphabet. According to Patrick O'Brian's biography, Picasso failed to learn reading or math in school.", 'Somehow the rudiments of these arts seeped into him quite early, but they did not do so in the classroom: to the end of his life he was not at home with the alphabet. In Creating Minds, Howard Gardner notes that Picasso had "precocious spatial intelligence but very meager scholastic intelligences."', 'My favorite observation comes from author Gertrude Stein: "Picasso wrote painting as other children wrote their ABCs." Another study showed that college art students had more dyslexia than students in other majors.', "Thomas West cites Thomas Edison, Albert Einstein, Gustave Flaubert, and William Butler Yeats, among others, as having dyslexia or a form of learning disability. A 2021 New Yorker profile of Ari Emanuel, the CEO of the talent agency Endeavor, revealed that the Hollywood rainmaker was dyslexic. He was unable to read by the third grade and was diagnosed with dyslexia and ADHD. He was teased a lot, and he fought back. In 2007, he received an award from the Lab School in Washington, DC, which specializes in working with kids with learning disabilities. His remarks on the occasion amplify Thomas West's. He told them dyslexia was a gift that could give them. His spelling remained highly personal. Drawing always was his only way of talking.\n"
    ]

    sentences: Sentences = api.parse_input_lines(input_lines)
    assert isinstance(sentences, Sentences)

    for sentence in sentences:
        assert isinstance(sentence, Sentence)
        for token in sentence:
            print(token.to_string())


def main():
    test_service()


if __name__ == "__main__":
    main()
