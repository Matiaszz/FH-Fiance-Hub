from django import forms


class UploadCSV(forms.Form):
    file = forms.FileField()
