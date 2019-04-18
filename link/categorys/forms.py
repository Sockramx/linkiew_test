from django import forms
from .models import Category, SubCategory



class SubCategoryModelForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = SubCategory 
        fields = '__all__'


class CategoryModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['subCategory'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Category
        fields = '__all__'