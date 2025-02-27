from django.urls import path
from leads.views import ( 
    lead_list, lead_detail, create_froms, lead_update, lead_delete,
                          LeadListView, LeadDetailView )

app_name = "leads"
urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
    path("<int:pk>/", LeadDetailView.as_view(),name="lead-detail"),
    path("<int:pk>/update", lead_update, name="lead-update"),
    path("<int:pk>/delete", lead_delete, name="lead-delete"),
    path("create/", create_froms, name="lead-create")
]
