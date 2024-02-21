from django.urls import path
from .views import StudentRegistrationview,StudentEnrollCourseView


urlpatterns=[
    path('register/',StudentRegistrationview.as_view(), name='student_registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(),name='student_enroll_course'),

]