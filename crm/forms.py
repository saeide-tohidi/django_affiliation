from django import forms

from crm.models import Lead
from product.models import AffiliatorProduct


class LeadForm(forms.Form):
    phone = forms.CharField()

    def save(self, source):
        lead = Lead()
        lead.phoneNo = self.cleaned_data["phone"]
        if source is not None:
            affiliator = AffiliatorProduct.objects.get(slug=source)
            lead.assignee = affiliator.user
            lead.affiliator_product = affiliator
            lead.price = affiliator.price
            lead.sale_price = affiliator.sale_price
        lead.save()
