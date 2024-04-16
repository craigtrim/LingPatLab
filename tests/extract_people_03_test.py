# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab.analyze.bp import ExtractPeople
from lingpatlab.utils.dto import Sentence, Sentences, SpacyResult


class TestExtractPeople(unittest.TestCase):

    def test_service(self):
        sentence = Sentence([
            SpacyResult(
                id='3339029993445334476#127', text='blah ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='compound', ent='',
                shape='Xxxxx', is_alpha=True, is_stop=False, head='9583229153074933549#128',
                is_punct=False, x=463, y=470, is_wordnet=True, normal='blah', stem='blah',
                other={
                    'i': 126, 'idx': 529, 'orth': 3339029993445334476, 'head_i': 128, 'head_idx': 538,
                    'head_orth': 9583229153074933549, 'head_text': 'McMorris'
                }),

            SpacyResult(
                id='3339029993445334476#127', text='Admiral ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='compound', ent='',
                shape='Xxxxx', is_alpha=True, is_stop=False, head='9583229153074933549#128',
                is_punct=False, x=463, y=470, is_wordnet=True, normal='admiral', stem='admir',
                other={
                    'i': 126, 'idx': 529, 'orth': 3339029993445334476, 'head_i': 128, 'head_idx': 538,
                    'head_orth': 9583229153074933549, 'head_text': 'McMorris'
                }),

            SpacyResult(
                id='9583229153074933549#129', text='McMorris ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='pobj', ent='PERSON',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='mcmorris', stem='mcmorri',
                other={
                    'i': 128, 'idx': 538, 'orth': 9583229153074933549, 'head_i': 124, 'head_idx': 523,
                    'head_orth': 18194338103975822726, 'head_text': 'like'
                }),

            SpacyResult(
                id='9583229153074933549#129', text='to ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='pobj', ent='',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='to', stem='to',
                other={
                    'i': 128, 'idx': 538, 'orth': 9583229153074933549, 'head_i': 124, 'head_idx': 523,
                    'head_orth': 18194338103975822726, 'head_text': 'like'
                }),

            SpacyResult(
                id='9583229153074933549#129', text='Spencer ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='pobj', ent='PERSON',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='spencer', stem='spence',
                other={
                    'i': 128, 'idx': 538, 'orth': 9583229153074933549, 'head_i': 124, 'head_idx': 523,
                    'head_orth': 18194338103975822726, 'head_text': 'like'
                }),

        ])

        bp = ExtractPeople()
        self.assertIsNotNone(bp)

        results = bp.process(Sentences([sentence]))
        print(results)
        self.assertEqual(results, {'McMorris': ['Admiral McMorris']})


if __name__ == "__main__":
    unittest.main()
