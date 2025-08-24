from . import models 
from django import forms
class TweetForm(forms.ModelForm):
    class Meta:
        model = models.Tweet
        fields = ['text' , 'photo']


        