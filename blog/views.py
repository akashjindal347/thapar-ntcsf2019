from django.shortcuts import render,redirect
from .forms import PostForm
from django.shortcuts import get_object_or_404
from .models import Post
# Create your views here.
def PostCreateView(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request,'blog/createpost.html',{'form':form})

def PostUpdateView(request,id = None):
    obj = get_object_or_404(Post,id = id)
    form = PostForm(request.POST or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('home')



    return render(request,'blog/updatepost.html',{'form':form})

def PostDeleteView(request,id=None):
    obj = get_object_or_404(Post,id = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')

    return render(request,'blog/deleteview.html',{'obj':obj})

def HomePage(request):
    return render(request,'blog/index.html',{})

def RegistrationPage(request):
    return render(request,'blog/registration.html',{})

def TravelPage(request):
    return render(request,'blog/accomodation.html',{})

def TaskPage(request):
    posts= Post.objects.all()
    return render(request,'blog/talk-schedule.html',{ 'posts':posts})

def ConferencePage(request):
    return render(request,'blog/conference.html',{})

def PosterPage(request):
    return render(request,'blog/poster.html',{})





