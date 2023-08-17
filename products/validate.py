from django.utils.translation import gettext_lazy as _
from django import forms
def validate_price(value):
        if value < 0:
            raise forms.ValidationError(_("Price must be non negative"))
        else:
            return value
        