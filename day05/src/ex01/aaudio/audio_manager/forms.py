from django import forms
from django.core.validators import FileExtensionValidator

class AudioUploadForm(forms.Form):
    file = forms.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['mp3'])
        ])

