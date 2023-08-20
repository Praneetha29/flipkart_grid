from django import forms
from inputPage.models import data_file
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = data_file
        fields=('file1',)