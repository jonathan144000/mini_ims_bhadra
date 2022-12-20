from django import forms
from .models import Item

class ItemCreateForm(forms.ModelForm):
    class Meta:
        fields = ("title", "category", "particular", \
            "ledger_folio", "quantity", "price")
        model = Item