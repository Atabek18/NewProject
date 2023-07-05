from .models import New_project
from django.forms import ModelForm, TextInput, Textarea, NumberInput

class New_projectForm(ModelForm):
    class Meta:
        model = New_project
        fields = ['file_name', 'file_size', 'some_info']

        widgets = {
            'file_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'File Name'
            }),
            'file_size': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Size'
            }),
            'some_info': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Info about something'
            })
        }
