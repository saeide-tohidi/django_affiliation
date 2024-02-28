from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import UpdateView
from financial.models import UserFinancial, FinancialRecord, UserPaymentRequestRecord


class UserFinancialInfo(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserFinancial
    fields = [
        "sheba",
        "card_num",
    ]
    template_name = "financial/financial_info.html"
    login_url = "/crm/"
    success_url = "/crm/financial/info/"
    success_message = "اطلاعات شما با موفقیت ثبت شد."

    def get_object(self):
        obj, created = UserFinancial.objects.get_or_create(user=self.request.user)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["financial_info"] = UserFinancial.objects.get_or_create(
            user=self.request.user
        )
        context["financial_record"] = FinancialRecord.objects.filter(
            user_financial__user=self.request.user
        ).order_by("-id")
        return context


class UserPaymentRequestView(View):
    def get(self, request):
        user_credit, creat = UserFinancial.objects.get_or_create(user=self.request.user)
        if user_credit.credit <= 50000:
            messages.error(
                request,
                " ثبت درخواست واریز وجه برای موجودی کمتر از ۵۰ هزار تومان امکان پذیر نمی‌باشد.",
            )
            return redirect(
                "/financial/info/",
            )
        else:
            user_req = UserPaymentRequestRecord()
            user_req.user = request.user
            user_req.amount = user_credit.credit
            user_req.save()
            messages.success(request, "درخواست واریز وجه با موفقیت ثبت شد.")
            return redirect(
                "/financial/info/",
            )
