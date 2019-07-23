
from django.urls import path,include
from .views import PostCreateView,PostDeleteView,PostUpdateView,HomePage,RegistrationPage,TravelPage,TaskPage
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('create-Post/',PostCreateView, name = 'create-Post'),
   path('edit/<int:id>',PostUpdateView, name = 'update-Post'),
   path('login',auth_views.LoginView.as_view(template_name = 'blog/login.html'),name = 'login'),
   path('logout',auth_views.LogoutView.as_view(template_name = 'blog/logout.html'),name = 'logout'),
      path('',HomePage, name = 'home'),
      path('task-schedule',TaskPage, name = 'task-schedule'),
      path('registration/',RegistrationPage, name = 'registration'),
      path('travel-and-accomodation',TravelPage, name = 'travel'),
      path('delete/<int:id>',PostDeleteView, name = 'delete-Post'),

    

]
