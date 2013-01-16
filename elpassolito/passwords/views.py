from __future__ import absolute_import
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django import forms
from passwords.models import Preset
from django.utils.translation import ugettext as _


SET_CHOICES = (
    ('digits', _('Numbers')),
    ('uppercase_ascii_letters', _('Capital letters (A-Z)')),
    ('lowercase_ascii_letters', _('Lowercase letters (a-z)')),
    ('ascii_letters', _('Letters (a-z, A-Z)')),
    ('punctuation', _('Punctuation')),
)


class PasswordGenerationForm(forms.ModelForm):
    class Meta:
        model = Preset
        exclude = ('created_by',)

    sets = forms.MultipleChoiceField(choices=SET_CHOICES,
                                     widget=forms.CheckboxSelectMultiple)

class PasswordGenerationView(FormView):
    form_class = PasswordGenerationForm
    template_name = 'passwords/generate.html'

    def get_initial(self):
        return { 'min_length': 10,
                 'max_length': 12,
                 'repeats_allowed': True,
                }

    def form_valid(self, form):
        preset = form.save(commit=False)
        print preset.generate_password()

    def get_success_url(self):
        return reverse('passwords:generate')