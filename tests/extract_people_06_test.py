# !/usr/bin/env python
# -*- coding: UTF-8 -*-


import unittest
from lingpatlab import LingPatLab
from lingpatlab.utils.dto import Sentence, SpacyResult


class TestSpacyCoreAPI(unittest.TestCase):

    def test_extract_phrases(self):

        sentence = Sentence([


            # The Admiral McMorris to Spencer
            SpacyResult(
                id='3339029993445334476#127', text='The ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='DET', tag='NNP', dep='compound', ent='PERSON',
                shape='Xxxxx', is_alpha=True, is_stop=False, head='9583229153074933549#128',
                is_punct=False, x=463, y=470, is_wordnet=True, normal='the', stem='the',
                other={}),
            SpacyResult(
                id='3339029993445334476#127', text='Admiral ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='compound', ent='PERSON',
                shape='Xxxxx', is_alpha=True, is_stop=False, head='9583229153074933549#128',
                is_punct=False, x=463, y=470, is_wordnet=True, normal='admiral', stem='admir',
                other={}),
            SpacyResult(
                id='9583229153074933549#129', text='McMorris ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='pobj', ent='PERSON',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='mcmorris', stem='mcmorri',
                other={}),
            SpacyResult(
                id='9583229153074933549#129', text='to ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='pobj', ent='',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='to', stem='to',
                other={}),
            SpacyResult(
                id='9583229153074933549#129', text='Spencer ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='pobj', ent='PERSON',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='spencer', stem='spence',
                other={}),

            # blah blah blah
            SpacyResult(
                id='9583229153074933549#129', text='blah ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='', tag='', dep='pobj', ent='',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='blah', stem='blah',
                other={}),
            SpacyResult(
                id='9583229153074933549#129', text='blah ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='', tag='', dep='pobj', ent='',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='blah', stem='blah',
                other={}),
            SpacyResult(
                id='9583229153074933549#129', text='blah ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='', tag='', dep='pobj', ent='',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='blah', stem='blah',
                other={}),

            # John McMorris
            SpacyResult(
                id='3339029993445334476#127', text='John ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='compound', ent='PERSON',
                shape='Xxxxx', is_alpha=True, is_stop=False, head='9583229153074933549#128',
                is_punct=False, x=463, y=470, is_wordnet=True, normal='john', stem='john',
                other={}),
            SpacyResult(
                id='9583229153074933549#129', text='McMorris ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='pobj', ent='PERSON',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='mcmorris', stem='mcmorri',
                other={}),

            # blah blah blah
            SpacyResult(
                id='9583229153074933549#129', text='blah ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='', tag='', dep='pobj', ent='',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='blah', stem='blah',
                other={}),
            SpacyResult(
                id='9583229153074933549#129', text='blah ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='', tag='', dep='pobj', ent='',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='blah', stem='blah',
                other={}),
            SpacyResult(
                id='9583229153074933549#129', text='blah ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='', tag='', dep='pobj', ent='',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='blah', stem='blah',
                other={}),


            # John Stacy McMorris
            SpacyResult(
                id='3339029993445334476#127', text='John ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='compound', ent='PERSON',
                shape='Xxxxx', is_alpha=True, is_stop=False, head='9583229153074933549#128',
                is_punct=False, x=463, y=470, is_wordnet=True, normal='john', stem='john',
                other={}),
            SpacyResult(
                id='3339029993445334476#127', text='Stacy ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='compound', ent='PERSON',
                shape='Xxxxx', is_alpha=True, is_stop=False, head='9583229153074933549#128',
                is_punct=False, x=463, y=470, is_wordnet=True, normal='stacy', stem='stacy',
                other={}),
            SpacyResult(
                id='9583229153074933549#129', text='McMorris ', tense='', noun_number='singular',
                verb_form='', sentiment=0.0, pos='PROPN', tag='NNP', dep='pobj', ent='PERSON',
                shape='XxXxxxx', is_alpha=True, is_stop=False, head='18194338103975822726#124',
                is_punct=False, x=471, y=479, is_wordnet=False, normal='mcmorris', stem='mcmorri',
                other={}),

        ])

        api = LingPatLab()
        results = api.extract_people(sentences=sentence)

        # expected_results = {
        #     'McMorris': ['Stacy McMorris', 'John Stacy McMorris', 'John McMorris', 'Admiral McMorris'],
        #     'Stacy': ['John Stacy']
        # }

        expected_results = {
            'McMorris': ['Stacy McMorris', 'John Stacy McMorris', 'John McMorris', 'Admiral McMorris']
        }

        self.assertEqual(results, expected_results)


if __name__ == "__main__":
    unittest.main()
