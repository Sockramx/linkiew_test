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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['link'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['source'].widget.attrs.update({'class': 'form-control'})
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        

    class Meta:
        model = Video
        fields = ['name', 'link', 'description', 'source', 'user', 'category']
       
    
