from django import forms
from .models import Category, SubCategory



class SubCategoryModelForm(forms.ModelForm):
    class Meta:
        model = SubCategory 
        fields = '__all__'


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'