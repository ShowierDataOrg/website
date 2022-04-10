from django import forms

class ContactForm(forms.Form):
    # only admin here so it can only go to me
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    