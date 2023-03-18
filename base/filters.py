import django_filters
from django import forms
from django_filters import CharFilter

from . models import *

class PostFilter(django_filters.FilterSet):
    headline = CharFilter(
        field_name="headline",
        lookup_expr="icontains",
        label="Headline",
        widget=forms.TextInput(attrs={'class': "form-input",'type':"text",'name':"query",'placeholder':"Article Search"})
        )
    class Meta:
        model = Post
        fields =['headline']