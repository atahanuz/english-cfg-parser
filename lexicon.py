"""
Lexicon for English CFG Parser
Uses Penn Treebank tagset with morphological features for agreement.

Penn Treebank Tags Used:
- CC: Coordinating conjunction
- DT: Determiner
- IN: Preposition or subordinating conjunction
- JJ: Adjective
- JJR: Adjective, comparative
- JJS: Adjective, superlative
- MD: Modal
- NN: Noun, singular
- NNS: Noun, plural
- NNP: Proper noun, singular
- NNPS: Proper noun, plural
- PRP: Personal pronoun
- PRP$: Possessive pronoun
- RB: Adverb
- RBR: Adverb, comparative
- RBS: Adverb, superlative
- TO: to
- VB: Verb, base form
- VBD: Verb, past tense
- VBG: Verb, gerund/present participle
- VBN: Verb, past participle
- VBP: Verb, non-3rd person singular present
- VBZ: Verb, 3rd person singular present
- WDT: Wh-determiner
- WP: Wh-pronoun
- WRB: Wh-adverb
"""

from morphology import MorphologicalAnalyzer

# ============================================================================
# CLOSED-CLASS WORDS (Comprehensive)
# ============================================================================

# Determiners (DT)
DETERMINERS = {
    'a': {'pos': 'DT', 'number': 'SG', 'definite': False},
    'an': {'pos': 'DT', 'number': 'SG', 'definite': False},
    'the': {'pos': 'DT', 'number': None, 'definite': True},  # Works with both SG/PL
    'this': {'pos': 'DT', 'number': 'SG', 'definite': True},
    'that': {'pos': 'DT', 'number': 'SG', 'definite': True},
    'these': {'pos': 'DT', 'number': 'PL', 'definite': True},
    'those': {'pos': 'DT', 'number': 'PL', 'definite': True},
    'some': {'pos': 'DT', 'number': None, 'definite': False},
    'any': {'pos': 'DT', 'number': None, 'definite': False},
    'every': {'pos': 'DT', 'number': 'SG', 'definite': False},
    'each': {'pos': 'DT', 'number': 'SG', 'definite': False},
    'no': {'pos': 'DT', 'number': None, 'definite': False},
    'all': {'pos': 'DT', 'number': 'PL', 'definite': False},
    'both': {'pos': 'DT', 'number': 'PL', 'definite': False},
    'many': {'pos': 'DT', 'number': 'PL', 'definite': False},
    'few': {'pos': 'DT', 'number': 'PL', 'definite': False},
    'several': {'pos': 'DT', 'number': 'PL', 'definite': False},
    'most': {'pos': 'DT', 'number': None, 'definite': False},
}

# Personal Pronouns (PRP)
PERSONAL_PRONOUNS = {
    'i': {'pos': 'PRP', 'person': 1, 'number': 'SG', 'case': 'NOM'},
    'me': {'pos': 'PRP', 'person': 1, 'number': 'SG', 'case': 'ACC'},
    'you': {'pos': 'PRP', 'person': 2, 'number': None, 'case': None},  # SG or PL
    'he': {'pos': 'PRP', 'person': 3, 'number': 'SG', 'case': 'NOM', 'gender': 'M'},
    'him': {'pos': 'PRP', 'person': 3, 'number': 'SG', 'case': 'ACC', 'gender': 'M'},
    'she': {'pos': 'PRP', 'person': 3, 'number': 'SG', 'case': 'NOM', 'gender': 'F'},
    'her': {'pos': 'PRP', 'person': 3, 'number': 'SG', 'case': 'ACC', 'gender': 'F'},
    'it': {'pos': 'PRP', 'person': 3, 'number': 'SG', 'case': None, 'gender': 'N'},
    'we': {'pos': 'PRP', 'person': 1, 'number': 'PL', 'case': 'NOM'},
    'us': {'pos': 'PRP', 'person': 1, 'number': 'PL', 'case': 'ACC'},
    'they': {'pos': 'PRP', 'person': 3, 'number': 'PL', 'case': 'NOM'},
    'them': {'pos': 'PRP', 'person': 3, 'number': 'PL', 'case': 'ACC'},
}

# Possessive Pronouns (PRP$)
POSSESSIVE_PRONOUNS = {
    'my': {'pos': 'PRP$', 'person': 1, 'number': 'SG'},
    'your': {'pos': 'PRP$', 'person': 2, 'number': None},
    'his': {'pos': 'PRP$', 'person': 3, 'number': 'SG', 'gender': 'M'},
    'her': {'pos': 'PRP$', 'person': 3, 'number': 'SG', 'gender': 'F'},
    'its': {'pos': 'PRP$', 'person': 3, 'number': 'SG', 'gender': 'N'},
    'our': {'pos': 'PRP$', 'person': 1, 'number': 'PL'},
    'their': {'pos': 'PRP$', 'person': 3, 'number': 'PL'},
}

# Modals (MD)
MODALS = {
    'will': {'pos': 'MD', 'tense': 'FUT'},
    'would': {'pos': 'MD', 'tense': 'COND'},
    'can': {'pos': 'MD', 'tense': 'PRES'},
    'could': {'pos': 'MD', 'tense': 'PAST'},
    'shall': {'pos': 'MD', 'tense': 'FUT'},
    'should': {'pos': 'MD', 'tense': 'COND'},
    'may': {'pos': 'MD', 'tense': 'PRES'},
    'might': {'pos': 'MD', 'tense': 'PAST'},
    'must': {'pos': 'MD', 'tense': 'PRES'},
    'do': {'pos': 'MD', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'does': {'pos': 'MD', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'did': {'pos': 'MD', 'tense': 'PAST'},
}

# Prepositions (IN)
PREPOSITIONS = {
    'in': {'pos': 'IN', 'type': 'LOC'},
    'on': {'pos': 'IN', 'type': 'LOC'},
    'at': {'pos': 'IN', 'type': 'LOC'},
    'to': {'pos': 'IN', 'type': 'DIR'},
    'for': {'pos': 'IN', 'type': 'BEN'},
    'from': {'pos': 'IN', 'type': 'SRC'},
    'with': {'pos': 'IN', 'type': 'INST'},
    'about': {'pos': 'IN', 'type': 'TOPIC'},
    'under': {'pos': 'IN', 'type': 'LOC'},
    'over': {'pos': 'IN', 'type': 'LOC'},
    'between': {'pos': 'IN', 'type': 'LOC'},
    'into': {'pos': 'IN', 'type': 'DIR'},
    'through': {'pos': 'IN', 'type': 'PATH'},
    'of': {'pos': 'IN', 'type': 'POSS'},
    'by': {'pos': 'IN', 'type': 'AGENT'},
    'as': {'pos': 'IN', 'type': 'ROLE'},
    'during': {'pos': 'IN', 'type': 'TEMP'},
    'before': {'pos': 'IN', 'type': 'TEMP'},
    'after': {'pos': 'IN', 'type': 'TEMP'},
}

# Coordinating Conjunctions (CC)
CONJUNCTIONS = {
    'and': {'pos': 'CC'},
    'or': {'pos': 'CC'},
    'but': {'pos': 'CC'},
    'nor': {'pos': 'CC'},
    'yet': {'pos': 'CC'},
    'so': {'pos': 'CC'},
}

# Wh-words
WH_ADVERBS = {
    'when': {'pos': 'WRB', 'type': 'TIME'},
    'where': {'pos': 'WRB', 'type': 'PLACE'},
    'why': {'pos': 'WRB', 'type': 'REASON'},
    'how': {'pos': 'WRB', 'type': 'MANNER'},
}

WH_PRONOUNS = {
    'who': {'pos': 'WP', 'case': 'NOM'},
    'whom': {'pos': 'WP', 'case': 'ACC'},
    'what': {'pos': 'WP', 'case': None},
    'which': {'pos': 'WP', 'case': None},
}

# Common Adverbs (RB)
ADVERBS = {
    'not': {'pos': 'RB', 'type': 'NEG'},
    'never': {'pos': 'RB', 'type': 'NEG'},
    'always': {'pos': 'RB', 'type': 'FREQ'},
    'often': {'pos': 'RB', 'type': 'FREQ'},
    'sometimes': {'pos': 'RB', 'type': 'FREQ'},
    'usually': {'pos': 'RB', 'type': 'FREQ'},
    'rarely': {'pos': 'RB', 'type': 'FREQ'},
    'yesterday': {'pos': 'RB', 'type': 'TIME', 'tense': 'PAST'},
    'today': {'pos': 'RB', 'type': 'TIME', 'tense': 'PRES'},
    'tomorrow': {'pos': 'RB', 'type': 'TIME', 'tense': 'FUT'},
    'tonight': {'pos': 'RB', 'type': 'TIME'},
    'here': {'pos': 'RB', 'type': 'PLACE'},
    'there': {'pos': 'RB', 'type': 'PLACE'},
    'lastly': {'pos': 'RB', 'type': 'TIME'},
    'quite': {'pos': 'RB', 'type': 'DEGREE'},
    'very': {'pos': 'RB', 'type': 'DEGREE'},
    'really': {'pos': 'RB', 'type': 'DEGREE'},
    'just': {'pos': 'RB', 'type': 'FOCUS'},
    'also': {'pos': 'RB', 'type': 'ADD'},
    'only': {'pos': 'RB', 'type': 'FOCUS'},
    'even': {'pos': 'RB', 'type': 'FOCUS'},
    'still': {'pos': 'RB', 'type': 'ASP'},
    'already': {'pos': 'RB', 'type': 'ASP'},
    'now': {'pos': 'RB', 'type': 'TIME', 'tense': 'PRES'},
    'then': {'pos': 'RB', 'type': 'TIME'},
    'away': {'pos': 'RB', 'type': 'PLACE'},
    'back': {'pos': 'RB', 'type': 'PLACE'},
    'every': {'pos': 'RB', 'type': 'FREQ'},
    'most': {'pos': 'RB', 'type': 'DEGREE'},  # "most beautiful"
}

# TO particle
TO_PARTICLE = {
    'to': {'pos': 'TO'},
}

# ============================================================================
# OPEN-CLASS WORDS (Sufficient Sample)
# ============================================================================

# Nouns with features
NOUNS = {
    # Common nouns from example sentences
    'present': {'pos': 'NN', 'number': 'SG'},
    'gift': {'pos': 'NN', 'number': 'SG'},
    'friend': {'pos': 'NN', 'number': 'SG'},
    'mother': {'pos': 'NN', 'number': 'SG'},
    'father': {'pos': 'NN', 'number': 'SG'},
    'dinner': {'pos': 'NN', 'number': 'SG'},
    'school': {'pos': 'NN', 'number': 'SG'},
    'village': {'pos': 'NN', 'number': 'SG'},
    'tree': {'pos': 'NN', 'number': 'SG'},
    'night': {'pos': 'NN', 'number': 'SG'},
    'meeting': {'pos': 'NN', 'number': 'SG'},
    'music': {'pos': 'NN', 'number': 'SG', 'countable': False},
    'novel': {'pos': 'NN', 'number': 'SG'},
    'fruit': {'pos': 'NN', 'number': 'SG'},
    'summer': {'pos': 'NN', 'number': 'SG'},
    'culture': {'pos': 'NN', 'number': 'SG'},
    'history': {'pos': 'NN', 'number': 'SG'},
    'moonlight': {'pos': 'NN', 'number': 'SG', 'countable': False},
    'watermelon': {'pos': 'NN', 'number': 'SG'},
    'epic': {'pos': 'NN', 'number': 'SG'},
    'book': {'pos': 'NN', 'number': 'SG'},
    'man': {'pos': 'NN', 'number': 'SG'},
    'woman': {'pos': 'NN', 'number': 'SG'},
    'child': {'pos': 'NN', 'number': 'SG'},
    'day': {'pos': 'NN', 'number': 'SG'},
    'year': {'pos': 'NN', 'number': 'SG'},
    'time': {'pos': 'NN', 'number': 'SG'},
    'way': {'pos': 'NN', 'number': 'SG'},
    'world': {'pos': 'NN', 'number': 'SG'},
    'life': {'pos': 'NN', 'number': 'SG'},
    'hand': {'pos': 'NN', 'number': 'SG'},
    'part': {'pos': 'NN', 'number': 'SG'},
    'place': {'pos': 'NN', 'number': 'SG'},
    'case': {'pos': 'NN', 'number': 'SG'},
    'week': {'pos': 'NN', 'number': 'SG'},
    'company': {'pos': 'NN', 'number': 'SG'},
    'system': {'pos': 'NN', 'number': 'SG'},
    'program': {'pos': 'NN', 'number': 'SG'},
    'question': {'pos': 'NN', 'number': 'SG'},
    'work': {'pos': 'NN', 'number': 'SG'},
    'government': {'pos': 'NN', 'number': 'SG'},
    'number': {'pos': 'NN', 'number': 'SG'},
    'home': {'pos': 'NN', 'number': 'SG'},
    'water': {'pos': 'NN', 'number': 'SG', 'countable': False},
    'room': {'pos': 'NN', 'number': 'SG'},
    'car': {'pos': 'NN', 'number': 'SG'},
    'market': {'pos': 'NN', 'number': 'SG'},
    'money': {'pos': 'NN', 'number': 'SG', 'countable': False},
    'story': {'pos': 'NN', 'number': 'SG'},
    'fact': {'pos': 'NN', 'number': 'SG'},
    'month': {'pos': 'NN', 'number': 'SG'},
    'lot': {'pos': 'NN', 'number': 'SG'},
    'right': {'pos': 'NN', 'number': 'SG'},
    'study': {'pos': 'NN', 'number': 'SG'},
    'problem': {'pos': 'NN', 'number': 'SG'},
    'game': {'pos': 'NN', 'number': 'SG'},
    # Additional nouns for test sentences
    'student': {'pos': 'NN', 'number': 'SG'},
    'teacher': {'pos': 'NN', 'number': 'SG'},
    'house': {'pos': 'NN', 'number': 'SG'},
    'city': {'pos': 'NN', 'number': 'SG'},
    'country': {'pos': 'NN', 'number': 'SG'},
    'family': {'pos': 'NN', 'number': 'SG'},
    'door': {'pos': 'NN', 'number': 'SG'},
    'window': {'pos': 'NN', 'number': 'SG'},
    'table': {'pos': 'NN', 'number': 'SG'},
    'chair': {'pos': 'NN', 'number': 'SG'},
    'morning': {'pos': 'NN', 'number': 'SG'},
    'evening': {'pos': 'NN', 'number': 'SG'},
    'afternoon': {'pos': 'NN', 'number': 'SG'},
}

# Plural nouns
PLURAL_NOUNS = {
    'friends': {'pos': 'NNS', 'number': 'PL', 'lemma': 'friend'},
    'novels': {'pos': 'NNS', 'number': 'PL', 'lemma': 'novel'},
    'books': {'pos': 'NNS', 'number': 'PL', 'lemma': 'book'},
    'epics': {'pos': 'NNS', 'number': 'PL', 'lemma': 'epic'},
    'children': {'pos': 'NNS', 'number': 'PL', 'lemma': 'child'},
    'men': {'pos': 'NNS', 'number': 'PL', 'lemma': 'man'},
    'women': {'pos': 'NNS', 'number': 'PL', 'lemma': 'woman'},
    'people': {'pos': 'NNS', 'number': 'PL', 'lemma': 'person'},
    'days': {'pos': 'NNS', 'number': 'PL', 'lemma': 'day'},
    'years': {'pos': 'NNS', 'number': 'PL', 'lemma': 'year'},
    'times': {'pos': 'NNS', 'number': 'PL', 'lemma': 'time'},
    'things': {'pos': 'NNS', 'number': 'PL', 'lemma': 'thing'},
    'students': {'pos': 'NNS', 'number': 'PL', 'lemma': 'student'},
    'teachers': {'pos': 'NNS', 'number': 'PL', 'lemma': 'teacher'},
    'nights': {'pos': 'NNS', 'number': 'PL', 'lemma': 'night'},
    'trees': {'pos': 'NNS', 'number': 'PL', 'lemma': 'tree'},
    'stories': {'pos': 'NNS', 'number': 'PL', 'lemma': 'story'},
    'cities': {'pos': 'NNS', 'number': 'PL', 'lemma': 'city'},
    'families': {'pos': 'NNS', 'number': 'PL', 'lemma': 'family'},
    'countries': {'pos': 'NNS', 'number': 'PL', 'lemma': 'country'},
}

# Proper nouns
PROPER_NOUNS = {
    'john': {'pos': 'NNP', 'number': 'SG'},
    'mary': {'pos': 'NNP', 'number': 'SG'},
    'london': {'pos': 'NNP', 'number': 'SG'},
    'paris': {'pos': 'NNP', 'number': 'SG'},
    'america': {'pos': 'NNP', 'number': 'SG'},
    'england': {'pos': 'NNP', 'number': 'SG'},
    'monday': {'pos': 'NNP', 'number': 'SG'},
    'tuesday': {'pos': 'NNP', 'number': 'SG'},
    'wednesday': {'pos': 'NNP', 'number': 'SG'},
    'thursday': {'pos': 'NNP', 'number': 'SG'},
    'friday': {'pos': 'NNP', 'number': 'SG'},
    'saturday': {'pos': 'NNP', 'number': 'SG'},
    'sunday': {'pos': 'NNP', 'number': 'SG'},
}

# Verbs with subcategorization frames
# subcat: what complements the verb can take
#   'NP': direct object (transitive)
#   'PP': prepositional phrase
#   'NONE': intransitive
#   'NP_PP': NP followed by PP
#   'CP': clause
VERBS = {
    # Base forms (VB) with subcategorization
    'buy': {'pos': 'VB', 'subcat': ['NP', 'NP_PP'], 'form': 'BASE'},
    'read': {'pos': 'VB', 'subcat': ['NP', 'NONE'], 'form': 'BASE'},
    'help': {'pos': 'VB', 'subcat': ['NP', 'NP_PP'], 'form': 'BASE'},
    'tell': {'pos': 'VB', 'subcat': ['NP', 'NP_PP', 'CP'], 'form': 'BASE'},
    'watch': {'pos': 'VB', 'subcat': ['NP'], 'form': 'BASE'},
    'attend': {'pos': 'VB', 'subcat': ['NP'], 'form': 'BASE'},
    'come': {'pos': 'VB', 'subcat': ['NONE', 'PP'], 'form': 'BASE'},
    'listen': {'pos': 'VB', 'subcat': ['PP'], 'prep': 'to', 'form': 'BASE'},
    'enjoy': {'pos': 'VB', 'subcat': ['NP'], 'form': 'BASE'},
    'go': {'pos': 'VB', 'subcat': ['PP'], 'prep': 'to', 'form': 'BASE'},
    'be': {'pos': 'VB', 'subcat': ['NP', 'ADJP', 'PP'], 'form': 'BASE'},
    'have': {'pos': 'VB', 'subcat': ['NP'], 'form': 'BASE'},
    'give': {'pos': 'VB', 'subcat': ['NP', 'NP_NP', 'NP_PP'], 'form': 'BASE'},
    'take': {'pos': 'VB', 'subcat': ['NP', 'NP_PP'], 'form': 'BASE'},
    'make': {'pos': 'VB', 'subcat': ['NP', 'NP_ADJP'], 'form': 'BASE'},
    'get': {'pos': 'VB', 'subcat': ['NP', 'PP', 'ADJP'], 'form': 'BASE'},
    'see': {'pos': 'VB', 'subcat': ['NP', 'CP'], 'form': 'BASE'},
    'know': {'pos': 'VB', 'subcat': ['NP', 'CP'], 'form': 'BASE'},
    'think': {'pos': 'VB', 'subcat': ['CP', 'PP'], 'form': 'BASE'},
    'find': {'pos': 'VB', 'subcat': ['NP', 'CP'], 'form': 'BASE'},
    'say': {'pos': 'VB', 'subcat': ['NP', 'CP'], 'form': 'BASE'},
    'put': {'pos': 'VB', 'subcat': ['NP_PP'], 'form': 'BASE'},
    'run': {'pos': 'VB', 'subcat': ['NONE', 'NP'], 'form': 'BASE'},
    'write': {'pos': 'VB', 'subcat': ['NP', 'NP_PP'], 'form': 'BASE'},
    'eat': {'pos': 'VB', 'subcat': ['NP', 'NONE'], 'form': 'BASE'},
    'drink': {'pos': 'VB', 'subcat': ['NP', 'NONE'], 'form': 'BASE'},
    'sing': {'pos': 'VB', 'subcat': ['NP', 'NONE'], 'form': 'BASE'},
    'swim': {'pos': 'VB', 'subcat': ['NONE'], 'form': 'BASE'},
    'walk': {'pos': 'VB', 'subcat': ['NONE', 'PP', 'NP'], 'form': 'BASE'},
    'talk': {'pos': 'VB', 'subcat': ['PP'], 'form': 'BASE'},
    'speak': {'pos': 'VB', 'subcat': ['PP', 'NP', 'NONE'], 'form': 'BASE'},
    'work': {'pos': 'VB', 'subcat': ['NONE', 'PP'], 'form': 'BASE'},
    'live': {'pos': 'VB', 'subcat': ['PP'], 'form': 'BASE'},
    'move': {'pos': 'VB', 'subcat': ['NP', 'PP', 'NONE'], 'form': 'BASE'},
    'play': {'pos': 'VB', 'subcat': ['NP', 'NONE'], 'form': 'BASE'},
    'open': {'pos': 'VB', 'subcat': ['NP'], 'form': 'BASE'},
    'close': {'pos': 'VB', 'subcat': ['NP'], 'form': 'BASE'},
    'start': {'pos': 'VB', 'subcat': ['NP', 'NONE'], 'form': 'BASE'},
    'stop': {'pos': 'VB', 'subcat': ['NP', 'NONE'], 'form': 'BASE'},
    'begin': {'pos': 'VB', 'subcat': ['NP', 'NONE'], 'form': 'BASE'},
    'finish': {'pos': 'VB', 'subcat': ['NP'], 'form': 'BASE'},
    'show': {'pos': 'VB', 'subcat': ['NP', 'NP_PP', 'NP_NP'], 'form': 'BASE'},
    'leave': {'pos': 'VB', 'subcat': ['NP', 'NONE'], 'form': 'BASE'},
    'call': {'pos': 'VB', 'subcat': ['NP', 'NP_NP'], 'form': 'BASE'},
    'try': {'pos': 'VB', 'subcat': ['NP', 'INF'], 'form': 'BASE'},
    'ask': {'pos': 'VB', 'subcat': ['NP', 'CP', 'NP_PP'], 'form': 'BASE'},
    'need': {'pos': 'VB', 'subcat': ['NP', 'INF'], 'form': 'BASE'},
    'feel': {'pos': 'VB', 'subcat': ['NP', 'ADJP'], 'form': 'BASE'},
    'become': {'pos': 'VB', 'subcat': ['NP', 'ADJP'], 'form': 'BASE'},
    'bring': {'pos': 'VB', 'subcat': ['NP', 'NP_PP'], 'form': 'BASE'},
    'hold': {'pos': 'VB', 'subcat': ['NP'], 'form': 'BASE'},
    'turn': {'pos': 'VB', 'subcat': ['NP', 'PP', 'ADJP'], 'form': 'BASE'},
    'follow': {'pos': 'VB', 'subcat': ['NP'], 'form': 'BASE'},
    'wait': {'pos': 'VB', 'subcat': ['NONE', 'PP'], 'form': 'BASE'},
}

# Past tense verbs (VBD)
PAST_VERBS = {
    'bought': {'pos': 'VBD', 'lemma': 'buy', 'tense': 'PAST'},
    'read': {'pos': 'VBD', 'lemma': 'read', 'tense': 'PAST'},  # Same as base
    'helped': {'pos': 'VBD', 'lemma': 'help', 'tense': 'PAST'},
    'told': {'pos': 'VBD', 'lemma': 'tell', 'tense': 'PAST'},
    'watched': {'pos': 'VBD', 'lemma': 'watch', 'tense': 'PAST'},
    'attended': {'pos': 'VBD', 'lemma': 'attend', 'tense': 'PAST'},
    'came': {'pos': 'VBD', 'lemma': 'come', 'tense': 'PAST'},
    'listened': {'pos': 'VBD', 'lemma': 'listen', 'tense': 'PAST'},
    'enjoyed': {'pos': 'VBD', 'lemma': 'enjoy', 'tense': 'PAST'},
    'went': {'pos': 'VBD', 'lemma': 'go', 'tense': 'PAST'},
    'was': {'pos': 'VBD', 'lemma': 'be', 'tense': 'PAST', 'number': 'SG', 'person': [1, 3]},
    'were': {'pos': 'VBD', 'lemma': 'be', 'tense': 'PAST', 'number': 'PL'},
    'had': {'pos': 'VBD', 'lemma': 'have', 'tense': 'PAST'},
    'gave': {'pos': 'VBD', 'lemma': 'give', 'tense': 'PAST'},
    'took': {'pos': 'VBD', 'lemma': 'take', 'tense': 'PAST'},
    'made': {'pos': 'VBD', 'lemma': 'make', 'tense': 'PAST'},
    'got': {'pos': 'VBD', 'lemma': 'get', 'tense': 'PAST'},
    'saw': {'pos': 'VBD', 'lemma': 'see', 'tense': 'PAST'},
    'knew': {'pos': 'VBD', 'lemma': 'know', 'tense': 'PAST'},
    'thought': {'pos': 'VBD', 'lemma': 'think', 'tense': 'PAST'},
    'found': {'pos': 'VBD', 'lemma': 'find', 'tense': 'PAST'},
    'said': {'pos': 'VBD', 'lemma': 'say', 'tense': 'PAST'},
    'put': {'pos': 'VBD', 'lemma': 'put', 'tense': 'PAST'},
    'ran': {'pos': 'VBD', 'lemma': 'run', 'tense': 'PAST'},
    'wrote': {'pos': 'VBD', 'lemma': 'write', 'tense': 'PAST'},
    'ate': {'pos': 'VBD', 'lemma': 'eat', 'tense': 'PAST'},
    'drank': {'pos': 'VBD', 'lemma': 'drink', 'tense': 'PAST'},
    'sang': {'pos': 'VBD', 'lemma': 'sing', 'tense': 'PAST'},
    'swam': {'pos': 'VBD', 'lemma': 'swim', 'tense': 'PAST'},
    'walked': {'pos': 'VBD', 'lemma': 'walk', 'tense': 'PAST'},
    'talked': {'pos': 'VBD', 'lemma': 'talk', 'tense': 'PAST'},
    'spoke': {'pos': 'VBD', 'lemma': 'speak', 'tense': 'PAST'},
    'worked': {'pos': 'VBD', 'lemma': 'work', 'tense': 'PAST'},
    'lived': {'pos': 'VBD', 'lemma': 'live', 'tense': 'PAST'},
    'moved': {'pos': 'VBD', 'lemma': 'move', 'tense': 'PAST'},
    'played': {'pos': 'VBD', 'lemma': 'play', 'tense': 'PAST'},
    'opened': {'pos': 'VBD', 'lemma': 'open', 'tense': 'PAST'},
    'closed': {'pos': 'VBD', 'lemma': 'close', 'tense': 'PAST'},
    'started': {'pos': 'VBD', 'lemma': 'start', 'tense': 'PAST'},
    'stopped': {'pos': 'VBD', 'lemma': 'stop', 'tense': 'PAST'},
    'began': {'pos': 'VBD', 'lemma': 'begin', 'tense': 'PAST'},
    'finished': {'pos': 'VBD', 'lemma': 'finish', 'tense': 'PAST'},
    'showed': {'pos': 'VBD', 'lemma': 'show', 'tense': 'PAST'},
    'left': {'pos': 'VBD', 'lemma': 'leave', 'tense': 'PAST'},
    'called': {'pos': 'VBD', 'lemma': 'call', 'tense': 'PAST'},
    'tried': {'pos': 'VBD', 'lemma': 'try', 'tense': 'PAST'},
    'asked': {'pos': 'VBD', 'lemma': 'ask', 'tense': 'PAST'},
    'needed': {'pos': 'VBD', 'lemma': 'need', 'tense': 'PAST'},
    'felt': {'pos': 'VBD', 'lemma': 'feel', 'tense': 'PAST'},
    'became': {'pos': 'VBD', 'lemma': 'become', 'tense': 'PAST'},
    'brought': {'pos': 'VBD', 'lemma': 'bring', 'tense': 'PAST'},
    'held': {'pos': 'VBD', 'lemma': 'hold', 'tense': 'PAST'},
    'turned': {'pos': 'VBD', 'lemma': 'turn', 'tense': 'PAST'},
    'followed': {'pos': 'VBD', 'lemma': 'follow', 'tense': 'PAST'},
    'waited': {'pos': 'VBD', 'lemma': 'wait', 'tense': 'PAST'},
}

# 3rd person singular present (VBZ)
PRESENT_3SG_VERBS = {
    'buys': {'pos': 'VBZ', 'lemma': 'buy', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'reads': {'pos': 'VBZ', 'lemma': 'read', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'helps': {'pos': 'VBZ', 'lemma': 'help', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'tells': {'pos': 'VBZ', 'lemma': 'tell', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'watches': {'pos': 'VBZ', 'lemma': 'watch', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'attends': {'pos': 'VBZ', 'lemma': 'attend', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'comes': {'pos': 'VBZ', 'lemma': 'come', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'listens': {'pos': 'VBZ', 'lemma': 'listen', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'enjoys': {'pos': 'VBZ', 'lemma': 'enjoy', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'goes': {'pos': 'VBZ', 'lemma': 'go', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'is': {'pos': 'VBZ', 'lemma': 'be', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'has': {'pos': 'VBZ', 'lemma': 'have', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'gives': {'pos': 'VBZ', 'lemma': 'give', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'takes': {'pos': 'VBZ', 'lemma': 'take', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'makes': {'pos': 'VBZ', 'lemma': 'make', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'gets': {'pos': 'VBZ', 'lemma': 'get', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'sees': {'pos': 'VBZ', 'lemma': 'see', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'knows': {'pos': 'VBZ', 'lemma': 'know', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'thinks': {'pos': 'VBZ', 'lemma': 'think', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'finds': {'pos': 'VBZ', 'lemma': 'find', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'says': {'pos': 'VBZ', 'lemma': 'say', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'puts': {'pos': 'VBZ', 'lemma': 'put', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'runs': {'pos': 'VBZ', 'lemma': 'run', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'writes': {'pos': 'VBZ', 'lemma': 'write', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'eats': {'pos': 'VBZ', 'lemma': 'eat', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'drinks': {'pos': 'VBZ', 'lemma': 'drink', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'sings': {'pos': 'VBZ', 'lemma': 'sing', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'swims': {'pos': 'VBZ', 'lemma': 'swim', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'walks': {'pos': 'VBZ', 'lemma': 'walk', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'talks': {'pos': 'VBZ', 'lemma': 'talk', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'speaks': {'pos': 'VBZ', 'lemma': 'speak', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'works': {'pos': 'VBZ', 'lemma': 'work', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'lives': {'pos': 'VBZ', 'lemma': 'live', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'moves': {'pos': 'VBZ', 'lemma': 'move', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'plays': {'pos': 'VBZ', 'lemma': 'play', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'opens': {'pos': 'VBZ', 'lemma': 'open', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'closes': {'pos': 'VBZ', 'lemma': 'close', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'starts': {'pos': 'VBZ', 'lemma': 'start', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'stops': {'pos': 'VBZ', 'lemma': 'stop', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'begins': {'pos': 'VBZ', 'lemma': 'begin', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'finishes': {'pos': 'VBZ', 'lemma': 'finish', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'shows': {'pos': 'VBZ', 'lemma': 'show', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'leaves': {'pos': 'VBZ', 'lemma': 'leave', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'calls': {'pos': 'VBZ', 'lemma': 'call', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'tries': {'pos': 'VBZ', 'lemma': 'try', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'asks': {'pos': 'VBZ', 'lemma': 'ask', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'needs': {'pos': 'VBZ', 'lemma': 'need', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'feels': {'pos': 'VBZ', 'lemma': 'feel', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'becomes': {'pos': 'VBZ', 'lemma': 'become', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'brings': {'pos': 'VBZ', 'lemma': 'bring', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'holds': {'pos': 'VBZ', 'lemma': 'hold', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'turns': {'pos': 'VBZ', 'lemma': 'turn', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'follows': {'pos': 'VBZ', 'lemma': 'follow', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
    'waits': {'pos': 'VBZ', 'lemma': 'wait', 'tense': 'PRES', 'person': 3, 'number': 'SG'},
}

# Non-3rd person present (VBP)
PRESENT_NON3SG_VERBS = {
    'buy': {'pos': 'VBP', 'lemma': 'buy', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'read': {'pos': 'VBP', 'lemma': 'read', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'help': {'pos': 'VBP', 'lemma': 'help', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'tell': {'pos': 'VBP', 'lemma': 'tell', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'watch': {'pos': 'VBP', 'lemma': 'watch', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'attend': {'pos': 'VBP', 'lemma': 'attend', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'come': {'pos': 'VBP', 'lemma': 'come', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'listen': {'pos': 'VBP', 'lemma': 'listen', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'enjoy': {'pos': 'VBP', 'lemma': 'enjoy', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'go': {'pos': 'VBP', 'lemma': 'go', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'am': {'pos': 'VBP', 'lemma': 'be', 'tense': 'PRES', 'person': 1, 'number': 'SG'},
    'are': {'pos': 'VBP', 'lemma': 'be', 'tense': 'PRES', 'person': [2, 3], 'number': 'PL'},
    'have': {'pos': 'VBP', 'lemma': 'have', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'give': {'pos': 'VBP', 'lemma': 'give', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'take': {'pos': 'VBP', 'lemma': 'take', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'make': {'pos': 'VBP', 'lemma': 'make', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'get': {'pos': 'VBP', 'lemma': 'get', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'see': {'pos': 'VBP', 'lemma': 'see', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'know': {'pos': 'VBP', 'lemma': 'know', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'think': {'pos': 'VBP', 'lemma': 'think', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'find': {'pos': 'VBP', 'lemma': 'find', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'say': {'pos': 'VBP', 'lemma': 'say', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'put': {'pos': 'VBP', 'lemma': 'put', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'run': {'pos': 'VBP', 'lemma': 'run', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'write': {'pos': 'VBP', 'lemma': 'write', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'eat': {'pos': 'VBP', 'lemma': 'eat', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'drink': {'pos': 'VBP', 'lemma': 'drink', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'sing': {'pos': 'VBP', 'lemma': 'sing', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'swim': {'pos': 'VBP', 'lemma': 'swim', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'walk': {'pos': 'VBP', 'lemma': 'walk', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'talk': {'pos': 'VBP', 'lemma': 'talk', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'speak': {'pos': 'VBP', 'lemma': 'speak', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'work': {'pos': 'VBP', 'lemma': 'work', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'live': {'pos': 'VBP', 'lemma': 'live', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'move': {'pos': 'VBP', 'lemma': 'move', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'play': {'pos': 'VBP', 'lemma': 'play', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'open': {'pos': 'VBP', 'lemma': 'open', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'close': {'pos': 'VBP', 'lemma': 'close', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'start': {'pos': 'VBP', 'lemma': 'start', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'stop': {'pos': 'VBP', 'lemma': 'stop', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'begin': {'pos': 'VBP', 'lemma': 'begin', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'finish': {'pos': 'VBP', 'lemma': 'finish', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'show': {'pos': 'VBP', 'lemma': 'show', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'leave': {'pos': 'VBP', 'lemma': 'leave', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'call': {'pos': 'VBP', 'lemma': 'call', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'try': {'pos': 'VBP', 'lemma': 'try', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'ask': {'pos': 'VBP', 'lemma': 'ask', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'need': {'pos': 'VBP', 'lemma': 'need', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'feel': {'pos': 'VBP', 'lemma': 'feel', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'become': {'pos': 'VBP', 'lemma': 'become', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'bring': {'pos': 'VBP', 'lemma': 'bring', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'hold': {'pos': 'VBP', 'lemma': 'hold', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'turn': {'pos': 'VBP', 'lemma': 'turn', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'follow': {'pos': 'VBP', 'lemma': 'follow', 'tense': 'PRES', 'person': [1, 2], 'number': None},
    'wait': {'pos': 'VBP', 'lemma': 'wait', 'tense': 'PRES', 'person': [1, 2], 'number': None},
}

# Gerund/Present participle (VBG)
GERUND_VERBS = {
    'buying': {'pos': 'VBG', 'lemma': 'buy', 'form': 'GERUND'},
    'reading': {'pos': 'VBG', 'lemma': 'read', 'form': 'GERUND'},
    'helping': {'pos': 'VBG', 'lemma': 'help', 'form': 'GERUND'},
    'telling': {'pos': 'VBG', 'lemma': 'tell', 'form': 'GERUND'},
    'watching': {'pos': 'VBG', 'lemma': 'watch', 'form': 'GERUND'},
    'attending': {'pos': 'VBG', 'lemma': 'attend', 'form': 'GERUND'},
    'coming': {'pos': 'VBG', 'lemma': 'come', 'form': 'GERUND'},
    'listening': {'pos': 'VBG', 'lemma': 'listen', 'form': 'GERUND'},
    'enjoying': {'pos': 'VBG', 'lemma': 'enjoy', 'form': 'GERUND'},
    'going': {'pos': 'VBG', 'lemma': 'go', 'form': 'GERUND'},
    'being': {'pos': 'VBG', 'lemma': 'be', 'form': 'GERUND'},
    'having': {'pos': 'VBG', 'lemma': 'have', 'form': 'GERUND'},
    'giving': {'pos': 'VBG', 'lemma': 'give', 'form': 'GERUND'},
    'taking': {'pos': 'VBG', 'lemma': 'take', 'form': 'GERUND'},
    'making': {'pos': 'VBG', 'lemma': 'make', 'form': 'GERUND'},
    'getting': {'pos': 'VBG', 'lemma': 'get', 'form': 'GERUND'},
    'seeing': {'pos': 'VBG', 'lemma': 'see', 'form': 'GERUND'},
    'knowing': {'pos': 'VBG', 'lemma': 'know', 'form': 'GERUND'},
    'thinking': {'pos': 'VBG', 'lemma': 'think', 'form': 'GERUND'},
    'finding': {'pos': 'VBG', 'lemma': 'find', 'form': 'GERUND'},
    'saying': {'pos': 'VBG', 'lemma': 'say', 'form': 'GERUND'},
    'putting': {'pos': 'VBG', 'lemma': 'put', 'form': 'GERUND'},
    'running': {'pos': 'VBG', 'lemma': 'run', 'form': 'GERUND'},
    'writing': {'pos': 'VBG', 'lemma': 'write', 'form': 'GERUND'},
    'eating': {'pos': 'VBG', 'lemma': 'eat', 'form': 'GERUND'},
    'drinking': {'pos': 'VBG', 'lemma': 'drink', 'form': 'GERUND'},
    'singing': {'pos': 'VBG', 'lemma': 'sing', 'form': 'GERUND'},
    'swimming': {'pos': 'VBG', 'lemma': 'swim', 'form': 'GERUND'},
    'walking': {'pos': 'VBG', 'lemma': 'walk', 'form': 'GERUND'},
    'talking': {'pos': 'VBG', 'lemma': 'talk', 'form': 'GERUND'},
    'speaking': {'pos': 'VBG', 'lemma': 'speak', 'form': 'GERUND'},
    'working': {'pos': 'VBG', 'lemma': 'work', 'form': 'GERUND'},
    'living': {'pos': 'VBG', 'lemma': 'live', 'form': 'GERUND'},
    'moving': {'pos': 'VBG', 'lemma': 'move', 'form': 'GERUND'},
    'playing': {'pos': 'VBG', 'lemma': 'play', 'form': 'GERUND'},
    'opening': {'pos': 'VBG', 'lemma': 'open', 'form': 'GERUND'},
    'closing': {'pos': 'VBG', 'lemma': 'close', 'form': 'GERUND'},
    'starting': {'pos': 'VBG', 'lemma': 'start', 'form': 'GERUND'},
    'stopping': {'pos': 'VBG', 'lemma': 'stop', 'form': 'GERUND'},
    'beginning': {'pos': 'VBG', 'lemma': 'begin', 'form': 'GERUND'},
    'finishing': {'pos': 'VBG', 'lemma': 'finish', 'form': 'GERUND'},
    'showing': {'pos': 'VBG', 'lemma': 'show', 'form': 'GERUND'},
    'leaving': {'pos': 'VBG', 'lemma': 'leave', 'form': 'GERUND'},
    'calling': {'pos': 'VBG', 'lemma': 'call', 'form': 'GERUND'},
    'trying': {'pos': 'VBG', 'lemma': 'try', 'form': 'GERUND'},
    'asking': {'pos': 'VBG', 'lemma': 'ask', 'form': 'GERUND'},
    'needing': {'pos': 'VBG', 'lemma': 'need', 'form': 'GERUND'},
    'feeling': {'pos': 'VBG', 'lemma': 'feel', 'form': 'GERUND'},
    'becoming': {'pos': 'VBG', 'lemma': 'become', 'form': 'GERUND'},
    'bringing': {'pos': 'VBG', 'lemma': 'bring', 'form': 'GERUND'},
    'holding': {'pos': 'VBG', 'lemma': 'hold', 'form': 'GERUND'},
    'turning': {'pos': 'VBG', 'lemma': 'turn', 'form': 'GERUND'},
    'following': {'pos': 'VBG', 'lemma': 'follow', 'form': 'GERUND'},
    'waiting': {'pos': 'VBG', 'lemma': 'wait', 'form': 'GERUND'},
}

# Past participle (VBN)
PARTICIPLE_VERBS = {
    'bought': {'pos': 'VBN', 'lemma': 'buy', 'form': 'PARTICIPLE'},
    'read': {'pos': 'VBN', 'lemma': 'read', 'form': 'PARTICIPLE'},
    'helped': {'pos': 'VBN', 'lemma': 'help', 'form': 'PARTICIPLE'},
    'told': {'pos': 'VBN', 'lemma': 'tell', 'form': 'PARTICIPLE'},
    'watched': {'pos': 'VBN', 'lemma': 'watch', 'form': 'PARTICIPLE'},
    'attended': {'pos': 'VBN', 'lemma': 'attend', 'form': 'PARTICIPLE'},
    'come': {'pos': 'VBN', 'lemma': 'come', 'form': 'PARTICIPLE'},
    'listened': {'pos': 'VBN', 'lemma': 'listen', 'form': 'PARTICIPLE'},
    'enjoyed': {'pos': 'VBN', 'lemma': 'enjoy', 'form': 'PARTICIPLE'},
    'gone': {'pos': 'VBN', 'lemma': 'go', 'form': 'PARTICIPLE'},
    'been': {'pos': 'VBN', 'lemma': 'be', 'form': 'PARTICIPLE'},
    'had': {'pos': 'VBN', 'lemma': 'have', 'form': 'PARTICIPLE'},
    'given': {'pos': 'VBN', 'lemma': 'give', 'form': 'PARTICIPLE'},
    'taken': {'pos': 'VBN', 'lemma': 'take', 'form': 'PARTICIPLE'},
    'made': {'pos': 'VBN', 'lemma': 'make', 'form': 'PARTICIPLE'},
    'gotten': {'pos': 'VBN', 'lemma': 'get', 'form': 'PARTICIPLE'},
    'seen': {'pos': 'VBN', 'lemma': 'see', 'form': 'PARTICIPLE'},
    'known': {'pos': 'VBN', 'lemma': 'know', 'form': 'PARTICIPLE'},
    'thought': {'pos': 'VBN', 'lemma': 'think', 'form': 'PARTICIPLE'},
    'found': {'pos': 'VBN', 'lemma': 'find', 'form': 'PARTICIPLE'},
    'said': {'pos': 'VBN', 'lemma': 'say', 'form': 'PARTICIPLE'},
    'put': {'pos': 'VBN', 'lemma': 'put', 'form': 'PARTICIPLE'},
    'run': {'pos': 'VBN', 'lemma': 'run', 'form': 'PARTICIPLE'},
    'written': {'pos': 'VBN', 'lemma': 'write', 'form': 'PARTICIPLE'},
    'eaten': {'pos': 'VBN', 'lemma': 'eat', 'form': 'PARTICIPLE'},
    'drunk': {'pos': 'VBN', 'lemma': 'drink', 'form': 'PARTICIPLE'},
    'sung': {'pos': 'VBN', 'lemma': 'sing', 'form': 'PARTICIPLE'},
    'swum': {'pos': 'VBN', 'lemma': 'swim', 'form': 'PARTICIPLE'},
    'walked': {'pos': 'VBN', 'lemma': 'walk', 'form': 'PARTICIPLE'},
    'talked': {'pos': 'VBN', 'lemma': 'talk', 'form': 'PARTICIPLE'},
    'spoken': {'pos': 'VBN', 'lemma': 'speak', 'form': 'PARTICIPLE'},
    'worked': {'pos': 'VBN', 'lemma': 'work', 'form': 'PARTICIPLE'},
    'lived': {'pos': 'VBN', 'lemma': 'live', 'form': 'PARTICIPLE'},
    'moved': {'pos': 'VBN', 'lemma': 'move', 'form': 'PARTICIPLE'},
    'played': {'pos': 'VBN', 'lemma': 'play', 'form': 'PARTICIPLE'},
    'opened': {'pos': 'VBN', 'lemma': 'open', 'form': 'PARTICIPLE'},
    'closed': {'pos': 'VBN', 'lemma': 'close', 'form': 'PARTICIPLE'},
    'started': {'pos': 'VBN', 'lemma': 'start', 'form': 'PARTICIPLE'},
    'stopped': {'pos': 'VBN', 'lemma': 'stop', 'form': 'PARTICIPLE'},
    'begun': {'pos': 'VBN', 'lemma': 'begin', 'form': 'PARTICIPLE'},
    'finished': {'pos': 'VBN', 'lemma': 'finish', 'form': 'PARTICIPLE'},
    'shown': {'pos': 'VBN', 'lemma': 'show', 'form': 'PARTICIPLE'},
    'left': {'pos': 'VBN', 'lemma': 'leave', 'form': 'PARTICIPLE'},
    'called': {'pos': 'VBN', 'lemma': 'call', 'form': 'PARTICIPLE'},
    'tried': {'pos': 'VBN', 'lemma': 'try', 'form': 'PARTICIPLE'},
    'asked': {'pos': 'VBN', 'lemma': 'ask', 'form': 'PARTICIPLE'},
    'needed': {'pos': 'VBN', 'lemma': 'need', 'form': 'PARTICIPLE'},
    'felt': {'pos': 'VBN', 'lemma': 'feel', 'form': 'PARTICIPLE'},
    'become': {'pos': 'VBN', 'lemma': 'become', 'form': 'PARTICIPLE'},
    'brought': {'pos': 'VBN', 'lemma': 'bring', 'form': 'PARTICIPLE'},
    'held': {'pos': 'VBN', 'lemma': 'hold', 'form': 'PARTICIPLE'},
    'turned': {'pos': 'VBN', 'lemma': 'turn', 'form': 'PARTICIPLE'},
    'followed': {'pos': 'VBN', 'lemma': 'follow', 'form': 'PARTICIPLE'},
    'waited': {'pos': 'VBN', 'lemma': 'wait', 'form': 'PARTICIPLE'},
}

# Adjectives (JJ)
ADJECTIVES = {
    'beautiful': {'pos': 'JJ', 'degree': 'POS'},
    'historical': {'pos': 'JJ', 'degree': 'POS'},
    'national': {'pos': 'JJ', 'degree': 'POS'},
    'loud': {'pos': 'JJ', 'degree': 'POS'},
    'far': {'pos': 'JJ', 'degree': 'POS'},
    'good': {'pos': 'JJ', 'degree': 'POS'},
    'bad': {'pos': 'JJ', 'degree': 'POS'},
    'big': {'pos': 'JJ', 'degree': 'POS'},
    'small': {'pos': 'JJ', 'degree': 'POS'},
    'old': {'pos': 'JJ', 'degree': 'POS'},
    'young': {'pos': 'JJ', 'degree': 'POS'},
    'new': {'pos': 'JJ', 'degree': 'POS'},
    'long': {'pos': 'JJ', 'degree': 'POS'},
    'short': {'pos': 'JJ', 'degree': 'POS'},
    'high': {'pos': 'JJ', 'degree': 'POS'},
    'low': {'pos': 'JJ', 'degree': 'POS'},
    'great': {'pos': 'JJ', 'degree': 'POS'},
    'little': {'pos': 'JJ', 'degree': 'POS'},
    'own': {'pos': 'JJ', 'degree': 'POS'},
    'other': {'pos': 'JJ', 'degree': 'POS'},
    'same': {'pos': 'JJ', 'degree': 'POS'},
    'different': {'pos': 'JJ', 'degree': 'POS'},
    'important': {'pos': 'JJ', 'degree': 'POS'},
    'large': {'pos': 'JJ', 'degree': 'POS'},
    'public': {'pos': 'JJ', 'degree': 'POS'},
    'early': {'pos': 'JJ', 'degree': 'POS'},
    'late': {'pos': 'JJ', 'degree': 'POS'},
    'possible': {'pos': 'JJ', 'degree': 'POS'},
    'able': {'pos': 'JJ', 'degree': 'POS'},
    'full': {'pos': 'JJ', 'degree': 'POS'},
    'free': {'pos': 'JJ', 'degree': 'POS'},
    'right': {'pos': 'JJ', 'degree': 'POS'},
    'wrong': {'pos': 'JJ', 'degree': 'POS'},
    'sure': {'pos': 'JJ', 'degree': 'POS'},
    'happy': {'pos': 'JJ', 'degree': 'POS'},
    'sad': {'pos': 'JJ', 'degree': 'POS'},
    'easy': {'pos': 'JJ', 'degree': 'POS'},
    'hard': {'pos': 'JJ', 'degree': 'POS'},
    'difficult': {'pos': 'JJ', 'degree': 'POS'},
    'simple': {'pos': 'JJ', 'degree': 'POS'},
    'clear': {'pos': 'JJ', 'degree': 'POS'},
    'open': {'pos': 'JJ', 'degree': 'POS'},
    'close': {'pos': 'JJ', 'degree': 'POS'},
    'hot': {'pos': 'JJ', 'degree': 'POS'},
    'cold': {'pos': 'JJ', 'degree': 'POS'},
    'warm': {'pos': 'JJ', 'degree': 'POS'},
    'cool': {'pos': 'JJ', 'degree': 'POS'},
    'fast': {'pos': 'JJ', 'degree': 'POS'},
    'slow': {'pos': 'JJ', 'degree': 'POS'},
    'quiet': {'pos': 'JJ', 'degree': 'POS'},
}

# Comparative adjectives (JJR)
COMPARATIVE_ADJECTIVES = {
    'better': {'pos': 'JJR', 'lemma': 'good', 'degree': 'COMP'},
    'worse': {'pos': 'JJR', 'lemma': 'bad', 'degree': 'COMP'},
    'bigger': {'pos': 'JJR', 'lemma': 'big', 'degree': 'COMP'},
    'smaller': {'pos': 'JJR', 'lemma': 'small', 'degree': 'COMP'},
    'older': {'pos': 'JJR', 'lemma': 'old', 'degree': 'COMP'},
    'younger': {'pos': 'JJR', 'lemma': 'young', 'degree': 'COMP'},
    'newer': {'pos': 'JJR', 'lemma': 'new', 'degree': 'COMP'},
    'longer': {'pos': 'JJR', 'lemma': 'long', 'degree': 'COMP'},
    'shorter': {'pos': 'JJR', 'lemma': 'short', 'degree': 'COMP'},
    'higher': {'pos': 'JJR', 'lemma': 'high', 'degree': 'COMP'},
    'lower': {'pos': 'JJR', 'lemma': 'low', 'degree': 'COMP'},
    'greater': {'pos': 'JJR', 'lemma': 'great', 'degree': 'COMP'},
    'larger': {'pos': 'JJR', 'lemma': 'large', 'degree': 'COMP'},
    'earlier': {'pos': 'JJR', 'lemma': 'early', 'degree': 'COMP'},
    'later': {'pos': 'JJR', 'lemma': 'late', 'degree': 'COMP'},
    'happier': {'pos': 'JJR', 'lemma': 'happy', 'degree': 'COMP'},
    'easier': {'pos': 'JJR', 'lemma': 'easy', 'degree': 'COMP'},
    'harder': {'pos': 'JJR', 'lemma': 'hard', 'degree': 'COMP'},
    'faster': {'pos': 'JJR', 'lemma': 'fast', 'degree': 'COMP'},
    'slower': {'pos': 'JJR', 'lemma': 'slow', 'degree': 'COMP'},
    'farther': {'pos': 'JJR', 'lemma': 'far', 'degree': 'COMP'},
    'further': {'pos': 'JJR', 'lemma': 'far', 'degree': 'COMP'},
    'more': {'pos': 'JJR', 'lemma': 'much', 'degree': 'COMP'},
    'less': {'pos': 'JJR', 'lemma': 'little', 'degree': 'COMP'},
}

# Superlative adjectives (JJS)
SUPERLATIVE_ADJECTIVES = {
    'best': {'pos': 'JJS', 'lemma': 'good', 'degree': 'SUPER'},
    'worst': {'pos': 'JJS', 'lemma': 'bad', 'degree': 'SUPER'},
    'biggest': {'pos': 'JJS', 'lemma': 'big', 'degree': 'SUPER'},
    'smallest': {'pos': 'JJS', 'lemma': 'small', 'degree': 'SUPER'},
    'oldest': {'pos': 'JJS', 'lemma': 'old', 'degree': 'SUPER'},
    'youngest': {'pos': 'JJS', 'lemma': 'young', 'degree': 'SUPER'},
    'newest': {'pos': 'JJS', 'lemma': 'new', 'degree': 'SUPER'},
    'longest': {'pos': 'JJS', 'lemma': 'long', 'degree': 'SUPER'},
    'shortest': {'pos': 'JJS', 'lemma': 'short', 'degree': 'SUPER'},
    'highest': {'pos': 'JJS', 'lemma': 'high', 'degree': 'SUPER'},
    'lowest': {'pos': 'JJS', 'lemma': 'low', 'degree': 'SUPER'},
    'greatest': {'pos': 'JJS', 'lemma': 'great', 'degree': 'SUPER'},
    'largest': {'pos': 'JJS', 'lemma': 'large', 'degree': 'SUPER'},
    'earliest': {'pos': 'JJS', 'lemma': 'early', 'degree': 'SUPER'},
    'latest': {'pos': 'JJS', 'lemma': 'late', 'degree': 'SUPER'},
    'happiest': {'pos': 'JJS', 'lemma': 'happy', 'degree': 'SUPER'},
    'easiest': {'pos': 'JJS', 'lemma': 'easy', 'degree': 'SUPER'},
    'hardest': {'pos': 'JJS', 'lemma': 'hard', 'degree': 'SUPER'},
    'fastest': {'pos': 'JJS', 'lemma': 'fast', 'degree': 'SUPER'},
    'slowest': {'pos': 'JJS', 'lemma': 'slow', 'degree': 'SUPER'},
    'farthest': {'pos': 'JJS', 'lemma': 'far', 'degree': 'SUPER'},
    'furthest': {'pos': 'JJS', 'lemma': 'far', 'degree': 'SUPER'},
    'most': {'pos': 'JJS', 'lemma': 'much', 'degree': 'SUPER'},
    'least': {'pos': 'JJS', 'lemma': 'little', 'degree': 'SUPER'},
}


# ============================================================================
# LEXICON CLASS
# ============================================================================

class Lexicon:
    """Main lexicon class that combines all word categories."""

    def __init__(self):
        self.morphological_analyzer = MorphologicalAnalyzer()

        # Combine all dictionaries
        self.entries = {}
        self._add_entries(DETERMINERS)
        self._add_entries(PERSONAL_PRONOUNS)
        self._add_entries(POSSESSIVE_PRONOUNS)
        self._add_entries(MODALS)
        self._add_entries(PREPOSITIONS)
        self._add_entries(CONJUNCTIONS)
        self._add_entries(WH_ADVERBS)
        self._add_entries(WH_PRONOUNS)
        self._add_entries(ADVERBS)
        self._add_entries(TO_PARTICLE)
        self._add_entries(NOUNS)
        self._add_entries(PLURAL_NOUNS)
        self._add_entries(PROPER_NOUNS)
        self._add_entries(VERBS)
        self._add_entries(PAST_VERBS)
        self._add_entries(PRESENT_3SG_VERBS)
        self._add_entries(PRESENT_NON3SG_VERBS)
        self._add_entries(GERUND_VERBS)
        self._add_entries(PARTICIPLE_VERBS)
        self._add_entries(ADJECTIVES)
        self._add_entries(COMPARATIVE_ADJECTIVES)
        self._add_entries(SUPERLATIVE_ADJECTIVES)

        # Build verb subcategorization lookup
        self._build_verb_subcat()

    def _add_entries(self, word_dict):
        """Add entries from a dictionary to the lexicon."""
        for word, features in word_dict.items():
            word_lower = word.lower()
            if word_lower not in self.entries:
                self.entries[word_lower] = []
            self.entries[word_lower].append(features.copy())

    def _build_verb_subcat(self):
        """Build verb subcategorization lookup from base verbs."""
        self.verb_subcat = {}
        for word, features in VERBS.items():
            if 'subcat' in features:
                self.verb_subcat[word] = features['subcat']
                if 'prep' in features:
                    self.verb_subcat[word + '_prep'] = features['prep']

    def lookup(self, word):
        """
        Look up a word in the lexicon.
        Returns a list of possible lexical entries with features.
        """
        word_lower = word.lower()

        if word_lower in self.entries:
            return self.entries[word_lower]

        # Try morphological analysis for unknown words
        return self._analyze_unknown(word)

    def _analyze_unknown(self, word):
        """Analyze an unknown word using morphology."""
        analyses = self.morphological_analyzer.analyze(word)
        entries = []

        for analysis in analyses:
            # Try to find the lemma in the lexicon
            if analysis.lemma in self.entries:
                for entry in self.entries[analysis.lemma]:
                    new_entry = entry.copy()
                    new_entry.update(analysis.features)
                    entries.append(new_entry)

        return entries if entries else None

    def get_pos_tags(self, word):
        """Get all possible POS tags for a word."""
        entries = self.lookup(word)
        if entries:
            return list(set(e['pos'] for e in entries))
        return []

    def get_features(self, word, pos=None):
        """Get features for a word, optionally filtered by POS."""
        entries = self.lookup(word)
        if not entries:
            return None

        if pos:
            entries = [e for e in entries if e.get('pos') == pos]

        return entries[0] if entries else None

    def get_verb_subcat(self, verb_lemma):
        """Get subcategorization frame for a verb."""
        return self.verb_subcat.get(verb_lemma, ['NP'])  # Default to transitive

    def has_word(self, word):
        """Check if a word is in the lexicon."""
        return word.lower() in self.entries or self._analyze_unknown(word) is not None


# Global lexicon instance
_lexicon = None


def get_lexicon():
    """Get the global lexicon instance."""
    global _lexicon
    if _lexicon is None:
        _lexicon = Lexicon()
    return _lexicon


# Demo
if __name__ == '__main__':
    lexicon = get_lexicon()

    test_words = [
        'I', 'bought', 'a', 'present', 'for', 'my', 'friend', 'yesterday',
        'beautiful', 'novels', 'went', 'is', 'will', 'not', 'the', 'most'
    ]

    print("Lexicon Lookup Examples:")
    print("=" * 60)
    for word in test_words:
        entries = lexicon.lookup(word)
        pos_tags = lexicon.get_pos_tags(word)
        print(f"\n{word}:")
        print(f"  POS tags: {pos_tags}")
        if entries:
            for entry in entries[:2]:  # Show first 2 entries
                print(f"  Entry: {entry}")
