from django.urls import path
from courses.views import courses, details

urlpatterns = [
    path('', courses, name='courses'),
    path('<int:pk>/', details, name='details')
]
