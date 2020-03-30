from unittest import TestCase

from Backspaces import clean_string


class Test(TestCase):
    def test_clean_string(self):
        self.assertEqual(clean_string('abc#d##c'), "ac")
        self.assertEqual(clean_string('abc####d##c#'), "")
        self.assertEqual(clean_string("#######"), "")
        self.assertEqual(clean_string(""), "")
