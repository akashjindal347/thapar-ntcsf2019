from django.shortcuts import render,redirect
from .forms import PostForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Post, AboutTheConference, ImportantDate, CallForPaper, Speaker, Announcement, Organiser, Contact, RegistrationContact, BankDetail, RegistrationFee, AccomodationAndTravel
# Create your views here.
def PostCreateView(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task-schedule')

    return render(request,'blog/createpost.html',{'form':form})

def PostUpdateView(request,id = None):
    obj = get_object_or_404(Post,id = id)
    form = PostForm(request.POST or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('task-schedule')



    return render(request,'blog/updatepost.html',{'form':form})

def PostDeleteView(request,id=None):
    obj = get_object_or_404(Post,id = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('task-schedule')

    return render(request,'blog/deleteview.html',{'obj':obj})

class AboutUpdateView(UpdateView):
    model = AboutTheConference
    template_name = "blog/updatepost.html"
    fields = ['description', 'link']
    success_url = "/"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = "blog/updatepost.html"
    fields = ['description', 'link']
    success_url = "/"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class RContactUpdateView(UpdateView):
    model = RegistrationContact
    template_name = "blog/updatepost.html"
    fields = ['description', 'link', 'highlight']
    success_url = "/registration/"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class AnnouncementsDeleteView(DeleteView):
	model = Announcement
	template_name = "blog/deleteview.html"
	success_url = "/"

class AnnouncementsCreateView(CreateView):
    model = Announcement
    template_name = "blog/createpost.html"
    fields = ['title', 'description', 'highlights']
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)

class AnnouncementsUpdateView(UpdateView):
    model = Announcement
    template_name = "blog/updatepost.html"
    fields = ['title', 'description', 'highlights']
    success_url = "/"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class AccomodationUpdateView(UpdateView):
    model = AccomodationAndTravel
    template_name = "blog/updatepost.html"
    fields = ['description', 'link']
    success_url = "/travel-and-accomodation"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class PapersUpdateView(UpdateView):
    model = CallForPaper
    template_name = "blog/updatepost.html"
    fields = ['description']
    success_url = "/"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class DatesUpdateView(UpdateView):
    model = ImportantDate
    template_name = "blog/updatepost.html"
    fields = ['description', 'date', 'highlighted']
    success_url = "/"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class DatesDeleteView(DeleteView):
	model = ImportantDate
	template_name = "blog/deleteview.html"
	success_url = "/"

class DatesCreateView(CreateView):
    model = ImportantDate
    template_name = "blog/createpost.html"
    fields = ['description', 'date', 'highlighted']
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)

class SpeakersUpdateView(UpdateView):
    model = Speaker
    template_name = "blog/updatepost.html"
    fields = ['name']
    success_url = "/"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class SpeakersDeleteView(DeleteView):
	model = Speaker
	template_name = "blog/deleteview.html"
	success_url = "/"

class SpeakersCreateView(CreateView):
    model = Speaker
    template_name = "blog/createpost.html"
    fields = ['name']
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)

class BankUpdateView(UpdateView):
    model = BankDetail
    template_name = "blog/updatepost.html"
    fields = ['description']
    success_url = "/registration/"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class BankDeleteView(DeleteView):
	model = BankDetail
	template_name = "blog/deleteview.html"
	success_url = "/registration/"

class BankCreateView(CreateView):
    model = BankDetail
    template_name = "blog/createpost.html"
    fields = ['description']
    success_url = "/registration/"

    def form_valid(self, form):
        return super().form_valid(form)

class OrganisersUpdateView(UpdateView):
    model = Organiser
    template_name = "blog/updatepost.html"
    fields = ['name']
    success_url = "/"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class OrganisersDeleteView(DeleteView):
	model = Organiser
	template_name = "blog/deleteview.html"
	success_url = "/"

class OrganisersCreateView(CreateView):
    model = Organiser
    template_name = "blog/createpost.html"
    fields = ['name']
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)

class FeesUpdateView(UpdateView):
    model = RegistrationFee
    template_name = "blog/updatepost.html"
    fields = ['description']
    success_url = "/registration/"
	
    def form_valid(self, form):
	    return super().form_valid(form)

class FeesDeleteView(DeleteView):
	model = RegistrationFee
	template_name = "blog/deleteview.html"
	success_url = "/"

class FeesCreateView(CreateView):
    model = RegistrationFee
    template_name = "blog/createpost.html"
    fields = ['description']
    success_url = "/registration/"

    def form_valid(self, form):
        return super().form_valid(form)

def HomePage(request):
    return render(request,'blog/index.html',{'atcs': AboutTheConference.objects.all(), 'impds': ImportantDate.objects.all(), 'cfps': CallForPaper.objects.all(), 'spkrs': Speaker.objects.all(), 'organisers': Organiser.objects.all(), 'contact': Contact.objects.all(), 'announce': Announcement.objects.all()})

def RegistrationPage(request):
    return render(request,'blog/registration.html',{'reg_con': RegistrationContact.objects.all(), 'bankdetails': BankDetail.objects.all(), 'regis_fee': RegistrationFee.objects.all(), 'contact': Contact.objects.all()})

def TravelPage(request):
    return render(request,'blog/accomodation.html',{'contact': Contact.objects.all(), 'ant': AccomodationAndTravel.objects.all()})

def TaskPage(request):
    posts= Post.objects.all()
    return render(request,'blog/talk-schedule.html',{ 'posts':posts})

def ConferencePage(request):
    return render(request,'blog/conference.html',{})

def PosterPage(request):
    return render(request,'blog/poster.html',{})






