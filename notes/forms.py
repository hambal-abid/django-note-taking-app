from django import forms

class NotesForm(forms.Form):
    image = forms.ImageField
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)