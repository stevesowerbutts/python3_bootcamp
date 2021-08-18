from exercise import Card, Deck
import unittest


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_init(self):
        """cards should have a suit and value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """cards should return a string of 'value of suit'"""
        self.assertEqual(repr(self.card), "A of Hearts")

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """decks should have cards attribute, which is a list of len 52"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """should return string 'Deck of count cards'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

if __name__ == '__main__':
    unittest.main()
