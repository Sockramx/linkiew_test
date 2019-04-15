from django import forms
from .models import Video, Category, SubCategory


class SubCategoryModelForm(forms.ModelForm):
    class Meta:
        model = SubCategory 
        fields = '__all__'


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class VideoModelForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['name', 'link', 'description', 'source', 'user', 'category']
       
    