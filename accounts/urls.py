from django.urls import path
from . import views

urlpatterns = [

    path('sign_in_admin', views.sign_in_admin , name='sign_in_admin'),

    path('signup_patient', views.signup_patient, name="signup_patient"),
    path('sign_in_patient', views.sign_in_patient , name='sign_in_patient'),
    path('savepdata/<str:patientusername>', views.savepdata , name='savepdata'),
   
    path('OTP', views.OTPAuthentication,name="OTP_Authentication"),
    path('QR',views.QRAuthentication,name="QR Authentication"),

    path('DOTP', views.DOTPAuthentication,name="DOTP_Authentication"),
    path('DQR',views.DQRAuthentication,name="DQR Authentication"),

    path('signup_doctor', views.signup_doctor , name="signup_doctor"),
    path('sign_in_doctor', views.sign_in_doctor , name='sign_in_doctor'),
    path('saveddata/<str:doctorusername>', views.saveddata , name='saveddata'),

    path('logout', views.logout , name='logout'),
]