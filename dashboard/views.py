from django.db.models import Count, Sum
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from crm.models import Lead
from financial.models import UserFinancial


class Sidebar(View):
    def get(self, request):
        return render(
            request,
            "shared/sidebar.html",
        )


class Header(View):
    def get(self, request):
        return render(
            request,
            "shared/header.html",
        )


class Dashboard(LoginRequiredMixin, ListView):
    model = Lead
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["leads"] = Lead.objects.filter(assignee=self.request.user)[0:10]
        context["all_leads_count"] = len(
            Lead.objects.filter(assignee=self.request.user)
        )
        context["buy_leads_count"] = len(
            Lead.objects.filter(assignee=self.request.user, status="F")
        )
        context["total_share_price"] = Lead.objects.filter(
            assignee=self.request.user, status="B"
        ).aggregate(Sum("affiliator_share"))
        context["financial_info"] = UserFinancial.objects.get(user=self.request.user)
        return context
