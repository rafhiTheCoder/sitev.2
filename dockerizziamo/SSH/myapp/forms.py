from django import forms

class Add(forms.Form):
    code = forms.CharField(label="code",max_length=200)