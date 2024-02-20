from django.urls import path
from .views import StudentRegistrationview


urlpatterns=[
    path('register/',StudentRegistrationview.as_view(), name='student_registration')
]