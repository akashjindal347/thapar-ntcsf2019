from django.contrib import admin
from .models import Post, AboutTheConference, CallForPaper, ImportantDate, Speaker, Organiser, Contact, Announcement, RegistrationContact, BankDetail, RegistrationFee, AccomodationAndTravel,ChiefPatron,Patron,Head,Convenor
# Register your models here.
admin.site.register(Post)
admin.site.register(AboutTheConference)
admin.site.register(CallForPaper)
admin.site.register(ImportantDate)
admin.site.register(Speaker)
admin.site.register(Organiser)
admin.site.register(Contact)
admin.site.register(RegistrationContact)
admin.site.register(BankDetail)
admin.site.register(RegistrationFee)
admin.site.register(AccomodationAndTravel)
admin.site.register(Announcement)
admin.site.register(ChiefPatron)
admin.site.register(Patron)
admin.site.register(Head)
admin.site.register(Convenor)