
from __future__ import absolute_import
import string
import random
from passwords import passwords
from django.test import TestCase


class TestPasswordGeneration(TestCase):

    def test_length_more_than_character_set(self):
        """
        This test makes sure that if the requested length of the password is not possible (for example, if
        the request is for a 50 character password with no repeated characters, but the set of characters
        to choose from is only uppercase ascii letters) then an exception will be thrown.
        """

        characters = string.ascii_lowercase
        self.assertRaises(passwords.RequestedPasswordTooLong, passwords.generate_password,
                          characters, 50, 50, repeats_allowed=False)


    def test_length_range(self):

        characters = string.letters
        for _ in range(0, 1000):
            min_length = random.randint(1, 50)
            max_length = random.randint(0, 20) + min_length

            password = passwords.generate_password(characters, min_length, max_length)
            self.assertLessEqual(min_length, len(password))
            self.assertGreaterEqual(max_length, len(password))

    def test_no_mystery_characters(self):

        for _ in range(0, 1000):
            count = random.randint(1, len(string.printable))
            characters = random.sample(string.printable, count)
            password = passwords.generate_password(characters, 20, 30)
            for char in password:
                self.assertIn(char, characters)
