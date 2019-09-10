
from django.urls import path,include
from .views import PostCreateView,PostDeleteView,PostUpdateView,FeesDeleteView,FeesCreateView,FeesUpdateView,AnnouncementsUpdateView,AnnouncementsCreateView,AnnouncementsDeleteView,HomePage,RegistrationPage,TravelPage,BankDeleteView, BankCreateView, BankUpdateView,TaskPage,ConferencePage,PosterPage,AccomodationUpdateView,RContactUpdateView,OrganisersCreateView,OrganisersDeleteView,OrganisersUpdateView, AboutUpdateView,ContactUpdateView, PapersUpdateView, DatesUpdateView, DatesDeleteView, DatesCreateView, SpeakersCreateView, SpeakersUpdateView, SpeakersDeleteView,ChiefPatronCreateView,ChiefPatronDeleteView,ChiefPatronUpdateView,PatronCreateView,PatronDeleteView,PatronUpdateView,HeadCreateView,HeadDeleteView,HeadUpdateView,ConvenorCreateView,ConvenorDeleteView,ConvenorUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('create-Post/',PostCreateView, name = 'create-Post'),
   path('edit/<int:id>',PostUpdateView, name = 'update-Post'),
   path('login',auth_views.LoginView.as_view(template_name = 'blog/login.html'),name = 'login'),
   path('logout',auth_views.LogoutView.as_view(template_name = 'blog/logout.html'),name = 'logout'),
   path('',HomePage, name = 'home'),
   path('task-schedule',TaskPage, name = 'task-schedule'),
   path('registration/',RegistrationPage, name = 'registration'),
   path('travel-and-accomodation/',TravelPage, name = 'travel'),
   path('delete/<int:id>',PostDeleteView, name = 'delete-Post'),
   path('conference-preceedings/',ConferencePage,name = 'conference'),
   path('poster',PosterPage,name ='poster'),
   path('edit/about-the-conference/<int:pk>',AboutUpdateView.as_view(), name = 'update-about'),
   path('edit/call-for-papers/<int:pk>',PapersUpdateView.as_view(), name = 'update-papers'),
   path('edit/accomodation-and-travel/<int:pk>',AccomodationUpdateView.as_view(), name = 'update-accomodation'),
   path('edit/registration-contact/<int:pk>',RContactUpdateView.as_view(), name = 'update-reg-contact'),
   path('create/announcement/',AnnouncementsCreateView.as_view(), name = 'add-announcement'),
   path('delete/announcement/<int:pk>',AnnouncementsDeleteView.as_view(), name = 'delete-announcement'),
   path('edit/announcement/<int:pk>',AnnouncementsUpdateView.as_view(), name = 'update-announcement'),
   path('edit/important-dates/<int:pk>',DatesUpdateView.as_view(), name = 'update-dates'),
   path('delete/important-dates/<int:pk>',DatesDeleteView.as_view(), name = 'delete-dates'),
   path('create/important-dates/',DatesCreateView.as_view(), name = 'new-dates'),
   path('edit/speakers/<int:pk>',SpeakersUpdateView.as_view(), name = 'update-speaker'),
   path('delete/speakers/<int:pk>',SpeakersDeleteView.as_view(), name = 'delete-speaker'),
   path('create/speakers/',SpeakersCreateView.as_view(), name = 'new-speaker'),
   path('edit/organisers/<int:pk>',OrganisersUpdateView.as_view(), name = 'update-organiser'),
   path('delete/organisers/<int:pk>',OrganisersDeleteView.as_view(), name = 'delete-organiser'),
   path('create/organisers/',OrganisersCreateView.as_view(), name = 'new-organiser'),
   path('edit/contact/<int:pk>',ContactUpdateView.as_view(), name = 'update-contact'),
   path('delete/bank-detail/<int:pk>',BankDeleteView.as_view(), name = 'delete-bank-detail'),
   path('new/bank-detail/',BankCreateView.as_view(), name = 'new-bank-detail'),
   path('edit/bank-detail/<int:pk>',BankUpdateView.as_view(), name = 'update-bank-detail'),
   path('delete/fee-details/<int:pk>',FeesDeleteView.as_view(), name = 'delete-fees'),
   path('new/fee-details/',FeesCreateView.as_view(), name = 'new-fees'),
   path('edit/fee-details/<int:pk>',FeesUpdateView.as_view(), name = 'update-fees'),

   path('edit/chief-patron/<int:pk>',ChiefPatronUpdateView.as_view(), name = 'update-chief-patron'),
   path('delete/chief-patron/<int:pk>',ChiefPatronDeleteView.as_view(), name = 'delete-chief-patron'),
   path('create/chief-patron/',ChiefPatronCreateView.as_view(), name = 'new-chief-patron'),

   path('edit/patron/<int:pk>',PatronUpdateView.as_view(), name = 'update-patron'),
   path('delete/patron/<int:pk>',PatronDeleteView.as_view(), name = 'delete-patron'),
   path('create/patron/',PatronCreateView.as_view(), name = 'new-patron'),

   path('edit/head/<int:pk>',HeadUpdateView.as_view(), name = 'update-head'),
   path('delete/head/<int:pk>',HeadDeleteView.as_view(), name = 'delete-head'),
   path('create/head/',HeadCreateView.as_view(), name = 'new-head'),

   path('edit/convenor/<int:pk>',ConvenorUpdateView.as_view(), name = 'update-convenor'),
   path('delete/convenor/<int:pk>',ConvenorDeleteView.as_view(), name = 'delete-convenor'),
   path('create/convenor/',ConvenorCreateView.as_view(), name = 'new-convenor'),
]
