from django.urls import path
from courses.views import courses, details

urlpatterns = [
    path('', courses, name='courses'),
    path('<slug:slug>/', details, name='details')
]
