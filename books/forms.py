from django import forms

class PublisherForm(forms.Form):
    name = forms.CharField(label='Your name',max_length=30)
    address = forms.CharField(max_length=50)
    city = forms.CharField(max_length=60)
    state_province = forms.CharField(max_length=30)
    country = forms.CharField(max_length=20)
    website = forms.CharField(max_length=50)
