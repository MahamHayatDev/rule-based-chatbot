"""Unit tests for the chatbot's core logic."""

import unittest

from chatbot.config import FALLBACK_RESPONSE
from chatbot.knowledge_base import INTENTS
from chatbot.processor import get_response, is_exit, sanitize


class TestSanitize(unittest.TestCase):
    def test_lowercase(self):
        self.assertEqual(sanitize("HELLO"), "hello")

    def test_strips_whitespace(self):
        self.assertEqual(sanitize("   hi   "), "hi")

    def test_removes_punctuation(self):
        self.assertEqual(sanitize("How are you??"), "how are you")

    def test_collapses_spaces(self):
        self.assertEqual(sanitize("good    morning"), "good morning")

    def test_empty_input(self):
        self.assertEqual(sanitize("   "), "")

    def test_space_before_punctuation(self):
        self.assertEqual(sanitize("how are you ?"), "how are you")


class TestResponses(unittest.TestCase):
    def test_known_greeting(self):
        self.assertIn("Welcome", get_response("hello"))

    def test_unknown_returns_fallback(self):
        self.assertEqual(get_response("pizza"), FALLBACK_RESPONSE)


class TestExit(unittest.TestCase):
    def test_exit_commands(self):
        for command in ("exit", "quit", "bye", "goodbye", "q"):
            self.assertTrue(is_exit(command))

    def test_normal_text_is_not_exit(self):
        self.assertFalse(is_exit("hello"))


class TestKnowledgeBase(unittest.TestCase):
    def test_every_intent_is_complete(self):
        self.assertGreaterEqual(len(INTENTS), 5)  # project requires 5+ intents
        for name, intent in INTENTS.items():
            self.assertTrue(intent["patterns"], f"{name} has no patterns")
            self.assertTrue(intent["response"], f"{name} has no response")


if __name__ == "__main__":
    unittest.main()