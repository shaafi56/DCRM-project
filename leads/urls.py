from django.urls import path
from leads.views import ( 
    lead_list, lead_detail, create_froms, lead_update, lead_delete,
                          LeadListView, LeadDetailView , leadCreateView, leadUpdateView, leadDeleteView)

app_name = "leads"
urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
    path("<int:pk>/", LeadDetailView.as_view(),name="lead-detail"),
    path("<int:pk>/update", leadUpdateView.as_view(), name="lead-update"),
    path("<int:pk>/delete", leadDeleteView.as_view(), name="lead-delete"),
    path("create/", leadCreateView.as_view(), name="lead-create")
]
