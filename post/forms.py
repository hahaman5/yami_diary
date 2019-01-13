from __future__ import unicode_literals

from django import forms

from .models import Idea,Division

#from django.contrib.admin import widgets

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('subject','division','image', 'pub_date', 'memo',)

    def __init__(self, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)
        self.fields['pub_date'].widget = forms.widgets.SelectDateWidget()
        self.fields['memo'].widget = forms.Textarea()

class FilterForm(forms.Form):
    divs = forms.CharField(label='분류', widget=forms.Select())
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields["divs"].choices = ("a","b")
