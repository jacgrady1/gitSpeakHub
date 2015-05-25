from django import forms
from string import lower
from django.contrib.auth.models import User

from models import *
from forms import *

class AudioForm(forms.ModelForm):

    class Meta:
        model = Audio
        fields = ['text','description','audiofile']
        widgets = {
        'discription': forms.Textarea(attrs={'class':"form-control" ,'rows':"3",'placeholder':"description"}),
        'audiofile' : forms.FileInput() }