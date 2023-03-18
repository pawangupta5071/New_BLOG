from django import forms
from django.forms import ModelForm


from .models import Post,Comment


class PostForm(ModelForm):
    
    headline = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'headline',
        'type':"text",
        'name':"headline",
        'id':"name"
    }))

    sub_headline = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'sub_headline',
        'type':"text",
        'name':"headline",
        'id':"name"
    }))

    thumbnail = forms.ImageField(widget=forms.ClearableFileInput())

    body = forms.CharField(widget=forms.Textarea(attrs={
        'name':"message",
        'id':"message",
        'cols':"30",
        'rows':"8",
        'placeholder':"BODY",
    }))

    active = forms.BooleanField(widget=forms.CheckboxInput())
    
    featured = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = Post
        fields = '__all__'
        