from django.views.generic import FormView
from django import forms

class PasswordGenerationForm(forms.Form):
    pass


class PasswordGenerationView(FormView):
    form_class = PasswordGenerationForm
    template_name = 'passwords/generate.html'