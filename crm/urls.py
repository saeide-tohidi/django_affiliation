from django.urls import path
from .views import CreateLead, LeadListView

urlpatterns = [
    path("lead/list/", LeadListView.as_view(), name="lead_list"),
    path("create/", CreateLead.as_view(), name="create_lead"),
]
