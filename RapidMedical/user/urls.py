from django.urls import path
from . import views
from .views import verification



urlpatterns=[
    path('register/', views.register, name='register'),
    path('verify/', views.verify_mail, name='verify'),
    path('hospitalprofile/', views.Hospitalprofile, name='hospitalprofile'),
    #path('profile/', views.profile, name='profile'),
    path('profile/<int:profileId>', views.profileView, name='profileview'),
    path('profile/Create-Hospital-Info/', views.hospitalinfo, name='Hreg-hos'),
    path('profile/hospitalupdate/<int:profileId>', views.HospitalUpdateProfile, name='H-update'),
    path('profile/update/<int:profileId>', views.UpdateProfile, name='update'),
    path('activate/<uidb64>/<token>', verification.as_view(), name='activate'),
]



