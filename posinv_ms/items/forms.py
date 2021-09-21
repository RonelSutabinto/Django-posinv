from django import forms
from .models import items, itemserials, itemserials_details


class itemForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ['iditems','itemcode','name','description','brand','category','unit','qty','price','saleprice','pricingbyID','pricingdate']
        labels = {
            'itemcode': 'Item Code', 'description': 'Description', 'saleprice': 'Sale Price', 'metertype': 'Meter Type', 'units': 'Unit'
        }
        widgets = {
            'dateforwarded': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'dateforwarded', 'placeholder': 'Select a date'}),
        }

    def __init__(self, *args, **kwargs):
        super(itemForm, self).__init__(*args, **kwargs)
        self.fields['itemcode'].required = False




