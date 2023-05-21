from .models import Ideas
from django.forms import ModelForm, Textarea, CheckboxInput


class IdeasForm(ModelForm):
    class Meta:
        model = Ideas
        fields = ['title', 'description', 'offer', 'effect', 'economic']

        widgets = {
            "title": Textarea(attrs={
                'class': 'form-control',
                'rows': '1'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'rows': '3'
            }),
            "offer": Textarea(attrs={
                'class': 'form-control',
                'rows': '3'
            }),
            "effect": Textarea(attrs={
                'class': 'form-control',
                'rows': '3'
            }),
            "economic": CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
            })
        }


