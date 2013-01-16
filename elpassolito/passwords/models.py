from __future__ import absolute_import

import string
from django.db import models
from django.contrib.auth.models import User
from gubbins.db.field import JSONField
from passwords import passwords


_SETS = {
    'digits': string.digits,
    'lowercase_ascii_letters': string.ascii_lowercase,
    'uppercase_ascii_letters': string.ascii_uppercase,
    'ascii_letters': string.ascii_letters,
    'punctuation': string.punctuation
}


class Preset(models.Model):

    name = models.CharField(max_length=255, blank=True)

    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)

    allowed_characters = JSONField(blank=True)
    repeats_allowed = models.BooleanField()

    min_length = models.IntegerField()
    max_length = models.IntegerField()

    def get_allowed_characters(self):
        # convert to a set to make sure there are no duplicates
        chars = set(self.allowed_characters['chars'])
        for set_name in self.allowed_characters['set_names']:
            chars += set(_SETS[set_name])
        return chars

    def generate_password(self):
        return  passwords.generate_password(self.get_allowed_characters(), self.min_length,
                                            self.max_length, self.repeats_allowed)

    def __unicode__(self):
        return self.name
