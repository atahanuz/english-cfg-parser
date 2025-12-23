"""
Context-Free Grammar for English in Chomsky Normal Form (CNF)

The grammar handles:
1. Declarative sentences (SVO)
2. Imperative sentences
3. Yes/No questions
4. Wh-questions

All rules are in CNF format:
- A → B C (two non-terminals)
- A → a (one terminal - handled by lexical rules)

Features for agreement:
- number: SG/PL
- person: 1/2/3
- tense: PRES/PAST/FUT/BASE
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set, Tuple, Any


@dataclass
class Rule:
    """Represents a grammar rule with optional features."""
    lhs: str  # Left-hand side non-terminal
    rhs: Tuple[str, ...]  # Right-hand side (1 or 2 symbols)
    features: Dict[str, Any] = field(default_factory=dict)
    feature_constraints: Dict[str, str] = field(default_factory=dict)  # Feature agreement constraints

    def __hash__(self):
        return hash((self.lhs, self.rhs))

    def __eq__(self, other):
        return self.lhs == other.lhs and self.rhs == other.rhs

    def is_lexical(self):
        """Check if this is a lexical (terminal) rule."""
        return len(self.rhs) == 1

    def is_binary(self):
        """Check if this is a binary (CNF) rule."""
        return len(self.rhs) == 2

    def __repr__(self):
        rhs_str = ' '.join(self.rhs)
        if self.features:
            return f"{self.lhs}[{self.features}] → {rhs_str}"
        return f"{self.lhs} → {rhs_str}"


class Grammar:
    """
    Context-Free Grammar in Chomsky Normal Form.
    """

    def __init__(self):
        self.rules: List[Rule] = []
        self.rules_by_lhs: Dict[str, List[Rule]] = {}
        self.rules_by_rhs: Dict[Tuple[str, ...], List[Rule]] = {}
        self.lexical_rules: Dict[str, List[Rule]] = {}  # POS -> rules
        self.non_terminals: Set[str] = set()
        self.terminals: Set[str] = set()

        # Build the grammar
        self._build_grammar()

    def _build_grammar(self):
        """Build the complete grammar."""
        self._add_sentence_rules()
        self._add_noun_phrase_rules()
        self._add_verb_phrase_rules()
        self._add_prepositional_phrase_rules()
        self._add_adjective_phrase_rules()
        self._add_adverb_phrase_rules()
        self._add_question_rules()
        self._add_lexical_rules()
        self._index_rules()

    def _add_rule(self, lhs: str, rhs: Tuple[str, ...], features: Dict = None, constraints: Dict = None):
        """Add a rule to the grammar."""
        rule = Rule(
            lhs=lhs,
            rhs=rhs,
            features=features or {},
            feature_constraints=constraints or {}
        )
        self.rules.append(rule)
        self.non_terminals.add(lhs)

    def _index_rules(self):
        """Index rules for efficient lookup."""
        for rule in self.rules:
            # Index by LHS
            if rule.lhs not in self.rules_by_lhs:
                self.rules_by_lhs[rule.lhs] = []
            self.rules_by_lhs[rule.lhs].append(rule)

            # Index binary rules by RHS
            if rule.is_binary():
                if rule.rhs not in self.rules_by_rhs:
                    self.rules_by_rhs[rule.rhs] = []
                self.rules_by_rhs[rule.rhs].append(rule)

            # Index lexical rules by POS (terminal)
            if rule.is_lexical():
                pos = rule.rhs[0]
                if pos not in self.lexical_rules:
                    self.lexical_rules[pos] = []
                self.lexical_rules[pos].append(rule)

    # =========================================================================
    # SENTENCE RULES
    # =========================================================================

    def _add_sentence_rules(self):
        """Add sentence-level rules."""

        # Declarative sentences: S → NP VP
        # "I bought a present"
        self._add_rule('S', ('NP', 'VP'),
                       features={'type': 'DECL'},
                       constraints={'number': 'agree', 'person': 'agree'})

        # S with trailing adverb: S → S_core ADVP
        # "I bought a present yesterday"
        self._add_rule('S', ('S_CORE', 'ADVP'),
                       features={'type': 'DECL'})

        # S with initial adverb: S → ADVP S_core
        self._add_rule('S', ('ADVP', 'S_CORE'),
                       features={'type': 'DECL'})

        # Core sentence (for adverb attachment)
        self._add_rule('S_CORE', ('NP', 'VP'),
                       constraints={'number': 'agree', 'person': 'agree'})

        # Imperative sentences: S → VP (bare)
        # "Listen to music"
        self._add_rule('S', ('IMP',),  # Single non-terminal for imperative
                       features={'type': 'IMP', 'person': 2})

        # IMP → VP_IMP (for imperative verb phrases)
        self._add_rule('IMP', ('VP_IMP',))

        # Negative imperative: IMP → RB VP_IMP
        # "Do not listen"
        self._add_rule('IMP', ('RB', 'VP_IMP'))

        # "Do not listen" with MD + RB pattern
        # S → MD_DO IMP_NEG where MD_DO is "do" and IMP_NEG handles "not listen"
        self._add_rule('S', ('MD', 'IMP_NEG'),
                       features={'type': 'IMP_NEG'})
        self._add_rule('IMP_NEG', ('RB', 'VP_BASE'))

    # =========================================================================
    # NOUN PHRASE RULES
    # =========================================================================

    def _add_noun_phrase_rules(self):
        """Add noun phrase rules."""

        # NP → PRP (pronoun)
        # "I", "you", "he"
        self._add_rule('NP', ('PRP',))

        # NP → NNP (proper noun)
        # "John", "Mary"
        self._add_rule('NP', ('NNP',))

        # NP → NBAR (bare noun - for mass nouns and bare plurals)
        # "Epics tell...", "Watermelon is..."
        self._add_rule('NP', ('NBAR',))

        # NP → ADJP_N (adjective + noun without determiner)
        # "historical novels", "loud music"
        self._add_rule('NP', ('ADJP_N',))

        # NP → DT NBAR
        # "the book", "a friend"
        self._add_rule('NP', ('DT', 'NBAR'),
                       constraints={'number': 'agree'})

        # NP → DT ADJP_N (det + adj phrase + noun)
        # "the beautiful book" via intermediate
        self._add_rule('NP', ('DT', 'ADJP_N'),
                       constraints={'number': 'agree'})

        # NP → PRP$ NBAR (possessive + noun)
        # "my friend", "his book"
        self._add_rule('NP', ('PRP$', 'NBAR'))

        # NP → PRP$ ADJP_N
        # "my beautiful friend"
        self._add_rule('NP', ('PRP$', 'ADJP_N'))

        # NP → NP PP (noun phrase with PP attachment)
        # "the book on the table"
        self._add_rule('NP', ('NP', 'PP'))

        # NBAR rules
        # NBAR → NN (singular noun)
        self._add_rule('NBAR', ('NN',),
                       features={'number': 'SG'})

        # NBAR → NNS (plural noun)
        self._add_rule('NBAR', ('NNS',),
                       features={'number': 'PL'})

        # NBAR → NN NN (compound noun)
        # "school bus"
        self._add_rule('NBAR', ('NN', 'NN'),
                       features={'number': 'SG'})

        # NBAR → NBAR NN (compound noun extension)
        self._add_rule('NBAR', ('NBAR', 'NN'))

        # Coordination: NBAR → NBAR CONJ_NBAR
        # "culture and history"
        self._add_rule('NBAR', ('NBAR', 'CONJ_NBAR'),
                       features={'number': 'PL'})
        self._add_rule('CONJ_NBAR', ('CC', 'NBAR'))

        # ADJP_N → JJ NBAR (adjective + noun bar)
        # "beautiful book"
        self._add_rule('ADJP_N', ('JJ', 'NBAR'))

        # ADJP_N → JJ ADJP_N (stacked adjectives)
        # "big beautiful book"
        self._add_rule('ADJP_N', ('JJ', 'ADJP_N'))

        # ADJP_N → ADJP NBAR (adj phrase + noun bar)
        self._add_rule('ADJP_N', ('ADJP', 'NBAR'))

        # ADJP_N → JJS NBAR (superlative)
        # "most beautiful fruit"
        self._add_rule('ADJP_N', ('JJS', 'NBAR'))

        # ADJP_N → ADVJJ NBAR (adverb-modified adj + noun)
        self._add_rule('ADJP_N', ('ADVJJ', 'NBAR'))

        # ADVJJ → RB JJ
        # "very beautiful"
        self._add_rule('ADVJJ', ('RB', 'JJ'))

        # For "the most beautiful fruit" pattern
        # ADJP_N → DT_JJS NBAR doesn't work in CNF
        # Use: NP → DT SUPNBAR
        # SUPNBAR → JJS NBAR
        self._add_rule('SUPNBAR', ('JJS', 'NBAR'))
        self._add_rule('NP', ('DT', 'SUPNBAR'))

        # For "the most beautiful X" with RB JJS pattern
        # "the most beautiful fruit"
        self._add_rule('RBJJS', ('RB', 'JJ'))  # "most beautiful"
        self._add_rule('ADJP_N', ('RBJJS', 'NBAR'))

    # =========================================================================
    # VERB PHRASE RULES
    # =========================================================================

    def _add_verb_phrase_rules(self):
        """Add verb phrase rules."""

        # -------------------------
        # Intransitive verbs
        # -------------------------

        # VP → VBZ (3sg present intransitive)
        # "He runs"
        self._add_rule('VP', ('VBZ',),
                       features={'tense': 'PRES', 'person': 3, 'number': 'SG'})

        # VP → VBP (non-3sg present intransitive)
        # "I run", "They run"
        self._add_rule('VP', ('VBP',),
                       features={'tense': 'PRES', 'person': [1, 2], 'number': None})

        # VP → VBD (past intransitive)
        # "He ran"
        self._add_rule('VP', ('VBD',),
                       features={'tense': 'PAST'})

        # -------------------------
        # Transitive verbs with NP
        # -------------------------

        # VP → VBZ NP (3sg present transitive)
        # "He buys a book"
        self._add_rule('VP', ('VBZ', 'NP'),
                       features={'tense': 'PRES', 'person': 3, 'number': 'SG'})

        # VP → VBP NP (non-3sg present transitive)
        # "I buy a book"
        self._add_rule('VP', ('VBP', 'NP'),
                       features={'tense': 'PRES', 'person': [1, 2], 'number': None})

        # VP → VBD NP (past transitive)
        # "He bought a book"
        self._add_rule('VP', ('VBD', 'NP'),
                       features={'tense': 'PAST'})

        # -------------------------
        # Verbs with PP
        # -------------------------

        # VP → VBZ PP (3sg present + PP)
        # "He goes to school"
        self._add_rule('VP', ('VBZ', 'PP'),
                       features={'tense': 'PRES', 'person': 3, 'number': 'SG'})

        # VP → VBP PP (non-3sg present + PP)
        self._add_rule('VP', ('VBP', 'PP'),
                       features={'tense': 'PRES', 'person': [1, 2], 'number': None})

        # VP → VBD PP (past + PP)
        # "He went to school"
        self._add_rule('VP', ('VBD', 'PP'),
                       features={'tense': 'PAST'})

        # -------------------------
        # Verbs with NP + PP
        # -------------------------

        # VP → V_NP PP
        # "bought a present for my friend"
        self._add_rule('VP', ('V_NP', 'PP'),
                       features={'tense': 'inherit'})

        # V_NP → VBZ NP
        self._add_rule('V_NP', ('VBZ', 'NP'),
                       features={'tense': 'PRES', 'person': 3, 'number': 'SG'})

        # V_NP → VBP NP
        self._add_rule('V_NP', ('VBP', 'NP'),
                       features={'tense': 'PRES', 'person': [1, 2], 'number': None})

        # V_NP → VBD NP
        self._add_rule('V_NP', ('VBD', 'NP'),
                       features={'tense': 'PAST'})

        # -------------------------
        # VP with adverb
        # -------------------------

        # VP → VP ADVP
        # "ran quickly"
        self._add_rule('VP', ('VP', 'ADVP'))

        # VP → ADVP VP
        # "quickly ran"
        self._add_rule('VP', ('ADVP', 'VP'))

        # VP → VP PP (VP with PP attachment)
        # "watched the moonlight under this tree"
        self._add_rule('VP', ('VP', 'PP'))

        # -------------------------
        # Modal verbs
        # -------------------------

        # VP → MD VP_BASE
        # "will attend", "can go"
        self._add_rule('VP', ('MD', 'VP_BASE'),
                       features={'tense': 'FUT'})

        # VP_BASE → VB (base form intransitive)
        self._add_rule('VP_BASE', ('VB',),
                       features={'form': 'BASE'})

        # VP_BASE → VB NP (base form transitive)
        self._add_rule('VP_BASE', ('VB', 'NP'),
                       features={'form': 'BASE'})

        # VP_BASE → VB PP
        self._add_rule('VP_BASE', ('VB', 'PP'),
                       features={'form': 'BASE'})

        # VP_BASE → V_NP_BASE PP
        self._add_rule('VP_BASE', ('V_NP_BASE', 'PP'))
        self._add_rule('V_NP_BASE', ('VB', 'NP'))

        # VP_BASE with adverb
        self._add_rule('VP_BASE', ('VP_BASE', 'ADVP'))
        self._add_rule('VP_BASE', ('ADVP', 'VP_BASE'))

        # -------------------------
        # Copula (be) constructions
        # -------------------------

        # VP → VBZ ADJP (is beautiful)
        self._add_rule('VP', ('VBZ', 'ADJP'),
                       features={'tense': 'PRES', 'person': 3, 'number': 'SG'})

        # VP → VBP ADJP (am/are beautiful)
        self._add_rule('VP', ('VBP', 'ADJP'),
                       features={'tense': 'PRES'})

        # VP → VBD ADJP (was/were beautiful)
        self._add_rule('VP', ('VBD', 'ADJP'),
                       features={'tense': 'PAST'})

        # VP → VBZ NP (is a teacher)
        # Already covered by transitive

        # VP → VBD RB_ADJP (was quite far)
        self._add_rule('RB_ADJP', ('RB', 'ADJP'))
        self._add_rule('VP', ('VBD', 'RB_ADJP'))
        self._add_rule('VP', ('VBZ', 'RB_ADJP'))
        self._add_rule('VP', ('VBP', 'RB_ADJP'))

        # -------------------------
        # Imperative VP
        # -------------------------

        # VP_IMP → VB (base form)
        self._add_rule('VP_IMP', ('VB',),
                       features={'form': 'BASE', 'person': 2})

        # VP_IMP → VB NP
        self._add_rule('VP_IMP', ('VB', 'NP'),
                       features={'form': 'BASE', 'person': 2})

        # VP_IMP → VB PP
        self._add_rule('VP_IMP', ('VB', 'PP'),
                       features={'form': 'BASE', 'person': 2})

        # VP_IMP → V_NP_BASE PP
        self._add_rule('VP_IMP', ('V_NP_BASE', 'PP'),
                       features={'form': 'BASE', 'person': 2})

    # =========================================================================
    # PREPOSITIONAL PHRASE RULES
    # =========================================================================

    def _add_prepositional_phrase_rules(self):
        """Add prepositional phrase rules."""

        # PP → IN NP
        # "for my friend", "to school"
        self._add_rule('PP', ('IN', 'NP'))

        # PP → TO NP (infinitive marker as prep)
        # Note: TO can also be a preposition
        self._add_rule('PP', ('TO', 'NP'))

    # =========================================================================
    # ADJECTIVE PHRASE RULES
    # =========================================================================

    def _add_adjective_phrase_rules(self):
        """Add adjective phrase rules."""

        # ADJP → JJ (simple adjective)
        # "beautiful"
        self._add_rule('ADJP', ('JJ',))

        # ADJP → RB JJ (adverb + adjective)
        # "very beautiful", "quite far"
        self._add_rule('ADJP', ('RB', 'JJ'))

        # ADJP → JJR (comparative)
        # "better", "bigger"
        self._add_rule('ADJP', ('JJR',))

        # ADJP → JJS (superlative)
        # "best", "biggest"
        self._add_rule('ADJP', ('JJS',))

        # ADJP → RB JJS
        # "most beautiful" - 'most' can be RB
        self._add_rule('ADJP', ('RB', 'JJS'))

        # ADJP → ADJP PP (adjective with PP)
        # "far from the village"
        self._add_rule('ADJP', ('ADJP', 'PP'))

    # =========================================================================
    # ADVERB PHRASE RULES
    # =========================================================================

    def _add_adverb_phrase_rules(self):
        """Add adverb phrase rules."""

        # ADVP → RB (simple adverb)
        # "yesterday", "quickly"
        self._add_rule('ADVP', ('RB',))

        # ADVP → RB RB (degree + adverb)
        # "very quickly"
        self._add_rule('ADVP', ('RB', 'RB'))

    # =========================================================================
    # QUESTION RULES
    # =========================================================================

    def _add_question_rules(self):
        """Add rules for questions."""

        # Yes/No questions: S → MD NP VP_BASE
        # "Will you attend the meeting?"
        # In CNF: S → MD S_YN
        self._add_rule('S', ('MD', 'S_YN'),
                       features={'type': 'YN_Q'})

        # S_YN → NP VP_BASE
        self._add_rule('S_YN', ('NP', 'VP_BASE'))

        # S_YN with trailing adverb
        self._add_rule('S_YN', ('S_YN_CORE', 'ADVP'))
        self._add_rule('S_YN_CORE', ('NP', 'VP_BASE'))

        # Wh-questions: S → WRB S_WH
        # "When did you come here?"
        self._add_rule('S', ('WRB', 'S_WH'),
                       features={'type': 'WH_Q'})

        # S_WH → MD S_YN
        # "did you come here"
        self._add_rule('S_WH', ('MD', 'S_YN'))

        # S_WH with trailing adverb
        self._add_rule('S_WH', ('S_WH_CORE', 'ADVP'))
        self._add_rule('S_WH_CORE', ('MD', 'S_YN'))

    # =========================================================================
    # LEXICAL RULES (Terminal rules)
    # =========================================================================

    def _add_lexical_rules(self):
        """Add lexical (terminal) rules connecting POS to categories."""
        # These map POS tags to pre-terminal categories

        # Determiners
        self._add_rule('DT', ('DT',))

        # Pronouns
        self._add_rule('PRP', ('PRP',))
        self._add_rule('PRP$', ('PRP$',))

        # Nouns
        self._add_rule('NN', ('NN',))
        self._add_rule('NNS', ('NNS',))
        self._add_rule('NNP', ('NNP',))
        self._add_rule('NNPS', ('NNPS',))

        # Verbs
        self._add_rule('VB', ('VB',))
        self._add_rule('VBD', ('VBD',))
        self._add_rule('VBG', ('VBG',))
        self._add_rule('VBN', ('VBN',))
        self._add_rule('VBP', ('VBP',))
        self._add_rule('VBZ', ('VBZ',))

        # Modals
        self._add_rule('MD', ('MD',))

        # Adjectives
        self._add_rule('JJ', ('JJ',))
        self._add_rule('JJR', ('JJR',))
        self._add_rule('JJS', ('JJS',))

        # Adverbs
        self._add_rule('RB', ('RB',))
        self._add_rule('RBR', ('RBR',))
        self._add_rule('RBS', ('RBS',))

        # Prepositions
        self._add_rule('IN', ('IN',))
        self._add_rule('TO', ('TO',))

        # Conjunctions
        self._add_rule('CC', ('CC',))

        # Wh-words
        self._add_rule('WRB', ('WRB',))
        self._add_rule('WP', ('WP',))
        self._add_rule('WDT', ('WDT',))

    # =========================================================================
    # QUERY METHODS
    # =========================================================================

    def get_rules_for_rhs(self, rhs: Tuple[str, str]) -> List[Rule]:
        """Get all rules with the given RHS."""
        return self.rules_by_rhs.get(rhs, [])

    def get_rules_for_lhs(self, lhs: str) -> List[Rule]:
        """Get all rules with the given LHS."""
        return self.rules_by_lhs.get(lhs, [])

    def get_lexical_rules_for_pos(self, pos: str) -> List[Rule]:
        """Get lexical rules for a POS tag."""
        return self.lexical_rules.get(pos, [])

    def get_all_non_terminals(self) -> Set[str]:
        """Get all non-terminal symbols."""
        return self.non_terminals

    def is_start_symbol(self, symbol: str) -> bool:
        """Check if symbol is the start symbol."""
        return symbol == 'S'

    def __repr__(self):
        return f"Grammar({len(self.rules)} rules, {len(self.non_terminals)} non-terminals)"


# Global grammar instance
_grammar = None


def get_grammar() -> Grammar:
    """Get the global grammar instance."""
    global _grammar
    if _grammar is None:
        _grammar = Grammar()
    return _grammar


# Demo
if __name__ == '__main__':
    grammar = get_grammar()

    print("English CFG Grammar")
    print("=" * 60)
    print(f"Total rules: {len(grammar.rules)}")
    print(f"Non-terminals: {len(grammar.non_terminals)}")

    print("\nSentence rules:")
    for rule in grammar.get_rules_for_lhs('S'):
        print(f"  {rule}")

    print("\nNP rules:")
    for rule in grammar.get_rules_for_lhs('NP'):
        print(f"  {rule}")

    print("\nVP rules (first 10):")
    for rule in grammar.get_rules_for_lhs('VP')[:10]:
        print(f"  {rule}")

    print("\nPP rules:")
    for rule in grammar.get_rules_for_lhs('PP'):
        print(f"  {rule}")
