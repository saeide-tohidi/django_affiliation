from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic import FormView
from crm.forms import LeadForm
from crm.models import Lead


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = "crm/lead_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        leads = Lead.objects.filter(assignee=self.request.user)
        context["leads"] = leads
        return context


class CreateLead(SuccessMessageMixin, FormView):
    form_class = LeadForm
    success_url = "/"
    print("valid")

    def form_valid(self, form):
        lead = self.request.session["lead"]

        form.save(lead)
        return super().form_valid(form)
