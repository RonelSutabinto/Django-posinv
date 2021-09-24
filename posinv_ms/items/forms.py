from django import forms
from .models import items, itemserials, itemserials_details


class itemForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ['id','itemcode','name','description','brand','category','unit','qty','price','saleprice',]
               
    def __init__(self, *args, **kwargs):
        super(itemForm, self).__init__(*args, **kwargs)
        self.fields['itemcode'].required = False




