from .models import Entry
from django import forms
from ckeditor.fields import RichTextField
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title','body','source','category']

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'body': forms.Textarea(attrs = {'class': 'form-control'}),
            'source': forms.TextInput(attrs = {'class': 'form-control'}),
            'category': forms.Select(attrs = {'class': 'form-control'}),

        }
