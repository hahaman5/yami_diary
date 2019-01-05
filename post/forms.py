from __future__ import unicode_literals

from django import forms

from .models import Idea

#from django.contrib.admin import widgets

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('subject','division','image', 'pub_date', )

    def __init__(self, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)
        self.fields['pub_date'].widget = forms.widgets.SelectDateWidget()


