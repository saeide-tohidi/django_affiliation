from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView

from user.models import UserProfile


class UserProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserProfile
    fields = [
        "first_name",
        "last_name",
        "phoneNo",
        "instagram",
        "telegram_channel",
        "website",
    ]
    template_name = "user/profile.html"
    login_url = "/crm/"
    success_url = "/crm/profile"
    success_message = "اطلاعات شما با موفقیت ثبت شد."

    def get_object(self):
        obj, created = UserProfile.objects.get_or_create(user=self.request.user)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
