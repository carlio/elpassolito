from __future__ import absolute_import

from django.test import TestCase
from passwords.views import SET_CHOICES
from passwords.models import _SETS


class TestConsistency(TestCase):

    def test_set_choices_matches_set_options(self):
        """
        Ensures that the list of sets made available to users in the Generate Password form matches the options
        used in the models when generating passwords.
        """

        self.assertEqual( set( [x[0] for x in SET_CHOICES] ),
                          set(_SETS.keys()) )