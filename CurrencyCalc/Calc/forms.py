from django import forms
from . models import Currencies


class CalcForm(forms.Form):
    qtity = forms.IntegerField()
    from_curr = forms.ModelChoiceField(queryset=Currencies.objects.all())
    to_curr = forms.ModelChoiceField(queryset=Currencies.objects.all())


class AddForm(forms.ModelForm):

    class Meta:
        model = Currencies
        fields = ('name', 'shortname', 'quantity', 'tobgn', 'frombgn')
