from django import forms  
from django.forms.widgets import NumberInput

class RangeInput(NumberInput):
    input_type = 'range'
class PasswordGenForm(forms.Form):
    length = forms.IntegerField(
        label='Password length',
        required = True,
        widget = RangeInput(
            attrs={'min':'1', 'max': '40', 'class':'range',
            'id': 'lengthRangeInput'}
        )
    )
    
    include_symbols = forms.BooleanField(
        label='Include symbols (@#$!?)',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class':'checkboxInput'}
        )
        
    )
    
    
    remove_similar_characters = forms.BooleanField(
        label = 'Exclude similar Characters (e.g 00 l1 2z)',
        required = False,
        widget=forms.CheckboxInput(
            attrs={'class': 'checkboxInput'}
        )
    )
    