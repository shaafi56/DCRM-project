from django.core.mail import send_mail
from django.shortcuts import render , redirect , reverse
from leads.forms import LeadForm, LeadModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView , UpdateView , DeleteView
from .models import lead , Agent
from django.http import HttpResponse

class landingPageView(TemplateView):
    template_name = "leads/landing.html"

def landing_page(request):
    return render(request, "leads/landing.html")

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = lead.objects.all()

# Create your views here.
def lead_list(request):
    leads = lead.objects.all()
    #context is a dictionary that contains the data that is to be rendered in the template
    context = {
        "leads" : leads
    }
    return render(request , "leads/lead_list.html", context)

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = lead.objects.all()
    context_object_name = "lead"

#we gone creacte a new function named lead_detail
def lead_detail(request, pk):
    Lead = lead.objects.get(id=pk)
    context = {
        "lead" : Lead
    }
    return render(request, "leads/lead_detail.html",context)

class leadCreateView(CreateView):
    template_name = "leads/create_froms.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        # Todo send email
        send_mail(
            subject="A new lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@gmail.com",
            recipient_list=["test2@gmail.com"]
        )
        return super(leadCreateView, self).form_valid(form)

#lead create function to create the lead details
def create_froms(request):
    form = LeadModelForm()
    if request.method == "POST":
        form =LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        "form" : form
    }
    return render(request, "leads/create_froms.html",context)

class leadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

#lead update function to update the lead details
def lead_update(request, pk):
    Lead = lead.objects.get(id=pk)
    form = LeadModelForm(instance=Lead)
    if request.method == "POST":
        form =LeadModelForm(request.POST, instance=Lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead" : Lead
    }
    return render(request, "leads/lead_update.html",context)

class leadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:lead-list")

#lead delete function to delete the lead details
def lead_delete(request, pk):
    Lead = lead.objects.get(id=pk)
    Lead.delete()
    return redirect("/leads")

#function to update the lead details 
# def lead_update(request, pk):
#     Lead = lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form =LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             Lead.first_name = first_name
#             Lead.last_name = last_name
#             Lead.age = age
#             Lead.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead" : Lead
#     }
#     return render(request, "leads/lead_update.html",context)

# def create_froms(request):
    # form = LeadForm()
    # if request.method == "POST":
    #     form =LeadForm(request.POST)
    #     if form.is_valid():
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         age = form.cleaned_data['age']
    #         agent = Agent.objects.first()
    #         lead.objects.create(
    #             first_name = first_name,
    #             last_name = last_name,
    #             age = age,
    #             agent = agent
    #         )
    #         return redirect("/leads")

#     context = {
#         "form" : form
#     }
#     return render(request, "leads/create_froms.html",context)