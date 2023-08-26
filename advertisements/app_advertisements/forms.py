from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields=("title", "description", "price", "image", "auction")
        widgets={
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "auction": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "image": forms.FileInput(attrs={'class': 'form-control'})
            }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака') 
        return title
    