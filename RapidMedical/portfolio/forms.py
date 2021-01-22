from django import forms

class contactformemail(forms.Form):
    name=forms.CharField(max_length=40, required=True)
    fromemail = forms.EmailField(required=True)
    subject=forms.CharField(max_length=120, required=True)
    message=forms.CharField(widget= forms.Textarea, max_length=500, required=True)


