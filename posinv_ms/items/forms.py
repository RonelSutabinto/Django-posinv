from django import forms
from .models import items, itemserials, itemserials_details,category


class itemForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ['id','itemcode','name','description','brand','category','unit','qty','price','saleprice',]
               
    def __init__(self, *args, **kwargs):
        super(itemForm, self).__init__(*args, **kwargs)
        self.fields['itemcode'].required = False


class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['id', 'category']
        readonly_fields = ['created_at', 'updated_at']
        
    def __init__(self, *args, **kwargs):
        super(categoryForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = True


