from django import forms

class EmailForm(forms.Form):
    recipient = forms.EmailField(label="To", max_length=255)
    subject = forms.CharField(label="Subject", max_length=255)
    message = forms.CharField(label="Message", widget=forms.Textarea)
